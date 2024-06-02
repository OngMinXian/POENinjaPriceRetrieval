import gspread
from google.oauth2.service_account import Credentials

class gSheetController:

    def __init__(self, league_name):
        self.league_name = league_name
        self.read_config()
        self.client = self.make_connection()
        self.gSheet = self.create_or_get_league_gSheet(league_name)

    def read_config(self):
        config = {}
        for line in open("C:/Users/ongmi/Documents/POENinjaPriceRetrieval/.config.txt").readlines():
            key, value = line.split(": ")
            config[key] = value
        self.personal_email = config["personal_email"]

    def make_connection(self):
        print("Establishing connection with google sheets API")
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file("C:/Users/ongmi/Documents/POENinjaPriceRetrieval/.credentials.json", scopes=scopes)
        client = gspread.authorize(creds)
        print("Connection made and client retrieved")
        return client
    
    def create_or_get_league_gSheet(self, league_name):
        gSheet_name = f"POENinjaPriceRetrieval - {league_name}"
        try:
            gSheet = self.client.open(gSheet_name)
        except:
            gSheet = self.client.create(gSheet_name)
            gSheet.share(self.personal_email, perm_type="user", role="writer")
        return gSheet
    
    def create_workSheet(self, worksheet_name, n_row, n_col):
        try:
            self.gSheet.add_worksheet(title=worksheet_name, rows=n_row, cols=n_col)
            print(f"Worksheet {worksheet_name} created")
        except:
            return

    def update_workSheet(self, worksheet_name, df):
        workSheet = self.gSheet.worksheet(worksheet_name)
        workSheet.update([df.columns.values.tolist()] + df.values.tolist())
        print(f"Worksheet {worksheet_name} updated")
