from POENinjaPriceRetrieval import POENinjaPriceRetrieval

if __name__ == "__main__":
    LEAGUE_NAME = "Necropolis"
    poeNinjaPriceRetrieval = POENinjaPriceRetrieval(LEAGUE_NAME)
    poeNinjaPriceRetrieval.save_data()
