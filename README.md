# IMDB

1) Used imdbPY python package to find movie ID and movie name of top 250 movies on IMDB. 
2) Created dataframe table having Movie ID , Movie name , Rating and Voter as columns and export the dataframe as Output.csv
3) Plotted scatter chart where Rating is on X axis and Voter on Y axis then save the chart as Scatterplot.jpg


Algorithm Behind IMDB top 250:
The formula for calculating the Top Rated 250 Titles gives a true Bayesian estimate: weighted rating

(WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × C  where:

R = average for the movie (mean) = (Rating)
v = number of votes for the movie = (votes)
m = minimum votes required to be listed in the Top 250 (currently 25000)
C = the mean vote across the whole report (currently 7.1)

For the Top 250, only votes from regular voters are considered.
