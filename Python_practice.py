voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for county in county_dict.keys():
        for voters in county_dict.values():
            print(f"{county_dict['county']} county has {county_dict['voters']} registered voters.")