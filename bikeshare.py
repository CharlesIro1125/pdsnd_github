import pandas as pd
import numpy as np
import time

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }



global city, month, day



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of month to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    print('There are Three cities avaliable.  Chicago,  New York City,  Washington \n \n')
    #  Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['Chicago', 'New York',  'Washington']
    city = input('Enter the city you would want to explore, Example: "Chicago", "New York", "Washington" \n--> ')
    while city.title() not in cities:
        print('oohhh!! you have entered an unknown city: "{}"'.format(city))
        city = input('Enter any of this cities: "Chicago", "New York", "Washington" \n--> ')

    print('Great !!!   you have entered the city: {}'.format(city))

    print('Would you like to explore the whole dataset or filter by Month \n \n')

    # Get user input for month (all, january, february, ... , june)

    option = input('Enter "All" to explore the whole Dataset or enter "Month" to filter by Month \n-->  ')
    options =['All','Month']
    while option.title() not in options:
        print('oohhh!! you have entered an unknown option: "{}"'.format(option))
        option = input('Enter either "All" to explore the whole Dataset or enter "Month" to filter by Month \n-->  ')
    if option.title() == 'Month':
        print('Great!!! Let\'s explore the bikeshare data for {} by {}'.format(city,option))
        month = int(input('Enter the month to explore in numbers, 01 for January. Example: 01,02,03,04,05,.... Note:The last avaliable month is 06 \n-->  '))
        months = [1,2,3,4,5,6]
        while month not in months:
            print('You have entered an unknown month for this dataset: "{}"'.format(month))
            month = int(input('Enter the month to explore in numbers, 01 for January. Example: 01,02,03,04,05,....  Note:The last avaliable month is 06 \n --> '))

        print('Great!! You have entered the city: {} and the month: {}'.format(city,month))


        # Get user input for day of week (all, monday, tuesday, ... sunday)

        print('Would you like to explore the month by day \n \n')
        day=input('Enter "All" to explore by month or enter a \"Day of the Month\" to explore by Day. Example: 1,2,3,4,5,....\n -->  ')
        daysinmonth={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        days = [str(i) for i in np.arange(1,32)]
        days.append('All')
        days.append('all')

        while day not in days:
            print('oohhh!! you have entered an unknown option: "{}" '.format(day))
            day=input('Enter "All" to explore by month or enter a \"Day of the Month\" to explore by Day. Example: 1,2,3,4,5,.... \n-->  ')

        if day.title() != 'All' :
            day = int(day)
            while day > daysinmonth[month] or day == 0:
                print('you have entered an incorrect day: "{}"'.format(day))
                day = int(input('Enter a Day for the Month: {} to explore by Day.\
                                                                        Example: 1,2,3,4,5,.... \n-->  '.format(month)))
            print('Great!!! you have entered the city: {}, and the month: {} and the day : {} \n \n'.format(city,month,day))

        else:

            print('Great!!! you have entered the city: {}, and the month: {} and the day : {} \n \n'.format(city,month,day))
            day = day.title()
        print('let\'s get started \n \n')
        print('-'*40)






    else:
        month = 'All'
        day = 'All'
        print('Great!!! you have entered the city: {}, and month: {}.\n \n'.format(city,month))
        print('let\'s get started \n \n')
        print('-'*40)

    #print('let\'s get started')
    #print('-'*40)
    return city.title(), month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day.
        Note: the Washington dataset has no Gender and Age attrobute

    """

    df = pd.read_csv('C:/Users/CHARLES OBINNA IRO/Downloads/Udacity_bikeshare/' + CITY_DATA[city.title()])

    if city.title() != 'Washington':

        df.fillna(value={'Gender':'unknown','Birth Year':0.0}, inplace= True)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df = df.sort_values(by =['Start Time'], ascending =True)
    df.set_index('Unnamed: 0',drop =True,inplace=True)
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day
    df['WeekDay'] = df['Start Time'].dt.weekday
    df['Hour'] = df['Start Time'].dt.hour

    monthname = {1:'January',2:'Febuary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',\
             9:'September',10:'October',11:'November',12:'December'}

    dayname  = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

    df['WeekDayString'] = df['WeekDay'].apply(lambda x : dayname[x])
    df['MonthString'] = df['Month'].apply(lambda x : monthname[x])

    if month == 'All':

        df = df

    else:

        df = df[df['Month'] == int(month)]


        if day == 'All':

            df = df

        else:

            df = df[df['Day'] == int(day)]



    return df


def time_stats(df,city,month,day):
    """
    Displays statistics on the most frequent times of travel..

    Args:
        (dataframe) df - the bikeshare user dataframe for the intended city to analyze
        (str) city - name of the city being analyze
        (str or int) month - digit of the month filtered by, or "all" for no month filter
        (str or int) day - digit of the day of month filtered by, or "all" for no day filter
    Returns:
        no return value, only Displays result of computation.
    """


    print('\nCalculating The Most Frequent Times of Travel for city: {}, month: {}, day: {}...\n'.format(city,month,day))
    start_time = time.time()


    # Display the most common month


    if month  == 'All':
        ttf = df.groupby(['MonthString','Day','WeekDayString'])[['MonthString','Day','WeekDayString']].count().idxmax()[0]
        commonMonth = ttf[0]
        commonday = ttf[1]
        commonWeekday = ttf[2]
        print('Most common travel month : {} \n Most common travel day : {}\n'.format(commonMonth,commonday))


        ddf = df[df['MonthString'] == commonMonth]

        # Display the most common day of week
        wwf = ddf.groupby(['WeekDayString'])[['WeekDayString']].count().idxmax()[0]
        commonWeekday1 = wwf
        print('Most common travel week day : {} \n'.format(commonWeekday1))
        # Display the most common start hour
        hhf = ddf.groupby(['Hour'])[['Hour']].count().idxmax()[0]
        commonhour = hhf
        print('Most common travel start time : {} hr\n'.format(commonhour))
    else:

        if day == 'All':
            # Display the most common day of week
            wwf = df.groupby(['WeekDayString'])[['WeekDayString']].count().idxmax()[0]
            commonWeekday1 = wwf
            print('Most common travel week day : {} \n'.format(commonWeekday1))

            # Display the most common start hour
            hhf = df.groupby(['Hour'])[['Hour']].count().idxmax()[0]
            commonhour = hhf
            print('Most common travel start time : {} hr\n'.format(commonhour))
        else:
            # Display the most common start hour
            hhf = df.groupby(['Hour'])[['Hour']].count().idxmax()[0]
            commonhour = hhf
            print('Most common travel start time : {} hr\n'.format(commonhour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display(dataset,output1='Nil',output2='Nil',output3='Nil',output4='Nil'):
    """
    Displays rows from the computed statistical result. The rows
     are displayed up to the next 5 index, and continues if more
      result are required to be outputed.When the dataset is empty,
      the rows prints a message indicating the end of the dataset.

    Args:
        (str) output1 - the first column from the computed statistical dataframe to display
        (str) output2 - the second column from the computed statistical dataframe to display
        (str) output3 - the third column from the computed statistical dataframe to display
        (str) output4 - the forth column from the computed statistical dataframe to display
    Returns:
        no return value, only Displays result of computation by rows.
    """


    row = 0
    more_result = 'Yes'
    incr = 5
    while more_result.title() == 'Yes' and row < len(dataset):
        if row + incr > len(dataset):
            if row - len(dataset) == 0:
                print('End of dataset. No more output to display')
                break

            else:
                incr -= 1
        else:
            if output4.title() != 'Nil' and output3.title() != 'Nil' and output2.title() != 'Nil' and output1.title() != 'Nil':
                try:
                    for i in range(row,row + incr):
                        print('{} : {} \n {} : {} \n {} : {} \n {} : {}\n'.format(output1,dataset.iloc[i][output1],\
                        output2,dataset.iloc[i][output2],output3,dataset.iloc[i][output3],output4,dataset.iloc[i][output4]))
                except e:
                    print('Wrong column name {}'.format(e))
            elif output4.title() == 'Nil' and output3.title() != 'Nil' and output2.title() != 'Nil' and output1.title() != 'Nil':
                try:
                    for i in range(row,row + incr):
                        print('{} : {} \n {} : {} \n {} : {} \n'.format(output1,dataset.iloc[i][output1],\
                        output2,dataset.iloc[i][output2],output3,dataset.iloc[i][output3]))
                except e:
                    print('Wrong column name {}'.format(e))
            elif output4.title() == 'Nil' and output3.title() == 'Nil' and output2.title() != 'Nil' and output1.title() != 'Nil':
                try:
                    for i in range(row,row + incr):
                        print('{} : {} \n {} : {}\n'.format(output1,dataset.iloc[i][output1],output2,dataset.iloc[i][output2]))
                except e:
                    print('Wrong column name {}'.format(e))
            elif output4.title() == 'Nil' and output3.title() == 'Nil' and output2.title() == 'Nil' and output1.title() != 'Nil':
                try:
                    for i in range(row,row + incr):
                        print('{} : {} \n'.format(output1,dataset.iloc[i][output1]))
                except e:
                    print('Wrong column name {}'.format(e))

            else:
                print('Enter the columns to output, starting from option1,option2,option3','option4')
            row += incr
            more_result = input('Type \'Yes\' to output next Five results or \'No\' to end output \n-->')

            while more_result.title() not in ['Yes','No']:
                print('ooohh you entered a wrong input: {} '.format(more_result))
                more_result = input('Type \'Yes\' to output next Five results or \'No\' to end output \n-->')
                print('\n')


def station_stats(df,city,month,day):

    """
    "Displays statistics on the most popular stations and trip
            using the DataFrame of the intended city being analyze."

    Args:
        (dataframe) df - the bikeshare user dataframe of the intended city being analyze
        (str) city - name of the city being analyze
        (str or int) month - digit of the month filtered by, or "all" for no month filter
        (str or int) day - digit of the day of month filtered by, or "all" for no day filter
    Returns:
        no return value, only Displays result of computation.
    """

    print('\nCalculating The Most Popular Stations and Trip for city: {}, month: {}, day: {} ...\n'.format(city,month,day))
    start_time = time.time()

    # Display most commonly used start station

    MostStartStation = df.groupby(['Start Station']).agg(Start_Station_Count =('Start Station','count'))\
                                    .sort_values(by=('Start_Station_Count'),ascending =False)
    MostStartStation = MostStartStation.reset_index()
    print('\nCalculating The most commonly used start station')
    print('-'*40,'\n')
    display(MostStartStation,output1='Start Station',output2='Start_Station_Count')

    # Display most commonly used End station

    MostEndStation = df.groupby(['End Station']).agg(End_Station_Count =('End Station','count'))\
                                .sort_values(by=('End_Station_Count'),ascending =False)
    MostEndStation = MostEndStation.reset_index()


    print('\nCalculating The most commonly used end station')
    print('-'*40,'\n')
    display(MostEndStation,output1='End Station',output2='End_Station_Count')


    # Display most frequent combination of start station and end station trip

    MostFreqTrip = df.groupby(['Start Station','End Station']).agg(Start_Station_Count=('Start Station','count'),\
        Start_to_End_Station_Count =('End Station','count')).sort_values(by=['Start_Station_Count','Start_to_End_Station_Count'],ascending =False)

    MostFreqTrip = MostFreqTrip.reset_index()

    print('\nCalculating The most frequent combination of start station and end station trip')
    print('-'*40,'\n')
    display(MostFreqTrip,output1='Start Station',output2='End Station',output3='Start_to_End_Station_Count')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city,month,day):
    """
    "Displays statistics on the total and average trip duration
            using the DataFrame of the intended city being analyze."

    Args:
        (dataframe) df - the bikeshare user dataframe of the intended city being analyze
        (str) city - name of the city being analyze
        (str or int) month - digit of the month filtered by, or "all" for no month filter
        (str or int) day - digit of the day of month filtered by, or "all" for no day filter
    Returns:
        no return value, only Displays result of computation.
    """

    print('\nCalculating Trip Duration for city: {}, month: {}, day: {} ...\n'.format(city,month,day))
    start_time = time.time()

    # Display total travel time and  mean travel time
    MostFreqTrip = df.groupby(['Start Station','End Station']).agg(StartStationCount=('Start Station','count'),\
        Trip_duration_in_seconds =('Trip Duration','sum'),Mean_Trip_duration_in_seconds =('Trip Duration','mean')).sort_values(by='StartStationCount',ascending =False)

    MostTripduration = MostFreqTrip.reset_index()
    print('\nCalculating The total travel time and mean travel time')
    print('-'*40,'\n')
    display(MostTripduration,output1='Start Station',output2='End Station',output3='Trip_duration_in_seconds',output4='Mean_Trip_duration_in_seconds')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city,month,day):
    """
    "Displays statistics on bikeshare users using the
            DataFrame of the intended city being analyze."

    Args:
        (dataframe) df - the bikeshare user dataframe of the intended city being analyze
        (str) city - name of the city being analyze
        (str or int) month - digit of the month filtered by, or "all" for no month filter
        (str or int) day - digit of the day of month filtered by, or "all" for no day filter
    Returns:
        no return value, only Displays result of computation.
    """



    print('\nCalculating Bikeshare User Stats for city: {}, month: {}, day: {} ...\n'.format(city,month,day))
    start_time = time.time()

    # Display counts of user types
    usertype = df.groupby(['User Type'])['User Type'].count().to_dict()
    for i, j in usertype.items():
        print('Bikeshare User Type : ', i,' = ', j)
    time.sleep(60)


    # Display counts of gender
    if city not in ['Washington','washington']:



        genderT = df.groupby(['Gender'])['Gender'].count().to_dict()
        for i, j in genderT.items():
            print('Gender : ', i,' = ', j)
        time.sleep(60)
        print('\n')

        # Display earliest, most recent, and most common year of birth
        minBirthyear = df[df['Birth Year'] != 0.0 ]['Birth Year'].min()
        maxBirthyear = df['Birth Year'].max()
        CommonBirthYearTable = df[df['Birth Year'] != 0.0 ].groupby(['Birth Year'])\
         .agg(Count_of_BirthYear =('Birth Year','count')).sort_values(by=('Birth Year'),ascending =True).reset_index()

        print('Earliest birth year of Bikeshare Users: {} \n'.format(minBirthyear))
        time.sleep(60)
        print('Most recent birth year of Bikeshare Users: {} \n'.format(maxBirthyear))
        time.sleep(60)

        print('\nCalculating the most common year of birth')
        print('-'*40,'\n')

        display(CommonBirthYearTable,output1='Birth Year',output2='Count_of_BirthYear')


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    "The main entry point of the algorithm"

    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df,city,month,day)
        station_stats(df,city,month,day)
        trip_duration_stats(df,city,month,day)


        user_stats(df,city,month,day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
