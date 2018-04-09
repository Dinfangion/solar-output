# solar-output
solar energy output - photovoltaic system

There are several options to monitor your solar energy output.

These notes describe the SAJ Sununo plus solar inverter.

Solar panels => solar inverter => rs232-to-ethernet module => router => LAN/internet.

1. Use the android app of SAJ, and the login that you received during installation.
   You can read the outputs and graphs which are posted from your solar inverter to a SAJ server in Alibaba Cloud.
2. Scan with nmap/zenmap gui for the MAC-address and IP of your solar inverter.
   Use your browser to go the overview on http://x.x.x.x
3. Make a script to post your energy output to your own database and/or pvoutput.org

# WORK IN PROGRESS
