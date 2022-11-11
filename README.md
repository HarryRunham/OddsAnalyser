# OddsAnalyser
Python script to analyse odds and return the predicted probabilities at which you should place bets. Designed for entity 1 vs entity 2 games with no draws possible. Made with Counter Strike: Global Offensive betting in mind.

Please note that only the decimal branch of the input section if statement is fully commented - this is due to how similar the branches are. If you understand the decimal branch, it's very unlikely you won't understand the other branches.

# Mathematics

Let:
o1 be the odds of team 1 winning y  $y$   $ y $

$$


# Potential Improvements
MatrixPrint doesn't print matrices in a very pretty way and could be improved, either by implementing slightly complex code or by using a module such as texttable.

Could add option to delete rows of the all_results matrix to remove results obtained by incorrectly input odds.

Could add support for fractional odds to be entered as integers where appropriate - I anticipate this needing quite a lot of code, so it's probably not worth it, at least for now.

# Potential Extensions
Support for analysing odds for events other than one side winning - some sites allow users to bet on specific events such as overtime being reached.

Scraping of odds from betting sites with automatic analysis.

GUI.
