import requests
import sqlalchemy as db
import pandas as pd
from pandas import DataFrame

fish_response = requests.get('https://acnhapi.com/v1/fish/')
sea_response = requests.get('https://acnhapi.com/v1/sea/')
bug_response = requests.get('https://acnhapi.com/v1/bugs/')

engine = db.create_engine('sqlite:///acnh.db')


def add_fish_table():
    fish_frame = pd.DataFrame.from_dict(fish_response.json())
    fish_frame.to_sql('acnh-fish', con=engine, if_exists='replace', index= False)


def add_sea_table():
    sea_frame = pd.DataFrame.from_dict(sea_response.json())
    sea_frame.to_sql('acnh-sea-creatures', con=engine, if_exists='replace', index=False)


def add_bug_table():
    bug_frame = pd.DataFrame.from_dict(bug_response.json())
    bug_frame.to_sql('acnh-bugs', con=engine, if_exists='replace', index=False)


'''
display table:

query_result = engine.execute("SELECT * FROM acnh-fish;").fetchall()
print(pd.DataFrame(query_result))
'''


def display_fish():
    """display acnh fish"""

    for i in fish_response.json():
        print(f"{i} info:")
        for key, val in fish_response.json()[i].items():
            if key == 'name':
                for k, v in val.items():
                    if k != 'name-USen':
                        continue
                    else:
                        print(f"{key} : {v}")
            elif key == 'price-cj':
                continue
            elif key == 'availability':
                print("")
                for k, v in val.items():
                    if k == 'month-array-northern' or k == 'month-array-southern' or k == 'time' or k == 'time-array':
                        continue
                    else:
                        print(f"{k} : {v}")
                print("")

            else:
                print(f"{key} : {val}")
        print("")


def display_sea_creatures():
    """display acnh sea creatures"""

    for i in sea_response.json():
        print(f"{i} info:")
        for key, val in sea_response.json()[i].items():
            if key == 'name':
                for k, v in val.items():
                    if k != 'name-USen':
                        continue
                    else:
                        print(f"{key} : {v}")
            elif key == 'availability':
                print("")
                for k, v in val.items():
                    if k == 'month-array-northern' or k == 'month-array-southern' or k == 'time' or k == 'time-array':
                        continue
                    else:
                        print(f"{k} : {v}")
                print("")
            else:
                print(f"{key} : {val}")
        print("")


def display_bugs():
    """display acnh bugs"""

    for i in bug_response.json():
        print(f"{i} info:")
        for key, val in bug_response.json()[i].items():
            if key == 'name':
                for k, v in val.items():
                    if k != 'name-USen':
                        continue
                    else:
                        print(f"{key} : {v}")
            elif key == 'price-flick':
                continue
            elif key == 'availability':
                print("")
                for k, v in val.items():
                    if k == 'month-array-northern' or k == 'month-array-southern' or k == 'time' or k == 'time-array':
                        continue
                    else:
                        print(f"{k} : {v}")
                print("")
            else:
                print(f"{key} : {val}")
        print("")
