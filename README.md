# real-estate-price-prediction

# PART I: Collecting data

## Description
The goal of this project was to collect information from the [immoweb website](https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance). We had to gather information about at least 10,000 properties all over Belgium and create a CSV file with the following columns.
* __Locality__
* __Type of property__ (House/apartment)
* __Subtype of property__ (Bungalow, Chalet, Mansion, ...)
* __Price__
* __Type of sale__ (Exclusion of life sales)
* __Number of rooms__
* __Living Area__
* __Fully equipped kitchen__ (Yes/No)
* __Furnished__ (Yes/No)
* __Open fire__ (Yes/No)
* __Terrace__ (Yes/No)
 -If yes: Area
* __Garden__ (Yes/No)
 -If yes: Area
* __Surface of the land__ (is none for each line, the information is given in the line : Surface area of the plot of land)
* __Surface area of the plot of land__ 
* __Number of facades__
* __Swimming pool__ (Yes/No)
* __State of the building__ (New, to be renovated, ...)


The dataset had to be clean in the sense of recording only numerical values. 


## Installation

The following packages were useful in order to make the project work: 

- json (built-in); 
    - This library provides a representation of the JavaScript Object Notation (JSON) with support for parsing, printing, and manipulating JSON values. 
- pandas (pip install pandas);
    - This library offers data structure and operations for data analysis and manipulation.
- bs4 (pip install bs4);
    - BeautifulSoup is a library for getting data out of XML and HTML files. The library's folder is bs4. 
- selenium (pip install selenium);
    - This library is useful when getting the content of dynamic web pages which rely on Javascript. It is useful when information is accessible by clicking on buttons. 
- threading.
    - This module can be used to execute tasks concurrently. 
- matplotlib
- seaborn


## Structure of the code

Our program consists of three different parts. The first part of the program is responsible for gathering all the necessary links that will be used for data collection. The second part of the program uses the collected links to scrape information from those webpages. The final step of the program is to "clean" the data that has been collected. This includes removing duplicates and formatting data to have (mainly) numerical values. However, the data is not processed to remove any errors or inconsistencies. 

### 1) Collecting the links
The aim of the [links_collection.ipynb](./data_acquisition/links_collection.ipynb) file is to collect the links of all houses and apartment for sale on the immoweb website. In practice, the house and apartment sections are done in parallel (using threads) and both are following the same algorithm:
* __first__, The algorithm goes through the 333 pages that are available:
* __then__, scrapes these pages to get all the links it contains
* <img title="333 pages" alt="immoweb picture" src="./images/333_pages.png">
* __lastly__, This part creates a csv file called [links.csv](./data_acquisition/links.csv) which stores all the links collected.

### 2) Scraping all the links
For all the links that are stored in the links.csv file, [house_scrapping.ipynb](./data_acquisition/house_scrapping.ipynb) will:
* open the link
* scrape the available information
* <img title="one page example" alt="immoweb picture2" src="./images/infos.png">
* store all the collected information into different csv files called all_info_TeamMember1_1-5000.csv, all_info_TeamMember1_1-10000.csv, all_info_TeamMember2_10000-15000.csv, etc. These files will be merged in the next step of the program. 

In this csv file, each line represents a new house/apartment. The column names are given in the Description section. In this part a special type of multithreading was implemented, which is called teamwork: 
- pip install nicePeople
- from nicePeople import teamwork 

 We have splitted the links (20000 in total) in three to collect the information in parallel. The reason for this was to minimize the risk of being blocked by the immoweb website if we'd have used 'real' concurrency. 

### 3) Cleaning the data

In this last part [merge_and_clean_data.ipynb](./data_acquisition/merge_and_clean_data.ipynb) we will merge all the csv files from the previous part. The dataframe is not clean yet. We only want to retrieve numerical values. So this part of code will include a mapping which is explained in the 'usage' of this 'readme' file.


## Usage

### 1) Collecting the data 
You can use any WebDriver through Selenium to get and extract the URL of each page. The Firefox WebDriver was used in this project with an additional option (headless) which doesn't show the process of opening and closing the pages. 

In order to collect the links of all houses and apartments for sale, we had a look on the website of immoweb and found 333 pages for each property type. This is something you need to check and change manually when running the program. You can also add an additional variable 'end_pagenumber' and scrape this information from the website. 

This workprocess will take about 1 hour. 

### 2) Scraping all the links

To scrape each propertylink we have parsed the HTML website using BeautifulSoup library. We saw that the information was under a "script" with type "text/javascript" and that property items could be found in "window_classified".

<img title="HTML documentation" alt="html" src="./images/html.png">

We converted the needed information into a Python dictionary using JSON. 

This (shared) workprocess can take up to 4 hours when divided between two or more computers. When there's a problem while running, the code will store the scraped information under a CSV file. The program will continue working with a new CSV file. You can add your name to distinguish between team members.

<img title="Saving information" alt="saving" src="./images/saving.png">

This will of course cause an additional task to merge all the CSV files. The [merge_and_clean_data.ipynb](./data_acquisition/merge_and_clean_data.ipynb) will execute this for you. 

### 3) Cleaning the data

The function 'create_df' will merge all the csv files into a single dataframe. This dataframe will have non-numerical values. In order to get only numerical values we have written the function clean_df. This part of the code will replace string values by numerical values (using mapping). 

## Visuals
In this part we would like to illustrate some visuals about the output of this program. After cleaning the data, the dataframe looks as follows:

<img title="Sample output data" alt="clean dataset" src="./images/cleaned_dataset.png">

Here we can see that the dataframe consists only of numerical values like required. We can see that the data is (almost) evenly distributed between the two property types (house/apartment) as we see from the pie chart below:

<img title="Pie chart distribution of data" alt="pie chart" src="./images/piechart.png">

We did also check the range of price across all the properties and the boxplot (below) looks quite normal. 

<img title="Boxplot price range" alt="boxplot" src="./images/boxplot.png">
--

# PART II: Analysing data

The process is divided into three stages. Initially, we will review and clean the dataset as necessary (Stage 1). Next, we will conduct an analysis of the data (Stage 2), and finally, we will interpret the results based on the two scenarios and additional questions specified in this project (Stage 3).

### Step 1: Cleaning the data 

A cleaned dataset is one that is free of duplicates, blank spaces, and errors. With this in mind, we have conducted an analysis. An initial review of our dataset revealed that certain columns and rows could be removed. It is also recommended to verify the data types for each column and make adjustments as necessary.

We are pleased that we invested the time to analyze our data, as we discovered that the sale prices for auctions or life annuity sales were also included in our dataset. Those sale prices are not final and can be removed. This will prevent any inaccuracies in the data, such as unreasonable prices as below.

<img title="Lowest price" alt="price" src="./images/minprice.png">



### Step 2 : Analysing the data

Now that the data has been collected and cleaned, it is time for the analysis. In this part we'll formulate an answer to the following questions: 

- How many rows and columns are left in our dataframe. 
- How many qualitative and quantitative variables are there?
- What the correlation between the variables.
- Which variables have the greatest/lowest influence on the price?
- What is the percentage of missing values per column?
- 
As one of the key goals of this project is to make predictions about prices, it is crucial to identify the variables that have an impact on the price. The bar chart below illustrates the significance of each variable in determining the price.

<img title="Correlation with price" alt="correlation" src="./images/correlation.png">


### Step 3 : Data Interpretation

In this section, we will conduct a deeper analysis of the data by addressing the questions in (3.1) as part of this challenge and by using our own case study (3.2). After completing the analysis, we will interpret the results and present the findings. We will provide a summary of the answers and visualizations here, however, a more detailed explanation and output can be found in [data_visualization.ipynb](./data_visualization/data_visualization.ipynb). Additionally, we will provide some additional answers and illustrations here as well.


#### 3.1: Questions
- Plot the outliers.  
- Represent the number of properties according to their surface using a histogram.

<img title="Number of properties according to their surface area" alt="surface area" src="./images/surface_area.png">

- What are the **most/less** expensive municipalities in Belgium/Wallonia/Flanders? (Average price, median price, price per square meter)

In this question, we needed to link postal codes with the corresponding region and province. In a later stage of our case study (3.2), we also had to divide the dataset by province. To do this, we created two functions that link the postal codes with their associated region and province. It's important to note that Brussels is considered a province as well. For future analysis, it would be more efficient to use one function that utilizes a dictionary. It's also recommended to work with a dataframe that includes city information.

From the analysis, we found that the highest price per square meter is found in cities with postal codes 8620 (Nieuwpoort), 3000 (Leuven), 1933 (Zaventem), 8301 (Knokke-Heist) and 8300 (Knokke). These municipalities are popular among investors looking to buy and rent properties for profit. The difference in prices between Knokke and other cities is notable and requires further investigation to determine if there are any errors in the dataset.

On the other hand, the least expensive municipalities are the cities with postal codes 5550 (Alle), 7804 (Aat), 6666 (Houffalize), 6741 (Étalle) and 5576 (Beauraing).

To further understand the prices, we also calculated the mean and median prices per square meter for the most and least expensive cities in Belgium.

<img title="Most and less expensive cities in Belgium" alt="belgium prices" src="./images/tabel_belgium.png">

This analysis can also be repeated for each region and province. 

#### 3.2: Case 

As part of the project, we were tasked with providing valuable insights about the dataset. We have therefore focused on two questions for the following clients:

- Client 1 is an apartment builder from Wallonia who is constructing apartment buildings and selling each unit. The builder is uncertain about whether to include an American-style kitchen in the units and if this will affect the house prices.
- Client 2 is an investor from Flanders who is interested in purchasing properties that need restoration. He is curious about which provinces would provide a higher profit margin after renovation.

##### Case 1: Analyzing the price difference between USA kitchens and normal kitchens in apartments in Wallonia. 

We separated the dataset into two categories based on kitchen type: American-style kitchen and normal kitchen in Wallonia. The graph below illustrates that there are notable differences in prices based on the kitchen type. We also verified other variables such as living area, and they were similar between the two kitchen types.

<img title="Apartment prices according to kitchen type" alt="belgium prices" src="./images/Boxplot_kitchen.png">

##### Case 2: Analyzing the price difference between several properties in the provinces of Flanders according to their state.

After analyzing the prices of new properties and properties that need restoration in each province, we found that there is a good profit margin for properties in Limburg and West Flanders.  

<img title="Prices according to state of property in each province" alt="province prices" src="./images/price_state.png">

## This concludes our case study. Both clients were satisfied with the analysis we provided.


