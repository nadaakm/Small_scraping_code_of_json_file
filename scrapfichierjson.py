import csv
import json

class ProductLogger():
    
    def __init__(self, json_file_path, csv_file_path):
        self.json_file_path = json_file_path
        self.csv_file_path = csv_file_path
    
    def log_products(self):
        # Lire le contenu du fichier JSON
        with open(self.json_file_path, "r") as f:
            data = json.load(f)
            dt = json.dumps(data, indent=4, sort_keys=False)
            print(type(dt))#### type str

        # Récupérer la liste des bundles
        sites = data["Bundles"]

        # Écrire les informations dans le fichier CSV
        with open(self.csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["produit_dispo", "Price"])
            ###parcourir les differents produit du fichier 
            for bundles in sites:   
                try:
                    products = bundles['Products']
                except:
                    print('Error')
                ### acceder aux elements du produit  
                for product in products:
                    try:
                        ## si le produit est  dispo
                        if product['IsAvailable'] == True:
                            print('You can buy:',product['Name'][:-10],'at our store at',product['Price'],'$')
                            ##si il n'est pas diso
                        else:
                            print(product['Name'],product['Stockcode'])
                            ##si il n'existe pas 
                    except:
                        print('ERROR') 
                writer.writerow([product['Name'][:-10],product['Price']])
mydata=ProductLogger('data.json','productsnada.csv')
mydata.log_products()

