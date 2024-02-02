# IMPORT PACKAGES
import requests
import urllib.parse as up
import json
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
 
# READ API KEY (COPIED FROM API URL): STORE TXT WITH API KEY FROM THE URL GENERATED IN THE QUERY MANAGER
# IN SAME PATH AS THIS SCRIPT. OTHERWISE YOU NEED TO ADD THE PATH TO THE BELOW TXT FILE
# (NOTE: ADD QUOTATION MARKS " AT START AND END OF API KEY IN THE TXT)
f = open("YOUR_SM_API_KEY.txt", "r")
api_key = f.read()
 
# SUPERMETRICS API URL EXAMPLE (WITH API KEY REMOVED)
url = "https://api.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22GA%22%2C%22ds_accounts%22%3A%5B%2220619257%22%5D%2C%22date_range_type%22%3A%22yesterday%22%2C%22fields%22%3A%5B%7B%22id%22%3A%22Date%22%7D%2C%7B%22id%22%3A%22Sessions%22%7D%5D%2C%22max_rows%22%3A1000%2C%22api_key%22%3A%22api_XXXX%22%7D"
 
# DECODE URL: HELPFUL TO IMPROVE READABILITY OF QUERY PARAMETERS => ALLOWS FOR EASIER EDITING
# ALTERNATIVE: GO TO https://www.urldecoder.org/ and decode the URL generated by the SM QUERY MANAGER: https://team.supermetrics.com/query-manager
print(up.unquote(url))
# PRINT ORIGINAL URL FOR COMPARISON
print(url)
 
# SPLIT UP DECODED URL AND MODIFY PARAMETERS, E.G. "date_range_type"
url_decoded = ('https://api.supermetrics.com/enterprise/v2/query/data/'
# CHOOSE OUTPUT FORMAT: JSON, KEYJSON, CSV, TSV, ETC: https://supermetrics.com/docs/product-api-output-formats/
# EXAMPLE: 'keyjson?json='
+'[INSERT_OUTPUT_FORMAT]?json='
# CHOOSE DATA SOURCE, e.g. "GA" or "FB" or "IG"
+'{"ds_id":"INSERT_DATA_SOURCE"'
# CHOOSE ACCOUNTS AND PARSE AS LIST, e.g. GA views: ["1234","5678"]
+',"ds_accounts":["INSERT_YOUR_ACCOUNTS"],'
# DEFINE DATE RANGE
# +'"start_date":"2020-06-01","end_date":"2020-06-30",'
+'"date_range_type":"last_week_mon_sun",'
# CHOOSE YOUR FIELDS, i.e. DIMENSIONS AND METRICS. SEE EXAMPLE FOR Google Analytics BELOW
+'"fields":[{"id":"Date"},{"id":"Sessions"},{"id":"Pageviews"},{"id":"Users"}],'
+'"max_rows":1000000,'
+'"api_key":'+api_key+'}')
 
# CALL SUPERMETRICS API
response = requests.get(url_decoded)
 
print(response)
 
# IF STATEMENT TO CHECK FORMAT
if 'data/json?' in url_decoded:
   # CONVERT JSON INTO PANDAS DATAFRAME
   data = json.loads(json.dumps(response.json()))
   df = pd.DataFrame.from_dict(data['data'])
   headers = df.iloc[0]
   df2 = pd.DataFrame(df.values[1:], columns=headers)
   df2.head()
   print(df2.head())
elif 'data/keyjson?' in url_decoded:
   # CONVERT JSON KEY-VALUE PAIR OUTPUT TO PD DF
   df2 = pd.read_json(json.dumps(response.json()))
   df2.head()
   print(df2.head())
else:
   # THROW EXCEPTION MESSAGE
   import sys
   sys.exit("DEFINE JSON OR KEYJSON AS OUTPUT FORMAT: https://supermetrics.com/docs/product-api-output-formats/")
 
 
# IF YOU PLAN ON LOADING THE DATAFRAME INTO A DATA WAREHOUSE,
# YOU WILL NEED TO ADD THE REQUIRED CREDENTIALS TO WRITE THE DATA INTO YOUR DWH
 
# MySQL EXAMPLE CODE CAN BE FOUND BELOW
# LOAD DATA TO MYSQL DB
from sqlalchemy import create_engine
import pymysql
 
# CONNECTION OPTION 1: READ CONNECTION DETAILS FROM TXT FILE (STORED IN SAME PATH AS THIS SCRIPT)
# YOU NEED TO CREATE THE TXT FILE YOURSELF. IT NEEDS TO CONTAIN THE CREDENTIALS THAT ARE INSERTED IN OPTION 2 BELOW
f = open("[INSERT_FILE_NAME].txt", "r")
sql_conn = f.read()
conn = create_engine(sql_conn)
 
# CONNECTION OPTION 2: INSIDE THE CODE
conn = create_engine("mysql+pymysql://[INSERT_USER]:[INSERT_PASSWORD]@[INSERT_HOST]/[INSERT_DATABASE_NAME]")
#Example: conn = create_engine("mysql+pymysql://root:PassWord123!@localhost/my_database")
 
# WRITE DATAFRAME INTO DB TABLE
df2.to_sql(name='[TABLE_NAME]', con=conn, if_exists = 'replace', index=False)
 
# SQL QUERY TO VALIDATE DATA LOAD
frame = pd.read_sql("select * from [INSERT_DATABASE_NAME].[TABLE_NAME]", con=conn)
print(frame.head())