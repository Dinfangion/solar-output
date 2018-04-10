#!/usr/bin/env python

#config
cfg = {
  'ip_net': '10.0.0.0',
  'mac': '00:00:00:00:00:00',
  'db': { 'h': 'localhost', 'u': 'dbuser', 'p': 'pwd', 'd': 'dbname' },
  'api-key': 'blah',
}

def _get_inverter_ip(ip_net, mac):
  #TODO
  inv_ip = '0.0.0.0'
  return inv_ip

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
eg, pg = get_inverter_data(cfg['ip_net'], cfg['mac'])
insert_in_db(cfg['db'], eg, pg)
post_pvoutput(cfg['api_key'], eg, pg)
