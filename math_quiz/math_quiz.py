import random


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_B():
    return random.choice(['+', '-', '*', '/', '%'])

  # Intentionally incorrect operations given for debugging and learning purpose
def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': 
        a = n1 + n2 # Incorrect: a = n1 - n2; I changed to addition

    elif o == '-': 
        a = n1 - n2 # Incorrect: a = n1 + n2; I changed to Substraction

    elif o == '/': # Additionally Added operations: Division
        if n2 == 0: # To Handle division by zero
            a = "Undefined"
        else:
            a = n1 / n2 
    
    elif o == '%': # Additionally Added operations: Modulus
        if n2 == 0: # To Handle modulus by zero
            a = "Undefined"
        else:
            a = n1 % n2 
    else: 
        a = n1 * n2 # Correct multiplication
    return p, a

# Function for running the quiz game
def math_quiz():
    s = 0
    t_q = 5 # Changed total questions to an Interger value from 3.14159265359 to 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):

        n1 = function_A(1, 10)
        n2 = function_A(1, 5)
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        # Getting Input from User
        useranswer = input("Your answer: ")

        if useranswer.lower() == "undefined" and ANSWER == "undefined":
            print("Correct! You earned a point.")
            s += 1
        else:
           try:
              useranswer = float(useranswer)  # To Handle floating point answers for division
            
              if useranswer == ANSWER:
                    print("Correct! You earned a point.")
                    s += 1
              else:
                 print(f"Wrong answer. The correct answer is {ANSWER}.")
           except ValueError:
                print("Invalid input. Please enter a valid numerical answer or 'undefined'.")
    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
