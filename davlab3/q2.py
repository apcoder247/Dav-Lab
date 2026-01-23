import numpy as np
arr1=np.array(list(map(int, input("Enter the elements of the first matrix separated by space\n").split()))).reshape(3,3)
arr2=np.array(list(map(int, input("Enter the elements of the first matrix separated by space\n").split()))).reshape(3,3)

print("Array 1:\n",arr1)
print("\nArray 2:\n",arr2)

print("\nSum of the Arrays:\n",arr1+arr2)
print("\nDifference of the Arrays:\n",arr1-arr2)
print("\nElement wise multiplication of the Arrays:\n",arr1*arr2)
print("\nDot product of the Arrays:\n",np.dot(arr1,arr2))
print("\nTranspose of the Array 1:\n",np.transpose(arr1))
print("\nTranspose of the Array 2:\n",np.transpose(arr2))
delta1= np.linalg.det(arr1)
delta2= np.linalg.det(arr2)
if delta1!=0:
    print("\nInverse of the Array 1:\n",np.linalg.inv(arr1))
else:
    print("First matrix is not invertible")


if delta2!=0:
    print("\nInverse of the Array 2:\n",np.linalg.inv(arr1))
else:
    print("Second matrix is not invertible")
    
