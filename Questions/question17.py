service_games_played = 76123
service_games_won = 23216

# Step 1: Calculate breaks of serve
breaks_of_serve = service_games_played - service_games_won

# Assume number of matches is equal to total service games won
# (as stated in the assumption)
total_matches = 23216

# Step 2: Calculate average breaks per match
average_breaks_per_match = breaks_of_serve / total_matches

# Output result
print("Breaks of serve:", breaks_of_serve)
print("Average breaks per match: {:.2f}".format(average_breaks_per_match))