
f1 = open("E:\\python\\assignments\\StudentMarksAssignment\\student_marks.csv")
f2 = open("E:\\python\\assignments\\StudentMarksAssignment\\subject_faculty.csv")
d1 = []
d2 = []
d = {}


for line in f1:
    col = line.rstrip('\n').split(',')
    rec = tuple([col[0], col[1], int(col[2])])
    d1.append(rec)
# print(d1)
# f1.close()


for line in f2:
    col = line.rstrip('\n').split(',')
    rec = tuple([col[0], col[1]])
    d2.append(rec)
# f2.close()
y = dict(d2)
# print(y)


for i, j, k in d1:
    if j not in d:
        d[j] = [k]
    else:
        d[j].append(k)
# print(d)


a = {}
for i in d:
    for k in range(len(d[i])):
        # print(k)
        if d[i][k] > 90:
            if i not in a:
                a[i] = [d[i][k]]
            else:
                a[i].append(d[i][k])
# print(a)


c = {}
for i in a:
    c.setdefault(i, len(a[i]))
# print(c)


e = max(list(c.items()), key=lambda x: x[1])
# print(e)
if e[0] in y:
    print("The faculty with highest student count who got more than 90% is = ", y[e[0]])


b = {}
for i in d:
    for k in range(len(d[i])):
        # print(k)
        if d[i][k] > 40:
            if i not in b:
                b[i] = [d[i][k]]
            else:
                b[i].append(d[i][k])
# print(b)


d4 = {}
for i in b:
    d4.setdefault(i, len(b[i]))
#print(d4)


f = max(list(d4.items()), key=lambda x: x[1])
# print(f)
if f[0] in y:
    print("The faculty with highest pass percentage (> 40%) = ",f, y[f[0]])

w = {}
for i in d:
    for k in range(len(d[i])):
        if d[i][k] <= 40:
            # print(d[i][k])
            if i not in w:
                w[i] = [d[i][k]]
            else:
                w[i].append(d[i][k])
#print(w)

d6 = {}
for i in w:
    d6.setdefault(i, len(w[i]))
#print(d6)

t = min(list(d6.items()), key=lambda x: x[1])
# t1 = t[1]

'''v = sorted(d6.items(), key=lambda x: x[1])
for i, j in v:
    if j == t1:
        print(i)'''

# print(f)
if t[0] in y:
    print("The faculty with least pass percentage (<= 40%) = ",t, y[f[0]])


d5 = {}
for i in d1:
    if i[0] not in d5:
        d5[i[0]] = [i[2]]
    else:
        d5[i[0]].append(i[2])
# print(d5)


d6 = {}
for i in d5:
    s = sum(d5[i])
    d6[i] = s
for i in d6:
    g = max(list(d6.items()), key=lambda x: x[1])
print("The top student with maximum total = ", g)


if 'Mathematics' in d:
    h = max(d['Mathematics'])
    for i, j, k in d1:
        if j == 'Mathematics':
            if k == h:
                print("The best student in Mathematics = ", i)


l = {}
for i in d:
    for k in range(len(d[i])):
        # print(k)
        if d[i][k] > 35:
            if i not in l:
                l[i] = [d[i][k]]
            else:
                l[i].append(d[i][k])

n = {}
for i in l:
    m = sum(l[i])/100
    n[i] = [m]
print("The average mark for each subject = ", n)

for i in d6:
    r = min(list(d6.items()), key=lambda x: x[1])
print("The student with least numbers of marks as total = ", r)

