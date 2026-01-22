from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
import joblib
import csv
import numpy as np

def safe_float(value):
    try:
        return float(value.strip()) if value.strip() else 0.0
    except ValueError:
        return 0.0


class EDASvm:
    train_vector_amusement = []
    target_vector_amusement = []
    train_vector_stress = []
    target_vector_stress = []
    train_vector_baseline = []
    target_vector_baseline = []

    ex_vector_amusement = []
    ex_vector_stress = []
    ex_vector_baseline = []

    def feature_selection(self):
        def load_csv(filepath):
            with open(filepath, 'r') as f:
                reader = csv.reader(f)
                data = [[safe_float(value) for value in line] for line in reader]
            return np.array(data) if data else np.zeros((1, 37))

        vector_amusement = load_csv('model\\amusement.csv')
        vector_stress = load_csv('model\\stress.csv')
        vector_baseline = load_csv('model\\baseline.csv')

        self.train_vector_amusement = vector_amusement [:, 0:34]
        self.target_vector_amusement = vector_amusement[:, 34:35]
        self.train_vector_stress = vector_stress [:, 0:34]
        self.target_vector_stress  = vector_stress [:, 34:35]
        self.train_vector_baseline = vector_baseline [:, 0:34]
        self.target_vector_baseline = vector_baseline [:, 34:35]

        print(f"Amusement data shape: {self.train_vector_amusement.shape}")
        print(f"Stress data shape: {self.train_vector_stress.shape}")
        print(f"Baseline data shape: {self.train_vector_baseline.shape}")

        clf = ExtraTreesClassifier()
        clf = clf.fit(self.train_vector_amusement, self.target_vector_amusement.ravel())
        model = SelectFromModel(clf, threshold='1.25*mean', prefit=True)
        joblib.dump(model, 'model\\vector_select.m')

        self.ex_vector_amusement = model.transform(self.train_vector_amusement)
        self.ex_vector_stress = model.transform(self.train_vector_stress)
        self.ex_vector_baseline = model.transform(self.train_vector_baseline)

    def svm_train(self):
        clf = svm.SVC()
        ovr_clf = OneVsRestClassifier(clf)

        X = np.vstack([self.ex_vector_amusement, self.ex_vector_stress, self.ex_vector_baseline])
        y = np.concatenate([
            np.full(len(self.ex_vector_amusement), 1),
            np.full(len(self.ex_vector_stress), 2),
            np.full(len(self.ex_vector_baseline), 0)
        ])

        ovr_clf.fit(X, y)
        joblib.dump(ovr_clf, 'model\\emotion_ovr_model.m')