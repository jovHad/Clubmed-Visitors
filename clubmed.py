#Yovel Hadari 208252668
#Hadar froimovichi
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.options.display.max_rows = None
pd.options.display.max_columns = None
sns.set_palette("Set2")
df = pd.read_csv("clubmed_HW2.csv")
print(df.head())
print(df.describe())
print()
print(df["age"].describe())

## 1
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.title("Age Histogram - bins = 80")
plt.hist(df.age, bins=80)
plt.show()
plt.title("Age Histogram - bins = 60")
plt.hist(df.age, bins=60)
plt.show()
plt.title("Age Histogram - bins = 40")
plt.hist(df.age, bins=40)
plt.show()
plt.title("Age Histogram - bins = 10")
plt.hist(df.age)
plt.show()

# We can learn that some visitors have age exception value. will check how many of them:

age_99 = df[df["age"] == 99]
print(age_99.describe())
# we can see there are only 8 objects that are 99 years old. it doest effects the df, and moreover, we should get it
# out.
#
# 2
Club_Member = df["club_member"].value_counts()
print(Club_Member)
sns.countplot(x=df["club_member"], palette=["gray", "lightblue"])
plt.xlabel("Membership")
plt.ylabel("Frequency")
plt.title("Club_Member Bar Plot")
plt.show()

## 3
#A
crostab_norm = pd.crosstab(index=df.status, columns=df.gender, normalize="index")
print(crostab_norm)
crostab_norm.plot.bar(stacked=True)
plt.show()
#B
crostab_norm = pd.crosstab(index=df.gender, columns=df.status, normalize="index")
print(crostab_norm)
crostab_norm.plot.bar(stacked=True)
plt.show()
#D - "couple - Yes because the normalize is between F and M so $$$
#E - "couple"
#F - "couple"
#G - 52.5%
print(df["status"].describe())

##5
#A
sns.countplot(df, x="accomodation", hue="club_member", palette=["brown", "skyblue"])
plt.title("Accommodation - Club Member")
plt.show()
#B
## Club Members:
# we can learn from it that top choice of accommodation of the club members is Junior Suite - above data count of 40,
# then, close in data value is standerd accommodation, around data count of 40,
# while the least and a little far from those, is delux villa accommodation,
# which it's data count value is a little above 10.
## Non - Club Members:
# we can learn from it that top choice of accommodation of non - club members is standard - around data count of 35,
# then, close in data value is Junior Suite, above data count of 30,
# and the least is delux villa, which it's data count value is under 30.
### An explenation to this may be that members come more frequntly so they don't want to spend as much money as
# non-members, that probably come once in a while.##

## we can print the data description and value_counts to get the exact numerical values and it's percent ratio:
print(df.groupby("club_member")["accomodation"].describe())
print(df.groupby("club_member")["accomodation"].value_counts(normalize="count"))
print()
print(df.groupby("accomodation")["club_member"].describe())
print(df.groupby("accomodation")["club_member"].value_counts(normalize="count"))
print(df["club_member"].value_counts(normalize="count"))
# More comes out of it: we can see that most of the visitors are memmbers of the club. But the ratios are not big: 1%
# It doesn't support my explanation because we can'n see that members do come more frequently than non-members from
# that.

#or
#A
crostab_norm = pd.crosstab(index=df.ranking, columns=df.accomodation, normalize="index")
crostab_norm.plot.bar(stacked=True)
plt.title("Ranking - Accommodation")
plt.show()
# B # Over all there is no correlation between rating to the accommodation choice. # this graf is problematic to see
# the difference because we can't see the presage frequency between each accommodation. We can se kind of normal
# distribution in the delux category, around 3 value rating, and a big jump at 7 value rating.

crostab_norm = pd.crosstab(index=df.ranking, columns=df.region, normalize="index")
crostab_norm.plot.bar(stacked=True)
plt.title("Ranking - region")
plt.show()
#will try it without normalize it:
crostab_norm = pd.crosstab(index=df.region, columns=df.ranking)
crostab_norm.plot.bar(stacked=True)
plt.title("Ranking - region")
plt.show()
#we can see the frequency of Eilat in general is high.
#
df_region_ranking = df.groupby("region")["ranking"].mean()
plt.bar(df_region_ranking.index, df_region_ranking.values)
plt.title("Mean Ranking - Region")
plt.xlabel("Region")
plt.ylabel("Mean Ranking")
plt.show()
#we can see Eilat got the lowst ranking but in general, the rankings are low.
#
df_accommendation_ranking = df.groupby("accomodation")["ranking"].mean()
plt.bar(df_accommendation_ranking.index, df_accommendation_ranking.values)
plt.title("Mean Ranking - accomendation")
plt.xlabel("Region")
plt.ylabel("Mean Ranking")
plt.show()
# There is no ranking difference between the acccommodations.
# It may be those who took "delux" were expacted for better.

#C
crostab_norm = pd.crosstab(index=df.status, columns=df.gender, normalize="index")
crostab_norm.plot.bar(stacked=True)
plt.title("Status - Gender")
plt.show()
# we can see that the distribution between men and women who contact and their status is the same.
crostab_norm = pd.crosstab(index=df.club_member, columns=df.gender, normalize="index")
crostab_norm.plot.bar(stacked=True)
plt.title("club_member - gender")
plt.show()

# Club_member category has more trend relationship to gender category.
# We can see a bigger correlation between them than the other graph, which has no correlation.
# The scatter in the status category graph is uniform distribution.
# at the club member gender bar chart, we can learn most of the club members are men,
# while the non-club members are women.

##6
plt.scatter(df["minibar"], df["age"])
plt.xlabel("minibar")
plt.ylabel("age")
plt.title("Minibar Expenditure - Age of Guest")
plt.show()
# without the edges - just for showing the syntax
plt.scatter(df["minibar"], df["age"])
plt.xlabel("age")
plt.ylabel("minibar")
plt.title("Minibar Expenditure - Age of Guest")
plt.ylim(10, 70)
plt.show()
# No correlation here between age and minibar use.
# The majority of minibar uses are fewer than 15 times

## 7
#A
print("empty:", df["room_price"].isna().sum())
# Only 3 so it doesn't matter if will take all NA of.
room_price = df["room_price"][df["room_price"].notna()]
print("empty check:", room_price.isna().sum())
quartiles = np.array([0, 0.25, 0.5, 0.75, 1])
quartiles_quartiles_df = room_price.quantile(q=quartiles)
print("quartiles_df:\n", quartiles_quartiles_df[0.25:1])
iqr = quartiles_quartiles_df.iloc[3] - quartiles_quartiles_df.iloc[1]
print("iqr: ", iqr)
print("std: ", room_price.std())
# right tailed asynchronicity

#B
print("median:", room_price.median())
#yes it corresponds to the definition of the median.
# the median value includs all values under the 50%.

#C
plt.hist(room_price)
plt.xlabel("room_price")
plt.ylabel("Frequency")
plt.title("room_price Histogram")
plt.axvline(x=room_price.mean(), ymin=0, ymax=1, color='g')
plt.axvline(x=room_price.mean() - room_price.std(), ymin=0, ymax=1, color='r')
plt.axvline(x=room_price.mean() + room_price.std(), ymin=0, ymax=1, color='r')
plt.show()

#D
# narrow division, non-symmetric with left tail

##8
boxplot_age_ranking = df.boxplot(column="age", by="ranking", showmeans=True)
#A
# 2 rank
#B
boxplot_age_ranking_presents = df.groupby("ranking")["age"].quantile(q=quartiles)
iqr = boxplot_age_ranking_presents.iloc[3] - boxplot_age_ranking_presents.iloc[1]
flier1 = boxplot_age_ranking_presents.iloc[1] - 1.5 * iqr
flier2 = boxplot_age_ranking_presents.iloc[3] + 1.5 * iqr
plt.axhline(y=flier1, color='r', linestyle='--')
plt.axhline(y=flier2, color='r', linestyle='--')
plt.show()

##9
boxplot_age_visits5years = df.boxplot(column="age", by="visits5years", showmeans=True)
plt.show()
#A
highest_mean_age_group = df.groupby("visits5years")["age"].mean().idxmax()
visits_for_highest_mean_age = df[df["visits5years"] == highest_mean_age_group]["visits5years"].sum()
print(f"Number of visits for the highest mean age group ({highest_mean_age_group}): {visits_for_highest_mean_age}")
#B
df.boxplot(column="room_price", by="visits5years", showmeans=True)
plt.show()
# We can learn that the highest mean age group visit 7 times which is alot, and pay the least because they probably
# get discount for their age. We can also see their std is very low.

##10
print(df["total_expenditure"].min())
print((df["total_expenditure"] < 0).sum())
# we need to take all minus out. There are only 5. will make it 0 and replace with the mean
df["total_expenditure"] = df["total_expenditure"].mask(df["total_expenditure"] < 0)
df["total_expenditure"] = df["total_expenditure"].replace(to_replace=np.nan, value=df.total_expenditure.mean())
print(df["total_expenditure"].describe())
plt.bar(df.ranking, df.total_expenditure)
plt.title("Ranking - total_expenditure")
plt.show()
# There is no correlation between visitir's renkings and their total_expenditure.
# We can see those who paid more ranked it more in general.
