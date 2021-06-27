import random

fname = ['Shane', 'David', 'Corey', 'Mike', 'Robert', 'Goodrich', 'Dave', 'Quircy', 'Clarke']
mname = ['T', 'S', 'P', 'L', 'K', 'M', 'E', 'R']
lname = ['Bucky', 'Madej', 'Bugara', 'Johannson', 'Schafer', 'Salmoni', 'Tamassia' , 'Larson']
address = ['Lorem ipsum dolor sit amet',
            'eliturpis vitae laortProin.',
            'mollis. Sed congue a purus.',
            'Duis sagittis tort quis.',
            'nisi fringilla. Dugittis t',
            'Proin laoreet turpvitae ',
            'pulvinar massa. Docfelis',
            ]

# ---------------- CREATE SOME SAMPLE STUDENT DATA IN 'SAMPLE_STUDENT.TXT' --------------------
required_students = 20
table = 'student'

def create_data(required_students):
    for i in range(required_students):
        yield 'insert into ' + table + ' values ' + '(' + '\'' + str(100000 + i)+'\''+ ','+ '\'' + str(100000000000 + i) \
        + '\''+ ',' + '\''+ random.choice(fname) + '\''+ ',' + '\'' + random.choice(mname) + '\'' + ',' + '\'' \
        + random.choice(lname)  + '\'' + ',' + '\'' + random.choice(address) + '\'' + ');' + '\n'

with open('sample_student.txt', 'w') as f:
    for i in create_data(required_students):
        f.write(i)


# -----------------CREATE SOME SAMPLE PROFESSOR DATA IN 'SAMPLE_PROFESSOR.TXT'--------------------------
required_professors = 10
table = 'professor'

def create_data(required_professors):
    for i in range(required_professors):
        yield 'insert into ' + table + ' values ' + '(' + '\'' + str(200000 + i) + '\'' + ',' + '\'' + str(200000000000 + i) \
        + '\''+ ',' + '\''+ random.choice(fname) + '\''+ ',' + '\'' + random.choice(mname) + '\'' + ',' + '\'' \
        + random.choice(lname)  + '\''  + ');' + '\n'

with open('sample_professor.txt', 'w') as f:
    for i in create_data(required_professors):
        f.write(i)





