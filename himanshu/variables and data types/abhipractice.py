arn = "arn:aws:iam::123456789012:user/johndoe"
print(arn.split("/")) #this will split our arn into 2 parts - 0,1

a = arn.split("/")[1]
print(a) #this will print only our arn
print(a.upper()) #this will change the arn number to upper case
