import json

# Charger la liste de tâches à partir d'un fichier json
def load_tasks(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        reader = json.reader(file)
        for row in reader:
            tasks.append(row)
    return tasks

# Afficher la liste de tâches
def display_tasks(tasks):
    for task in tasks:
        print(task)

# Écrire la liste de tâches dans un fichier json
def write_tasks(tasks, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = json.writer(file)
        for task in tasks:
            writer.writerow(task)

if __name__ == '__main__':
    # Créer une nouvelle liste de tâches
    new_tasks = [
        ['Faire du sport', 'Courir 5 km', 'Moyenne'],
        ['Lire un livre', 'Terminer le dernier best-seller', 'Haute']
    ]
    
    # Afficher les nouvelles tâches créées
    print("Nouvelle liste de tâches créée :")
    display_tasks(new_tasks)
    
    # Demander à l'utilisateur s'il souhaite sauvegarder les nouvelles tâches
    response = input("Souhaitez-vous sauvegarder ces nouvelles tâches ? (Oui/Non): ")
    
    if response.lower() == 'oui':
        # Écrire les nouvelles tâches dans un fichier new_tasks.json
        write_tasks(new_tasks, 'new_tasks.json')
        print("Nouvelles tâches sauvegardées dans new_tasks.json.")
    else:
        print("Les nouvelles tâches n'ont pas été sauvegardées.")
