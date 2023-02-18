def arithmetic_arranger(problems, show_answer=False):
    import re
    # Error checking
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        if not re.match(r"^\d+\s*[+\-\*/]\s*\d+$", problem):
            return "Error: Numbers must only contain digits."
        
        num1, operator, num2 = re.split(r"\s*([+\-\*/])\s*", problem)
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
    
    # Calculation and formatting
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []
    
    for problem in problems:
        num1, operator, num2 = re.split(r"\s*([+\-])\s*", problem)
        max_width = max(len(num1), len(num2)) + 2
        
        first_line.append(num1.rjust(max_width))
        second_line.append(operator + num2.rjust(max_width-1))
        dash_line.append("-" * max_width)
        
        if show_answer:
            if operator == "+":
                answer = int(num1) + int(num2)
            else:
                answer = int(num1) - int(num2)
            answer_line.append(str(answer).rjust(max_width))
    
    # Output formatting
    arranged_problems = []
    arranged_problems.append("    ".join(first_line))
    arranged_problems.append("    ".join(second_line))
    arranged_problems.append("    ".join(dash_line))
    
    if show_answer:
        arranged_problems.append("    ".join(answer_line))
    
    return "\n".join(arranged_problems)
