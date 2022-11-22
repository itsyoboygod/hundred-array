import sys
import numpy as np

arr = np.arange(100)

#arr[:] = np.random.randint(0, 1)

#arr = np.random.randint(2, size=(10, 10))

#np.set_printoptions(100,100, 5, linewidth=10)
#np.set_printoptions(10, 0, 100, 50)

#np.set_printoptions(threshold=sys.maxsize)

#arr.reshape(100,10).tolist()

print("#--------------------------------------------------------- \n")

print("arr = np.random.randint(2, size=100)")
print("")
print("np.set_printoptions(10, 0, 100, 30)")
print("")
print(arr)
print("")
print("#--------------------------------------------------------- \n")


print("#--------------------------------------------------------- \n")

print("arr.reshape(10,10).tolist()")
print("")
#arr.reshape(100,10).tolist()
#print(arr)
print("")
print("#--------------------------------------------------------- \n")

#print(arr)


with open("rdm_arr_output.csv", "a") as f:
	print(arr, file=f)

arr.tofile('rdm_arr_output.csv', sep = ',', format='%s')



#np.set_printoptions(threshold=np.inf, linewidth=50, edgeitems=5)


#values = np.array([-3,-2,-1,0,1,2,3])
#values = np.clip(values,-2,2)

#print(values)

# Create an array list from 1 to 100 values
#	arr = list(range(1,100))

# Show before a certain point
#	print (arr[:50])

# Add a value
#	arr.append('theValue')

# Remove a value
#	arr.pop(0)


#arr = list(range(0,100))
#x = list(range(0,100))

# SHOW FULL ARRAY LIST
#x = np.random.randint(0, 100, size=(32, 32))
#x = np.random.randint(0, 100)
#x = np.arange(100)
#x = np.arange(0, 100)
#print(x)
#np.set_printoptions(edgeitems=9)
#print(x)
#np.set_printoptions(threshold=np.inf, linewidth=50, edgeitems=5)
#np.set_printoptions(threshold=np.inf, linewidth=50)
#np.set_printoptions(threshold=5, linewidth=50)
#np.set_printoptions(linewidth=10)
#print(x)

#with open("arr_output.csv", "a") as f:
#	print(x, file=f)

#x.tofile('arr_output.csv', sep = ',')

#print (arr[5])


#imgarr = np.asarray(img)
#print (img[:,:,:])


#arr = np.arange(0, 100)
#np.set_printoptions(threshold=50)

#     * vertical axis downwards, summarizing across rows (axis=0)
#np.max(arr, axis=1)
#     * hortizontal axis, summarizing across columns (axis=1)


# Print array till certaind point with x of increment
#	print (arr[0:100:2])
#print (np.max(arr, axis=0))

#print(arr[])
# Print array length
#	print (len(arr))


#print (list(arr[::]))


#print (arr)


