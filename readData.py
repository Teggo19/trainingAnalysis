
def kmRun(data):
    res = []
    for i in data:
        if i["cellTagName"] == "LongDistanceRunning.KilometersRunning":
            res.append[{"date":i["workoutDate"][:10], "value":int(i["value"])}]

def form(data):
    res = []
    for i in data:
        if i["cellTagName"] == "LongDistanceRunning.FormN":
            res.append({"date":i["wor"]})