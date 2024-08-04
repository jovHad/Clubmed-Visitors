import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#importing the file:
sns.set_palette("Set2")
df = pd.read_csv("clubmed_HW2.csv")
# Making sure all the data is printed :
pd.options.display.max_rows = None
pd.options.display.max_columns = None

# Presentation for a general introduction :
print(df.head())
print(df.describe())
print()

## Customer's Age Histogram :
plt.xlabel('Ages')
plt.ylabel('Frequency')
plt.title("Customer's Age Histogram")
plt.hist(df.age)
plt.show()

# As we divide the histogram to more bins,(def of bins = 10),
# it helps to understand better the distribution of the data.
# However, too many bins can make it difficult to identify patterns due to excessive noise.:
plt.title("Customer's Age Histogram - bins = 40")
plt.hist(df.age, bins=40)
plt.show()

plt.title("Customer's Age Histogram - bins = 60")
plt.hist(df.age, bins=60)
plt.show()

plt.title("Customer's Age Histogram - bins = 80")
plt.hist(df.age, bins=80)
plt.show()

# We can observe that some visitors have age values that are outliers.
# Let's check how many outlier age values there are:
age_99 = df[df['age'] == 99]
print(age_99.describe())
# We can see that there are only 8 objects that are 99 years old.
# This number is less than 10% of the total database records.
# If it was part of the instructions, we probably would drop them from the DF.


## Custumer's Membership Bar Chart :
# map: with value_count:
members = df.club_member.value_counts()
plt.bar(members.index.map({True: 'True', False: 'False'}), members.values)
plt.xlabel("Has a membership at the club")
plt.ylabel("Frequency of customers")
plt.title("Custumer's Membership Bar Chart")
plt.show()


## Relationship between gender and family status :
crosstab_norm1 = pd.crosstab(index = df.status, columns = df.gender, normalize=True)
crosstab_norm2 = pd.crosstab(index = df.gender, columns = df.status, normalize=True)
crosstab_norm1.plot.bar()
plt.ylabel("Amount of custumers")
plt.title("Relationship between gender and family status")
crosstab_norm2.plot.bar()
plt.ylabel("Amount of custumers")
plt.title("Relationship between gender and family status")
plt.show()

# The family status with the highest percentage of men is "couple".
# This is based on normalized values, indicating the proportion of men in percentages within this family status.
# However, looking only at the "M" group (men), it doesn't necessarily mean that this family status has the highest absolute number of men.

# The most common family status for females is also couple.

# The percentage of un-married woman is the combination os single and couple: 14% + 23% = 37%
# When concluding that a married woman will only appear under the family column and not the couple column.

# The percentage of men from all the single's is 50%.
single_df = df[df["status"] == "single"]
print(single_df.groupby("gender")["status"].describe())


## Accommodation - Club Member :
# countplot of accommodation by club_mamber
sns.countplot(df, x="accomodation", hue="club_member", palette=["brown", "skyblue"])
plt.title("Accommodation - Club Member")
plt.show()

'''
# Club Members :
we can learn from it that top choice of accommodation of the club members is Junior Suite - above data count of 40,
then, close in data value is standerd accommodation, around data count of 40,
while the least and a little far from those, is delux villa accommodation,
which it's data count value is a little above 10.
# Non - Club Members :
we can learn from it that top choice of accommodation of non - club members is standard - around data count of 35,
then, close in data value is Junior Suite, above data count of 30,
and the least is delux villa, which it's data count value is under 30.
# An explenation to this may be that members come more frequntly so they don't want to spend as much money as
non-members, that probably come once in a while.##
'''

# We can print the data description and value_counts to get the exact numerical values and it's percent ratio:
print(df.groupby("club_member")["accomodation"].describe())
print(df.groupby("club_member")["accomodation"].value_counts(normalize="count"))
print()
print(df.groupby("accomodation")["club_member"].describe())
print(df.groupby("accomodation")["club_member"].value_counts(normalize="count"))
print(df["club_member"].value_counts(normalize="count"))
# More comes out of it: we can see that most of the visitors are memmbers of the club. But the ratios are not big: 1%
# It doesn't support my explanation because we can'n see that members do come more frequently than non-members from
# that.

## Ranking - Accommodation :
# Crostab norm of accommodation by ranking :
crostab_norm = pd.crosstab(index=df.ranking, columns=df.accomodation, normalize="index")
crostab_norm.plot.bar(stacked=True)
plt.title("Ranking - Accommodation")
plt.show()

# Over all, there is no correlation between rating to the accommodation choice. # this graf is problematic to see
# the difference because we can't see the presage frequency between each accommodation. We can se kind of normal
# distribution in the deluxe category, around 3 value rating, and a big jump at 7 value rating.

## Ranking - Region :
# Crosstab norm of region by ranking :
crosstab_norm = pd.crosstab(index=df.ranking, columns=df.region, normalize="index")
crosstab_norm.plot.bar(stacked=True)
plt.title("Ranking - Region")
plt.show()
# We will observe this with a non-normalized crosstab :
crosstab = pd.crosstab(index=df.region, columns=df.ranking)
crosstab.plot.bar(stacked=True)
plt.title("Ranking - Region")
plt.show()
#we can see the frequency of Eilat in general is high.

# Bar chart of mean ranking values by region:
df_region_ranking = df.groupby("region")["ranking"].mean()
plt.bar(df_region_ranking.index, df_region_ranking.values)
plt.title("Mean Ranking - Region")
plt.xlabel("Region")
plt.ylabel("Mean Ranking")
plt.show()
# We can see Eilat got the lowst ranking but in general, the rankings are low.

# Bar chart of mean ranking values by accomendation:
df_accommendation_ranking = df.groupby("accomodation")["ranking"].mean()
plt.bar(df_accommendation_ranking.index, df_accommendation_ranking.values)
plt.title("Mean Ranking - Accomendation")
plt.xlabel("Region")
plt.ylabel("Mean Ranking")
plt.show()
# There is no ranking difference between the acccommodations.
# It may be those who took "delux" were expacted for better.

## Status - Gender :
# Crosstab norm of gender by status :
crostab_norm = pd.crosstab(index=df.status, columns=df.gender, normalize="index")
crostab_norm.plot.bar(stacked=True)
plt.title("Status - Gender")
plt.show()
# The distribution between men and women who contact and their status is the same.
# Crosstab norm of gender by club_member :
crostab_norm = pd.crosstab(index=df.club_member, columns=df.gender, normalize="index")
crostab_norm.plot.bar(stacked=True)
plt.title("club_member - gender")
plt.show()
'''
Club_member category has more trend relationship to gender category.
We can see a bigger correlation between them than the other graph, which has no correlation.
The scatter in the status category graph is uniform distribution.
At the club member gender bar chart, we can learn most of the club members are men,
while the non-club members are women.
'''
   
## Minibar Expenses scatter plot:
plt.scatter(df.minibar, df.age, color="purple", alpha = 0.3)
plt.title("Minibar expenses and age correlation")
plt.xlabel("Minibar Expenses")
plt.ylabel("age")
plt.show()

# Without the edges - just to show it without extremes
plt.scatter(df["minibar"], df["age"],color="purple", alpha = 0.3)
plt.xlabel("Minibar expenses and age correlation")
plt.ylabel("minibar expenses")
plt.title("Minibar Expenditure - Age of Guest")
plt.ylim(10, 70)
plt.show()
# No correlation here between age and minibar use.
# The majority of minibar uses are fewer than 15 times

## Room price :

# Missing Values : 
print("empty:", df["room_price"].isna().sum())
# Only 3 rows have NaN values in this field. Will drop them :
room_price = df["room_price"][df["room_price"].notna()]
print("empty check:", room_price.isna().sum())

# Descriptive statistics :
quartiles = np.array([0, 0.25, 0.5, 0.75, 1])
quartiles_room_price_df = room_price.quantile(q=quartiles)
print("quartiles_df:\n", quartiles_room_price_df[0.25:1])
iqr = quartiles_room_price_df.iloc[3] - quartiles_room_price_df.iloc[1]
print("iqr: ", iqr)
print("std: ", room_price.std())
# A right tailed asynchronicity
median_price_room = room_price.median()
print("median:", median_price_room)
smaller_than_med = (df.room_price <= median_price_room).count()
print("the amount of values smaller than the median is: " + str(smaller_than_med))
# The value does match the median definition.
# The median value includes all room_price values under the 50%.
# The explanation to that is that we droped from room_price the empty values (NaN) that.
# If we won't, it would affect the median value calculation.

# room_price Histogram with some descriptive statistics:
plt.hist(room_price,bins = 30)
plt.xlabel("room_price")
plt.ylabel("Frequency")
plt.title("room_price Histogram")
plt.axvline(x=room_price.mean(), ymin=0, ymax=1, color='r')
plt.axvline(x=room_price.mean() - room_price.std(), ymin=0, ymax=1, color='y')
plt.axvline(x=room_price.mean() + room_price.std(), ymin=0, ymax=1, color='y')
plt.show()
# The distribution is narrow division, asymmetric with a left tail.
# Narrow - since the standard deviation from the average is close to the minimum and maximum values of the data.


# Box plot of age by ranking : 
boxplot_age_ranking = df.boxplot(column="age", by="ranking", showmeans=True)
# The widest age distribution in Q3 is rank number 2.
boxplot_age_ranking_presents = df.groupby("ranking")["age"].quantile(q=quartiles)
iqr = boxplot_age_ranking_presents.iloc[3] - boxplot_age_ranking_presents.iloc[1]
flier1 = boxplot_age_ranking_presents.iloc[1] - 1.5 * iqr
flier2 = boxplot_age_ranking_presents.iloc[3] + 1.5 * iqr
plt.axhline(y=flier1, color='r', linestyle='--')
plt.axhline(y=flier2, color='r', linestyle='--')
plt.show()

# Box plot of age by 'visits5years' : 
df.boxplot(column=['age'], by=['visits5years'])
plt.title("Age distribution according to the number of visits\nin the last five years")
plt.xlabel('Number of visits')
plt.ylabel('Age')
plt.suptitle("")
# mean age by 'visits5years' : 
mean_age_by_year = df.groupby('visits5years')['age'].mean()
print("the max age mean in the box plot is at: " + str(
    mean_age_by_year.idxmax()) + " visits box." + '\nWhich value is: ' + str(mean_age_by_year.max()))

# Box plot of room_price by 'visits5years' : 
plt.title("Room price distribution according to the number of visits\nin the last five years")
df.boxplot(column="room_price", by="visits5years", showmeans=True)
plt.xlabel('Number of visits')
plt.ylabel('Room price')
plt.suptitle("")
plt.show()
# We can learn that the highest mean age group visit 7 times which is alot, and paid the lowest price for the room
# because they probably get discount for their age. We can also see their std is very low.

## Ranking - Total Expenditure :
print(df["total_expenditure"].min())
print((df["total_expenditure"] < 0).sum())
# we need to take all minus out. There are only 5. will make it 0 and replace with the mean
df["total_expenditure"] = df["total_expenditure"].mask(df["total_expenditure"] < 0)
df["total_expenditure"] = df["total_expenditure"].replace(to_replace=np.nan, value=df.total_expenditure.mean())
print(df["total_expenditure"].describe())
plt.bar(df.ranking, df.total_expenditure)
plt.title("Ranking - Total Expenditure")
plt.show()
# There is no correlation between visitir's renkings and their total_expenditure.
# We can see those who paid more ranked it more in general.
