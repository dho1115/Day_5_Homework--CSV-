from csv import reader;
from statistics import mean, median, stdev;

open_csv = open('./sample_grades.csv');
readcsv = reader(open_csv);

ClassYears = dict.fromkeys(set([i[1] for i in readcsv]), []); #Inializes each key to a value of []. Returns { "Fall 2016": [], "Spring 2016": [] }. I decided to use set([i[1] for i in readcsv]), []) instead of ['Fall 2016', 'Spring 2016'] so as to make this more 'dynamic' in case more years are added.

open_csv.seek(0) #resets FileIO pointer to the beginning after reading. Otherwise, it would stay at the end of the file and cannot read anymore.

for i in readcsv:
   ClassYears[i[1]] = [*ClassYears[i[1]], i] # returns series of rows. Each row is of type list[[name, year, score]...].

def MeanMedianStdev(Year:str, data:list):
   '''
   This function takes in a year and a list of data as parameters and returns dict{'Year': {...data as string}}.
   parameters:
   Year: The year to look up as a string.
   data: A dictionary comprising of {mean, median, stdev}.
   '''
   scores = [float(lst[2]) for lst in data] # returns an array of scores (index 2 inside each inner array) for that year (1st argument).
   
   return { Year: dict(mean=f"{round(mean(scores), 3):.3f}", median=f"{round(median(scores), 3):.3f}", stdev=f"{round(stdev(scores), 3):.3f}") } #returns dict{'Year': {...data as string}}

def Table(*data:dict):
   '''
   This creates a table.
   parameters:
   data: This parameter operates like a 'spread operator' in that it can take in multiple data in the form of a dictionary.
   '''
   getKeys = [list(i.keys())[0] for i in data]; #returns a list of keys to be used in formatting.
   getValues = [list(i.values())[0] for i in data];
   getMean = [f"{i['mean']}   " for i in getValues]; #Extra spaces are for formatting in the return.
   getMedian = [f"{i['median']}   " for i in getValues];#returns a list of median values to be used in formatting.
   getStdev = [f"{i['stdev']}   " for i in getValues]; #Same for stdev.

   return f"\t   {' '.join(getKeys)}\nMean:      {' '.join(getMean)} \nMedian:    {' '.join(getMedian)}\nSTD:       {' '.join(getStdev)}"; #Formatting.

print(Table(MeanMedianStdev('Fall 2016', ClassYears['Fall 2016']), MeanMedianStdev('Spring 2016', ClassYears['Spring 2016'])))

open_csv.close();