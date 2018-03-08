if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
        student_marks.update({name:scores})
    query_name = raw_input()
    for x in student_marks.keys():
        if x==query_name:
            avg=sum(student_marks[x])/3
    print ("%.2f" % avg)
