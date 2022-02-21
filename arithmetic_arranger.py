def arithmetic_arranger(problems, calcul = False):
    for problem in problems:
        problem = problem.split()
        line_length = max([len(item) for item in problem])
        first_operand = problem[0]
        second_operand = problem[2]
        operator = problem[1]
        print(first_operand.rjust(line_length + 2 , ' ') + "\n" + operator + " " + second_operand.rjust(line_length, ' ') + "\n" + "-"*(line_length+2))
        if (calcul):
            if (operator == "+"):
                result = int(problem[0]) + int(problem[2])
                print(str(result).rjust(line_length + 2, ' '))
            elif (operator == "-"):
                result = int(problem[0]) - int(problem[2])
                print(str(result).rjust(line_length + 2, ' '))
        print("\n")
        

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)