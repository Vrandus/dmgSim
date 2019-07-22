import readCSV
import math

level = readCSV.numberedDictCSV("level.csv")
job = readCSV.dictCSV("job.csv")
def levelInfo(lvl, x):
    return level[lvl-1].get(x)


def getMainAtt(jobName):
    return job[jobName]["MAIN"]


def jobInfo(x, y):
    return job.get(x).get(y)


def fPot(potency):
    return potency / 100


def fWD(lvl, jobName, WD):
    return math.floor((((int(level[lvl]["MAIN"])) * int(job[jobName][getMainAtt(jobName)])/1000) + WD))


def fAP(AP):
    return math.floor(((125 * (AP-292))/292) + 100) / 100


def fMAP(MAP):
    return math.floor(((125 * (MAP-292))/292) + 100) / 100


def fDET(lvl, DET):
    return math.floor((130 * (DET - int(level[lvl]["MAIN"])))/(int(level[lvl]["DIV"] + 1000))) / 1000


def fTNC(lvl, TNC):
    return math.floor((100 * (TNC - int(level[lvl]["SUB"])))/(int(level[lvl]["DIV"] + 1000))) / 1000


def fSS(lvl, SS):
    return math.floor((130 * (DET - int(level[lvl]["SUB"])))/(int(level[lvl]["DIV"] + 1000))) / 1000


def fCRIT(lvl, CRIT):
    return math.floor((200 * (DET - int(level[lvl]["SUB"])))/(int(level[lvl]["DIV"] + 1400))) / 1000


def