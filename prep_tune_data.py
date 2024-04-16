import pandas as pd
import json
import streamlit as st

def df_to_jsonl(df):
  """
  Converts a pandas dataframe with 'text_input' and 'output' fields to JSONL format.

  Args:
      df (pandas.DataFrame): The dataframe to convert.

  Returns:
      str: A JSON string in JSONL format.
  """
  data = []
  for index, row in df.iterrows():
    data.append({
      "messages": [
        {"role": "user", "content": row["text_input"]},
        {"role": "model", "content": row["output"]},
      ]
    })
  return json.dumps(data, indent=2)
def app():
    st.title("Data Preparation")

    # open a csv file using sa dataframe
    df = pd.read_csv("data/akeanon-sentences.csv")

    st.write("The dataset")
    st.write(df)

    # convert the dataframe to jsonl
    jsonl_str = df_to_jsonl(df)

    st.write(jsonl_str)

    # save the jsonl string to a file
    with open("data/aleanon-sentences.jsonl", "w") as f:
        f.write(jsonl_str)

if __name__ == "__main__":
    app()   