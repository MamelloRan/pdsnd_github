###Python Script to BikeShare Project###

import time
import pandas as pd
import numpy as np

###Start of the actual code to run over the imported dictionaries ###
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ('Enter the name of the city, between Chicago, New York City or Washington, you would like to analyse: ').lower()
        if city in ('washington', 'chicago', 'new york city'):
            break
        elif city == 'new york':
            city += ' city'
            break
        else:
            print('Your answer does not match any of the options provided. Please try again!')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input ('Which month would you like to sort the data by?: ').lower()
        if month in (months):
            break
        else:
            print('Your answer does not match any of the options provided. Please try again, and make sure that your answer lies between "january and june"(inclusive) and is all in lowercase!!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input('Enter the week-day you would like to filter by (Monday to Sunday): ').lower()
        if day in (days):
            break
        else:
            print('Your answer does not match any of the options provided. Please try again, and make sure that your answer is all in lowercase!')

    return city, month, day
    print('-'*40)


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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Frequent Start Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Frequent Start Day:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode()

    print('Most Popular Trip:', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types:', user_types)

    # TO DO: Display counts of gender


def user_stats_gender(df):
    if 'Gender' in df.columns:
        user_stats_gender(df)

    counts_of_gender =  df['Gender'].value_counts()
    print('Counts of gender:', counts_of_gender)

    #Iteration of answers#
    for index, count_of_gender in enumerate(counts_of_gender):
        print("  {}: {}".format(counts_of_gender.index[index], count_of_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
def user_stats_birth(df):
    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    start_time = time.time()

    earliest_year_of_birth = df['Birth Year'].value_counts().min()
    print('Earliest birth year', earliest_year_of_birth)

    most_recent_year_of_birth = df['Birth Year'].value_counts().max()
    print('Latest birth year', most_recent_year_of_birth)

    most_common_year_of_birth = df['Birth Year'].value_counts().mode
    print('Most common birth year', most_recent_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Display of the raw data."""
    answer = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()

    if answer=='yes' or answer=='y' or answer=='yus':
        answer=True
    elif answer=='no' or answer=='n' or answer=='nope':
        answer=False
    else:
        print('You might have made a typing error. Please consider your options, and try that again.')
        display_data(df)
        return

    if answer:
        while True:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Would you like to see 5 more lines of raw data? Yes/No ').lower()
            if choice=='yes' or choice=='y' or choice=='yus':
                continue
            elif choice=='no' or choice=='n' or choice=='nope':
                break
            else:
                print('You might have made a typing error. Please consider your options, and try that again.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
