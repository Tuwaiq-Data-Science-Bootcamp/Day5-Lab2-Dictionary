'''
| Name    | Number      |
| -------- | ---------- |
| Amal     | 1111111111 |
| Mohammed | 2222222222 |
| Khadijah | 3333333333 |
| Abdullah  | 4444444444 |
| Rawan    | 5555555555 |
| Faisal   | 6666666666 |
| Layla    | 7777777777 |'''

phone_book : dict = {1111111111 : 'Amal', 2222222222 : 'Mohammed' , 3333333333 : 'Khadijah', 4444444444 : 'Abdullah', 5555555555 : 'Rawan', 6666666666 : 'Faisal', 7777777777 : 'Layla'}

# - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
for k, v in phone_book.items():
    number : int = input('Enter the number : ')
    #If the number is less or more than 10 numbers, print "This is invalid number".
    if len(str(number)) == 10:
        number = int(number)
        if k in phone_book:
            print(f'The owner is {phone_book[number]}')
        else:
            ('Sorry, the number is not found')
    #If the number contains letters or symbols, print "This is invalid number".
    else:
        print('This is invalid number')
    break

   


