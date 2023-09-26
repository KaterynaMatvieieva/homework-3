# Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо

# try:
#     print("Enter any number from 1 to 7 to show corresponding name of the weekday")
#
#     weekday=int(input("(For example 1 for Monday, 2 for Tuesday etc.):"))
#
#     match weekday:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")
#         case 7:
#             print("Sunday")
#         case _:
#             raise Exception("You have not entered the number from the specified range. Please try again")
#
# except ValueError as e:
#     print("Enter only integer numbers please")
#     print(f"ValueError: {e}")
# except Exception as e:
#     print(f"Error: {e}")



#Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

# try:
#     print("Enter two numbers for comparison and displaying them in the order of growth")
#     number1 = float(input("Number 1 is:"))
#     number2 = float(input("Number 2 is:"))
#
#     if number1 == number2:
#         print("Numbers are equal")
#     elif number1 > number2:
#         print(number2, number1)
#     else:
#         print(number1, number2)
# except ValueError as e:
#     print("Enter only numeric values please")
#     print(f"Error: {e}")



# Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат
#
# try:
#     print("Enter two numbers")
#     number1 = float(input("Number 1 is:"))
#     number2 = float(input("Number 2 is:"))
#
#     print("Enter + to find the sum of entered numbers\nEnter - to find the difference of entered numbers\nEnter * to find the product of entered numbers\nEnter / to find the division of entered numbers")
#     user_select = input("Enter required operation: ")
#
#     match user_select:
#         case "+":
#             sum = number1 + number2
#             print(f"The sum of entered numbers is: {sum}")
#         case "-":
#             dif = number1 - number2
#             print(f"The difference of entered numbers is: {dif}")
#         case "*":
#             product = number1 * number2
#             print(f"The product of entered numbers is: {product}")
#         case "/":
#             div = number1 / number2
#             print(f"The division of entered numbers is: {div}")
#         case _:
#             raise Exception("Entered one of the symbols described above please")
#
# except ValueError as e:
#     print("Enter only numeric values please")
#     print(f"Error: {e}")
# except ZeroDivisionError as e:
#     print("It is not allowed to divide by 0. Please try another values or another operation")
#     print(f"ZeroDivisionError occurred: {e}")
# except Exception as e:
#     print(f"Error: {e}")




