# --------------
#Code starts here

#Function to read file
def read_file(path):
    file = open(path, mode = 'r')
    sentence = file.readline()
    print(sentence)
    file.close()
    return sentence

    
#Opening of the file located in thee has been stored in a variable file_pat path in 'read' mode
sample_message = read_file(file_path)
print(sample_message)
    
#Printing the line of the file
#Function to fuse message
def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    return quotient

#Calling the function to read file  
message_1 = read_file(file_path_1)
print(message_1)
message_2 = read_file(file_path_2)
print(message_2)
secret_msg_1 = str(fuse_msg(message_1,message_2))
print(str(secret_msg_1))
#Calling the function to
#Calling the function 'fuse_msg'
#Printing the secret message
#e has been stored in a variable file_pat
#Function to substitute the message
message_3 = 'Green'
print(message_3)

def substitute_msg(message_c):
    sub = None
    if message_c is 'Red':
        sub = 'Army General'
    elif message_c is 'Green':
        sub = 'Data Scientist'
    elif message_c is 'Blue':
        sub = 'Marine Biologist'
    return sub

secret_msg_2 = substitute_msg(str(message_3))
print(secret_msg_2)

#Function to compare message
def compare_msg(message_d,message_e):

    a_list = message_d.split()
    print(a_list)
    
    b_list = message_e.split()
    print(b_list)    
    
    c_list = []
    for word in a_list:
        if word not in b_list:
            c_list.append(word)
    print(c_list)
    #Combining the words of a list back to a single string sentence
    final_msg = ' '.join(c_list)
    print(final_msg)
    #Returning the sentence
    return final_msg
    
#Calling the function to read file
message_4 = read_file(file_path_4)
print(message_4)

#Calling the function to read file
message_5 = read_file(file_path_5)
print(message_5)


#Calling the function 'compare messages'
secret_msg_3 =  compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)

#Function to filter message
def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x : len(x) % 2 == 0
    b_list = list(filter(even_word,a_list))
    final_msg = ' '.join(b_list)
    return final_msg
    
#Calling the function to read file
message_6 =  read_file(file_path_6)
#Calling the function 'filter_msg'
secret_msg_4 = extract_msg(message_6)

#Printing the secret message
print("secter_msg_4" + secret_msg_4)
print(secret_msg_3)
print(secret_msg_1)
print(secret_msg_2)

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg =  ' '.join(message_parts)
print(secret_msg)

#Function to write inside a file
def write_file(secret_msg,path):
    open(path, 'a+')
    path.write(secret_msg)
    path.close()
    #Opening a file named 'secret_message' in 'write' mo#Writing to the file
   

    #Closing the file


#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


