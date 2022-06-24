import pandas as pd

def main():
    print('\nStarting validate_data.py ...')

    # 👇️ set encoding to latin-1
    df = pd.read_csv('suicide_detection.csv', sep=',', encoding='latin-1')

    num_rows = len(df.index)
    num_rows_suicide = 0
    num_rows_non_suicide=0
    num_rows_other_label=0
    for row in df.rows:
        label = row[0]
        if label == "suicide":
            num_rows_suicide += 1
        elif label == "non-suicide":
            num_rows_non_suicide += 1
        else:
            # debug
            print("found other label: %s" % (label))
            num_rows_other_label += 1

    print("number of rows: %d" % (num_rows))
    print("number of suicide rows: %d" % (num_rows_suicide))
    print("number of non-suicide rows: %d" % (num_rows_non_suicide))
    print("number of other label rows: %d" % (num_rows_other_label))


if __name__ == '__main__':
    main()

