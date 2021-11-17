'''
File to load the vector
'''
def open_file(name, option):
    
    try:
        file = open(name,option)
        
        return file
        
    except:
        print('Error while opening file: %s' %name)
        exit(-1)




def load_data(name):

    user_data = []
    
    file = open_file('./biometrics/' + name + '_data.csv', 'r')
    
    for line in file:
        
        line_saver = []
        #Get each line
        line = line.split('\n')[0]
        line = line.split(',')
        
        #foe each value
        for i in range(len(line)):
            line_saver.append(line[i])
            
        user_data.append(line_saver)      
    
    print(user_data)
    #Close the file
    file.close()
    
    return user_data



if __name__ == '__main__':
    
    name = input('Name of the person of the data you want to load\n')

    user_data = load_data(name)
    
    '''
        user_data[0] represents all the input delays for the first pair of letters
        user_data[0][1] represents the input delay between the first pair of letters on the second attempt
    '''