#!/usr/bin/env python
import subprocess
import requests
import pymysql
from config import cfg

def _get_inverter_ip(ip_net, mac): # may raise exception
  print 'using nmap to find inverter'
  cmd = 'nmap -sP -sn --host-timeout 20 -n %s' % ip_net
  out = subprocess.check_output(cmd, shell=True)
  """ example ouput:
  Starting Nmap 7.70 ( https://nmap.org ) at 2018-04-10 18:41 CEST
  Nmap scan report for 192.168.0.2
  Host is up (0.18s latency).
  MAC Address: 11:11:11:11:11:11 (Vendor)
  Nmap scan report for 192.168.0.1
  Host is up.
  Nmap done: 256 IP addresses (2 hosts up) scanned in 6.77 seconds
  """
  last_ip = ''
  for line in out.splitlines():
    if 'report for' in line:
      last_ip = line.strip().split()[-1]
    if 'MAC Address' in line:
      outmac = line.split('(')[0].strip().split()[-1]
      if outmac.lower().startswith(mac.lower()):
        return last_ip
  return ''

def get_inverter_data(ip_net, mac): # may raise exception
  retry = 2
  while retry:
    try:
      with open('cached_ip.txt', 'r') as f:
        ip = f.readline().strip()
    except:
      ip = ''
    if not ip:
      try:
        ip = _get_inverter_ip(ip_net, mac)
        with open('cached_ip.txt', 'w') as f:
          f.write(ip)
      except Exception as e:
        print 'ignoring error:', type(e).__name__, str(e)
    if not ip:
      raise Exception('unable to get inverter IP address')
    print 'trying to get data xml from', ip
    try:
      resp = requests.get('http://%s/real_time_data.xml' % ip, timeout=10)
    except Exception as e:
      try:
        with open('cached_ip.txt', 'w') as f:
          f.write('')
      except:
        pass
      retry -= 1
      if retry:
        continue # while retry
      raise e
    retry = 0
  pac1 = ''
  e_today = ''
  for line in resp.text.splitlines():
    if '<pac1>' in line:
      pac1 = line.split('>')[1].split('<')[0]
    if '<e-today>' in line:
      e_today = line.split('>')[1].split('<')[0]
  if '' in (pac1, e_today):
    raise Exception('unable to extract all data from inverter response:\n%s' % resp.text)
  print 'got data: pac1=%s e_today=%s' % (pac1, e_today)
  return dict(pac1=pac1, e_today=e_today)

def insert_in_db(cfg_db, data):
  if not cfg_db['host']:
    print 'skipping database insert'
    return
  db = pymysql.connect(host=cfg_db['host'],
                       connect_timeout=10,
                       user=cfg_db['user'],
                       password=cfg_db['pwd'],
                       db=cfg_db['db_name'],
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
  with db.cursor() as c:
    columns = ','.join(data.keys())
    value_holders = ','.join(('%s',)*len(data.keys()))
    sql = 'insert into %s (%s) values (%s)' % (cfg_db['table'], columns, value_holders)
    c.execute(sql, data.values())
  db.commit()
  print 'data inserted in database'
  return

def post_pvoutput(cfg_api_key, data):
  #TODO
  return

#main
try:
  data = get_inverter_data(cfg['ip_net'], cfg['mac'])
  try:
    insert_in_db(cfg['db'], data)
  except Exception as e:
    print 'db insert failed:', type(e).__name__, str(e)
    print 'moving on anyway'
  post_pvoutput(cfg['api_key'], data)
except Exception as e:
  print type(e).__name__, str(e)
print 'Done'
