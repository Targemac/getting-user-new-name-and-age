default_name = 'charles';
default_age = 26;

change_name = str(input("Enter new name: "))
change_age = int(input("Enter new age: "))


if change_name == default_name:
    print("Cannot use " + default_name + ' as new name !' + ' already taken.')
    change_name = str(input("Enter new name: "))
elif change_age == default_age:
    print("Cannot use " + default_age + ' as new age !' + ' already taken.')
    change_age = int(input("Enter new age: "))
else:
    new_name = change_name
    new_age = change_age
    file = open( new_name + '.txt', 'w')
    file.write('New name: ' + new_name + ', New age: ' + str(new_age) + '. is a good student.')
    file.close()
    print("New details accepted, file created succesfully")
    
