from csv import reader;
from statistics import mean, median, stdev;

def FindInvalidData(*data: dict):
   try:
      invalidData = list(filter(lambda x: type(x).__name__ != 'dict', [i for i in data]))

      if len(invalidData): raise AttributeError(f"While running invalidData = list(filter(lambda x: type(x).__name__ != 'dict', [i for i in data])), the following INVALID DATA WAS FOUND (see below):\n\n*** {invalidData[0]}. ***\n\nPlease go into your .csv file correct this error!!!");

   except AttributeError as ae:
      return f"ATTRIBUTE ERROR inside FindInvalidData function:\n{ae}."
   except Exception as exc:
      return f"Exception inside FindInvalidData function:\n{exc}."
   
def MeanMedianStdev(Year:str, data:list):
   try:
      '''
      This function takes in a year and a list of data as parameters and returns dict{'Year': {...data as string}}.\n\n
      ***** PARAMETER(S). *****\n
      Year: The year to look up as a string.
      data: A dictionary comprising of {mean, median, stdev}.
      '''

      scores = [float(lst[2])for lst in data] # returns an array of scores (index 2 inside each inner array) for that year (1st argument).
      
      return { Year: dict(mean=f"{round(mean(scores), 3):.3f}", median=f"{round(median(scores), 3):.3f}", stdev=f"{round(stdev(scores), 3):.3f}") } #returns dict{'Year': {...data as string}}
   
   # ***** ERROR HANDLING. *****

   except TypeError as te:
      return f"Data Type Error Inside MeanMedianStdev function. Please make sure you enter the right data type in your parameters: The year parameter should be a string & data should be a list.\nAlso, make sure each value inside scores can be evaluated as an integer.\n{te}\n{te.args}."
   except ValueError as ve:
      return f"VALUE ERROR INSIDE MeanMedianStdev function.!!! One of your values or value types cannot be evaluated:\n{ve}\n{ve.args}."
   except Exception as exc:
      return f"Some other error occurred inside your MeanMedianStdev function. Please see error code below:\n{exc}."


def Table(*data:dict):
   '''
   This function a table that displays the mean, median and standard deviation of the student data entered.\n
   !!!IMPORTANT!!! The data entered MUST have the student date/year as the KEY and the values must be in the form of {mean:number, median:number, stdev:number}. Having said that...\n\n
   ***** PARAMETER(s). *****:
   data: This parameter operates like a 'spread operator' in that it can take in multiple data in the form of a dictionary.
   '''
   try:
      FindInvalidData(*data) #Function to find invalid data.

      getKeys = [list(i.keys())[0] for i in data]; #returns a list of keys to be used in formatting.
      print(getKeys)
      getValues = [list(i.values())[0] for i in data];
      getMean = [f"{i['mean']}   " for i in getValues]; #Extra spaces are for formatting in the return.
      getMedian = [f"{i['median']}   " for i in getValues];#returns a list of median values to be used in formatting.
      getStdev = [f"{i['stdev']}   " for i in getValues]; #Same for stdev.

      return f"\t   {' '.join(getKeys)}\nMean:      {' '.join(getMean)} \nMedian:    {' '.join(getMedian)}\nSTD:       {' '.join(getStdev)}"; #Formatting.

   # ***** ERROR HANDLING. *****

   except AttributeError as ae:
      return f"ATTRIBUTE ERROR INSIDE Tables function! Please check your .csv file to make sure your data types are correct and are 'castable': {ae}";
   except Exception as exc:
      return f"An exception occurred inside your Table function: {exc}.";

