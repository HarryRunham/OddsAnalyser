# NOTES
# 
# When done add comments.
#
# Could improve MatrixPrint but at that point I think using TextTable would just be better
# 
# Could add a converter so the user doesn't have to convert the odds themselves. Should really do this.
# 
# Am going to make huge changes to INPUT RECEPTION, PROCESSING AND VALIDATION to complete the above. Upload to GitHub before doing this.

# ------------------------------
# FUNCTIONS
# ------------------------------

def MatrixPrint(list):
    print("Name, Team 1 Bet Criterion, Team 2 Bet Criterion")
    i = 0
    while i < len(list):
        j = 0
        row = ""
        while j < len(list[i]):
            row += list[i][j] + 7*" "
            j += 1
        print(row)
        i += 1

# ------------------------------
# INITIALISATION AND WELCOME
# ------------------------------

program_exit_confirmation = False
all_results_matrix = []

print(3*"\n")
print("Welcome to your betting analyser. ")

# ------------------------------
# MAIN BODY
# ------------------------------

while program_exit_confirmation == False:

# ------------------------------
# INPUT RECEPTION, PROCESSING AND VALIDATION
# ------------------------------
    
    print()
    print("If the odds you are presented with are fractional, represent that fraction as a decimal and add 1 to achieve its decimal form. ") # DELETE AFTER DIFFERENT FORMS SUPPORTED
    print("If you are presented with moneyline odds x, represent x/100 as a decimal and add 1 to achieve its decimal form. ") # DELETE AFTER DIFFERENT FORMS SUPPORTED

    variable_check_done = False
    value_check_done = False
    


    # print("Decimal odds look like: 1.45, 2.55")
    # print("Fractional odds look like: 45/100, 155/100")
    # print ("Moneyline odds look like: +45, +155") - NVM, HOW I THOUGHT THEY WORKED WAS INCORRECT, NEED TO RECTIFY ESPECIALLY BEFORE ADDING A CONVERTER, USE https://www.aceodds.com/bet-calculator/odds-converter.html
    # odds_form_chosen = False
    # while odds_form_chosen = False:
    #     odds_form_choice = input("What form are the odds in? ")
    # SWITCH CASE STATEMENT (OR EQUIVALENT) HERE, TO CHOOSE BETWEEN WHICH WHILE LOOP TO USE TO PROCESS THE INPUT - THEN HAVE THE VALUE CHECK AS BEING SEPARATE AFTER THE VARIABLE CHECK WHILE LOOPS (THERE SHOULD BE 3 OF THEM) 


    while variable_check_done == False or value_check_done == False: # This loop can only be exited if both the variables are true. value_check_done can only become true if variable_check_done is true. therefore you could have this as simply being value_check_done == False, but I will leave it as is for code readability.

        variable_check_done = False
        value_check_done = False
        
        print()
        odds1_raw = input("Enter the odds for team 1 in decimal form: ")
        odds2_raw = input("Enter the odds for team 2 in decimal form: ")
        
        try:
            # Try converting input into floats.
            odds1 = float(odds1_raw)
            odds2 = float(odds2_raw)
        except:
            # The values input failed to be converted; the user messed up in some way.
            try:
                # Strip input of all characters except for digits and periods, then try converting into floats.
                odds1 = float("".join(filter(lambda x: x.isdigit() or x == ".", odds1_raw)))
                odds2 = float("".join(filter(lambda x: x.isdigit() or x == ".", odds2_raw)))
            except:
                # One or more of the values contained more than one period, or no period at all. Not worth going through every possible value the user could have meant to input - just return to ask for input again.
                print("\n" + "Both inputs must contain digits and exactly one period each.")
            else:
                # The values were succesfully cleaned. Check that the result is the values the user meant to submit.
                confirmation_check_done = False
                while confirmation_check_done == False:
                    confirmation = input("\n" + "Are these the correct odds? Enter Y or N. Value 1: " + str(odds1) + " Value 2: " + str(odds2) + " ")
                    if confirmation == "Y":
                        confirmation_check_done = True
                        variable_check_done = True
                        # This allows both while loops to end, releasing control to the rest of the program.
                    elif confirmation == "N":
                        confirmation_check_done = True
                        # variable_check_done remains False, allowing the user to enter new odds.
                    else:
                        print("\n" + "Please enter Y or N." + "\n")
                        # confirmation_check_done remains False, prompting the user to respond correctly.
        else:
            # The values input were successfuly converted into floats. Assume correct input.
            variable_check_done = True
        
        if variable_check_done == True:
            if odds1 >= 1 and odds2 >= 1:
                value_check_done = True
            else:
                print("\n" + "The odds are invalid - they should both be more than or equal to 1. Please re-enter the odds. ")

# ------------------------------
# ANALYSIS CALCULATIONS
# ------------------------------

    # Analysis algorithm is my own work.

    team1_bet_criterion = 100*(1/odds1)
    team1_bet_criterion_formatted = round(team1_bet_criterion, 2)

    if team1_bet_criterion_formatted < team1_bet_criterion:
        team1_bet_criterion_formatted = round(team1_bet_criterion_formatted + 0.01, 2)
    
    team1_bet_criterion_formatted = str(team1_bet_criterion_formatted) + str("%")
    
    team2_bet_criterion = 100*(odds2 - 1)/odds2
    team2_bet_criterion_formatted = round(team2_bet_criterion, 2)

    if team2_bet_criterion_formatted > team2_bet_criterion:
        team2_bet_criterion_formatted = round(team2_bet_criterion_formatted - 0.01, 2)
    
    team2_bet_criterion_formatted = str(team2_bet_criterion_formatted) + str("%")

    print()
    name_of_site = input("Enter a name for this analysis. ")

    all_results_matrix.append([name_of_site, "p > " + team1_bet_criterion_formatted, "p < " + team2_bet_criterion_formatted])

# ------------------------------
# ANALYSIS RESULT OUTPUT
# ------------------------------

    print("\n" + "The following probabilities are rounded to 2 decimal places. ")
    print("Let p be the probability of team 1 winning. ")
    print("\n" + "Bet on team 1 if you believe p is more than " + team1_bet_criterion_formatted)
    print("Bet on team 2 if you believe p is less than " + team2_bet_criterion_formatted)

    print("\n" + "All other things remaining equal, you should bet on the site that provides the best odds. All analysis results so far: ")

    print()
    MatrixPrint(all_results_matrix)

    program_exit_check_done = False

    while program_exit_check_done == False:
        program_exit_answer = input("\n" + "Would you like to continue or exit the program? Enter C or E. ")
        if program_exit_answer == "E":
            program_exit_check_done = True
            program_exit_confirmation = True
        elif program_exit_answer == "C":
            program_exit_check_done = True
        else:
            print("\n" + "Please enter C or E.")

print("\n" + "Thankyou for using this betting analyser. Good luck with your bets! ")