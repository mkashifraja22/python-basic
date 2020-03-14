#f = open("C:/Users/Muham/Desktop/python/test.txt")

try:
 f = open("C:/Users/Muham/Desktop/python/csv.csv",mode='r',encoding = 'utf-8')
 # perform file operations
 #f.write("this file is being created")
finally:
 f.close()
