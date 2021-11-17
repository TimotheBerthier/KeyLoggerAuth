# -*- coding: utf-8 -*-
"""
Machine Learning Project
"""
from tkinter.filedialog import askopenfilename, askdirectory 
import glob
import os.path

#FAzer o try to open except aqui
def choose_path():
    
    try:
        path = askdirectory()
        
        return path
    
    except:
        print('Error while opening the file')
        
        return -1
        pass


def open_file(name, option):
    
    try:
        file = open(name,option)
        
        return file
        
    except:
        print('Error while opening file: %s' %name)
        exit(-1)

def processing_the_data(path_to_files):
    
    #Will save the content from all the files processed
    profile = []
    file_num = 0
    for filename in glob.glob(os.path.join(path_to_files,"*.csv")):
        
        file = open_file(filename, 'r')
        
        #Flags
        first_line = -1
        previous_time = -1
        
        #Aux variables
        aux_profile = []
        
        for line in file:
            
            #Ignores the first line of the file
            if first_line == -1:
                first_line = 0
                continue
            
            #Splits the line and formats the time the way we want
            info = line.split(',')
            # Remove the \n
            info[5] = info[5][:-1]
            ms = int(info[5])
            s = int(info[4])
            m = int(info[3])
            h = int(info[2])
            
            #Calculate time in milliseconds
            time = ms + s*1000 + m*60*1000 + h*60*60*1000
            
            #First time a key is pressed
            if previous_time == -1:
                previous_time = time
            
            #If another key is pressed we count the interval between it
            elif info[0] == 'true':
                interval = time - previous_time
                previous_time = time
        
                #Add an item to the profile list
                aux_profile.append(interval)
            else:
                continue
        
        profile.append(aux_profile)
       
        #close current file
        file.close()
    
    print(profile)
    
    '''
    To print the profile we have profile[x][0] will print the value for the same pair of letters in distinct data
    
    profile[0][x] will print the times for all the pairs, ordered, for the same training data examplez
    '''
    
    return profile

def save_parameters(user_data,name):
    
    folder_name = './biometrics/'
    
    if not(os.path.exists(folder_name)):
        os.makedirs(folder_name)
        
    
    #Creates the output file
    output = open(folder_name + name + '_data.csv',"a")
    
    num_of_writtings = len(user_data)
    num_of_pairs = len(user_data[0])
    
    #Orders the file where each line are all the values associated to a delay in inseting a pair of letters
    for i in range(num_of_pairs):
        
        for j in range(num_of_writtings):
            output.write(str(user_data[j][i]))
            
            #Write the correct separator
            if j == num_of_writtings - 1:
                output.write('\n')
            else:
                output.write(',')
    
    
    
    output.close()
    return

if __name__ == '__main__':
    name = input('Who is this data from?\n')
    print('name: %s' %name)
    
    #path = choose_path();
    path = 'C:/Users/Utilizador/Desktop/Insa Lyon Semestre/Machine Learning/2º Projeto/smaller_sentence'
    print(path)
    user_data = processing_the_data(path)
    
    #Saves the values in a csv filea
    save_parameters(user_data, name)
    
    

    
    