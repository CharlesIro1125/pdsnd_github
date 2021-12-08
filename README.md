---
Title: "Bikeshare project"
date: 2021-12-3
output: Markdown_document
---


### BIKESHARE USAGE ANALYSIS IN CHICAGO, WASHINGTON AND NEW YORK CITY.


### Description
The Bikeshare project is an analysis and exploration into the Bikeshare usage in some regions in the United State.

For a better understanding into the mobility of individuals using the rental service in this region. This project analysis the usage in various levels, such as yearly, monthly and daily. These are describe below.

- It provides insight into the most frequent time of travels within the year, month or day being considered.

- It provides insight on the most popular stations and most popular trips within given periods. An insight into the most popular stations and trip will aid to better utilize the services provided.

- It provides insight into the various trip duration in seconds, also listing the most popular trips and the trip duration. An insight into the trip duration is also necessary in identifying trips and stations that produces more financial return to the bikeshare company.

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
The Washington dataset doesn't include the Gender and Birthyear columns.

### Environment Set-up

```
  Python version
    python >= 3.0

  Pandas version
    Pandas >= 0.25
    Run: pip install --upgrade pandas

```

### Cloning this repository.

After setting up your environment with the appropriate python and pandas version.
clone this repository into your local repository by running the git command within git bash as follows.

```
  $ git clone https://github.com/CharlesIro1125/pdsnd_github.git

```

 Go to the directory and run the bikeshare.py file in your command line to begin analysis.

`python bikeshare.py`

### Credits

I want to acknowlegde the knowlegde depth provided by **UDACTIY** and **BLACKS IN TECHNOLOGY** to attain this heights in programming for Data Science.
