voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353}, 
{"county":"Jefferson", "registered_voters": 432438}]

for i in voting_data:
    for key in i.keys():
       for x in voting_data:
        for values in x.values():
            print(f"({x}[0]) county has ({i}[0]) registered voters.")


 
