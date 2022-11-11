# OddsAnalyser
Python script to analyse odds and return the predicted probabilities at which you should place bets. Designed for entity 1 vs entity 2 games with no draws possible. Made with Counter Strike: Global Offensive betting in mind.

Please note that only the decimal branch of the input section if statement is fully commented - this is due to how similar the branches are. If you understand the decimal branch, it's very unlikely you won't understand the other branches.

# Mathematics

Let:    
$o_1$ be the odds of team 1 winning, in decimal form. $o_1 \ge 1$         
$o_2$ be the odds of team 2 winning, in decimal form. $o_2 \ge 1$      
$b_1$ be the bet on team 1. $b_1 \ge 0$    
$b_2$ be the bet on team 2. $b_2 \ge 0$   
$p$ be the probability of team 1 winning. $0 \le p \le 1$    
$E$ be the expected income.  
&nbsp;

$$
\begin{align}
E &= p((o_1 - 1)b_1 - b_2) + (1-p)(-b_1 + (o_2 - 1)b_2) \\
\\
&= b_1p(o_1 - 1) -b_2p -b_1 + b_2(o_2-1) + b_1p + b_2(-p(o_2 - 1)) \\
\\
&= b_1(p(o_1 - 1) - 1 + p) + b_2(-p + (o_2 - 1) + p(1 - o_2)) \\
\\
&= b_1(po_1 - 1) + b_2(-po_2 + o_2 - 1)
\end{align}
$$

$\frac{dE}{db_1} = po_1 - 1$

$\therefore \frac{dE}{db_1} > 0$ when $po_1 - 1 > 0$

$\therefore \frac{dE}{db_1} > 0$ when $p > \frac{1}{o_1}$

$\frac{dE}{db_2} = o_2(1 - p) - 1$

$\therefore \frac{dE}{db_2} > 0$ when $o_2(1 - p) - 1 > 0$

$$
\begin{align}
o_2(1 - p) - 1 &> 0 \\
-o_2p &> 1 - o_2 \\
p &< \frac{o_2 - 1}{o_2}
\end{align}
$$

$\therefore \frac{dE}{db_2} > 0$ when $p < \frac{o_2 - 1}{o_2}$

Therefore:
* When $p > \frac{1}{o_1}$ you should increase $b_1$ (i.e. bet on team 1)
* When $p < \frac{o_2 - 1}{o_2}$ you should increase $b_2$ (i.e. bet on team 2)

The script does the above calculation for you. In the script there is code to round the decimal forms of the above fractions - this is for readability of output, and the adjustments following it are to ensure the analysis results remain correct - for example, if a figure is rounded down, then telling the user to bet if they believe the "real" number to be above that is incorrect advice if their prediction is between the original value and the rounded value.

# Potential Improvements
MatrixPrint doesn't print matrices in a very pretty way and could be improved, either by implementing slightly complex code or by using a module such as texttable.

Could add option to delete rows of the all_results matrix to remove results obtained by incorrectly input odds.

Could add support for fractional odds to be entered as integers where appropriate - I anticipate this needing quite a lot of code, so it's probably not worth it, at least for now.

# Potential Extensions
Support for analysing odds for events other than one side winning - some sites allow users to bet on specific events such as overtime being reached.

Scraping of odds from betting sites with automatic analysis.

GUI.

Based off of a user-input budget for a number of match bets and a user-input array of predicted team 1 chances of winning for those matches, advise the user on how much they should bet on each match.
