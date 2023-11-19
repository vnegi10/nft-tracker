import pandas as pd
from utils.api import get_response, PRO_URL, use_pro

def get_nft_markets(order_by, num_entries):
    
    page_params = {
                    "per_page": num_entries,
                    "page": 1,
                    "order": order_by
                  }
    
    nft_markets = get_response("/nfts/markets", use_pro, page_params, PRO_URL)
    nft_all = []

    for i in range(len(nft_markets)):
        nft_select = nft_markets[i]
        temp_dict = dict(
                         id = nft_select["id"],
                         asset_platform_id  = nft_select["asset_platform_id"],
                         floor_price_native = nft_select["floor_price"]["native_currency"],
                         floor_price_usd    = nft_select["floor_price"]["usd"],
                         market_cap_usd     = nft_select["market_cap"]["usd"],
                         volume_24h_usd     = nft_select["volume_24h"]["usd"]
                        )
        nft_all.append(temp_dict)
            
    return pd.DataFrame(nft_all)

def get_nft_hist(nft_id, num_days):

    hist_params = {"days": num_days}
    hist_url = f"/nfts/{nft_id}/market_chart"
    
    nft_hist = get_response(hist_url, use_pro, hist_params, PRO_URL)
    all_time, all_floor_price_usd = [], []

    floor_price_usd = nft_hist["floor_price_usd"]

    for i in range(len(floor_price_usd)):
        time = floor_price_usd[i][0]
        all_time.append(time)
        
        price = floor_price_usd[i][1]
        all_floor_price_usd.append(price)

    df_hist = pd.DataFrame(list(zip(all_time, all_floor_price_usd)),
                           columns =['Time', 'Price_usd'])

    df_hist["Time"] = pd.to_datetime(df_hist["Time"], unit = "ms")
    
    return df_hist