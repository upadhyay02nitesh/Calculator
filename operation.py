from main import *
def main():
    while True:
        
        try:
            print("****************WELCOME TO MINI CALCULATOR****************")
            print("PRESS 1 TO ADD")
            print("PRESS 2 TO substract")
            print("PRESS 3 TO MULTIPLICATION ")
            print("PRESS 5 TO DIVIDE")
            print("PRESS 6 TO MODULE")
            print("PRESS 7 TO POWER")
            print("PRESS 8 TO FLOORVALUE")
            print("PRESS 9 TO break the program")
            print()
        
        
            num1=int(input("Enter the first number -> "))
            num2=int(input("Enter the second number -> "))
            choice=input("Enter the choice ->")
            
            if choice=="1":
               add(num1,num2)
               break
            elif choice=="3":
                sub(num1,num2)
                break
            
            elif choice=="4":
                multi(num1,num2)
                break
            elif choice=="5":
                divide(num1,num2)
                break
            elif choice=="6":
                module(num1,num2)
                break
            elif choice=="7":
                power(num1,num2)
                break
            elif choice=="8":
                Floorvalue(num1,num2)
                break
            elif choice=="9":
                break
            else:
               print("INVALID input")
        
        except Exception as e:
                print(e)
                print("INVALID INPUT !!!")
        
    
if __name__=="__main__":
    main()