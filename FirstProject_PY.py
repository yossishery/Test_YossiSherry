import requests
import json
import mysql.connector

##DEFINE THE DATABASE CREDENTIALS
# user = 'interview_user'
# password = 'aviv_2021_07_06_!!@@QQ'
# host = '104.197.7.195'
# port = '3306'
# database = 'interview'


def InsertData(myCursor,mydb, data, table_name):
   for OneUser in data:
      #start off your query string
      queryInsert = 'Insert into ' + table_name +' ('
      ValINRow = []
      first_item = True
      for Column in OneUser:
         Column_validate = OneUser.get(Column, None)
         if (type(Column_validate) == dict):
            #print("dict")
            for key, value in Column_validate.items():
               if (type(value) == dict): #case of location-> street
                  #print("street", key, value)
                  if(key == "street"):
                     ValINRow.append(str(value["number"]))
                     queryInsert += "," +str(Column) + "_" + str(key) + "_number"

                     ValINRow.append(value["name"])
                     queryInsert += ", " + str(Column) + "_" + str(key) + "_name"

                  elif(key == "coordinates"):
                     ValINRow.append(value["latitude"])
                     queryInsert +=', '+str(Column) + "_" + str(key) + "_" + "latitude"
                                          #location             #coordinates
                                          # "country": "Turkey", = בעצם טורקיה משמשת ערך

                     ValINRow.append(value["longitude"])
                     queryInsert +=  ', '+str(Column) + "_" + str(key) + "_" + "longitude"

                  elif (key == "timezone"):
                   ValINRow.append(value["offset"])
                   queryInsert += ', ' + str(Column) + "_" + str(key) + "_" + "offset"
                   ValINRow.append(value["description"])
                   queryInsert += ', ' + str(Column) + "_" + str(key) + "_" + "description"

               else:
                  if(value==None):
                     value = "null"
                  ValINRow.append(value)
                  queryInsert += ', '
                  queryInsert += str(Column) + "_" + str(key)

         else:
            ValINRow.append(Column_validate)
            if not first_item:
               #add a comma and space to the query if it's not the first item
               queryInsert += ', '
            #add the field name to the query
            queryInsert += Column
         # mark that it's no longer the first item
         first_item = False

         #finish off the query string
      queryInsert += ') VALUES {}'

      #print(queryInsert.format(tuple(ValINRow)))

      myCursor.execute(queryInsert.format(tuple(ValINRow)))
   mydb.commit()



########################## Main  ##########################
users_data = requests.get('https://randomuser.me/api/?results=4500').json()

UsersAllUsers = []
male_data = []
female_data = []

for user in users_data["results"]:
      UsersAllUsers.append(user)

#print_Pretty_UsersAllUsers

#json_user_data = json.dumps(users_data,indent=2)
#print(json_user_data)

for user in users_data["results"]:
      if user['gender'] == 'male':
         male_data.append(user)
      elif user['gender'] == 'female':
            female_data.append(user)


#print_Pretty_Male_data_&&_Female_data

#Male_data_Pretty = json.dumps(male_data,indent=2)
#Female_data_Pretty = json.dumps(female_data,indent=2)
# print(Male_data_Pretty)
# print(Female_data_Pretty)

try:
   mydb = mysql.connector.connect(host='104.197.7.195',user='interview_user',password='aviv_2021_07_06_!!@@QQ',port='3306',database='interview')
   print('Log in successfully')

   #myCursor = mydb.cursor()
   myCursor_Dict = mydb.cursor(dictionary=True)

   #checks
   #print ('Open curser')
   #myCursor.execute('show tables')
   #for i in myCursor:
      #print(i)

    #call to Func
   # InsertData(myCursor,mydb, UsersAllUsers   ,"YossiSherry_AllUsers")
   # InsertData(myCursor,mydb, male_data    ,"YossiSherry_test_male")
   # InsertData(myCursor, mydb, female_data , "YossiSherry_test_female")

except Exception as ex:
          print("Connection could not be made due to the following error: \n",ex)




#######################query####################

select_first ="""
         /*6_union*/
         select  *
         from
                 (
                 select distinct * from YossiSherry_Test_20
                 union
                 select distinct * from YossiSherry_Test_5
                 ) as d
         order by name_first ;
         
         """

select_second = """
         /*7_unionAll*/
         select *
         from

         (
         select * from YossiSherry_Test_20
         union all
         select * from YossiSherry_Test_5
         ) as d
         order by name_first ;

         """


#########################first.json##################################
myCursor_Dict.execute(select_first)
result_select = myCursor_Dict.fetchall() #run THE Query and return result
#print(result_select)

json_result_select = json.dumps(result_select,indent=2)
#print(json_result_select)

#json_string variable
with open('first.json', 'w') as outfile:
   outfile.write(json_result_select)


#########################Second.json##################################
myCursor_Dict.execute(select_second)
result_select = myCursor_Dict.fetchall() #run THE Query and return result
#print(result_select)

json_result_select = json.dumps(result_select,indent=2)
#print(json_result_select)

#json_string variable
with open('Second.json', 'w') as outfile:
   outfile.write(json_result_select)


mydb.close()


########################## END Main  ##########################












