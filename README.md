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

lst = {
    "Amal" : "1111111111",
    "Mohammed" : "2222222222",
    "Khadijah" : "3333333333",
    "Abdullah" : "4444444444",
    "Rawan" : "5555555555",
    "Faisal" : "6666666666",
    "Layla" : "7777777777",
      }
i = True
numberExists = False
while i == True:
    userAnput = input("Please enter the phone number ")
    for n in lst:
        phone = lst.get(n)
        if (len(userAnput) < 10):
            print ("This is invalid number")
        
        elif not(userAnput.isdigit()): 
            print ("This is invalid number")
    
    
        for num in lst:
            if (lst.get(num) == userAnput):
                print(num)
                numberExists = True
                break
           
        if(numberExists == True):
             break
                
        else:
            print("Sorry, the number is not found")
            break

