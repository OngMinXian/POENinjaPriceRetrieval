import requests
import pandas as pd
import datetime
import os.path
import time

class POENinjaPriceRetrieval:

    def __init__(self, league_name, fileSaveDir = None):
        self.league_name = league_name

        if fileSaveDir == None:
            self.fileSaveDir = "C:/Users/ongmi/Documents/POETools/priceHistory/POENinja/"
        else:
            self.fileSaveDir = fileSaveDir

        self.currency_URL = f"https://poe.ninja/api/data/currencyoverview?league={league_name}&type=Currency"
        self.fragment_URL = f"https://poe.ninja/api/data/currencyoverview?league={league_name}&type=Fragment"
        self.divination_card_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=DivinationCard"
        self.artifact_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Artifact"
        self.oil_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Oil"
        self.incubator_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Incubator"
        self.unique_weapon_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=UniqueWeapon"
        self.unique_armour_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=UniqueArmour"
        self.unique_accessory_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=UniqueAccessory"
        self.unique_flask_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=UniqueFlask"
        self.unique_jewel_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=UniqueJewel"
        self.unique_relic_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=UniqueRelic"
        self.skill_gem_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=SkillGem"
        self.cluster_jewel_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=ClusterJewel"
        self.map_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Map"
        self.blighted_map_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=BlightedMap"
        self.blight_ravaged_map_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=BlightRavagedMap"
        self.unique_map_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=UniqueMap"
        self.delirium_orb_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=DeliriumOrb"
        self.invitation_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Invitation"
        self.scarab_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Scarab"
        self.memory_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Memory"
        self.base_type_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=BaseType"
        self.fossil_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Fossil"
        self.resonator_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Resonator"
        self.beast_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Beast"
        self.essence_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Essence"
        self.vial_URL = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Vial"

    def retrieve_currency_price(self, URL, type):
        print(f"Retrieving {type} prices")
        response = requests.get(URL)
        response_json = response.json()["lines"]

        # Parse json data for currency information
        data = []
        for currency in response_json:
            name = currency["detailsId"]
            try:
                chaos_price = currency["receive"]["value"]
                listing_count = currency["receive"]["listing_count"]
            except:
                chaos_price = pd.NA
                listing_count = pd.NA
            data.append((type, name, chaos_price, listing_count))

        df = pd.DataFrame(data, columns=["Type", "Name", "Chaos Price", "Listing Count"])
        return df
    
    def retrieve_item_price(self, URL, type):
        print(f"Retrieving {type} prices")
        response = requests.get(URL)
        response_json = response.json()["lines"]

        # Parse json data for item information
        data = []
        for item in response_json:
            name = item["detailsId"]
            chaos_price = item["chaosValue"]
            listing_count = item["listingCount"]
            data.append((type, name, chaos_price, listing_count))

        df = pd.DataFrame(data, columns=["Type", "Name", "Chaos Price", "Listing Count"])
        return df

    def retrieve_prices_from_POENinja(self):
        print("Sending HTTP Get Requests")
        self.df_price = pd.concat([
            self.retrieve_currency_price(self.currency_URL, "Currency"),
            self.retrieve_currency_price(self.fragment_URL, "Fragment"),
            self.retrieve_item_price(self.divination_card_URL, "Divination Card"),
            self.retrieve_item_price(self.artifact_URL, "Artifact"),
            self.retrieve_item_price(self.oil_URL, "Oil"),
            self.retrieve_item_price(self.incubator_URL, "Incubator"),
            self.retrieve_item_price(self.unique_weapon_URL, "Unique Weapon"),
            self.retrieve_item_price(self.unique_armour_URL, "Unique Armour"),
            self.retrieve_item_price(self.unique_accessory_URL, "Unique Accessory"),
            self.retrieve_item_price(self.unique_flask_URL, "Unique Flask"),
            self.retrieve_item_price(self.unique_jewel_URL, "Unique Jewel"),
            self.retrieve_item_price(self.unique_relic_URL, "Unique Relic"),
            self.retrieve_item_price(self.skill_gem_URL, "Skill Gem"),
            self.retrieve_item_price(self.cluster_jewel_URL, "Cluster Jewel"),
            self.retrieve_item_price(self.map_URL, "Map"),
            self.retrieve_item_price(self.blighted_map_URL, "Blighted Map"),
            self.retrieve_item_price(self.blight_ravaged_map_URL, "Blighted Ravaged Map"),
            self.retrieve_item_price(self.unique_map_URL, "Unique Map"),
            self.retrieve_item_price(self.delirium_orb_URL, "Delirium Orb"),
            self.retrieve_item_price(self.invitation_URL, "Invitation"),
            self.retrieve_item_price(self.scarab_URL, "Scarab"),
            self.retrieve_item_price(self.memory_URL, "Memory"),
            self.retrieve_item_price(self.base_type_URL, "Base Type"),
            self.retrieve_item_price(self.fossil_URL, "Fossil"),
            self.retrieve_item_price(self.resonator_URL, "Resonator"),
            self.retrieve_item_price(self.beast_URL, "Beast"),
            self.retrieve_item_price(self.essence_URL, "Essence"),
            self.retrieve_item_price(self.vial_URL, "Vial"),
            print("All prices retrieved")
        ])

    def save_prices(self):
        today = datetime.date.today()
        file_name = f"{self.fileSaveDir}{self.league_name}_{today}-POENinja_Prices.csv"
        # Data generated already today
        if os.path.isfile(file_name):
            print(f"Prices already exist at {file_name}")
            return
        
        # Generate data
        else:
            self.retrieve_prices_from_POENinja()
            self.df_price.to_csv(file_name, header=True, index=False)
            print(f"Prices saved to {file_name}")

    def retrieve_prices(self, league_name = None, date = None):
        if league_name == None:
            league_name = self.league_name
        if date == None:
            date = datetime.date.today()
        file_name = f"./priceHistory/POENinja/{league_name}_{date}-POENinja_Prices.csv"

        try:
            self.df_price = pd.read_csv(file_name)
        except FileNotFoundError:
            self.save_prices()

        return self.df_price
    
def retrieve_league_name():
    request = requests.get("https://poe.ninja/api/data/getindexstate?")
    LEAGUE_NAME = request.json()["economyLeagues"][0]["name"]
    return LEAGUE_NAME
    
if __name__ == "__main__":
    time.sleep(15)
    while True:
        try:
            LEAGUE_NAME = retrieve_league_name()
            print(f"Running POENinja Price Retrieval on {LEAGUE_NAME} league")
            poeNinjaPriceRetrieval = POENinjaPriceRetrieval(LEAGUE_NAME)
            poeNinjaPriceRetrieval.save_prices()
            break
        except Exception as err:
            print(f"Error encountered: {err}")
    print("Programme will exit in 15 seconds")
    time.sleep(15)
