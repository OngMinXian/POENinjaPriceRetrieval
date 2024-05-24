from POENinjaPriceRetrieval import POENinjaPriceRetrieval

if __name__ == "__main__":
    LEAGUE_NAME = "Necropolis"
    poeNinjaPriceRetrieval = POENinjaPriceRetrieval(LEAGUE_NAME)
    df_price = poeNinjaPriceRetrieval.retrieve_prices()
    print(df_price)
    