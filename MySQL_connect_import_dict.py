import mysql.connector
import GuiDBConfig as guiConf

# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)
print(conn)