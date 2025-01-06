import mysql.connector



DBUrl = "localhost"
DBUser = "root"
DBPass = "root"
DBName = "shopbotdb"

dbconnect = mysql.connector.connect(user=DBUser,password=DBPass,host=DBUrl,database=DBName)
cursor = dbconnect.cursor()


def addUserId(message):
	query = f'INSERT INTO users(id) VALUES ("{message.chat.id}")'
	try:
		cursor.execute(query)
	except:
		print("Allready exist!")
	dbconnect.commit()
	

def getUserBalance(message):
	query = f"SELECT * FROM users WHERE id='{message.chat.id}'"
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		fresult = result['balance']
		return result
	except:
		return "Unexpected error"
	
def getuserid(message):
	# query = f"SELECT * FROM users WHERE id='{message.chat.id}'"
	try:
		select_all_rows = f"SELECT id, balance FROM users WHERE id='{message.chat.id}'"
		# select_all_rows = f"SELECT id, balance FROM users WHERE id ='{message.chat.id}'"
		cursor.execute(select_all_rows)
		rows = cursor.fetchall()
		for row in rows:
			return " " + 'Id -' + " " + str(row[0]) + " | " + "Баланс -" + " " + str(row[1])

	except:
		return 'Ошибка'


    


