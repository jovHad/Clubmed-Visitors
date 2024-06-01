# Project Name 
medical_insurance_portfolio.md

## Description

For this project, I will be investigating a Claubmed csv costs dataset in a .csv file of 1339 subjects,
using the Python skills that you have developed. 
 
Will Explore areas where the data may include bias and how that would impact potential use cases.
In this code, we analyze the 'smoker' era, and will investigate if and how this status affects the other variables. 

It is implemented in Python and is part of my portfolio.

## About the Data

Data on 198 ClubMed guests in 2016.
sex- F/M
age- in years
status- marital status
roomservice- number of times guest ordered room service during his last stay
room price- in USD
region- ClubMed resort
accomodation- room type
nights- no. of nights accomodated in ClubMed during last visit
minibar- minibar bill for total stay in USD
visits2016- no. of visits to any ClubMed resort during 2016
visits5years- no. of visits to any ClubMed resort during 2012-2016 period
total expenditure- in ClibMed resort including hospitality and extras, in USD
clubmember- whether the guest is a mmber of the club or not
ranking- guest ranking of club during the last stay.


## Some Conclusions
### countplot of accommodation by club_mamber:
![image](https://github.com/jovHad/Clubmed-Visitors/assets/166914091/38250782-8d6d-4110-84d9-1a2031057600)
Club Members:
we can learn from it that top choice of accommodation of the club members is Junior Suite - above data count of 40,
then, close in data value is standerd accommodation, around data count of 40,while the least and a little far from those,
is delux villa accommodation, which it's data count value is a little above 10.
Non - Club Members:
We can learn from it that top choice of accommodation of non - club members is standard - around data count of 35,
then, close in data value is Junior Suite, above data count of 30,
and the least is delux villa, which it's data count value is under 30.

An explenation to this may be that members come more frequntly so they don't want to spend as much money as
non-members, that probably come once in a while.##

### crostab norm of ranking by accommodation:
![image](https://github.com/jovHad/Clubmed-Visitors/assets/166914091/8268187a-b1d6-470c-b7e5-c821343ab0f9)
Over all :
There is no correlation between rating to the accommodation choice. 
this graf is problematic to see
the difference because we can't see the presage frequency between each accommodation. We can se kind of normal
distribution in the delux category, around 3 value rating, and a big jump at 7 value rating.

## Requirements

To run this project, you need:
- Python 3.x
- Necessary libraries (listed in `requirements.txt`)

## How to Run

1. Clone the repository and open it on PyCharm:
   ```sh
   https://github.com/jovHad/Clubmed-Visitors
