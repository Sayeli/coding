# Upper Confidence Bond

# Importing the data

dataset = read.csv('Ads_CTR_Optimisation.csv')

#Implementing UCB
N = 10000
d =10
ads_selected = integer()
numbers_of_selections = integer(d)
sums_of_rewards = integer(d)
for (n in 1:N){
  max_upper_bound = 0
  for (i in 1:d) {
    average_reward = sums_of_rewards[i] / numbers_of_selections[i]
    delta_i =sqrt(3/2 *log(n)/ numbers_of_selections[i])
    upper_bound = average_reward + delta_i
    if (upper_bound > max_upper_bound){
      max_upper_bound = upper_bound
      ad = i
    }
  }
}
