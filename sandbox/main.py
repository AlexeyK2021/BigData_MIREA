import pandas as pd


def main():
    df = pd.DataFrame([
        [1, 'Bob', 'Builder'],
        [2, 'Sally', 'Baker'],
        [3, 'Scott', 'Candle Stick Maker'],
        [4, None, None],
        [5, None, None],
        [6, None, None],
    ],
        columns=['id', 'name', 'occupation'])

    df = df[
        df["name"].notnull() &
        df["occupation"].notnull()
        ]

    print(df)


if __name__ == '__main__':
    main()
