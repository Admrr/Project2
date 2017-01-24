import psycopg2


def interact_with_database(command):

    connection = psycopg2.connect('dbname = euromast user=postgres password=123456!qQ')

    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:

        pass

    cursor.close()
    connection.close()

    return results

def upload_score(playername, score):
    interact_with_database("UPDATE highscore SET score = {} WHERE playername = '{}'".format(score,playername))

def download_scores():
    return interact_with_database("SELECT * FROM highscore ORDER BY score DESC")

def download_top_score():
    result = interact_with_database("SELECT * FROM highscore ORDER BY score DESC")[0]
    return result


topscore = download_top_score()
allscore = download_scores()
print(allscore)
print("HIGHSCORE: " + str(topscore))
