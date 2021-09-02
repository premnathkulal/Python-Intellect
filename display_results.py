import styles_f
import json

def disply(dis_ov,over_score_list,total_over_score,count_six, count_four,total_score,wicket):
    styles_f.loading()
    print("\nOVER :", dis_ov)
    print("\n\t\t", over_score_list,"\n")
    print(total_score,"/",wicket,"\t\t\t\t\t\tSIX :",count_six,"\tFOUR :",count_four,"\n")
    styles_f.divider()


def half_match_result():

    with open('player1.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            total_sc = p['total']
            name = p['name']
            six = p['six_c']
            wicket1 = p['wicket']
            four = p['four_c']
        json_file.close()

    styles_f.loading()
  
    print("\nRESULT OF FIRST INNINGS")
    print("TEAM NAME :", name)
    print("TOTAL SCORE :", total_sc,"/",wicket1)
    print("SIX :",six)
    print("FOUR :",four)
    print("TARGET : ",total_sc+1)


def match_result():
    with open('player1.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            total_sc = p['total']
            name = p['name']
            six = p['six_c']
            wicket1 = p['wicket']
            termf = p['term']
            four = p['four_c']
        json_file.close()

    with open('player2.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            total_sc2 = p['total']
            name2 = p['name']
            six2 = p['six_c']
            wicket2 = p['wicket']
            terms = p['term']
            four2 = p['four_c']
        json_file.close()

    print("\nSCORE LIST")
    print("\nRESULT OF FIRST INNINGS")
    print("TEAM NAME :", name)
    print("TOTAL SCORE :", total_sc,"/",wicket1)
    print("SIX :", six)
    print("FOUR :", four)

    print("\nRESULT OF SECOND INNINGS")
    print("TEAM NAME :", name2)
    print("TOTAL SCORE :", total_sc2,"/",wicket2,"")
    print("SIX :", six2,)
    print("FOUR :", four2,)
    print("\n")

    if(total_sc > total_sc2):
        if termf == 1:
            print(name,"WIN BY",total_sc-total_sc2,"RUNS")
        else:
            print(name,"WIN BY",10-wicket1,"WICKETS")

    elif (total_sc2 > total_sc):
        if terms == 1:
            (name2,"WIN BY",total_sc2-total_sc,"RUNS")
        else:
            print(name2,"WIN BY",10-wicket2,"WICKETS")

    else:
        print("MATCH DRAW")

    print("\n")
    print("$"*100)
    print("\n")