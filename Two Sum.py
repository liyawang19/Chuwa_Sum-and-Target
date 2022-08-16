def findArrayIndex(arr,target):
    temp = 0
    arrResult =[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            temp = arr[i] + arr[j]
            if (temp == target):
                pair = [i,j]
                arrResult.append(pair)      
    print(arrResult)            
    return arrResult
                
if __name__ == "__main__":
    arr = [2,3,6,7,8]
    target = 9
    findArrayIndex(arr, target)
  

    