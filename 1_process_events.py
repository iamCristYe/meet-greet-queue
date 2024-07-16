import json
with open("events.json") as f:
    data=json.load(f)
    with open("events_processed.json","w") as res:
        json.dump(data,res,ensure_ascii=False,indent=4)