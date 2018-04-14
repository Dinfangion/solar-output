# config file for solar-output.py
cfg = {
  'wake_hour': 8, # hour of day to start measurements
  'sleep_hour': 21, # hour of day to stop measurements
  'ip_net': '192.168.0.0/24', #local IP subnet having inverter
  'mac': '00:90:A9', #prefix of (or full) inverter MAC address
  'db': {
    'host': 'localhost', # mysql/mariadb server ip or hostname; leave empty to skip database
    'user': 'root',
    'pwd': '',
    'db_name': 'solar',
    'table': 'solar_output',
  },
  'pvoutput': {
    'system_id': '', #pvoutput system id; leave empty to skip upload
    'api_key': '', #pvoutput webservice API key
  },
}

