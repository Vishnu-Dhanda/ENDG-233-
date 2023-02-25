# calculator.py
# Vishnu Dhanda, 30145576, ENDG 233 F21

# User Input and assigning of variables to user inputs.
value_one = int(input('Enter the first value: '))       #prompts user to enter first integer 
operator_one = input('Enter the first operator: ')      #prompts user to enter first operator
value_two = int(input('Enter the second value: '))      #prompts user to enter second integer
operator_two = input('Enter the second operator: ')     #prompts user to enter second operator
value_three = int(input('Enter the third value: '))     #prompts user to enter third integer

# Since 2 operators are used out of the possible 4 for each calculation there are 16 possible combinations.

# Possible combinations of operations are: (*,*), (/,/), (*,/), (/,*), (+,+), (-,-) (+,*), (*,+), (+,/), (/,+),
# (-,*), (*,-), (-,/), (/,-), (+,-) and (-,+).

#Depending on the input of operators the following operations are carried out.
if operator_one == '*' and operator_two == '*':                     #(*,*)
    final_answer = (value_one * value_two * value_three)

elif operator_one == '/' and operator_two == '/':                   #(/,/)
    final_answer = (value_one // value_two // value_three)

elif operator_one == '*' and operator_two == '/':                   #(*,/)
    final_answer = ((value_one * value_two) // value_three)

elif operator_one == '/' and operator_two == '*':                   #(/,*)
    final_answer = ((value_one // value_two) * value_three)

elif operator_one == '*' and operator_two == '+':                   #(*,+)
    final_answer = ((value_one * value_two) + value_three)

elif operator_one == '+' and operator_two == '*':                   #(+,*)
    final_answer = (value_one + (value_two * value_three))

elif operator_one == '*' and operator_two == '-':                   #(*,-)
    final_answer = ((value_one * value_two) - value_three)

elif operator_one == '-' and operator_two == '*':                   #(-,*)
    final_answer = (value_one - (value_two * value_three))

elif operator_one == '/' and operator_two == '+':                   #(/,+)
    final_answer = ((value_one // value_two) + value_three)

elif operator_one == '+' and operator_two == '/':                   #(+,/)
    final_answer = (value_one + (value_two // value_three))

elif operator_one == '/' and operator_two == '-':                   #(/,-)
    final_answer = ((value_one // value_two) - value_three)

elif operator_one == '-' and operator_two == '/':                   #(-,/)
    final_answer = (value_one - (value_two // value_three))

elif operator_one == '+' and operator_two == '+':                   #(+,+)
    final_answer = (value_one + value_two + value_three)

elif operator_one == '-' and operator_two == '-':                   #(-,-)
    final_answer = (value_one - value_two - value_three)

elif operator_one == '+' and operator_two == '-':                   #(+,-)
    final_answer = ((value_one + value_two) - value_three)

elif operator_one == '-' and operator_two == '+':                   #(-,+)
    final_answer = ((value_one - value_two) + value_three)

# Displaying the complete expression entered by the user.
print('Entered expression:', value_one, operator_one, value_two, operator_two, value_three)

# Displaying the final answer calculated by the program.
# Using int to ensure that final_answer remains in a integer format.
print('Your final answer =', int(final_answer) )

# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.