import pandas as pd


def main():
    print('\nStarting validate_data.py ...')

    # input file name base
    file_name_base = 'suicide_detection'
    input_file_name = file_name_base + '.csv'
    clean_file_name = file_name_base + '-clean.csv'
    error_file_name = file_name_base + '-error.csv'

    # read csv with latin-1 encoding
    df = pd.read_csv(input_file_name, sep=',', encoding='latin-1')

    # select "suicide" rows
    suicide_df = df.loc[df['class'] == 'suicide']
    non_suicide_df = df.loc[df['class'] == 'non-suicide']
    other_label_df = df.loc[~df['class'].isin(['suicide', 'non-suicide'])]

    num_rows = len(df.index)
    num_rows_suicide = len(suicide_df.index)
    num_rows_non_suicide= len(non_suicide_df.index)
    num_rows_other_label= len(other_label_df.index)

    # print stats
    print("number of rows: %d" % (num_rows))
    print("number of suicide rows: %d" % (num_rows_suicide))
    print("number of non-suicide rows: %d" % (num_rows_non_suicide))
    print("number of other label rows: %d" % (num_rows_other_label))

    # export csv with latin-1 encoding
    clean_df = pd.concat([suicide_df, non_suicide_df], ignore_index = True)
    clean_df.to_csv(clean_file_name, sep=',', encoding='latin-1')
    other_label_df.to_csv(error_file_name, sep=',', encoding='latin-1')


if __name__ == '__main__':
    main()

