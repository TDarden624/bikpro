import time
import pandas as pd
import numpy as np

cities = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Args:
        None.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in cities:
        while city.lower() not in cities:
            city = input("\n Which city would you like to analyze? (Chicago, New York City, Washington DC) \n").lower()
        if city.lower() == 'Chicago':
            return 'chicago.csv'
        elif city.lower() == 'New York City':
            return 'new york.csv'
        elif city.lower() == 'Washington DC':
            return 'washington.csv'
        else:
            print("\n Please enter a valid city")

    months:['January','February','March','April','May','June','None']
    month = ''
    while month not in months:
        while month.lower() not in months:
            month = input("\nPlease choose a month to filter by. \nJanuary, February, March, April, May, June, None \n")
        if month in months:
            return("\nYou've chose {month.title()} as your month.")
        else:
            print("\nPlease enter a valid month")
            
    days:['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    day = ''
    while day not in days:
        while day.lower() not in days:
            day = input("\nWhat day would you like to filter by? \nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All\n")
            if day in days:
                    return("\n Let's pull all the data for all {}s." .format.title())
        else:
            print("\nPlease enter a valid day")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    df = pd.read_csv(CITY_DATA[city])


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

def common_day(df):   
    """Display the most common day of the week to travel."""
    print('\nCalculating The Most Common Day To Travel...\n')
    common_day = df['day_of_week'].mode()[0]


def common_hour(df):
    """Display the most common hour of travel in the day."""
    print('\nCalculating The Most Common Hour Of Day To Travel...\n')
    common_hour = df['hour'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

def common_start_station(df):
    """Displays the most popular start station."""
    
    print('\nCalculating The Most Common Start Station...\n')
    common_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station is {}".format(common_start_station))

def common_end_station(df):    
    """Displays the most popular end station."""
    
    print('\nCalculating The Most Common End Station...\n')
    common_end_station = df['End Station'].mode()[0]
    print("The most common End Station is {}".format(common_end_station))


def frequent_combo(df):  
    """Displays the most frequented start and end station."""
    print('\nCalculating The Most Frequented Start And End Station...\n')
    frequent_combo = df['Start Station', 'End Station'].mode()[0]
    print("The most frequented combo is {}, {}".format(frequent_combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {} seconds.'.format(hour, minute, second))


    mean_time = df['Trip Duration'].mean()
    minute, second = divmod(mean_time, 60)
    if min > 60:
        hour, minute = divmod(minute, 60)
        print('The average trip is {} hours, {} minutes and {} seconds.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts()
    print("The user types are:\n", user_counts)


    if city == 'chicago.csv' or city == 'new_york_city.csv':
        User_gender = df['Gender'].value_counts()
        print("The types of user by 'Gender' are:\n", User_gender) 

def birth_year(df):
    """Displays the earliest, most recent, and most common year of birth."""
    earliest_year = df['birth_year'.min()]
    latest_year = df['birth_year'.max()]
    common_year = df['birth_year'.mode()]
    print('The oldest users are born in {}.''\nThe youngest users are born in {}.''\nThe most common year users are born in {}.'.format(earliest_year, latest_year, common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
