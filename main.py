from csv import reader;
from statistics import StatisticsError;
from folder.functions import MeanMedianStdev, Table;

try:
   open_csv = open('./sample_grades.csv');
   readcsv = reader(open_csv);

   ClassYears:dict = dict.fromkeys(set([i[1] for i in readcsv]), []); #Inializes each key to a value of []. Returns { "Fall 2016": [], "Spring 2016": [] }. I decided to use set([i[1] for i in readcsv]), []) instead of ['Fall 2016', 'Spring 2016'] so as to make this more 'dynamic' in case more years are added.

   open_csv.seek(0) #resets FileIO pointer to the beginning after reading. Otherwise, it would stay at the end of the file and cannot read anymore.

   for i in readcsv:
      ClassYears[i[1]] = [*ClassYears[i[1]], i] # returns series of rows. Each row is of type list[[name, year, score]...].

   print(Table(MeanMedianStdev('Fall 2016', ClassYears['Fall 2016']), MeanMedianStdev('Spring 2016', ClassYears['Spring 2016']))) #Result.

   open_csv.close();

# ***** ERROR HANDLING!!! *****

except TypeError as te:
   print(f"TYPE ERROR: You are putting in the wrong type - {te}.");

except FileNotFoundError as fnfe:
   print(f"You may have mis-typed the file you are trying to open - {fnfe}.")

except IndexError as ie:
   print(f"INDEX ERROR: Please check inside your .csv file to see if you have a number with nothing in front of it. Each number should have some data (e.g.: 1 data, 2 data, 3 data, etc...) - {ie}.");

except StatisticsError as se:
   print(f"STATISTICS ERROR: If you are doing standard deviation, you need AT LEAST TWO SETS OF DATA - {se}.");

except NameError as ne:
   print(f"NAMING ERROR!!!\nThis could be in your .csv file. It is possible that one of your data types cannot be casted or evaluated as a float/int. Please see NameErrorBelow:\n{ne}.");

except KeyError as ke:
   print (f"KEY ERROR INSIDE main.py!!!!!\nYou tried to access a key that does NOT exist inside your dictionary. Please Check your spelling for the following key to make sure it is correct:\n{ke}\n{ke.args}")

except Exception as exc:
   print(f"You goofed up somewhere :( :( :( - {exc}.")