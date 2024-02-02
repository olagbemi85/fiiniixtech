import time
from time import sleep
from datetime import date
#from datetime import time
from datetime import datetime
#import pandas as pd
import numpy as np
import time
from time import sleep
import random
import sqlite3 

#dbconn = sqlite3.connect('db.sqlite3')
#cur = dbconn.cursor()

while True:
    time.sleep(1)
    today1 = date.today()
    t = time.localtime()
    today2 = time.strftime("%H:%M:%S", t) 
    #today2 = datetime.now()
    i_r = random.randrange(34)
    i_y = random.randrange(34)
    i_b = random.randrange(34)
    v_r = random.randrange(9,14)
    v_y = random.randrange(9,14)
    v_b = random.randrange(9,14)
    powers_r = i_r*v_r
    powers_y = i_y*v_y
    powers_b = i_b*v_b
    temps = random.randrange(35,40)
    station = "AEDC-KWB-235465"
    dbconn = sqlite3.connect('db.sqlite3')
    cur = dbconn.cursor()
    sql = "INSERT INTO iotPowerSystem_data (voltage_r, voltage_y, voltage_b, currents_r, currents_y, currents_b, power_r, power_y, power_b, temp, station_code, days,hourly) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(sql, (v_r,v_y,v_b,i_r,i_y,i_b,powers_r,powers_y,powers_b,temps,station,today1,today2))
    #cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (today1, t, v, i, powers, temps, inten)")
    #cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (3-26-2023, 02, 12, 10, 120, 36, 23)")
    dbconn.commit()
    dbconn.close()
    sleep(18)
    print('successful')
'''
    try:
        cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (today1, t, v, i, powers, temps, inten)")
        #cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (3-26-2023, 02, 12, 10, 120, 36, 23)")

        dbconn.commit()
        
        print('successful')
    except:
        print('fail to connect')
        dbconn.close()
    sleep(18) 
'''

main()    
