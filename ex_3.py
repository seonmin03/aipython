#다음 리스트에서 확장자가 png나 jpg인 파일명 확장자를 출력하는 코드를 작성하시오

n=int(input())
a=[input() for i in range(n)]
b=[i for i in a if i.split(',')[-1]=='jpg' or i.split('.')[-1]=='png']
print(b)