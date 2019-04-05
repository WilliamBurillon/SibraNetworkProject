#!/usr/bin/python3
# -*-coding:utf-8-*-
from os.path import basename

data_file_name = 'data/1_Poisy-ParcDesGlaisins.txt'
data_file_name2 = 'data/2_Piscine-Patinoire_Campus.txt'
import time

try:
    with open(data_file_name, 'r', encoding="utf_8") as f:
        content = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")

try:
    with open(data_file_name2, 'r', encoding="utf_8") as f:
        content2 = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")

def dates2dic(dates):
    """

    :param dates:
    :return dic:
    """
    dic = {}
    splitted_dates = dates.split("\n")
    # print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    # print(dic['Ponchy'])
    return dic
def strToDate(dic):

    for key in dic.keys():

        for i in range(0, len(dic[key])):
            if dic[key][i] ==  '-' :

                dic[key][i] = None
            else:
                dic[key][i]= time.strptime(dic[key][i],"%H:%M")

    return dic

def getNextGo(stopList, stop):
    """

    :param stopList:
    :param stop:
    :return res :  the next stop of the parm stop


    """

    res = []
    theList = stopList.split(" N ")

    if "+" in theList[0]:

        resTemp = theList[0].split(" + ")
        start1 = [resTemp[0]] + theList[1:len((theList))]
        start2 = [resTemp[1]] + theList[1:len((theList))]

        if stop in start1 and stop in start2:

            try:
                res.append(start1[start1.index(stop) + 1])

            except IndexError:
                pass
        elif stop in start1 and stop not in start2:

            try:
                res.append(start1[start1.index(stop) + 1])
            except IndexError:
                pass
        elif stop not in start1 and stop in start2:

            try:
                res.append(start2[start2.index(stop) + 1])
            except IndexError:
                pass

    else:

        if stop in theList:
            try:
                res.append(theList[theList.index(stop) + 1])
            except IndexError:
                pass

    return res


def getNextBack(stopList, stop):
    res = []
    theList = stopList.split(" N ")

    if "+" in theList[0]:

        resTemp = theList[0].split(" + ")
        start1 = [resTemp[0]] + theList[1:len((theList))]
        start2 = [resTemp[1]] + theList[1:len((theList))]
        start1.reverse()
        start2.reverse()

        if stop in start1 and stop in start2:

            try:
                res.append(start1[start1.index(stop) + 1])
                res.append(start2[start2.index(stop) + 1])
                if res[0] == res[1]:
                    del res[1]
            except IndexError:
                pass

    else:
        theList.reverse()

        if stop in theList:
            try:
                res.append(theList[theList.index(stop) + 1])
            except IndexError:
                pass

    return res


def time2Stop(strT1, strT2):
    t1 = time.strptime(strT1, "%H:%M")
    t2 = time.strptime(strT2, "%H:%M")
    t1Min = t1.tm_hour * 60 + t1.tm_min
    t2Min = t2.tm_hour * 60 + t2.tm_min
    return t2Min - t1Min


# ------------ All the data file ------------------------------------------------------------------


slited_content1 = content.split("\n\n")  # Line list of the data file [list arrets, arret + horaire]
slited_content2 = content2.split("\n\n")

# print(slited_content)
# ------------ Concerning the regular path --------------------------------------------------------

regular_path1 = slited_content1[0]
regular_path2 = slited_content2[0] # type : str, content : the stop
regular_date_go1 = strToDate(dates2dic(slited_content1[1]))
regular_date_back1 = strToDate(dates2dic(slited_content1[2]))
regular_date_go2 = strToDate(dates2dic(slited_content2[1]))  # type : dict, content : date go
regular_date_back2 = strToDate(dates2dic(slited_content2[2]))
                                        # type : dict, content : date back

# ------------ Concerning the holiday and WE path -------------------------------------------------------

we_holidays_path1 = slited_content1[3]

we_holidays_date_go1= dates2dic(slited_content1[4])
we_holidays_date_back1 = dates2dic(slited_content1[5])

# ------------ TESTS -------------------------------
# return the key of the dict
# res=[]
# for key in regular_date_go.keys():
#     print(str(key))

# print(getNextBack(regular_path, "GARE"))

