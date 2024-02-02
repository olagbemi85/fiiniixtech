'''
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

while True:
    time.sleep(1)
    today1 = date.today()
    t = time.localtime()
    today2 = time.strftime("%H:%M:%S", t) 
    #today3 = datetime.now()
    i = random.randrange(34)
    v = random.randrange(9,14)
    powers = i*v
    temps = random.randrange(35,40)
    inten = random.randrange(9,76)
    
    
    try:
        dbconn = sqlite3.connect('db.sqlite3')
        cur = dbconn.cursor()
        print("Successfully Connected to SQLite")
        print(today1,today2, v, i, powers, temps, inten)
        cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (str(today1), str(today2), v, i, powers, temps, inten)")
        #cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (3-26-2023, '21:00:24 ', 12, 10, 120, 36, 23)")

        dbconn.commit()
        
        print('successful')
        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if dbconn:
            dbconn.close()
            print("The SQLite connection is closed")
    sleep(18) 


main()    
'''
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
    i = random.randrange(34)
    v = random.randrange(9,14)
    powers = i*v
    temps = random.randrange(35,40)
    inten = random.randrange(9,76)
    dbconn = sqlite3.connect('db.sqlite3')
    cur = dbconn.cursor()
    sql = "INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cur.execute(sql, (today1, today2, v, i, powers, temps,  inten))
    #cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (today1, t, v, i, powers, temps, inten)")
    #cur.execute("INSERT INTO iotSolar_proj_datasolar (days, hourly, voltage, currents, power, temp, intensity) VALUES (3-26-2023, 02, 12, 10, 120, 36, 23)")
    dbconn.commit()
    dbconn.close()
    sleep(18)
    print('successful')


main()    
