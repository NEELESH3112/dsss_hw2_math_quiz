import random

def generate_number(min, max):
    """
    Generate a random integer between min and max.
    """
    return random.randint(min, max)

def choose_operator():
    """
    Select a random math operator.
    """
    return random.choice(['+', '-', '*', '/', '%'])

def calculate(n1, n2, operator):
    """
    Calculate the result of applying an operator to two numbers.
    """
    expression = f"{n1} {operator} {n2}"
    if operator == '+': 
        result = n1 + n2
    elif operator == '-': 
        result = n1 - n2
    elif operator == '/':
        result = "Undefined" if n2 == 0 else n1 / n2
    elif operator == '%':
        result = "Undefined" if n2 == 0 else n1 % n2
    else:
        result = n1 * n2
    return expression, result

# Function for running the quiz game
def math_quiz():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems. Provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_number(1, 10)
        num2 = generate_number(1, 5)
        operator = choose_operator()

        problem, correct_answer = calculate(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Getting Input from User
        user_answer = input("Your answer: ")
        if user_answer.lower() == "undefined" and correct_answer == "undefined":
            print("Correct! You earned a point.")
            score += 1
        else:
            try:
                user_answer = float(user_answer)
                if user_answer == correct_answer:
                    print("Correct! You earned a point.")
                    score += 1
                else:
                    print(f"Wrong answer. The correct answer is {correct_answer}.")
            except ValueError:
                print("Invalid input. Please enter a valid numerical answer or 'undefined'.")
                
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()

