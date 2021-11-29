from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import csv

# Function to get birdrow and bird Id
def returnBirdRow(bird_id):

    BirdInfo = df.loc[df['bird_id'] == str(bird_id)]

    #Create dictionary
    our_dict = dict()
    for row_index in range(len(birds_dataset_with_ranks)):
        row = birds_dataset_with_ranks[row_index]
        our_dict[row[0]] = row_index

    # print(our_dict.keys())

    bird_index = bird_id
    if bird_index in set(our_dict.keys()):
        bird_row = our_dict[bird_index]
        return bird_row
    else:
        return None

df = pd.read_excel('static/Data/birds_dataset_with_ranks_new.xlsx')

birds_dataset_with_ranks = list()
int_columns = [-3, -5, -7, -9]
numeric_columns = [0, -1, -2, -4, -6, -8]
with open('static/Data/birds_dataset_with_ranks_new.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            column_names = row
            line_count += 1
        else:
            for int_element in int_columns:
                row[int_element] = int(row[int_element])
            for numeric_element in numeric_columns:
                row[numeric_element] = float(row[numeric_element])
            birds_dataset_with_ranks.append(row)
            line_count += 1
    print(f'Processed {line_count} lines.')



# Making the flask Application
app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        BirdInfo = request.form['bird_number']

        return redirect(url_for('modal', BirdInformation = BirdInfo.zfill(4)))


    else:
        return render_template('base.html')

@app.route('/<BirdInformation>')
def modal(BirdInformation):
    try:
        BirdInfo = int(BirdInformation)
        if BirdInfo<=9:
            birdCatergory = 'Super Founder'
        elif 100 > BirdInfo >= 10 :
            birdCatergory = 'Founder'
        elif 1000 > BirdInfo >= 100 :
            birdCatergory = 'Rare'
        elif 10000 > BirdInfo >= 1000 :
            birdCatergory = 'Limited Edition'

        bird_row = returnBirdRow(BirdInfo)

        
        if len(BirdInformation) != 4:
            return render_template('404.html')

        else:
            if bird_row == None:
                return render_template('error.html',BirdInfo = BirdInformation)

            else:
                print('bird_row',bird_row)
                """ function(int(BirdInfo),BirdInfo)

                T_score, T_rank, H_score, H_rank, E_score, E_rank, OA_score, OA_rank = function(int(BirdInfo),BirdInfo) """
                T_score = str(round(df.loc[df['bird_id'] == BirdInfo]['trait_score'][bird_row],2))
                T_rank = str(round(df.loc[df['bird_id'] == BirdInfo]['trait_rank'][bird_row],2))
                H_score = str(round(df.loc[df['bird_id'] == BirdInfo]['set_score'][bird_row],2))
                H_rank = str(round(df.loc[df['bird_id'] == BirdInfo]['set_rank'][bird_row],2))
#                 E_score = str(round(df.loc[df['bird_id'] == BirdInfo]['edition_score'][bird_row],2))
#                 E_rank = str(round(df.loc[df['bird_id'] == BirdInfo]['edition_rank'][bird_row],2))
                OA_score = str(round(df.loc[df['bird_id'] == BirdInfo]['weighted_score'][bird_row],2))
                OA_rank = str(round(df.loc[df['bird_id'] == BirdInfo]['weighted_rank'][bird_row],2))

                return render_template('modal.html',BirdInfo = BirdInformation,
                                                    bird_image = BirdInformation,
                                                    T_score = T_score,
                                                    T_rank = T_rank,
                                                    H_score = H_score,
                                                    H_rank = H_rank,
#                                                     E_score = E_score,
#                                                     E_rank = E_rank,
                                                    bird_Catergory = birdCatergory,
                                                    OA_score = OA_score,
                                                    OA_rank = OA_rank)

    except ValueError:
        return render_template('404.html')

@app.route('/allStats')
def allStats():
#     return render_template('graphs.html',lable = sorted_Ranks, value = sorted_Score)
    return render_template('graphs.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)