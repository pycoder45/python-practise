print("\n \t •-- Welcome To Coding Academy --•")
print("\t  [ LOGIN ]    ||    [ SIGN UP ] \n ")

# User Login Details
u_data = {
  "du_name" : [],
  "du_email" :  [],
  "du_password" : []
}

import os 
import pickle

#--------------------------------------------
# Checking whether user is Exited Or Not

if os.path.isfile("userData1.txt") == False : 
  fileToStore = open("userData1.txt","wb")
  pickle.dump(u_data,fileToStore)
  fileToStore.close()
  print("New User Created")
else : 
  print("Existed User Found")

fileToOpen = open("userData1.txt","rb")

#--------------------------------------------
# Taking Input From User
def u_com(): 
  print("* Commands Of The Coding Academy are Below --->\n • Login To Account : L | l \n • Create New Account : N | n \n • To See Commands : C | c \n • Exit From Account : -1 ")
u_com()
print("")
login_signup = input("~ ")

#--------------------------------------------

while login_signup != "-1" : 
  
# Conditions For Login and SignUp

  if login_signup == "L" or login_signup == "l" : 
    
    def fun_login() :
      print("\t{ Welcome Again To Coding Academy } \n ")
      l_email = input("• Email    : ")
      l_email = l_email.lower()
      l_password = input("• Password : ")
      
      spUDO = pickle.load(fileToOpen)
      
      if spUDO["du_email"].count(l_email.strip()) == 1 : 
        if spUDO["du_password"][spUDO["du_email"].index(l_email.strip())] == l_password : 
          print("\n\t Logged In Successfully ✓ !\n")
        else :
          print("\n\t --Please Enter Your Password Correct--\n")
      else : 
        print("\t\t !! Account Not Found !! \n\t --Please Check Your Email Address and Password-- \n\t\t\t OR \n\t\t •|CREATE A NEW ACCOUNT|• \n")
      
    fun_login()

  elif login_signup == "N" or login_signup == "n" :
 
    def fun_signup() : 
      print("\t{ Welcome To Coding Academy }","\n")
      s_name =  input("• Name     : ")
      s_email = input("• Email    : ")
      s_password = input("• Password : ")
      
      
      fileToStore = open("userData1.txt","rb")
      storeD = pickle.load(fileToStore)

      storeD["du_name"].append(s_name.strip())
      storeD["du_email"].append(s_email.strip().lower())
      storeD["du_password"].append(s_password)

      print("\n\tWell Done || Account Successfully Created ! \n ") 
  
      print(f"\t\t Welcome ",s_name.upper(), "\n\t |•• Let's Explore and Enjoy ••|\n\t |-- The World Of Programming--|\n ") 

    fun_signup()

  elif login_signup == "C" or login_signup == "c" :
    # For Users, to see commands
    u_com()
  
  else : 
    print("\tSorry, You Missed Something :( ")
    print("\tPlease enter command correctly ! \n ")

  login_signup = (input("~ "))
  
print("\t •---| Exit Successfully |---•\n ")

#--------------------------------------------
