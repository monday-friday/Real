""" #datetime 이용 함수 

from datetime import datetime as dt 

#현재시간출력 

print(dt.now())

def get_dtnow() :
    return dt.now()

def cvt_time2str(objtime) :
    return dt.strptime(objtime, '%Y-%m-%d')

#특정 시간대의 현재 시간 출력 
#from pytz import timezone 
#import timezone 
#tz = timezone('Asia/Seoul')
#tz = time('UTC')
#print("timezon:", dt.now(tz))



#문자열을 날짜로 변환 
date_string = '2021-07-08'
date_object = dt.strptime(date_string,'%Y-%m-%d')
print(date_object)

#날짜를 문자열로 변환 
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string)


#import mod.utils as mu
#dtnow = mu.get_dtnow()
#print(dtnow)
'''import os
os.chdir('../.')
print(os.getcwd())


print(os.listdir())

os.rmdir('new_directory')
print(os.listdir(0))

os.mkdir('new_direcotory')
print(os.listdir())
'''

import mod.utils as mu
import os 

print(mu.get_curdir())

pname="python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())

import sys
print(sys.version)
print(sys.argv)

st = []

st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)
print(st) #[1,2,3]
top = st.pop

print(top)
print(st)
print(len(st))

queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue) #[1,2,3]
front = queue.pop

print(front)
print(queue)
print(len(queue))

 """


""" qlist = []

def enqueue(qlist, data) :
    qlist.append(data)
    
def dequeue(qlist) :
    data = qlist[0]
    del qlist[0]
    return data

enqueue(qlist, 1)
print(qlist)

enqueue(qlist, 2)
print(qlist)

enqueue(qlist, 3)
print(qlist)

enqueue(qlist, 4)
print(qlist)

dequeue(qlist)
print(qlist)

dequeue(qlist)
print(qlist) """


# O(1)
""" arr = [1, 2, 3, 4, 5]

def ret_01(idx) :
    return arr[idx]

print(ret_01(2))

# O(1) 시간

import time 
arr = [1, 2, 3, 5, 6]

def ret_01(idx) :
    return arr[idx]

start = time.time()
print(ret_01(2))
end = time.time()
print(f"{end - start : 5f} sec") """
# print("spend time : ", f"{end = start : 5f}, sec")


# O(n) 선형복잡도

""" import time
arr = [1, 2, 3, 4, 5]

def print_elements(arr) :
    for elem in arr :
        print(elem)


start = time.time()        
print_elements(arr)
end = time.time()

print(f"{end - start : 5f} sec")


# O(log n)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

result = binary_search(my_list, 4)
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.")

# O(n2) : 2차 복잡도

def mul_for() :
    for i in range(5) :
        for j in range(5) :
            print(i, j)
            
mul_for

import time

def mul_for() :
    for i in range(5) :
        for j in range(5) :
            print(i, j)
            
start = time.time()
mul_for()
end = time.time()
print(f"{end - start : 5f} sec")


import time
def fibonacci(n) :
    if n == 0 :
        return 0
    elif n ==1 :
        return 1
    else : 
 """

# 버블정렬
""" 
def bubble_sort(arr) :
    N = len(arr) # 데이터의 갯수 : 5
    for i in range(N) : #0,1,2,3,4,5
        print(i, arr)
        for j in range(N-i-1) : # 4, 3, 2, 1
            if arr[j] > arr[j+1] : #arr[4], arr[5] #
                # print(arr[j+1], arr[j])
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(i, j, arr, arr[i], arr[j])
    
    return arr

Irr = [1, 9, 2, 7, 5]
print(bubble_sort(Irr)) # [-1, 0, 9, 11, 45] """

# 퀵소트

""" def quick_sort(arr) :
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] # 가운데 값을 피벗으로 선택
    left = [ x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("piv", pivot)
    print("left", left)
    print("mid", middle)
    print("rgt", right)

    return quick_sort(left) + middle + quick_sort(right)


my_list = [1, 9, 6, 4, 5, 7, 3, 2]
print(len(my_list))

sorted_list = quick_sort(my_list)
print(sorted_list)


# 참고 코드
def search(arrlist, k) :
    for i in range(len(arrlist)) :
        if arrlist[i] == k :
            return 1
    return 0

mylist = [1, 2, 3, 4, 5]
key = 5

res = search(mylist, key)

if res != 0 :
    print(f"{mylist} : {res}")
else :
    print(f"Not found")    
 """

import requests

res = requests.get('https://www.google.com')
# res = requests.get("https://www.daum.net")
print(res)
print(res.content)







