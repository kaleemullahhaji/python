num_of_tries = 0
while num_of_tries !=3:
    username = input('please insert username : ')
    password = input('please insert password : ')
    if username == 'kaleem' and password == '123':
        print('welcome in web')
        num_of_tries = 0
        exit()
    else:
        print('Error')
        num_of_tries = num_of_tries +1
        print('you have ' + str(3-num_of_tries) + ' lift')
