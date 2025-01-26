from csv import reader;
from functions import MeanMedianStdev, Table;

with open('../sample_grades_v2.csv') as sample:
   readSample = reader(sample, delimiter=",");
   AvailableDates = set([i[1] for i in readSample]);
   DatesToSearch = []
   CreateTableForTheseDates = []
   finished = False;
   sample.seek(0);

   while not finished:
      entry = input(f"Enter a date to search from these available dates: {AvailableDates}.");

      if entry not in AvailableDates:
         print(f"Your entry MUST be within one of these dates: {AvailableDates}!!!");
      else: DatesToSearch = [*DatesToSearch, entry];

      finished = input("Are you Finished? N = No. Y = Yes.");
      if finished.upper() == 'N': finished = False;
      elif finished == '': finished = True;
      else: finished == True;
   
   ClassYears:dict = dict.fromkeys(set([i[1] for i in readSample]), []);
   sample.seek(0)

   for i in readSample:
      if i[1] in DatesToSearch:
         CreateTableForTheseDates = [*CreateTableForTheseDates, i[1]]
         ClassYears[i[1]] = [*ClassYears[i[1]], i]

   EndResult = {}
   for year in DatesToSearch:
      EndResult = {**EndResult, **MeanMedianStdev(year, ClassYears[year])}
   
   print("END RESULT:", EndResult)




   






