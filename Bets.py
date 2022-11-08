# NOTES
#
# Could improve MatrixPrint but at that point I think using TextTable would just be better
#
# Could add option to delete rows of the all_results matrix to remove results obtained by incorrectly input odds.
#
# Could add support for fractional odds to be entered as integers where appropriate - I anticipate this needing quite a lot of code, so it's probably not worth it, at least for now.
# 
# The input section has 3 main branches of the if statement, each handling a different format of odds. As each of these branches are similar, only the decimal branch is fully commented.
# 
# Explanation of the mathematics of the analysis itself will soon be available in the README. 

# ------------------------------
# FUNCTIONS
# ------------------------------

def MatrixPrint(list):
    '''
    Prints rows of a matrix with visually labelled columns.
    '''
    print("\n" + "Name, Team 1 Bet Criterion, Team 2 Bet Criterion")
    i = 0
    while i < len(list):
        j = 0
        row = ""
        while j < len(list[i]):
            row += list[i][j] + 7*" "
            j += 1
        print(row)
        i += 1

def IsValid(float_1, float_2):
    '''
    Checks for the decimal forms of the two values in an odds pair to be both more than or equal to 1 - odds values of less than 1 are impossible.
    '''
    if float_1 >= 1 and float_2 >= 1:
        return True
    else:
        print("\n" + "The odds values are invalid. Please re-enter the odds. ")
        return False

def ConvertFromFractional(float_1, float_2):
    '''
    Converts a fractional odds value float_1/float_2 to decimal format.
    '''
    return float_1/float_2 + 1

def ConvertFromMoneyline(float):
    '''
    Converts a moneyline odds value to decimal format.
    '''
    if float > 0:
        return float/100 + 1
    else:
        return -100/float + 1

def ExitProgram():
    '''
    Prints a goodbye message and exits the program.
    '''
    print("\n" + "E entered. Thankyou for using this betting analyser. Good luck with your bets! " + "\n")
    raise SystemExit

# ------------------------------
# INITIALISATION AND WELCOME
# ------------------------------

all_results_matrix = []

print(3*"\n" + "Welcome to your betting analyser. ")
print("Enter E at any point to exit the program. ")

# ------------------------------
# MAIN BODY
# ------------------------------

while True:
    
# ------------------------------
# INPUT RECEPTION, PROCESSING AND VALIDATION
# ------------------------------
    
    format_chosen = False
    
    while format_chosen == False:
        
        input_validated = False
        
        print("\n" + "Decimal odds look like: 1.45, 2.55")
        print("Fractional odds look like: 45/100, 155/100")
        print("Moneyline odds look like: -222, +155")

        format_input = input("\n" + "What format are the odds in? Type D for decimal, F for fractional, and M for moneyline. Enter R to reset format choice. ")
        
        if format_input == "D":
            format_chosen = True
            while input_validated == False:
                odds1_raw = input("\n" + "Enter the odds for team 1 in decimal form: ")
                odds2_raw = input("Enter the odds for team 2 in decimal form: ")
                if odds1_raw == "E" or odds2_raw == "E":
                    ExitProgram()
                elif odds1_raw =="R" or odds2_raw == "R":
                    format_chosen = False
                else:
                    try:
                        odds1 = float(odds1_raw)
                        odds2 = float(odds2_raw)
                    except: # The values input are not floats; the user messed up in some way.
                        try: # Attempt to rectify input.
                            odds1 = float("".join(filter(lambda x: x.isdigit() or x == ".", odds1_raw)))
                            odds2 = float("".join(filter(lambda x: x.isdigit() or x == ".", odds2_raw)))
                        except: # One or more of the values contained more than one period. Not worth going through every possible value the user could have meant to input, so return to ask for input again (achieved by leaving input_validated as False)
                            print("\n" + "Both inputs must contain digits and at most one period each.")
                        else: # After cleaning the input resembles floats. Check that these floats are the values the user meant to submit.
                            confirmation_check_done = False
                            while confirmation_check_done == False:
                                confirmation = input("\n" + "Are these the correct odds? Enter Y or N. Value 1: " + str(odds1) + " Value 2: " + str(odds2) + " ")
                                if confirmation == "Y":
                                    confirmation_check_done = True
                                    if IsValid(odds1, odds2) == True:
                                        input_validated = True
                                elif confirmation == "N":
                                    confirmation_check_done = True # input_validated remains False, allowing the user to enter new odds.
                                elif confirmation == "E":
                                    ExitProgram()
                                elif confirmation == "R":
                                    confirmation_check_done = True
                                    format_chosen = False
                                else:
                                    print("\n" + "Please enter Y or N.") # confirmation_check_done remains False, prompting the user to respond correctly.
                    else: # The values input were successfuly converted into floats. Assume correct input.
                        if IsValid(odds1, odds2) == True:
                            input_validated = True
        
        elif format_input == "F":
            format_chosen = True
            while input_validated == False:
                print("\n" + "When entering the odds, make sure to include a forward slash: / ") # For now I will require fractional odds such as 3 to be written as 3/1.
                odds1_raw = input("\n" + "Enter the odds for team 1 in fractional form: ")
                odds2_raw = input("Enter the odds for team 2 in fractional form: ")
                if odds1_raw == "E" or odds2_raw == "E":
                    ExitProgram()
                elif odds1_raw =="R" or odds2_raw == "R":
                    format_chosen = False
                else:
                    try:
                        odds1_numerator, odds1_denominator = odds1_raw.split("/")
                        odds2_numerator, odds2_denominator = odds2_raw.split("/")
                    except:
                        print("\n" + "Both inputs must contain exactly one / each. ")
                    else:
                        try:
                            odds1_numerator = float(odds1_numerator)
                            odds1_denominator = float(odds1_denominator)
                            odds2_numerator = float(odds2_numerator)
                            odds2_denominator = float(odds2_denominator)
                        except:
                            try:
                                odds1_numerator = float("".join(filter(lambda x: x.isdigit() or x == ".", odds1_numerator)))
                                odds1_denominator = float("".join(filter(lambda x: x.isdigit() or x == ".", odds1_denominator)))
                                odds2_numerator = float("".join(filter(lambda x: x.isdigit() or x == ".", odds2_numerator)))
                                odds2_denominator = float("".join(filter(lambda x: x.isdigit() or x == ".", odds2_denominator)))
                            except:
                                print("\n" + "Please ensure that the numerators and denominators of the fractions contain one period at most, and otherwise only contain digits. ")
                            else:
                                confirmation_check_done = False
                                while confirmation_check_done == False:
                                    confirmation = input("\n" + "Are these the correct odds? Enter Y or N. Value 1: " + str(odds1_numerator) + "/" +  str(odds1_denominator) + " Value 2: " + str(odds2_numerator) + "/" + str(odds2_denominator) + " ")
                                    if confirmation == "Y":
                                        confirmation_check_done = True
                                        odds1 = ConvertFromFractional(odds1_numerator, odds1_denominator)
                                        odds2 = ConvertFromFractional(odds2_numerator, odds2_denominator)
                                        if IsValid(odds1, odds2) == True:
                                            input_validated = True
                                    elif confirmation == "N":
                                        confirmation_check_done = True
                                    elif confirmation == "E":
                                        ExitProgram()
                                    elif confirmation == "R":
                                        confirmation_check_done = True
                                        format_chosen = False
                                    else:
                                        print("\n" + "Please enter Y or N." + "\n")
                        else:
                            odds1 = ConvertFromFractional(odds1_numerator, odds1_denominator)
                            odds2 = ConvertFromFractional(odds2_numerator, odds2_denominator)
                            if IsValid(odds1, odds2) == True:
                                input_validated = True
        
        elif format_input == "M":
            format_chosen = True
            while input_validated == False:
                odds1_raw = input("\n" + "Enter the odds for team 1 in moneyline form: ")
                odds2_raw = input("Enter the odds for team 2 in moneyline form: ")
                if odds1_raw == "E" or odds2_raw == "E":
                    ExitProgram()
                elif odds1_raw =="R" or odds2_raw == "R":
                    format_chosen = False
                else:
                    try:
                        odds1 = float(odds1_raw)
                        odds2 = float(odds2_raw)
                    except:
                        try:
                            odds1 = float("".join(filter(lambda x: x.isdigit() or x == "." or x == "-", odds1_raw)))
                            odds2 = float("".join(filter(lambda x: x.isdigit() or x == "." or x == "-", odds2_raw)))
                        except:
                            print("\n" + "Both inputs must contain digits and at most one period each.")
                        else:
                            confirmation_check_done = False
                            while confirmation_check_done == False:
                                confirmation = input("\n" + "Are these the correct odds? Enter Y or N. Value 1: " + str(odds1) + " Value 2: " + str(odds2) + " ")
                                if confirmation == "Y":
                                    confirmation_check_done = True
                                    odds1 = ConvertFromMoneyline(odds1)
                                    odds2 = ConvertFromMoneyline(odds2)
                                    if IsValid(odds1, odds2) == True:
                                        input_validated = True
                                elif confirmation == "N":
                                    confirmation_check_done = True
                                elif confirmation == "E":
                                    ExitProgram()
                                elif confirmation == "R":
                                    confirmation_check_done = True
                                    format_chosen = False
                                else:
                                    print("\n" + "Please enter Y or N." + "\n")
                    else:
                        odds1 = ConvertFromMoneyline(odds1)
                        odds2 = ConvertFromMoneyline(odds2)
                        if IsValid(odds1, odds2) == True:
                            input_validated = True
        
        elif format_input == "R":
            print("\n" + "This option is for use once a format has already been chosen. ") # The reset format choice option is not meant to be used at this juncture, as no format has been chosen yet.
        
        elif format_input == "E":
            ExitProgram()
        
        else:
            print("\n" + "Invalid input. ")

# ------------------------------
# ANALYSIS CALCULATIONS
# ------------------------------

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

    name_of_analysis = input("\n" + "Enter a name for this analysis. Entering E will exit the program. ")
    if name_of_analysis == "E":
        ExitProgram()

    all_results_matrix.append([name_of_analysis, "p > " + team1_bet_criterion_formatted, "p < " + team2_bet_criterion_formatted])

# ------------------------------
# ANALYSIS RESULT OUTPUT
# ------------------------------

    print(3*"\n" + "The following probabilities are rounded to 2 decimal places. ")
    print("Let p be the probability of team 1 winning. ")
    print("\n" + "Bet on team 1 if you believe p is more than " + team1_bet_criterion_formatted)
    print("Bet on team 2 if you believe p is less than " + team2_bet_criterion_formatted)

    print("\n" + "All other things remaining equal, you should bet on the site that provides the best odds. All analysis results so far: ")

    MatrixPrint(all_results_matrix)

    program_exit_check_done = False
    while program_exit_check_done == False:
        program_exit_answer = input("\n" + "Would you like to continue or exit the program? Enter C or E. ")
        if program_exit_answer == "E":
            ExitProgram()
        elif program_exit_answer == "C":
            program_exit_check_done = True
        else:
            print("\n" + "Please enter C or E. ")