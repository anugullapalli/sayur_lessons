
user_email=input("Enter the email:")
char = "@"
user_pwd = input("Enter the password:")
valid_flag = True

if char not in user_email:
    valid_flag = False
    print("Email not valid")

parts1= user_email.split("@")

username=parts1[0]  
parts2=parts1[1].split(".")
company=parts2[0]
end=parts2[1] 

if end not in ("org","com","tech","edu"):
    print("Email not valid")

password_begin = username[0]+username[2] + username[-3:] + company[:3] 

user_last3 = user_pwd[-3:]

if not user_pwd.startswith(password_begin):
    print("password is not valid")

if not user_last3.isdigit():
    print("password does not end with 3 digits")