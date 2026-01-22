import os
import generatevector
import getattr
from eda_svm import EDASvm
import joblib
import csv
import numpy as np

def train_module():
    if os.path.isfile('model\\emotion_ovr_model.m'):
        print('The model already exists, do you want to retrain it?')
        print('1: skip 2: retrain')

        choice = input()
        while choice not in ['1', '2']:
            print('Error input, please retry')
            choice = input()
        if choice == '1':
            print('Using last model')
            return
    print("Training... please wait")
    generatevector.generate_vector()
    eda_svm = EDASvm()
    eda_svm.feature_selection()
    eda_svm.svm_train()
    print('Training finished, using new model')

def predict_result():
    file_path = os.path.join('han_experiment_test//胡wt.csv')

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data_batch = []

        with open('han_experiment_test//result//胡wt_result.csv', 'w', newline='') as result_file:
            writer = csv.writer(result_file)

            for row in reader:

                row = [float(value) for value in row]
                data_batch.append(row)

                if len(data_batch) >= 50:

                    clf = joblib.load('model//emotion_ovr_model.m')
                    select = joblib.load('model/vector_select.m')

                    vector = getattr.get_vector(data_batch)
                    if np.iscomplexobj(vector):
                        vector = np.real(vector)
                    vector = vector.reshape(1, -1)

                    new_vector = select.transform(vector)
                    print(new_vector)

                    result = clf.predict(new_vector)

                    if result[0] == 1:
                        res = '愉悦'
                    elif result[0] == 2:
                        res = '压力'
                    else:
                        res = '基线'


                    writer.writerow([res])
                    data_batch.clear()

    print("over,收工")

if __name__ == '__main__':
    predict_result()




