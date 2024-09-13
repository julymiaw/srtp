import logging
import sys
from sqlalchemy import false
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
import time
from prettytable import PrettyTable

# 创建一个 PrettyTable 对象
table = PrettyTable()
table.field_names = ["Name", "Age"]
table.add_row(["Alice", 25])
table.add_row(["Bob", 30])
# 创建一个进度条对象
with logging_redirect_tqdm():
    for i in tqdm(
        range(10),
        desc=f"Processing batches - Epoch",
        total=10,
        ncols=80,
        leave=False,
    ):
        # 模拟耗时操作
        time.sleep(0.1)
        # 使用 logging 输出信息
        tqdm.write(str(table))
