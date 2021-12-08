
### Date created

Date.format(new Date("10 Jan 2011"), "%B %d, %Y")

date: "`r format(Sys.Date(), '%d %B, %Y')`"


Include the date you created this project and README file.

### BIKESHARE USAGE ANALYSIS IN CHICAGO, WASHINGTON AND NEW YORK CITY.


### Description
The Bikeshare project is an analysis and insights into the Bikeshare usage in some regions in the United State.

For a better understanding into the mobility of individuals using the rental service in this region, this project analysis the usage in various levels, such as yearly, monthly and daily. These are describe below.

- It provides insight into the most frequent time of travels within the year, month or day being considered.

- It provides insight on the most popular stations and most popular trips within given periods. An insight into the most demanding/popular stations and trip will aid a better utility of the service.

- It provides insight into the various trip duration in seconds, also listing the most popular trips and the trip duration. An insight into the trip duration is also necessary in identifying trips that produce more financial return to the bikeshare company.

-  It provides insight into the user type , gender and age. This is key in knowing the type of subscribers who uses the services the most.

### Files used
The files used are the csv data files of bikeshare usage in Chicago, New York City and Washington, and the python code file for analysis . This file are defined as

- [x] chicago.csv

- [x] new_york_city.csv

- [x] washington.csv

- [x] bikeshare.py

The csv files are made up of column attributes such as.

```
[
  "Start time",
  "End time",
  "Trip duration",
  "Start Station",
  "End Station",
  "User Type",
  "Gender",
  "Birthyear",
]
```  
But the Washington dataset doesn't include the Gender and Birthyear columns.

### Environment Set-up

```
  Python version
    python >= 3.0

  Pandas verion
    Pandas >= 0.25
    Run: pip install --upgrade pandas

```

### Cloning this repository.

After setting up your environment with the appropriate python and pandas version.
clone this repository into your local repository by running the git command within git bash as follows.

```
  $ git clone https://github.com/CharlesIro1125/pdsnd_github.git

```
### Credits

I want to acknowlegde the knowlegde depth provided by **UDACTIY** and **BLACKS IN TECHNOLOGY** to attain this heights in programming for Data Science.
