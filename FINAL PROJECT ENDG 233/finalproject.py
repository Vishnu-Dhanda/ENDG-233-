# ENDG 233 FINAL PROJECT - POPULATION AND THREATENED SPECIES DATA
# VISHNU DHANDA AND HARSH CHITRODA, ENDG 233 F21 FINAL PROJECT
# A terminal-based application to process and plot data based on given user input and provided csv files.
#importing modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class threatened_species_data:
    """ A class used to create the print_all_stats object.

        Attributes:
            most_threatened_species (str): String that represents the most threatened species within a country.
            least_threatened_species (str): String that represents the least threatened species within a country.
            total_threatened_species (int): Integer that represents the total number of threatened species within a country.
            average_threatened_species (float): Float that represents the average number of threatened species within a country.

    """
    def __init__(self, most_threatened_species, least_threatened_species, total_threatened_species, average_threatened_species):
        self.average_threatened = average_threatened_species
        self.most_threatened = most_threatened_species
        self.least_threatened = least_threatened_species
        self.total_threatened = total_threatened_species
    
    def print_all_stats(self):
        """A function that prints the Total number of threatened species, average number of threatened species
            , most threatened species and least threatened species.

        Parameters: None
        Return: None

        """
        print(f'Total number of threatened species: {self.total_threatened}')
        print(f'Average number of threatened species: {self.average_threatened}')
        print(f'Most threatened species: {self.most_threatened}')
        print(f'Least threatened species: {self.least_threatened}')
        
def change_in_pop(years_list, population_data, country_index, starting_year, ending_year):
    """ A function that calculates the change in population of a country between years specified by the user.

    Parameters:
    years_list -- list of years created from first row of Population_Data.csv
    population_data -- imported data from Population_Data.csv
    country_index -- integer value found from checking the index of the country entered in the countries list
    starting_year -- integer value of the starting year entered by the user.
    ending_year -- integer value of the ending year entered by the user.

    Return: Calculated integer value of change in population within the specified range of years.

    """
    starting_year_index = int(years_list.index(starting_year)) #gets index of the starting year entered from the list of years and casts it to an integer.
    ending_year_index = int(years_list.index(ending_year)) #gets index of the ending year entered from the list of years and casts it to an integer.
    delta_population = int(population_data[country_index, int(ending_year_index)]) - int(population_data[country_index, int(starting_year_index)]) #calculating the change in population.
    return (delta_population)

def average_pop_function(population_data, country_index, starting_year_index, ending_year_index):
    """ A function that calculates the average population of a country between years specified by the user.

    Parameters:
    population_data -- imported data from Population_Data.csv
    country_index -- integer value found from checking the index of the country entered in the countries list
    starting_year_index -- integer value found from checking the index of the starting_year entered in the years_list.
    ending_year_index -- integer value found from checking the index of the ending_year entered in the years_list

    Return: Calculated integer value of the average population within the specified range of years.

    """
    #creates a list from population_data containing values within the years entered by the user.
    average_population = list(population_data[country_index, starting_year_index : ending_year_index]) 
    average_population = int(np.mean(average_population)) #calculates mean of all the values in the list and casts it to an integer.
    return(average_population)

def pop_density_function(population_data, years_list, square_km_list, country_index, max_year):
    """ A function that calculates the  population density of a country using the population of the country and the square Km of the country.

    Parameters:
    population_data -- imported data from Population_Data.csv
    years_list -- list of years created from first row of Population_Data.csv
    square_km_list -- list of years created from the 4th column of country_data.csv
    country_index -- integer value found from checking the index of the country entered in the countries list
    max_year -- largest interger value in years_list

    Return: Calculated value of the population density for a given country.

    """
    max_year_index = int(years_list.index(max_year)) #find the greatest value in the year_list.
    #calculates population density by dividing the population in the greatest year by the square Km of the country entered. 
    population_density = (population_data[country_index, max_year_index]) / (square_km_list[country_index])
    return(population_density)

def theatened_species_information(threatened_species, threatened_species_list, country_index):
    """A function that calculates the total number of threatened species, average number of threatened species and 
    the least and most threated species within a country.

    Parameters:
    threatened_species -- imported data from Threatened_Data.csv
    threatened_species_list -- list of threatened species created form first row of threatened_species.csv
    country_index --integer value found from checking the index of the country entered in the countries list

    Return: Passes most_threatened_species, least_threatened_species, total_threatened and average_threatened
    into the threatened_species Class and calls the method print_all_stats to display the data to the user.
    """
    #finding the most threatened species 
    most_threatened_species_index = list(threatened_species[country_index]).index(np.max(threatened_species[country_index])) #finds index of max value in list and checks its index.
    most_threatened_species = threatened_species_list[most_threatened_species_index] #checks the value of the corresponding index in the threatened species list.
    #finding the least threatened species.
    least_threatened_species_index = list(threatened_species[country_index]).index(np.min(threatened_species[country_index])) #finds index of min value in list and checks its index.
    least_threatened_species = threatened_species_list[least_threatened_species_index] #checks the value of the corresponding index in the threatened species list.
    #finding the total number of threatened species within the country entered.
    total_threatened  = int(np.sum(list(threatened_species[country_index])))
    #finding average number of threatened species within the country entered.
    average_threatened = np.mean(list(threatened_species[country_index]))
    average_threatened = (f'{average_threatened:.1f}') #formats average_threatened to 1 decimal place.
    return(threatened_species_data(most_threatened_species, least_threatened_species, total_threatened, average_threatened).print_all_stats())

def main():
    #importing data
    #importing data from 'Population_Data.csv'
    years_data = np.genfromtxt('Population_Data.csv', delimiter = ',', encoding='utf-8-sig')
    #converting the header of years_data to a list.
    years_list = list(years_data[0])
    #importing data from 'Population_Data.csv', header is removed when importing.
    population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = True)
    #importing data from 'Country_Data.csv', header is removed.
    country_data = pd.read_csv('Country_Data.csv', header = None, skiprows = 1)
    #converting the first column of country_data into a list of all the countries.
    countries_list = list(country_data[0])
    #converting the third column of country data into a list with all the sq Km.
    square_km_list = list(country_data[3])
    #importing data from 'Threatened_Species.csv' , header is removed when importing.
    threatened_species = np.genfromtxt("Threatened_Species.csv", delimiter = ',', skip_header = True)
    #importing data from 'Threatened_Species.csv', then first column is converted to a list.
    threatened_species_list = list((np.genfromtxt('Threatened_Species.csv', delimiter = ',', encoding= 'utf-8-sig', dtype = None)[0]))

    print('ENDG 233 FINAL PROJECT BY HARSH CHITRODA AND VISHNU DHANDA')
    print('Select 1 for information on population data of a country within a specified timeframe')
    print('Select 2 for information on threatened species within a country.')
    print('Select 0 to exit.')

    #asking user to select an option from 1,2,3 and 0
    user_option = input('Enter a option: ')
    #correcting for user_option if user_option is not numeric, will ask user to enter their input again.
    while user_option.isnumeric() == False:
        print('Option entered is not valid.')
        user_option = input('Enter a option: ')
    user_option = int(user_option) #casting user_option to an integer
    #correcting for user_option if user_option is not 1,2,3 or 0, will ask user to enter their input again.
    while user_option != 1 and user_option!= 2 and user_option !=0:
        print('Option entered is not valid.')
        user_option = int(input('Enter a option: '))

    #Executes the while loop as long as this condition is true, that is user_option is not equal to 0 
    # If not the program prints the final 'Thank you for using the data analysis program.'
    #message and terminates.
    while user_option !=0:
        if user_option == 1:
            #the code below is executed if user selects option1.
            country_entered = input('Enter a country: ')
            #correcting for country input. If country entered is not in list of countries, user will be asked to enter a country again.
            while country_entered not in countries_list:
                print ('Please enter a valid country.')
                country_entered = input('Enter a country: ')
            #finds the index of the the country_entered in the list of countries.
            country_index = countries_list.index(country_entered)
            country_index = int(country_index) #casts the index found to an integer.
            #Finding the minimum year in years_list
            min_year = int(np.min(years_list))
            #Finding the maximum year in years_list
            max_year = int(np.max(years_list))
            #asks user to enter a starting year. For example if you would like to find-
            #change in population from 2003 to 2019 starting year entered should be 2003.
            starting_year = input(f'Enter a starting year from {min_year} to {max_year-1}: ')
            #corrects for starting year, if starting_year entered is not numeric, user will be asked to enter the starting year again.
            while starting_year.isnumeric() == False:
                print('Please enter a valid year.')
                starting_year = input(f'Enter a starting year from {min_year} to {max_year-1}: ')
            starting_year = int(starting_year) #casting starting_year to an integer.

            #corrects for starting year, if starting_year entered is not found in years list, user will be asked to enter the starting year again.
            while starting_year not in years_list:
                print('Please enter a valid year.')
                starting_year = input(f'Enter a starting year from {min_year} to {max_year-1}: ')
            starting_year = int(starting_year) #casting starting_year to an integer.
            #corrects for starting year, if starting year entered is equal to the maximum year in years list.
            while starting_year == max_year:
                print('Please enter a valid year.')
                starting_year = input(f'Enter a starting year from {min_year} to {max_year-1}: ')
            starting_year = int(starting_year) #casting starting_year to an integer.

            ending_year = input(f'Enter a ending year from {starting_year+1} to {max_year}: ')
            #corrects for ending year, if ending year entered is not numeric, user will be asked to enter the ending year again.
            while ending_year.isnumeric() == False:
                print('Please enter a valid year.')
                ending_year = input(f'Enter a ending year from {starting_year+1} to {max_year}: ')
            ending_year = int(ending_year)

            #corrects for ending year if ending year entered is less than or equal to starting year
            ending_year = int(ending_year)
            while ending_year <= starting_year:
                print('Please enter a year greater than the starting year entered.')
                ending_year = input(f'Enter a ending year from {starting_year+1} to {max_year}: ')
                ending_year = int(ending_year) #casting ending year to an integer.
            #corrects for ending year, if ending year entered is not found in years list, user will be asked to enter the ending year again.
            while ending_year not in years_list:
                print('Please enter a valid year.')
                ending_year = input(f'Enter a ending year from {starting_year+1} to {max_year}: ')
                ending_year = int(ending_year) #casting ending year to an integer.
            print('')
            #passes years_list, population_data, country_index, starting_year and ending_year into the delta_population function.
            delta_population = change_in_pop(years_list, population_data, country_index, starting_year, ending_year)
            print (f'Change in population for {country_entered} between {starting_year} to {ending_year} is {delta_population}')
            starting_year_index = int(years_list.index(starting_year)) #gets index of the starting year entered from the list of years
            ending_year_index = int(years_list.index(ending_year)) #gets index of the ending year entered from the list of years
            
            #passes population_data, country_index, starting_year_index and ending_year_index into the average population function.
            average_pop_calculated = average_pop_function(population_data, country_index, starting_year_index, ending_year_index)
            print(f'The average population from {starting_year} to {ending_year} is: {average_pop_calculated}')
            
            #passes population_data, years_list, square_km_list, country_index and max_year into current_population_density function.
            current_population_density = pop_density_function(population_data, years_list, square_km_list, country_index, max_year)
            print(f'The current population density is: {current_population_density} people per sq km')
            
            print('')

            graph_option = input('Would you to display a graph (y/n)? ')
            graph_option = graph_option.capitalize() #capitalizes graph_option entered
            #Corrects for user input if Y or N is not entered, asks user to enter a valid option again without terminating the program.
            while graph_option != 'Y' and graph_option != 'N':  
                print('Please enter y or n')
                graph_option = input('Would you to display a graph (y/n)? ')
                graph_option = graph_option.capitalize() #capitalizes graph_option entered

            #plotting graph
            if graph_option == 'Y': #the graph only displayed to the user if user selects y.
                #plotting graph for population
                plt.subplot(1,1,1)
                #title of the plot
                plt.title(f'Population of {country_entered} from {starting_year} to {ending_year}')
                plt.xlabel ('Year') #x-axis title
                plt.ylabel ('Population') #y-axis title
                #setting the x axis values to range from starting to minimum year to maximum year
                plt.xticks(list(years_list))
                plt.xlim(starting_year, ending_year) #shows the x axis range within years entered by user.
                #Finding the population data for the entered country using the corresponding country index.
                y = population_data[country_index]
                #shows y axis population data within range of years entered by user.
                plt.ylim(population_data[country_index,starting_year_index], population_data[country_index,ending_year_index]) 
                #Plotting a line graph of population against the year, setting the color of the line to be red.
                plt.plot(years_list,y, label = f'Population of {country_entered}', color = 'green')
                plt.legend(loc="upper left")  #legend created at upper left position
                #disables the scientific notation for y axis, causes values to be shown the way they are seen in the csv
                plt.ticklabel_format(useOffset = False, style = 'plain') 
                plt.show()
            

        if user_option == 2:
            country_entered = input('Enter a country: ')
            #correcting for country input. If country entered is not in list of countries, user will be asked to enter a country again.
            while country_entered not in countries_list:
                print ('Please enter a valid country.')
                country_entered = input('Enter a country: ')
            #finds the index of the the country_entered in the list of countries.
            country_index = countries_list.index(country_entered)
            print('')
            #passes threatened_species, threatened_species_list and country_index 
            theatened_species_information(threatened_species, threatened_species_list, country_index)
            #plotting graph
            print('')
            graph_option = input('Would you to display a graph (y/n)? ')
            graph_option = graph_option.capitalize()
            while graph_option != 'Y' and graph_option != 'N':
                print('Please enter y or n')
                graph_option = input('Would you to display a graph (y/n)? ')
                graph_option = graph_option.capitalize()
            
            if graph_option == 'Y':
                plt.subplot(1,1,1)
                plt.title(f'Threatened species in {country_entered}')
                plt.xlabel ('Threatened species') #x-axis title
                plt.ylabel ('Number of threatened species') #y-axis title
                x = threatened_species_list 
                y = threatened_species[country_index] 
                #plotting bar graph and setting colours of the bars.
                plt.bar(x[0],y[0], color = ('#F8B195'), label = threatened_species_list[0])
                plt.bar(x[1], y[1], color = ('#FDD056'),label = threatened_species_list[1])
                plt.bar(x[2], y[2], color = ('#00AA8F'), label = threatened_species_list[2]) 
                plt.bar(x[3], y[3], color = ('#88CED2'), label = threatened_species_list[3]) 
                plt.legend(loc="upper right") #legend created at upper right position
                plt.show()

        print('')
        print('Select 1 for information on population data of a country within a specified timeframe')
        print('Select 2 for information on threatened species within a country.')
        print('Select 0 to exit.')

        #asking user to select an option from 1,2,3 and 0
        user_option = input('Enter a option: ')
        #correcting for user_option if user_option is not numeric, will ask user to enter their input again.
        while user_option.isnumeric() == False:
            print('Option entered is not valid.')
            user_option = input('Enter a option: ')
        user_option = int(user_option) #casting user_option to an integer
        #correcting for user_option if user_option is not 1,2 or 0, will ask user to enter their input again.
        while user_option != 1 and user_option!= 2 and user_option !=0:
            print('Option entered is not valid.')
            user_option = int(input('Enter a option: '))
    print('Thank you for using the data analysis program.')

if __name__ == '__main__':
    main()