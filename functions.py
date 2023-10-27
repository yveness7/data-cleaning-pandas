#%load_ext autoreload    #### it has to appear on top of our code
#%autoreload 2

#read the file
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/yveness7/IronHackIvet/main/Week_2/sharkattack!/sharks.csv'

sharks_df = pd.read_csv(url)

#after checking the contant of the columns
#we need to drop the columns that don't contain
#info that we need or do now have values at all


def drop_columns():

    sharks_df.drop("pdf", axis='columns',inplace=True)
    sharks_df.drop("href formula", axis='columns',inplace=True)
    sharks_df.drop("href", axis='columns',inplace=True)
    sharks_df.drop('Case Number', axis='columns',inplace=True)
    sharks_df.drop("Case Number.1", axis='columns',inplace=True)
    sharks_df.drop("original order", axis='columns',inplace=True)
    sharks_df.drop("Unnamed: 21", axis='columns',inplace=True)
    sharks_df.drop("Unnamed: 22", axis='columns',inplace=True)
    sharks_df.drop("Unnamed: 11", axis='columns',inplace=True)
    sharks_df.drop("Source", axis='columns',inplace=True)


    return sharks_df.columns

#fix the column names to lower case

def columns_lower():

    sharks_df.columns = sharks_df.columns.str.lower()

    return sharks_df.columns


#we remove rows with all Nan values


def drop_na():

sharks_df.dropna(how='all', inplace=True)

    return sharks_df


#after checking the number of missing values
#using sharks_df.isna().sum() we start checking each
#column independetly using .value_counts() and
#we want to fill the missing values in the
#columns we have with 'N' to make the analysis
#easier for now


def fill_na():

sharks_df['state'].fillna('N',inplace=True)
sharks_df['location'].fillna('N',inplace=True)
sharks_df['injury'].fillna('N',inplace=True)
sharks_df['year'].fillna('N',inplace=True)
sharks_df['name'].fillna('N',inplace=True)
sharks_df['activity'].fillna('N',inplace=True)
sharks_df['time'].fillna('N',inplace=True)
sharks_df['age'].fillna('N',inplace=True)
sharks_df['species '].fillna('N',inplace=True)

    return sharks_df

#now we will start working with column 'type' to
#narrow down the cagtegories for our analysis

def activity_mapping():
    mapping = {

    'Invalid':'Unconfirmed',
    'Questionable':'Unconfirmed',
    'Sea Disaster':'Unconfirmed',
    'Unconfirmed':'Unconfirmed',
    'N':'Unconfirmed',
    'Unverified':'Unconfirmed',
    'Under investigation':'Unconfirmed',
    '?':'Unconfirmed',
    'Boat':'Watercraft',
    'Watercraft':'Watercraft'

    }

    sharks_df['type'] = sharks_df['type'].replace(mapping)

    return sharks_df['type']

#we can check the new categories using sharks_df['type'].value_counts()
#and we narrowed them down to Unprovoked -5077, Unconfirmed - 836, Provoked - 632 & Watercraft - 361

#now we will work on the column 'injury'

def injury_cleaning():

    injuries_lambda = lambda x:'Injury' if isinstance(x, str) and any(keyword in x for keyword in ['foot',
                                                                                   'wounds','bitten',
                                                                                   'Lacerated','wound',
                                                                                   'Lacerations','Laceration',
                                                                                   'Abrasions','thigh',
                                                                                   'Injury','Bitten',
                                                                                   'lacerated','bite',
                                                                                   'injury','laceration',
                                                                                   'injured','nipped',
                                                                                   'injuries','Injured',
                                                                                   'Left','Abrasion',
                                                                                   'Legs','gashed',
                                                                                   'Foot','bruised',
                                                                                   'drowning','Punctures',
                                                                                   'leg','knocked out',
                                                                                   'Leg', 'abraded','grazed',
                                                                                   'severed','lacerating',
                                                                                   'Survived','Scratches',
                                                                                   'bitten']) else x


    sharks_df['injury'] = sharks_df['injury'].apply(injuries_lambda)

    fatal_lambda = lambda y:'Fatal' if isinstance(y, str) and any(keyword in y for keyword in ['FATAL','remains',
                                                                                          'Missing','Torso recovered',
                                                                                           'Drowned',
                                                                                           'Body not recovered',
                                                                                           'Recuers','Body found',
                                                                                           'Body recovered',
                                                                                           'consumed the body',
                                                                                           'bodies','Murdered',
                                                                                           'drowned',
                                                                                           'attacked sailors',
                                                                                           'Fatal'

                                                                                           ]) else y

    sharks_df['injury'] = sharks_df['injury'].apply(fatal_lambda)


    unclear_lambda = lambda z:'Unclear' if isinstance(z, str) and any(keyword in z for keyword in ['No details','N',
                                                                                               'PROVOKED INCIDENT',
                                                                                               'unconfirmed',
                                                                                               'Non-fatal',
                                                                                               'Thought to',
                                                                                               'not confirmed',
                                                                                               'Recovered',
                                                                                               'Disappeared',
                                                                                               'Unknown'

                                                                                              ]) else z


    sharks_df['injury'] = sharks_df['injury'].apply(unclear_lambda)

    return sharks_df['injury']

#if we use the following code
#injuries_series = sharks_df["injury"]
#injuries_series.value_counts(ascending=False).head()
#we narrowed down to the basic categories
#Injury     5227
#Fatal      1126
#Unclear     273


#now we will fix the column 'activity'

def activity_clean():

    fishing_lambda = lambda i:'Fishing' if isinstance(i, str) and any(keyword in i for keyword in ['Spearfishing',
                                                                                               'Fishing ',
                                                                                               'Shark fishing',
                                                                                               'Surf fishing',
                                                                                               'Wade Fishing',
                                                                                               'Kayak Fishing',
                                                                                               'Crabbing',
                                                                                               'Wade-fishing',
                                                                                               'Wade fishing',
                                                                                               'Clamming',
                                                                                               'Crayfishing',
                                                                                               'Sculling',
                                                                                               'Shell diving'


                                                                                   ]) else i


    sharks_df['activity'] = sharks_df['activity'].apply(fishing_lambda)


    swimming_lambda = lambda o:'Swimming' if isinstance(o, str) and any(keyword in o for keyword in ['Wading',
                                                                                                 'Bathing',
                                                                                                 'Standing',
                                                                                                 'Swimming ',
                                                                                                 'Scuba diving',
                                                                                                 'Floating',
                                                                                                 'Jumped overboard',
                                                                                                 'Jumping',
                                                                                                 'Boat swamped',
                                                                                                 'Splashing',
                                                                                                 'Kayaking / Fishing',
                                                                                                 'Seine netting',
                                                                                                 'Dangling feet in the water',
                                                                                                 'Kayak fishing',
                                                                                                 'Jumped into the water',
                                                                                                 'Freedom Swimming',
                                                                                                 'Freedom swimming'

                                                                                   ]) else o
    sharks_df['activity'] = sharks_df['activity'].apply(swimming_lambda)

    diving_lambda = lambda p:'Scuba Diving' if isinstance(p, str) and any(keyword in p for keyword in ['Diving',
                                                                                                   'Pearl diving',
                                                                                                   'Sponge diving',
                                                                                                   'Hard hat diving',
                                                                                                   'Skindiving',
                                                                                                   'SCUBA diving'

                                                                                   ]) else p
    sharks_df['activity'] = sharks_df['activity'].apply(diving_lambda)



    walking_lambda = lambda w:'Walking' if isinstance(w, str) and any(keyword in w for keyword in ['Treading water',
                                                                                       'Standing','Playing',
                                                                                       'Walking out of the water after surfing'

                                                                                   ]) else w
    sharks_df['activity'] = sharks_df['activity'].apply(walking_lambda)


    surfing_lambda = lambda k:'Surfing' if isinstance(k, str) and any(keyword in k for keyword in ['Body boarding',
                                                                                       'Body surfing',
                                                                                               'Skin diving',
                                                                                               'Boogie boarding',
                                                                                               'Boogie Boarding',
                                                                                               'Surf-skiing',
                                                                                               'Surf skiing',
                                                                                               'Sitting on surfboard',
                                                                                               'Surfing ',
                                                                                               'Surfing, paddling seawards',
                                                                                               'Body Surfing',
                                                                                               'Paddling on surfboard',
                                                                                               'Paddling',
                                                                                               'Body-boarding',
                                                                                               'Paddleskiing',
                                                                                               'Body Boarding',
                                                                                               'Paddle boarding',
                                                                                               'Kite Surfing',
                                                                                               'Kite surfing',
                                                                                               'Stand-Up Paddleboarding'

                                                                                              ]) else k
    sharks_df['activity'] = sharks_df['activity'].apply(surfing_lambda)


    freediving_lambda = lambda q:'Free Diving' if isinstance(q, str) and any(keyword in q for keyword in ['Freediving',
                                                                                            'Free diving for abalone',
                                                                                                      'Free diving'

                                                                                              ]) else q
    sharks_df['activity'] = sharks_df['activity'].apply(freediving_lambda)

    accident_lambda = lambda a:'Accident' if isinstance(a, str) and any(keyword in a for keyword in ['Fell overboard',
                                                                                                    'Fell into the water',
                                                                                                    'Sea disaster',
                                                                                                 'Sea Disaster',
                                                                                                 'Knocked overboard',
                                                                                                 'Shipwreck',
                                                                                                 'Murder',
                                                                                                 'Wreck of the schooner Pohoiki',
                                                                                                 'boat capsized',
                                                                                                 'Suicide'


                                                                                              ]) else a
    sharks_df['activity'] = sharks_df['activity'].apply(accident_lambda)

    unknown_lambda = lambda un:'Unknown' if isinstance(un, str) and any(keyword in un for keyword in ['N','.']) else un

    sharks_df['activity'] = sharks_df['activity'].apply(unknown_lambda)

    other_lambda = lambda t:'Various' if isinstance(t, str) and any(keyword in t for keyword in ['Shark watching',
                                                                                             'Feeding fish',
                                                                                             'Shark watching',
                                                                                             'Lifesaving drill',
                                                                                             'Feeding sharks',
                                                                                             'Tagging sharks',
                                                                                             'SUP','Boat',
                                                                                             'Watercraft',
                                                                                             'Sitting on gunwale of boat',
                                                                                             'Competing in the Woodvale Atlantic Rowing Race',
                                                                                         'Escaping from Alacatraz',
                                                                                             'Sitting'
                                                                                            ]) else t

    sharks_df['activity'] = sharks_df['activity'].apply(other_lambda)

    return sharks_df['activity']

#now we narrowed down the column 'activity' to 14 basic categories
"""Swimming        1900
Surfing         1448
Fishing         1153
Unknown          681
Scuba Diving     429
Accident         131
Snorkeling       127
Walking           89
Various           74
Kayaking          39
Windsurfing       20
Canoeing          16
Rowing            12
Sailing            9"""


#now we want to clean the 'sex' column

def gender_clean():
    gender_mapping = {
    'M':'M',
    'N':'N',
    'lli':'N',
    'M x 2':'M',
    ' M':'M',
    '.':'N',
    'M ':'M'
}

    sharks_df['sex'] = sharks_df['sex'].replace(gender_mapping)


#and we have the categories 'M for male, 'F' for female and 'N' - no answer


    return sharks_df['sex']

## Display of the results:

def display_type():
    # Plot a bar chart 'type'
    sns.countplot(x='type', data=sharks_df)

def display_country():    
    # Plot a bar chart 'country'
    sns.countplot(x='country', data=sharks_df, order=sharks_df['country'].value_counts().head(10).index)
    plt.xticks(rotation=45)
    plt.show()

def display_sex(): 
    # Plot a pie chart 'sex'
    gender_counts = sharks_df['sex'].value_counts()
    plt.figure(figsize=(6, 6))  # Optional: Adjust the figure size
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)


sharks_df