# KRAMER — Kanaria RArity MEteR

by Yash Madhwal, Osoiotoko and Yury Yanovich for RMRKable Hacktoberfest

The data mining and machine learning parts are performed in IPython and notebooks are in the IPython folder. Namely, 

* ReadDataset: reads the Kanaria dataset and saves it as a bird-trait table
* ReadTradeDataset: reads the trade data of the Kanaria dataset and saves it as an event list
* ConstructTradeDataset: construct dataset with trade data
* ComputeIndex: computes scores based on traits, sets, and edition
* FitWeights: fits the best combination of traits, sets, and edition scores to trade data
* GetJPEGCollections: downloads all the birds' images
* CompressJPEGs: compresses jpegs.

You need RMRK 2 consolidated dump (see https://docs.rmrk.app/syncing/#consolidation) named as 'rmrk20211118.json' in the same folder with notebooks to run notebooks one-by-one.

