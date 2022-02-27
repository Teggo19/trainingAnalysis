import numpy as np


def formAsFunctionOfKMRanDayBefore(dataArray):
    n = len(dataArray)
    array = np.zeros((30, 2))
    for ind, day in enumerate(dataArray[1:]):
        kmPreviousDay = int(dataArray[ind-1, 2])
        if kmPreviousDay <= 30:
            array[kmPreviousDay, 0] += 1
            array[kmPreviousDay, 1] += day[0]
    averagePerKm = np.zeros(30)
    for ind, value in enumerate(array):
        if value[0]:
            averagePerKm[ind] = value[1] / value[0]
    dataPointsPerValue = array[:, 0]

    return averagePerKm, dataPointsPerValue


def formAsFunctionOfTotalExertionDayBefore(dataArray):
    array = np.zeros((20, 2))
    for ind, day in enumerate(dataArray[1:]):
        totalExertionPreviousDay = int(dataArray[ind-1, 1])
        array[totalExertionPreviousDay, 0] += 1
        array[totalExertionPreviousDay, 1] += day[0]
    averagePerExertion = np.zeros(20)
    for ind, value in enumerate(array):
        if value[0]:
            averagePerExertion[ind] = value[1]/value[0]
    dataPointsPerValue = array[:, 0]
    return averagePerExertion, dataPointsPerValue
