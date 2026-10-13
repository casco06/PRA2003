from collections import Counter
# import relevant function

def analyze(fileraw):

    file = fileraw.strip('"')
    with open(file , 'r') as f:
    # ask user for file path and open it, also strip it of the parentheses that are often included

        experiments = 0
        total_elements3 = []
        # declare 2 variables to store the total experiments, and an empty list for the ID occurrences

        for line in f:
            elements = line.split()
            # for a line in the file split the entries into indexable strings.

            if len(elements) < 4 and elements[1] != str(0):
                experiments +=1
                continue
            # if the line is a header for an experiments (less then 4 elements), and the second entry is not 0 (the experiment wasnt empty)
            # add 1 to the experiment counter

            elif len(elements) == 4:
                total_elements3.append(elements[3])
            # if it is not a header (4 elements) then append the ID for that line to the list

        

    ID_occurences = Counter(total_elements3)
    # use the Counter function on the list with all ID occurences to count each unique appearance

    Avg_per_experiment = {k : [v, v/experiments] for k, v in ID_occurences.items()}
    # make a dictionary that containts the ID and its average per experiment by dividing the keys by the experiment variable


    
    with open('total_data.csv', 'a') as r:
        r.write('\n')
        for k, v in Avg_per_experiment.items():
            r.write(f'{k}, {v[0]}, {v[1]}, {v[1]**0.5}\n')

analyze(r'C:\Users\casco\Downloads\output-Set8.txt')
analyze(r'C:\Users\casco\Downloads\output-Set9.txt')
analyze(r'C:\Users\casco\Downloads\output-Set10.txt')
