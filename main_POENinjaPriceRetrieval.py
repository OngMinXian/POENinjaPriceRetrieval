import time
from POENinjaPriceRetrieval import POENinjaPriceRetrieval

if __name__ == "__main__":
    countdown_to_start = 5*1
    while countdown_to_start:
        print(f"POENinja Price Retrieval will start in {countdown_to_start} seconds.", "\r", end="")
        countdown_to_start -= 1
        time.sleep(1)
    print("")

    poeNinjaPriceRetrieval = POENinjaPriceRetrieval()
    poeNinjaPriceRetrieval.update_gSheet_with_prices()

    countdown_to_end = 1*60
    while countdown_to_end:
        print(f"POENinja Price Retrieval will close in {countdown_to_end} seconds.", "\r", end="")
        countdown_to_end -= 1
        time.sleep(1)
    print("")