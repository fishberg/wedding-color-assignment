# wedding-color-assignment

Simple Python code for processing our wedding party's Google Form responses and producing a color assignment. This is a simple variation of [rank choice voting](https://en.wikipedia.org/wiki/Ranked_voting).

## Quick Start

1. Add output from Google Form to directory as `input.csv`.
2. Run `./01_Preprocess.py` to create `suit.csv` and `dress.csv` from `input.csv`.
3. Run `./02_Assign.py INPUT` to process `INPUT`, a preprocessed file, and produce an assignment. Here, `INPUT` is either `suit.csv` or `dress.csv`.
4. Run `./03_Minimize.py` to run `./02_Assign.py suit.csv` and `./02_Assign.py dress.csv` each 100 times and output the observed assignment(s) with minimum cost (i.e., smallest sum of ranking).


## Algorithm Explanation
Participants order each color from `1` to `9`. `1` represents their first choice, `9` represents their last choice. The Google Form ensures every color must have a ranking and no two colors can have the same ranking.

The suits and dresses will be processed separately.

For suits (or dresses) the following steps are followed: 
1. Look at everyone's #1 color choice.
2. If anyone is alone in picking a particular color as their #1, they get it assigned. (That color and person are removed from future iterations.)
3. For any color where two or more people picked it as their #1, the algorithm randomly (uniformly) selects one person to get that color. (That color and person are removed from future iterations.)
4. Repeat for everyone's #2 choice, #3 choice, etc.
