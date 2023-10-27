### Shark Attacks - Quest ### 
# data-cleaning-pandas
by Carmen Matos & Ivet Petkowa
content:    shark_attacks.ipynb
            function.py 
            shark_attacks_quest_CI (Google Slides)
            README.md

https://docs.google.com/presentation/d/11ye4-GP-n4HfBIPm6amLJylLqzfgfPGQ_Uyl_nkTGlM/edit?usp=sharing

To start the project we had to read the file and load the given database.
The dataset sharks_csv contains information about the sharks attacks from various locations around the world.

Here's a summary of the columns:

1. **Date:** The date when the attack has happened.
2. **Year:** The year in which the attack has happened.
3. **Type:** The type of the attack.
4. **Country:** The country of the attack's location.
5. **State:** The state where the attack was reported.
6. **Location:** The location where the attack was reported.
7. **Activity:** The activity that the attacked person was practicing in water.
8. **Name:** The name of the attacked person.
9. **Sex:** The gender of the attacked person.
10. **Age:** The age of the attacked person.
11. **Injury:** The injury the attacked person has suffered.
12. **Unnamed: 11:** Column with NaN
13. **Time:** The time in which the attack has happened.
14. **Species:** The specie of the shark related to the reported attack.
15. **Source:** Where the information is coming from.
16. **pdf:** Links to pdf documents related to the incident.
17. **href formula:** Function returns a hyperlink from a given destination and link text.
18. **href:** The href attribute specifies the URL of the page the link goes to.
19. **Case Number:** Case number of the incident
20. **Case Number.1:** Column with NaN
21. **original order:** Column with NaN
22. **Unnamed: 21:** Column with NaN
23. **Unnamed: 22:** Column with NaN

After checking the contents of the columns, we need to drop the columns that don't contain the information we need or that now have no values at all. 

We check the number of missing values with sharks_df.isna().sum(), we start checking each column independently with .value_counts() and
we want to fill the missing values in the columns we have with 'N' to make the analysis easier for now.

We also created lambda functions to replace the names of the variables of interest in our analysis. 

Once the collums of interest were clear, we carried out some methods to validate our hypothesis. We have also created some plots to validate our findings and conclusions.








