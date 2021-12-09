# -*- coding: utf-8 -*-
"""
Manhattan Norm (scaled) for key strokes dynamics

"""


#Opens a file in a directory - name, with a certain option - option
def open_file(name, option):
    
    try:
        file = open(name,option)
        
        return file
        
    except:
        print('Error while opening file: %s' %name)
        exit(-1)



def load_data(name,mode):

    user_data = []
    
    #Decodes the mode
    
    #training folder
    if mode == 'train':
        folder = './biometrics_training/'
    
    #test data folder
    elif mode == 'test':
        folder = './biometrics_test/'
    
    #error
    else:
        exit(-1)
        
    
    
    
    file = open_file(folder + name + '_data.csv', 'r')
    
    for line in file:
        
        line_saver = []
        #Get each line
        line = line.split('\n')[0]
        line = line.split(',')
        
        #foe each value
        for i in range(len(line)):
            line_saver.append(line[i])
            
        user_data.append(list(map(int,line_saver)))     
    

    #print(user_data)
    #Close the file
    file.close()
    
    return user_data


def get_mean_vect (user_data):
    
    mean_vect = []
    
    #for each data sentence input that will be used as training data
    for j in range(len(user_data[0])):
        
        #For each pair of inputs in the sentence
        for i in range(len(user_data)):
            
            #If this is the first input sentence
            if j == 0:
                mean_vect.append(user_data[i][j])
            else:
                mean_vect[i] = mean_vect[i] + user_data[i][j]
                
    
    for i in range(len(user_data)):
        mean_vect[i] = int(mean_vect[i]/len(user_data[0]))
        
    print(mean_vect)
        
    return mean_vect

# Get the absolute deviation between
def get_abs_deviation (user_data, mean_vect):
    
    deviation = []
    
    
    #for each data sentence input that will be used as training data
    for j in range(len(user_data[0])):
        
        #Set max deviation of current iteration to 0
        curr_max = 0
        
        #For each pair of inputs in the sentence
        for i in range(len(user_data)):
            
            # Mean value minus one iteration is a deviation
            curr_dev = abs(mean_vect[i] - user_data[i][j])
            
            
            #If this is the first input sentence
            if j == 0:
                deviation.append(curr_dev)
                
            else:
                deviation[i] = deviation[i] + curr_dev
                
    #Performs the average of each absolute deviation
    for i in range(len(user_data)):
        deviation[i] = int(deviation[i]/len(user_data[0]))
    
    
    return deviation


# Application of the manhattan scaled formula
def get_score (test, mean_vect, dev_vect):
    
    score_now = 0
    all_scores = []
    
    #for each data sentence input that will be used as training data
    for j in range(len(test[0])):
        score_now = 0
        #Set max deviation of current iteration to 0
        
        #For each pair of inputs in the sentence
        for i in range(len(test)):
            
            aux_score = abs(test[i][j] - mean_vect[i])/float(dev_vect[i])
                
            # The score in a test input is the sum of manhattan score for all pairs inside the sentence
            score_now +=aux_score
        
        #Adds a new score corresponding to a full input
        all_scores.append(score_now)
        
    #Returns the vectors of all the scores achieved
    return all_scores

# Main function of the program
if __name__ == '__main__':
    name = input('Name of the person of the data you want to load\n')
    
    #vector of the mean
    mean_vect = []
    # average absolute deviation
    avg_abs_dev = []
    
    #Get training data
    user_data = load_data(name,'train')
    
    #Build the mean vector
    mean_vect = get_mean_vect(user_data)
    
    #Builds the average of the absolute deviations
    avg_abs_dev = get_abs_deviation (user_data, mean_vect)
    
    print(avg_abs_dev)
    
    #Gets the test data
    test_data = load_data(name, 'test')
    
    results = get_score(test_data,mean_vect, avg_abs_dev)
    
    print (results)
    