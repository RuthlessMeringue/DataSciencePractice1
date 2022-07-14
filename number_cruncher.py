''' Basic Number Cruncher including unittest code
Step 1: Add two numbers include test code and range and exception handling
Step 2: Subtract two numbers inlcude test code and range and exception handling
Step 3: square two numbers and subtract include test code and  range and exception handling
step 4: include float date types'''

def main():
    
    def addition():
        result_addition = 0
        while True:
            try:
                first_input = int(input('Please give a whole number between 0 and 10: '))
                break
            except ValueError:
                print('Thats not a whole number in range, try again')
        while True:
            try:
                second_input = int(input('another whole number please: '))
                break
            except ValueError:
                print('Thats not a whole number in range, try again')                  
        result_addition = first_input + second_input
        print('the sum of:', first_input, 'and', second_input, 'is', result_addition)
    addition()
    

main()
