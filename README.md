# wouterk

AI Crypto Project

DOEL: 
Om koersverwachtingen te voorspellen in de cryptocurrencie
Om cashflow tussen verschillende markten te analyseren

BENODIGD:
-DATASET (Trainingscorpus)
	Cryptocurrencies downloaded from Marketcap
		More: Stockexchange in Valuta, Dowjones, raw materials, etc
-Definition and Creation of Global Parameters
-Definition and Creation of Derivative Parameters
	News indicator (google search index quantitiy), Technology is useful and can or is adopted in current market?
-Definition and Creation of Moneyflow Parameters
		
Function for converting correct data format for AI implementation: AARF format.
Import in WEKA.
 
MORE on moneyflow:

The marketcycles need to be identified and analysed. 
Are stockexchange price values in valuta, coorporations, crypto or raw material going correlated? What is their relation? 
Which coins and coingroups are correlated?
Which parameters best present this moneyflow?
MONEYFLOWS:
-van Stockmarket naar Crypto. Door vergelijking total marketcap change
- van Bitcoin naar other crypto. Door %bitcoin dominance richting. ( is marketcap change vergelijk)
- Moneyflow tussen Bitcoin naar other  coins:


WERKING



 

 
Data Download
 
 
Array cryptos is nu een fixed list met cryptocurrency namen. Liever een gedownloade lijst van de top 200 coins) is zeker 95%) 
 

TO DO:stockmarket etc exchange download (of globale info enkel, zoals marketcap en volume
 
Bereken globale marktgegevens. 		
Formule					naamparameter		Indicator van
Totalcap/TotalCap_yesterday			%capchange		totalecryptomarkt daily pricechange
 	Ook voor	3dagen	
En voor 7,21,30 ,90,120 ,365

Dus resultaat nieuwe tabel met globale dagelijkse info
 



Bereken derivative parameters voor elke coin en elke dag:
Formule					naamparameter		Indicator van
	Thiscoin_marketcap_today / totalcap_today	coindom			coin marktaandeel	
	coindom/coindom_yesterday			Coindom_1d		marktaandeel change
coindom/coindom_bitcoin 			Bitcoindomrel		coin marktaandeel relatief tot bitcoin
Bitcoindomrel_today / Bitcoindomrel_yesterday	Bitcoindom_1d		coin marktaandeel change relatief tot bitcoin
*Ook voor	3dagen	
*En voor 7,21,30 ,90,120 ,365
	Coindom_1d_today / bitcoindom_1d_today				analysetool cash flow coinmarket/bitcoinmarket
	Coindom_3d_today / bitcoindom_3d_today
En ook voor 3d, 7d,, 21d ,, 30d,, …
closeprice_today / closeprice_yesterday 	pricechange_1d		winst
volume_today/ marketcap_today 		dailytraded   		marktSnelheid
dailytraded_today / dailytraded_yesterday	dailytraded_1d
volume_today / volume_yesterday		vol_1d
En ook voor 3d, 7d,, 21d ,, 30d,, …

Dus resultaat extra kollommen met info per coin per dag:
 


 
Days since last min 
Days since last max 



