# solar-output
solar energy output - photovoltaic system

There are several (3) options to monitor your solar energy output.

These notes describe the SAJ Sununo plus solar inverter.

Solar panels => solar inverter => rs232-to-ethernet module => router => LAN/internet.

Option 1. Use the android app of SAJ, and the login that you received during installation.  
   You can read the outputs and graphs which are posted from your solar inverter to a SAJ server in Alibaba Cloud.  

Option 2. Scan with nmap/zenmap gui for the MAC-address and IP of your solar inverter.  
   Use your browser to go the overview on http://x.x.x.x

Option 3. Use Home Assistant https://www.home-assistant.io/integrations/saj/

Option 4. (this project) Make a script to post your energy output to your own database and/or pvoutput.org  

**My setup:**

Hardware: Raspberry Pi 3 Model B Rev 1.2 https://www.raspberrypi.org/  
Operating system: Raspbian 10 buster https://distrowatch.com/table.php?distribution=raspbian     
Software: Bash 5.0.3, Python 3.7.3, Mariadb-server 10.3.17, Nmap 7.70   
sudo apt-get install mariadb-server python3-requests python3-pymysql nmap

1. Activate your API-Key on pvoutput.org
2. Create your local database (optional)

```
CREATE DATABASE solar DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
use solar;
create table solar_output (
	time_stamp DATETIME PRIMARY KEY,
	pac1 INT,
	e_today FLOAT
);
```
3. Edit config.py
4. chmod +x solar-output.py
5. sudo crontab -e

crontab for root: (yes root, otherwise nmap doesn't output everything you need)
```
*/10 * * * * /home/pi/solar/solar-output.py
```
