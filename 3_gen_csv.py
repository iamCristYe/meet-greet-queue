import json
import os

memberDict = {}
with open("events_processed.json") as events_json:
    events = json.load(events_json)
    for artistArrayDict in events["appGetEventResponse"]["artistArray"]:
        if artistArrayDict["artCode"] == "SA00000001":
            for event in artistArrayDict["eventArray"]:
                if event["evtCode"] == "10100126":
                    for e in event["dateArray"][0]["timeZoneArray"]:
                        for member in e["memberArray"]:
                            print(member["shCode"], member["mbName"], member["shName"])
                            memberDict[member["shCode"]] = member["shName"]
print(memberDict)
result_headcount = {}
result_second = {}
for t in range(1300, 1700):
    if os.path.exists(f"0623-{(t)}.json"):
        with open(f"0623-{(t)}.json") as time_json:
            time_data = json.load(time_json)
            e_data = {}
            if t < 1515:
                e_data = time_data["timezones"][2]["members"]
            else:
                e_data = time_data["timezones"][3]["members"]

            for member in e_data:
                if member != "SC201003550028" and member != "SC201003560028":
                    print(
                        memberDict[member],
                        e_data[member]["totalCount"],
                        e_data[member]["totalWait"],
                    )
                    if memberDict[member] not in result_headcount:
                        result_headcount[memberDict[member]]=[]
                        result_second[memberDict[member]]=[]
                    result_headcount[memberDict[member]].append(e_data[member]["totalCount"])
                    result_second[memberDict[member]].append(e_data[member]["totalWait"])

with open("result_headcount.csv" ,"w") as result_headcount_csv:
    result_headcount_csv.write("member\n")
    for member in result_headcount:
        result_headcount_csv.write(str(member))
        result_headcount_csv.write(",")
        for headcount in result_headcount[member]:
            result_headcount_csv.write(str(headcount))
            result_headcount_csv.write(",")
        result_headcount_csv.write("\n")

with open("result_second.csv" ,"w") as result_secone_csv:
    result_secone_csv.write("member\n")
    for member in result_second:
        result_secone_csv.write(str(member))
        result_secone_csv.write(",")
        for second in result_second[member]:
            result_secone_csv.write(str(second))
            result_secone_csv.write(",")
        result_secone_csv.write("\n")