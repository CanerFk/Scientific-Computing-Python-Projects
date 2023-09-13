def arithmetic_arranger(problems, showAnswer=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arrangedProblems = []
    arrangedAnswers = []
    firstLine = []
    secondLine = []
    dashes = []

    for p in problems:
        parts = p.split()
        if len(parts) != 3:
            return "Error: Each problem should have two operands and an operator"
        
        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        maxWidth = max(len(num1), len(num2)) + 2
        firstLine.append(num1.rjust(maxWidth))
        secondLine.append(operator + num2.rjust(maxWidth - 1))
        dashes.append("-" * maxWidth)

        num1, num2 = int(num1), int(num2)
        if operator == '+':
            answer = num1 + num2
        else:
            answer = num1 - num2
        answerLine = str(answer).rjust(maxWidth)
        arrangedAnswers.append(answerLine)
        if showAnswer:
            arrangedProblems = "    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(dashes) + "\n" + "    ".join(arrangedAnswers)
        else:
            arrangedProblems = "    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(dashes)
    return arrangedProblems

