# Day5-Lab2-Dictionary

Build a phone book program that receives the phone number, and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 1111111111 |
| Mohammed | 2222222222 |
| Khadijah | 3333333333 |
| Abdullah  | 4444444444 |
| Rawan    | 5555555555 |
| Faisal   | 6666666666 |
| Layla    | 7777777777 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".


def getNum(numValue): 
                    
                    phonebook_name  = ["Amal","Mohammed","Khadijah","Abdullah","Rawan","Faisal","Layla"]
                    phonebook_num = [1111111111,2222222222,3333333333,4444444444,5555555555,6666666666,7777777777]
                    name="Sorry, the number is not found"
                    for i in phonebook_num :
                                            if i==numValue:  
                                                          nameIndex=phonebook_num.index(i) 
                                                          name= 'The name is: '+phonebook_name[nameIndex]
                                                          
                                          
                                                

                    return name
    

numValue = 0
numValue=input("Enter a  phone number:")
while str(numValue).isdigit()==False or int(numValue)<=0 or int(numValue)<=999999999 or int(numValue)>10000000000 :
                  numValue=input("This is invalid number\nEnter a valid phone number:")
                   
if int(numValue)>0:  
              print(getNum(int(numValue)))
              
