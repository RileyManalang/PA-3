# PA-3
### Version
- Python 3.12.4 (Jupyter Notebook)

For starters: import the pandas library to the python code

# Problem #1: Getting a Specific row in the pandas data
> Tasks: Save your file as Surname_Pandas-P1.py then load the corresponding .csv file into a data frame named cars using pandas. Display the first five and last five rows of the resulting cars.

- For the first problem, I first imported the pandas library then extracted the content of the provided csv file which is named "cars.csv".
- I tried to experiment with some syntaxes using .iloc and .loc so that I can get the desired data in the table. Unfortunately, I had trouble with the knowledge I currently have about pandas.
- After a few tutorials and research, I managed to think of ways or approaches to solve the problem which I used a concatenate function of pandas to try and concatenate the rows of the first five and the last five, which resulted in a somehow close display of the desired output
- I then tried using a numpy function to stack the rows to each other, but this just created an array that is hard to read
- I then settled with just using the .head() and .tail() feature of pandas


# Problem#2: Use subsetting, slicing and indexing operations to extract data from the provided data
> Tasks: Display the first five rows with odd-numbered columns. Display the row that contains the ‘Model’ of ‘Mazda RX4’. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

- For this task, I mainly used .iloc when I wanted to get a whole row and column based on their positions
- In the other tasks, I used .loc so that I could easily specify what cell I wanted to be printed

## Challenges
- It was challenging to print the first 5 and last 5 rows of the data together
- In the second problem, I had difficulty in figuring out what was the best syntax for me using .iloc or .loc since the way it can be read is a bit tricky for me

## Learnings
- I managed to learn other syntax that I can use to attach a variable or output to one another such as .join() and .append()
- I also learned to use .iloc and .loc

## Version History:
### [v1.1.0] - 9/15/24
- initial work
### [v1.2.0] - 9/16/24
- improved the output displayed at the first problem
