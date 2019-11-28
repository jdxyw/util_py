import xlrd
import collections

wb = xlrd.open_workbook("*")
sheet = wb.sheet_by_index(0)

cid2tag2 = collections.defaultdict(set)
cid2tag3 = collections.defaultdict(set)
cid2tag4 = collections.defaultdict(set)

#print(sheet.nrows)
#print(sheet.row_values(0))
nrows = sheet.nrows

for i in range(1, nrows):
    row = sheet.row_values(i)
    cid = row[0]

    tag2 = "_".join(row[15].split("_")[:-1])
    tag3 = "_".join(row[16].split("_")[:-1])
    tag4 = "_".join(row[17].split("_")[:-1])
    flag = row[18]
    if len(flag) > 2:
        continue
    cid2tag2[cid].add(tag2)
    cid2tag3[cid].add(tag3)
    cid2tag4[cid].add(tag4)

for cid in cid2tag2:
    print("%s\t%s\t%s\t%s" % (cid, ",".join(list(cid2tag2[cid])), ",".join(
        list(cid2tag3[cid])), ",".join(list(cid2tag4[cid]))))
