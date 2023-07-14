import csv

hash_table = {}  # Create an empty hash table

with open('E:\\python\\trabalhofinal\\notas.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')  # Read the CSV file
    for row in csv_reader:
        key = row[0]  # First column as the key
        value = row[1:]  # Remaining columns as the value
        hash_table[key] = value  # Add the key-value pair to the hash table

print(hash_table)  # Print the hash table

search_id = '22045'  # Replace '1234' with the ID you want to search for

# Perform the search
if search_id in hash_table:
    print("ID encontrado!")
    print("Notas do aluno:", hash_table[search_id])
else:
    print("ID não encontrado!")
