class Person:

    @staticmethod
    def calculators():

        # functions
        def addition(num1, num2):
            return num1 + num2

        def subtract(num1, num2):
            return num1 - num2

        def multiplication(num1, num2):
            return num1 * num2

        def divide(num1, num2):
            return num1 / num2

        operations_symbol = {
            "+": addition,
            "-": subtract,
            "/": divide,
            "*": multiplication
        }
    # first calculation
        n1 = int(input("Write number 1: "))
        operation = input('Write operation symbol (+ , - , * or / ): ')
        n2 = int(input("Write number 2: "))

        my_operation = operations_symbol[operation]
        answer = my_operation(n1, n2)

        print(f'{n1} {operation} {n2} is equal {answer}')

    # second calculation
        new_n1 = int(input("Write another number: "))
        new_operation = input('Write operation symbol (+ , - , * or / ): ')

        new_my_operation = operations_symbol[new_operation]
        new_answer = new_my_operation(answer, new_n1)

        print(f'{answer} {new_operation} {new_n1} is equal {new_answer}')


