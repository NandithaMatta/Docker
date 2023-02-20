import os
from collections import Counter
import socket
output = '\n'

path = "./home/data/"
dir_list = os.listdir(path)
output += "Files & directories in " + str(path) +" : " + str(dir_list)
# print("\nFiles & directories in '", path, "': ", dir_list)

def count_words_in_file(filename):
	# print(filename)
	number_of_words = 0
	with open('./home/data/' + filename,'r') as file:
		data = file.read()
		lines = data.split()
		number_of_words += len(lines)
	return number_of_words

number_of_words1 = count_words_in_file('Limerick.txt')
number_of_words2 = count_words_in_file('IF.txt')

output += "\n\nNumber of words in Limerick.txt: " + str(number_of_words1)
# print("\nNumber of words in Limerick.txt: ", number_of_words1)
output += "\nNumber of words in IF.txt: " + str(number_of_words2)
# print("Number of words in IF.txt: ", number_of_words2)

output += "\n\nTotal number of words in both files: " + str(number_of_words2)+str(number_of_words1)
# print("\ntTotal number of words in both files: ", number_of_words2+number_of_words1)

def k_most_frequent_words(filename, k=3):
	with open('./home/data/' + filename,'r') as file:
		data_set = file.read()
	split_it = data_set.split()
	counter = Counter(split_it)
	most_occur = counter.most_common(k)
	return most_occur

top_3_words = k_most_frequent_words('IF.txt')
output += "\n\n Top three frequent words in IF.txt: " + str(top_3_words)
# print("\n Top three frequent words in IF.txt: ", top_3_words)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
output += "\n\nIP Address is: " + str(IPAddr) + "\n"
# print("\nIP Address is: " + IPAddr)

# print(Output)


file1 = open('./home/output/result.txt', 'w')
file1.write(Output)
file1.close()

print("Writing to ./home/output/result.txt")
  
file1 = open('./home/output/result.txt', 'r')
print(file1.read())
file1.close()

