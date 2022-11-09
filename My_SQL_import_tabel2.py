import mysql.connector
import GuiDBConfig as guiConf

GUIDB = 'GuiDB'

# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)

cursor = conn.cursor()

cursor.execute("USE guidb")
# cursor.execute("CREATE TABLE Books (         \
#         Book_ID INT NOT NULL AUTO_INCREMENT, \
#         Book_Title VARCHAR(25) NOT NULL,     \
#         Book_Page INT NOT NULL,              \
#         PRIMARY KEY (Book_ID)                \
#     ) ENGINE=InnoDB")

# create second Table inside DB
cursor.execute("CREATE TABLE Quotations (    \
        Quote_ID INT AUTO_INCREMENT,         \
        Quotation VARCHAR(250),              \
        Books_Book_ID INT,                   \
        PRIMARY KEY (Quote_ID),              \
        FOREIGN KEY (Books_Book_ID)          \
            REFERENCES Books(Book_ID)        \
            ON DELETE CASCADE                \
    ) ENGINE=InnoDB")

# show Tables from guidb DB
cursor.execute("SHOW TABLES FROM guidb")
print(cursor.fetchall())

conn.close()