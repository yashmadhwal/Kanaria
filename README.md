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

### Recreating Project
Prerequisites:
- [Python](https://www.python.org/) 3.7 or later
- [Node](https://nodejs.org/en/download/)

## Installation

[![Test](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

1. Clone repository, In terminal: 
    ```
    git clone https://github.com/yashmadhwal/Kanaria.git
    ```
2.  Install and Create virtual environment
    ```
    pip install virtualenv
    virtualenv venv
    ```
3. Activate environment
    ```
    source venv/bin/activate
    ```
4. Install dependencies and requirements
    ```
    npm i
    pip install -r requirements.txt
    ```
5. Run the project
    ```
    python app.py
    ```
6. After exploring, deactivate by running following command in a seperate terminal
    ```
    deactivate
    ```
**Note:** _On cloning the repository, please note that the bird's image will not be available (as it does not exist in the repository because the file exceeds more than 1Gb), but instead alternative text will appear that will indicate bird's ID. Use [`GetJPEGCollections`](https://github.com/yashmadhwal/Kanaria/blob/main/IPython/CompressJPEGs.ipynb) to downloads all the birds' images. After downloading, save at `/Kanaria/static/` as `jpgs`._
