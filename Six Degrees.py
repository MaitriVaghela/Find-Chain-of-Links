"""
language: python3
description: To find a chain of no more than three links that connects two given names.
"""

#Three dictionaries are created.

#dict1 has movie names as keys.
dict1={}

#dict2 has names of the actors as keys.
dict2={}

#dict3 is used for tracing path
dict3={}

#This list keeps a track of the actors visited while searching
actorsVisited = []

#This list keeps a track of the movies visited while searching
moviesVisited = []

#This list will deal with the pushing and popping of elements to find a chain
queue = []

#counter is initialised to 0 to keep a track of finding a chain of no more than three links
counter = 0

max_depth=3

def form_data_Structure():
    """
                       This function reads the file contents into the data structure and prints the contents of the
                       data structure.
    """

    #It prompts the user to type the filename
    fname=input("enter the file name")

    #It opens the file and performs following computations
    with open(fname) as f:
        for line in f:

            #The words in the line are splitted on the basis of whitespace character
            line=line.split()

            temp=line[1:]
            i=0

            #An empty list is created
            finallist=[]

            #The loop is iterated untill the length of temp
            #and two names are concatanated and appended into the finallist at the end of each iteration
            while(i<len(temp)):
                new_name=temp[i]+" "+temp[i+1]
                finallist.append(new_name)
                i=i+2

            #finallist is given as a value of key 'line[0]' of dict1
            dict1[line[0]] = finallist

            #another empty list vallist is created
            vallist=[]

            #Contents are added into dict2
            for key in finallist:
                if key in dict2.keys():
                    init_list=dict2[key]
                    init_list.append(line[0])
                    dict2[key]=init_list
                else:
                    init_list=[]
                    init_list.append(line[0])
                    dict2[key]=init_list


    #Contents of the data structure is printed
    print("Dictionary 1 is:",dict1)
    print("Dictionary 2 is:",dict2)

    #It prompts the user to give two names for trying to connect it
    source = input("Enter the starting goal name")
    target = input("Enter the goal node name")

    #start actor name is appended into the queue
    queue.append(source)

    #'source' key in dict3 is given None as value
    dict3[source] = None

    #This function is called to find a chain between two names
    find_chain(source,target,counter)

def printpath(target):
    """
        This function traces the path/chain found between two names.
        :param target:the name from which the chain has to be found to the source
        :return: None
    """

    #It checks whether we have reached the source name
    if dict3[target]==None:
        print(target)
        return

    #Function is called recursively for further computation
    printpath(dict3[dict3[target]])

    #links of chain are printed
    print("     was in " + dict3[target] + " with")
    print(target)

def find_chain(source,target,counter):
    """
            This function finds the chain between two names.
            :param source:the start actor name
            :param target:the finish actor name
            :param counter:to restrict the chain till three links
            :return: printpath
    """

    #It is iterated till the queue is not empty and chain has three links
    while len(queue) != 0 and counter <= 2 * max_depth:
        counter += 1
        size = len(queue)

        #It iterates till the size of the queue obtained above
        for i in range(0, size):
            val = queue.pop(0)

            #If the value popped is our target, then it calls the printpath function to trace the path
            if val == target:
                return printpath(val)

            #It checks whether the value popped is in dict2
            #If it is, then that value is appended into actorsvisited list
            if val in dict2:
                actorsVisited.append(val)

                #for the value of key 'val' in dict2,
                #If that movie is not in moviesVisited list, then that movie name is made as key in dict3 and val is inserted
                #as its value in it.
                #Also that movie name is appended into the queue
                for movie in dict2[val]:
                    if movie not in moviesVisited:
                        dict3[movie] = val
                        queue.append(movie)

            # It checks whether the value popped is in dict1
            # If it is, then that value is appended into moviesVisited list
            if val in dict1:
                moviesVisited.append(val)

                # for the value of key 'val' in dict1
                # If that star is not in actorsVisited list, then that star name is made as key in dict3 and val is inserted
                # as its value in it
                # Also that star name is appended into the queue
                for star in dict1[val]:
                    if star not in actorsVisited:
                        dict3[star] = val
                        queue.append(star)

    #If conditions of while loop fails, Then it prints the following
    print("No Chain exists")


def main():
    """
               This function calls the function form_data_Structure.
    """
    form_data_Structure()



if __name__=="__main__":
    #main() is called
    main()