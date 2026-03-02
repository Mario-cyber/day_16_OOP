from  prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name",["Pikachu","Charizard","Lapras"]) 
table.add_column("Type",["Electric","Fire","Water"]) 

print(table)