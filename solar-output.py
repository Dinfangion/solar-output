#!/usr/bin/env python

import subprocess

#config
cfg = {
  'ip_net': '192.168.0.0/24', #local IP subnet having inverter
  'mac': '34:A3:95', #prefix of (or full) inverter MAC address
  'db': {
    'h': 'localhost',
    'u': 'dbuser',
    'p': 'pwd',
    'd': 'dbname'
  },
  'api_key': 'itsasecret', #pvoutput webservice API key
}

def _get_inverter_ip(ip_net, mac): # may raise exception
  cmd = 'nmap -sP -sn -n %s' % ip_net
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
      outmac = line.split()[-2]
      if outmac.lower().startswith(mac.lower()):
        return last_ip
  return ''

def get_inverter_data(ip_net, mac):
  #TODO
  eg = pg = 0
  return eg, pg

def insert_in_db(cfg_db, eg, pg):
  #TODO
  return

def post_pvoutput(cfg_api_key, eg, pg):
  #TODO
  return

#main
try:
  #testing, remove me later
  print _get_inverter_ip(cfg['ip_net'], cfg['mac']) or 'No inverter found'
  
  eg, pg = get_inverter_data(cfg['ip_net'], cfg['mac'])
  insert_in_db(cfg['db'], eg, pg)
  post_pvoutput(cfg['api_key'], eg, pg)
except Exception as e:
  print type(e).__name__, str(e)
print 'Done'
