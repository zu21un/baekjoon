import sys

input = sys.stdin.readline

def divide_paper(paper):
  paper_sum = 0
  for line in paper:
    paper_sum += sum(line)
  if paper_sum == 0:
    return [1, 0]
  elif paper_sum == len(paper)**2:
    return [0, 1]
  else:
    p1, p2, p3, p4 = [], [], [], []
    for i in range(len(paper)//2):
      p1.append(paper[i][0:len(paper)//2])
      p2.append(paper[i][len(paper)//2:])
    for i in range(len(paper)//2, len(paper)):
      p3.append(paper[i][0:len(paper)//2])
      p4.append(paper[i][len(paper)//2:])
    a1 = divide_paper(p1)
    a2 = divide_paper(p2)
    a3 = divide_paper(p3)
    a4 = divide_paper(p4)
    result = [a1[i] + a2[i] + a3[i] + a4[i] for i in range(len(a1))]
    return result
      
    
N = int(input())
paper = []
for _ in range(N):
  line = list(map(int, input().split()))
  paper.append(line)

result = divide_paper(paper)
for r in result:
  print(r)
