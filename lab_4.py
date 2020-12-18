"""
This program allows a user three tries to uess the correct answer to the question
the question is "what is the capital of California?" the answer is "Sacramento"
we first set max_tries = 3. Then we create a loop to iterate 3 times.
for each iteration, we ask the user for the answer (user input). then based on the answer the user gives,
we check to see if the user input matches the answer. if so, print "Correct!", then terminatethe loop with a break statement.
if the user could not guess the correct answer within the max_tries, print
"You have used up your allotment of guesses.",
then print "The correct answer is Sacramento."

"""
"""
main
    question = "What is the capital of California?"
    answer = "Sacramento"
    ask(question, answer)
ask
    tries = 0
    loop thrre times
        increment tries
        ask user input ()
        check to see if user input is equal to answer
            if so, print "Correct!", then exit loop
    if not correct
       print to the user "You have used up your allotment of guesses."
       print "the correct snwer is Sacramento."
"""

def main():
    question = "What is the capital of California?"
    answer = "Sacramento"
    ask(question, answer)

    def ask(question, asnwer, max_tries = 3):
        tries = 0
        ans = ""
        while tries < max_tries:
            tries += 1
            ans = input(question)
            if ans == answer:
                print("Correct!")
                break
        if ans != answer:
            print("You have used up your allotment of guesses.")
            print("The correct answer is Sacramento.")
    main()            
