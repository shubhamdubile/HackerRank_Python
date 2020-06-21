student = []
for _ in range(int(input())):
    name=input()
    score=float(input())
    student.append([name, score])
       
second_low_score = sorted(set([x[1] for x in student]))
for _ in sorted(x[0] for x in student if x[1] == second_low_score[1]):
    print(_)
