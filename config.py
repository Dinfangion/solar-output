# config file for solar-output.py
cfg = {
  'wake_hour': 6, # hour of day to start measurements
  'sleep_hour': 23, # hour of day to stop measurements
  'ip_net': '192.168.0.0/24', #local IP subnet having inverter
  'mac': 'e0:02:02', #prefix of (or full) inverter MAC address
  'db': {
    'host': 'localhost', # mysql/mariadb server ip or hostname; leave empty to skip database
    'user': 'solar_rw',
    'pwd': 'yourpassword',
    'db_name': 'solar',
    'table': 'solar_output',
  },
  'pvoutput': {
    'system_id': '', #pvoutput system id; leave empty to skip upload
    'api_key': '', #pvoutput webservice API key
  },
}

