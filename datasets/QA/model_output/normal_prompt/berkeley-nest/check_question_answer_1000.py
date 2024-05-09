## question_answer_1000.csvをpandasで読み込んで、冒頭の1000行を表示する

import pandas as pd

df = pd.read_csv('Starling-LM-7B-alpha/question_answer_1000.csv')

print(df['LLMAnswer'].head(10))


