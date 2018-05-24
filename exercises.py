#1. Open the filenames.txt file with read-only access with the open() function

files = open('filenames.txt', 'r')

#2. Print the name of the file and if it is open or closed using the .name and .closed properties

print(files)

#3. Use a for loop to read all lines of filenames.txt into a list variable

for line in files:
    print(line)

#4. Print out all the lines from the file from your variable

#5. Close the filenames.txt file and print if the file is open or closed

files.close()

print(files)


#6. Create a file using the open() function called secrets.txt

new_file = open('secrets.txt', 'w')
print(new_file)

#7. Write your own secrets to the file with the write() function

new_file.write('i have many secrets')
new_file.write('and more secrets')

#8. Close the secrets.txt file using the close() method. DON'T FORGET!

new_file.close()


#9. Print out the contents of the text file in your terminal to prove it worked


print(new_file)

#10. Open your secrets.txt file in append mode and write some more super secret info

another_file = open('secrets.txt', 'a')
another_file.write('\nno secret gets leaked')

#11. Close the secrets.txt file again using the close() function

another_file.close()
print(another_file)

#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function

import os
os.rename('secrets.txt', '.superdupersecret.txt')


#13. See if you can see the file in your file explorer



#14. Create a list variable named file_names that contains a list of filenames

file_names = ['file_a.txt', 'file_b.txt', 'file_c.txt']


#15. Use the writelines() function to append the filenames to the filenames.txt file

update_file = open('filenames.txt', 'a')

for line in file_names:
    update_file.writelines(file_names)

#16. Delete the initial secrets.txt file now that you have a super secret hidden version

#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.

input_prompt = input('user.txt')
user_file = open(input_prompt, 'w')

print(user_file)
