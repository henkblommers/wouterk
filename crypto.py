import sys
import re
import mmap
from urllib.request import urlopen
import argparse
import datetime
import csv
import pandas as pd
import io
import numpy

def downloadcoins(cryptos, startdate, enddate):
    #provides header & df with cryptos 
    for i in range(len(cryptos)):  
        print(i, ". Downloading data for", cryptos[i])
        url = 'https://coinmarketcap.com/currencies/' + cryptos[i] + '/historical-data/' + '?start=' + startdate + '&end=' + enddate
        df[i]= urlopen(url,timeout=10).read()
        urlopen(url,timeout=10).close() 
        df[i]= str(df[i],'utf-8')
        if (i == 0): #for each crypto
            header = list(re.findall(r'<th .*>([\w ]+)</th>', re.search(r'<thead>(.*)</thead>', df[i], re.DOTALL).group(1)))
            header.insert(0,'Currency') #add label "currency"
            header = pd.DataFrame(header).T
            rows = re.findall(r'<tr[^>]*>' + r'\s*<td[^>]*>([^<]+)</td>'*7 + r'\s*</tr>', re.search(r'<tbody>(.*)</tbody>', df[i], re.DOTALL).group(1))
        for j in range(len(rows)):  #for each datarow
            row = list(rows[j]) #convert to list, 
            row.insert(0,cryptos[i]) # add currency to first element of each row
            rows[j]= tuple (row)  # and convert back to row
        df[i]= pd.DataFrame(list(rows)) #add all rows into dataframe df[i] for this crypto
        
return header, df 

def savenewcsv(header, df, filename, length):
      header.to_csv(filename, mode= 'a',index=False, header=False) #write header in csv
    for i in range(length)
        df[i].to_csv(filename, mode= 'a',index=False, header=False) #write data in csv

def updatecsv(header, df, filename) #check for each coin till what date is already downloaded, download the rest, put it together and save it accordingly
return 0


def addglobalparameters(header, df{}, cryptoi:
    globalpars = []
    dates = df{header.index(Date)}
        print (dates)
        
    #GMC Globalmarketcap
    GMC = []
    for i 

    #Bitcoinprice
    #1week regressie, 14d,30d,90,365,alltime
    
    
return 
def main(args=None):

    cryptos = ['Bitcoin','Ethereum']
    #,'Ripple','Bitcoin-Cash','Cardano','Litecoin','NEM','NEO','Stellar','EOS','IOTA','Dash','Monero','TRON','Bitcoin-Gold','ICON','Qtum','Ethereum-Classic','Lisk','RaiBlocks','VeChain','OmiseGO','Tether','Populous','Zcash','Verge','Siacoin','Binance-Coin','Stratis','Bytecoin-bcn','Steem','Ardor','Status','Maker','Augur','BitShares','KuCoin-Shares','0x','Waves','Dogecoin','Electroneum','Veritaseum','Walton','Komodo','Dragonchain','Decred','Dentacoin','Loopring','SALT','Ark','QASH','DigiByte','Basic-Attention-token','Golem','Hshare','Kyber-Network','Gas','Ethos','SmartCash','PIVX','Byteball','WAX','FunFair','RChain','Aion','ZClassic','Factom','Dent','MonaCoin','Power-Ledger','Kin','DigixDAO','aelf','Aeternity','Bytom','ReddCoin','Nebulas-token','Syscoin','Enigma','Request-Network','Emercoin','Nexus','ChainLink','Neblio','ZCoin','MaidSafeCoin','Substratum','Experience-points','Bitcore','GXShares','Nxt','Bancor','Cindicator','MediBloc','Cryptonex','Quantstamp','Gnosis','PACcoin','Particl','Iconomi','TenX','GameCredits','BitcoinDark','Civic','Pillar','DigitalNote','SIRIN-LABS-Token','Skycoin','Raiden-Network-token','Poet','SophiaTX','BLOCKv','Vertcoin','DEW','Storj','BridgeCoin','Santiment','VIBE','RLC','Cobinhood','Ubiq','NAV-Coin','BitConnect','Telcoin','Blocknet','PayPie','XTRABYTES','Time-New-Bank','ETHLend','Monaco','Achain','Dynamic-Trading-rights','Simple-Token','Storm','SingularDTV','Enjin-Coin','Red-Pulse','AirSwap','Revain','INS-Ecosystem','DeepBrain-Chain','high-performance-blockchain','AppCoins','Counterparty','WaBi','Peercoin','Edgeless','Ripio-Credit-network','Bibox-Token','BitBay','HTMLCOIN','Einsteinium','SONM','SpankChain','Aragon','IoT-Chain','Decentraland','Melon','Amber','CyberMiles','Internet-Node-token','Quantum-resistant-ledger','AdEx','ZenCash','attention-token-of-media','Streamr-DATAcoin','Modum','NAGA','Gulden','UTRUST','Centra','MediShares','district0x','Metal','SuperNET','ION','Nuls','Rise','Electra','Etherparty','library-credit','Unikoin-Gold','Viacoin','Triggers','Metaverse','CloakCoin','Agoras-Tokens','QLINK','Wings','IOCoin','MobileGo','Wagerr','Oyster','Burst','HempCoin','SaluS','Asch','Bread','Eidoo','Tierion','Decision-Token','Lamden','DECENT','Hive','CoinDash','Lunyr','FirstBlood','Aeon','Grid','Voxels','Genesis-Vision','ECCoin','HelloGold','Groestlcoin','Lykke','MinexCoin','safe-exchange-coin','Gifto','Mooncoin','BitClave','TokenCard','Cofound-it','Dimecoin','Shift','Mercury','TaaS','Namecoin','Trust','Everex','Agrello-delta','Presearch','Crown','Pura','Ink','Monetha','Feathercoin','SHIELD','Trade-Token','Pepe-Cash','Worldcore','adToken','Viberate','Flash','Jinn','Spectrecoin','Voise','iXledger','bitCNY','YOYOW','Neumark','Paypex','EncrypGen']
    filename = "histcoinsdata2.csv"

    header, df{} = downloadcoins(cryptos)
    #header, df{} = addglobalparameters(header, df{})
    #header, df{} = addparameters
    #header, df{} = addprofitlabels
    safenewcsv(header, df{}, filename, len(cryptos))
    #updatecsv(header, df{}, filename)
    
   

