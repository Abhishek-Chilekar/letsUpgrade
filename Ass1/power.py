while True:
    number = int(input("Enter the number "))
    power = int(input("Enter the power "))
    result = 1
    for i in range(0,power):
        result = result * number
    print(f'{number} ^ {power} is {result}')
    
    choice = input("Want to continue ? (y/n) : ").lower()
    if(choice == 'y'):
      break;