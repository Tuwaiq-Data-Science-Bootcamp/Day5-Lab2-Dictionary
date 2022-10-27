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

def phone_book():
        number = input('Enter The Required Number\n')
        number = str(number)
        num_len = len(number)
        phone_book = {'1111111111' :'Amal' ,
                '2222222222' : 'Mohammed',
                 '3333333333' : 'Khadijah',
                 '4444444444' : 'Abdullah' ,
                 '5555555555' :'Rawan',
                 '6666666666' : 'Faisal',
                 '7777777777' : 'Layla'}


        klist = list(phone_book.keys())
        vlist = list(phone_book.values())
        
        if num_len != 10 or type(number) == int  :
            print('This is invalid number')
            
        else:
            pos = klist.index(number)
            print(vlist[pos])
phone_book()
