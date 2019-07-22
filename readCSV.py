import csv
import pprint
def numberedDictCSV(filename):
    dict_lvl = {}
    count = 0
    reader = csv.DictReader(open(filename))
    for line in reader:
        if count is not 0:
            dict_lvl[count + 1] = dict(line) 
        count += 1
        # dict_lvl.append(dict(line))
    return dict_lvl



def dictCSV(filename):
    dict_job = {}
    reader = csv.DictReader(open(filename))
    for line in reader:
        dict_job[line['Job']] = (dict(line))
    return dict_job
# pprint.pprint(dict_lvl)
# print(dict_lvl[60].get('PIE'))

# level = numberedDictCSV('level.csv')
# print(level[70]['PIE'])

# job = dictCSV('job.csv')
# pprint.pprint(job)
# print(job["GLA"]["STR"])
