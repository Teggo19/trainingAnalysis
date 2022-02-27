import numpy as np
import datetime

def dataAsNumpyArraybyDayMaxForm(data):
    """
    Structure of numpy array:
    1. value: maximum form for that day
    2. value: total perceived exertion for that day
    3. value: total km run that day
    4.-11. values: total minutes in zone 1-8 from OLT
    12. value: total strength that day
    :param data:
    :return:
    """

    firstDay = datetime.datetime.strptime(data[0]["workoutDate"], "%Y-%m-%d %H:%M:%S")
    for dataPoint in data:
        if dataPoint["cellTagName"][:18] == "CrossCountrySkiing":
            lastDay = datetime.datetime.strptime(dataPoint["workoutDate"], "%Y-%m-%d %H:%M:%S")
            break
    numOfDays = (firstDay - lastDay).days
    result = np.zeros((numOfDays, 12))

    for dataPoint in data:
        date = datetime.datetime.strptime(dataPoint["workoutDate"], "%Y-%m-%d %H:%M:%S")
        index = (firstDay - date).days
        if dataPoint["cellTagName"] == "LongDistanceRunning.FormN":
            if int(dataPoint["value"][4:5]) > result[index, 0]:
                result[index, 0] = int(dataPoint["value"][4:5])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.PerceivedExertion":
            # result[index, 1] += int(dataPoint["value"])
            if int(dataPoint["value"]) > result[index, 1]:
                result[index, 1] = dataPoint["value"]
        elif dataPoint["cellTagName"] == "LongDistanceRunning.KilometersRunning":
            result[index, 2] += float(dataPoint["value"].replace(",", "."))
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI1Easy":
            result[index, 3] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI2Moderate":
            result[index, 4] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI3LAT":
            result[index, 5] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI4HAT":
            result[index, 6] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI5MaxO2":
            result[index, 7] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI6AnaerobicT":
            result[index, 8] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI7AnaerobicP":
            result[index, 9] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"] == "LongDistanceRunning.EnduranceI8Speed":
            result[index, 10] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])
        elif dataPoint["cellTagName"][:28] == "LongDistanceRunning.Strength":
            result[index, 11] += int(dataPoint["value"][:2])*60 + int(dataPoint["value"][3:4])

    return result

def formAsFunctionOfPreviousTraining(data):
    result = np.zeros((len(data)-7, 45))
    result[:, 0] = data[7:, 0]
    for ind, day in enumerate(data[7:]):
        result[ind - 7, 1:12] = data[ind - 1, 1:]
        for i in range(1, 15):
            if i < 4:
                result[ind-7, 12:23] += data[ind-i, 1:]
            if i < 8:
                result[ind - 7, 23:34] += data[ind - i, 1:]
            result[ind - 7, 34:45] += data[ind - i, 1:]
        result[ind - 7, 23:34] += data[ind - i, 1:]

    return result

def removeZeroForm(data):
    result = np.copy(data)
    zeroIndexes = []
    for ind, val in enumerate(data):
        if not val[0]:
            zeroIndexes.append(ind)
    for i in reversed(zeroIndexes):
        result = np.delete(result, i, 0)
    return result
