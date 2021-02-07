# 1st change
# 2nd change
import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    flag = True
    city_input = input("Which city would you like to see data from Chicago, New york city or Washington?\n")
    while  flag:
        for city_name, filename in CITY_DATA.items():
            if city_input.lower() == city_name:
                # print(filename)
                city = city_name
                flag = False
        if flag == True:
           city_input = input("Can't find the data, please type city name  from Chicago, New york city or Washington?\n")
    month=6
    day=1
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    time_filter = input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter.\n")
    time_filter_str = ["month", "day", "both","none"]
    week_day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    month_name = ['january', 'february', 'march', 'april', 'may', 'june','all']
    time_filter_flag = True
    while  time_filter_flag:
        if time_filter.lower() == 'both':
            time_filter_flag = False
            month = input("Which month? January, Februray, March, April, May, or June\n")
            day = input("Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday\n")
        elif time_filter.lower() == 'month':
            time_filter_flag = False
            month = input("Which month? January, Februray, March, April, May, or June\n")
            day = 'all'
        elif time_filter.lower() == 'day':
            time_filter_flag = False
            day = input("Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday\n")
            month = 'all'
        elif time_filter.lower() == 'none':
            time_filter_flag = False
            day = 'all'
            month = 'all'
        else:
            time_filter = input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter.\n")
        if time_filter_flag == False and not (month.lower() in month_name and day.lower() in week_day):
            time_filter_flag = True
            print('Month or day is wrong, please input again\n')

    print('-'*40)
    return city, month, day, time_filter

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
    for city_name, filename in CITY_DATA.items():
        if city.lower() == city_name:
            filename_str = filename
    # load data file into a dataframe
    df = pd.read_csv(filename_str)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['Start_hour']  = df['Start Time'].dt.hour
    df['Start_month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_n = months.index(month.lower()) + 1
        # filter by month to create the new dataframe
        df = df[df['Start_month'] == month_n]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print(filename_str)
    return df

def time_stats(df, city, month, day, time_filter):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_count = df['Start_month'].value_counts()
    # print(month_count)
    month_popular = df['Start_month'].mode()[0]
    month_name = months[int(month_popular - 1)].title()
    # print(month_count[6])
    month_max_count = month_count[month_popular]
    print("What is the most popular month for traveling?")
    print(month_name)
    print("Most popular month:{}, Count:{}, Filter:{}\n".format(month_name,month_max_count,time_filter))

    # display the most common day of week
    week_day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    week_day_count = df['day_of_week'].value_counts()
    week_day_popular = df['day_of_week'].mode()[0]
    week_day_max_count = week_day_count[week_day_popular]
    print("What is the most popular day for traveling?")
    print(week_day_popular)
    print("Most popular day:{}, Count:{}, Filter:{}\n".format(week_day_popular,week_day_max_count,time_filter))

    # display the most common start hour
    hour_count = df['Start_hour'].value_counts()
    hour_popular = df['Start_hour'].mode()[0]
    hour_max_count = hour_count[hour_popular]
    print("What is the most popular hour for traveling?")
    print(hour_popular)
    print("Most popular hour:{}, Count:{}, Filter:{}\n".format(hour_popular,hour_max_count,time_filter))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df,city, month, day, time_filter):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_station_count = df['Start Station'].value_counts()
    Start_station_popular = df['Start Station'].mode()[0]
    Start_station_max_count = Start_station_count[Start_station_popular]
    print("What is the most popular Start Station for traveling?")
    print(Start_station_popular)
    print("Most popular Start Station:{}, Count:{}, Filter:{}\n".format(Start_station_popular,Start_station_max_count,time_filter))


    # display most commonly used end station
    End_Station_count = df['End Station'].value_counts()
    End_Station_popular = df['End Station'].mode()[0]
    End_Station_max_count = End_Station_count[End_Station_popular]
    print("What is the most popular end station for traveling?")
    print(End_Station_popular)
    print("Most popular end station:{}, Count:{}, Filter:{}\n".format(End_Station_popular,End_Station_max_count,time_filter))


    # display most frequent combination of start station and end station trip
    Start_End_Station_count = df.groupby(['Start Station','End Station']).size().reset_index(name="count")
    Start_End_Station_max = Start_End_Station_count['count'].max()
    Start_End_Station_name = Start_End_Station_count.loc[Start_End_Station_count['count'] == Start_End_Station_max]
    print("What is the most popular start and end station for traveling?")
    print(Start_End_Station_name)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df, city, month, day, time_filter):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Trip_Duration_sum = df['Trip Duration'].sum()
    Trip_Duration_count = len(df)
    # display mean travel time
    Trip_Duration_avg = df['Trip Duration'].mean()
    print("What is the total travel time and mean travel time?")
    print("Total Duration:{}, Count:{}, Avg Duration:{}, Filter:{}\n".format(Trip_Duration_sum, Trip_Duration_count, Trip_Duration_avg, time_filter))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day, time_filter):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    User_Type_count = df['User Type'].value_counts()
    print("What is the breakdown of users?")
    print(User_Type_count)
    print("\n")

    # Display counts of gender
    Gender_exists = 'Gender' in df
    if Gender_exists:
        Gender_count = df['Gender'].value_counts()
        print("What is the breakdown of gender?")
        print(Gender_count)
        print("\n")
    else:
        print("No gender data to share.\n")

    # Display earliest, most recent, and most common year of birth
    birth_year_exists = 'Birth Year' in df
    if birth_year_exists:
        birth_year_count = df['Birth Year'].value_counts()
        print("What is the oldest, youngest, and most popular year of birth?")
        # print(birth_year_count)
        birth_year_youngest = df['Birth Year'].max()
        birth_year_oldest = df['Birth Year'].min()
        birth_year_popular = df['Birth Year'].mode()[0]
        print("Year of birth: Oldest:{}, youngest{}, most popular year of birht{}, Filter:{}\n".format(birth_year_oldest, birth_year_youngest, birth_year_popular, time_filter))
    else:
        print("No Birth Year data to share.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day, time_filter = get_filters()
        df = load_data(city, month, day)
        time_stats(df,city, month, day, time_filter)
        station_stats(df,city, month, day, time_filter)
        trip_duration_stats(df,city, month, day, time_filter)
        user_stats(df, city, month, day, time_filter)

        head_print_input = input("Would you like see 5 lines of raw data? Enter \'yes\' for see data\n")
        if head_print_input.lower() == 'yes':
            pd.set_option('display.max_rows', 1000)
            print(df.sample(n = 5).drop(columns=['Start_hour', 'Start_month','day_of_week']))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
