#Apriori

# data preprocessing

install.packages('arules')
library(arules)
# Importing the dataset
dataset = read.csv('Market_Basket_Optimisation.csv', header = F)
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = T)
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

# Training Apriori on the dataset

rules = apriori(data = dataset, parameter = list(support = 0.003, confidence = 0.4 ))
# FOR SUPPORT WE WILL CONSIDER PRODUCTS WHICH ARE PURCHASED MINIMUM THREE TIMES A DAY.
# SO IN A WEEK ITS 3*7= 21. SO MINIMUM SUPPPORT : 21/7500 = 0.0028

# VISUALIZATION OF RESULT
inspect(rules[1:10])

#better way is to sort by lift(decrrasing lift)
inspect(sort(rules, by = 'lift')[1:10])

# Here we can see that we are  getting the productes that have high support. the high purchased product. Which is effecting the lift.
#So to get a better combination we will change the confidence.

rules = apriori(data = dataset, parameter = list(support = 0.003, confidence = 0.2 ))

#better way is to sort by lift(decrrasing lift)
inspect(sort(rules, by = 'lift')[1:10])

rules = apriori(data = dataset, parameter = list(support = 0.004, confidence = 0.2 ))
# FOR SUPPORT WE WILL CONSIDER PRODUCTS WHICH ARE PURCHASED MINIMUM FOur TIMES A DAY.
# SO IN A WEEK ITS 3*7= 21. SO MINIMUM SUPPPORT : 28/7500 = 0.0037

#better way is to sort by lift(decrrasing lift)
inspect(sort(rules, by = 'lift')[1:10])
