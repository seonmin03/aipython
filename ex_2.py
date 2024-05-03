#n개의 숫자가 공백없이 입력된다. 이 숫자를 모두 합쳐서 합을 출력하는 프로그램을 작성하시오

num=input()
num_list=list(num)
aa=map(int, num_list)

print(sum(aa))