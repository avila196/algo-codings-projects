import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Stage 1: Read and process the data
def read_and_process(csv_filename):
    #We open input file name as csv
    iris = pd.read_csv(csv_filename)
    #Now, we drop rows with empty columns. We first replace all empty
    #strings by NaN and then we drop the one rows with any NaN on its columns
    iris.replace("", np.nan, inplace=True)
    iris.dropna(subset=iris.columns, inplace=True)
    #Then, we remove " cm" and " mm" from each data point and we convert them
    #all (except last one) to floats
    #We use a lambda expression to apply a given function (special trim) to each data
    iris = iris.applymap(
        lambda x : x[:-3] if (str(x).endswith("mm") or str(x).endswith("cm")) else x)
    float_columns = iris.columns.drop("species")
    iris[float_columns] = iris[float_columns].apply(pd.to_numeric, errors='coerce', axis=1)
    #Then, we divide the 'sepal_width' column by 10
    iris['sepal_width'] /= 10
    #Finally, we return the adjusted DF
    return iris

# Stage 3: Process text analysis
def text_analysis(iris, species_names):
    #We ask user to select the species from available ones
    str_species = ", ".join(["all"]+species_names)
    species = input("Select species (" + str_species + "): ")
    #Now, depending on the answer we get the respective stats
    if species == "all":
        stat_df = iris.copy()
    else:
        stat_df = iris[iris["species"] == species].copy()
    stat_df.drop(columns=["species"], inplace=True) #remove species col, not needed anymore
    #Now, for given data frame, we get the needed stats
    values = {"Mean":stat_df.mean().tolist(), "25%":stat_df.quantile(0.25).tolist(), 
              "Median":stat_df.median().tolist(), "75%":stat_df.quantile(0.75).tolist(), 
              "Std":stat_df.std().tolist()}
    #Then, we create a new dataframe with given values and needed indices
    stat_df = pd.DataFrame(values, index=stat_df.columns)
    return stat_df

# Stage 4: Process graphics-based analysis
def graphics_analysis(iris):
    #We first ask for x-characteristic
    x = input("Choose the x-axis characteristic (all, sepal_length, sepal_width, petal_length, petal_width): ")
    #Check for given choice
    if x == "all":
        #If all, we do a pairplot for the dataframe
        sns.pairplot(iris, hue="species")
    else:
        #If not all, we ask for y-characteristic
        y = input("Choose the y-axis characteristic (sepal_length, sepal_width, petal_length, petal_width): ")
        #Now, we plot both x and y for all species
        sns.scatterplot(x=x, y=y, hue="species",data=iris)
    #Now, we ask for file name to store the result
    outfile = input("Enter save file: ")
    plt.savefig(outfile)
    plt.clf()
    
    
# Stage 5: Conclusion
def conclusion():
    # Return the two (non-species) categories that best identify the species of iris
    # Your code here
    #TODO: This is an analysis totally up to you! Look at the final results
    #and answer the final conclusion questions needed
    pass

# Stage 2: User menu
def print_menu():
    print('1. Create textual analysis')
    print('2. Create graphical analysis')
    print('3. Exit')
    choice = input('Please select an option: ')
    if choice != '1' and choice != '2' and choice != '3':
        print('Not a valid option')
    return choice


if __name__ == '__main__':
    #Start asking for filename
    iris_filename = input("Enter the csv file: ")
    #Process file and get DF
    iris = read_and_process(iris_filename)
    #For analysis purposes, we get unique species names sorted
    available_species = iris["species"].unique().tolist()
    available_species.sort()
    exit_chosen = False
    while not exit_chosen:
        choice = print_menu()
        if choice == '1':
            # We call for function that creates the needed stat DF
            df = text_analysis(iris, available_species)
            #Then, we print it
            print(df)
        elif choice == '2':
            # We call for function that does graphical analysis
            graphics_analysis(iris)
        elif choice == '3':
            exit_chosen = True