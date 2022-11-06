import os.path

import pandas as pd


frame = pd.read_csv(os.path.abspath("operating_systems.txt"), skiprows=[i for i in range(101, 150)])

new_frame = frame.value_counts()

new_frame.to_csv(os.path.abspath("oper_sys_after_pd.txt"))
