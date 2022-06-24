    for i in range(len(df)):
        label = df.iloc[i,0]
        row = df.iloc[i]
        #print("label: %s" % (label))
        if label == "suicide":
            num_rows_suicide += 1
            clean_df = pd.concat([clean_df, row], ignore_index = True)
        elif label == "non-suicide":
            num_rows_non_suicide += 1
            clean_df = pd.concat([clean_df, row], ignore_index = True)
        else:
            num_rows_other_label += 1
            print("found other label on row %d: %s" % (i, label))
            error_df = pd.concat([error_df, row], ignore_index = True)