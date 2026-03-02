from  prettytable import PrettyTable

table = PrettyTable()

# '()' implies method
table.add_column("Pokemon Name",["Pikachu","Charizard","Lapras"]) 
table.add_column("Type",["Electric","Fire","Water"]) 

# setting value by '=' implies attribute
table.align = "l"
print(table)