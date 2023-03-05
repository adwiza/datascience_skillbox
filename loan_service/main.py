import json
from pprint import pprint
import pandas as pd

import joblib


def main():
    model = joblib.load('model/loan_pipe.pkl')

    with open('model/data/form_LP001014.json') as fin:
        form = json.load(fin)
        df = pd.DataFrame.from_dict([form])
        y = model['model'].predict(df)
        print(f'{form["Loan_ID"]}: {y[0]}')
    # pprint(model['metadata'])


if __name__ == '__main__':
    main()
