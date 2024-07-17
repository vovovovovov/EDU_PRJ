import pandas as pd
import mysql.connector

# 读取 CSV 文件
df = pd.read_csv('./output_data/output.csv')

# 连接到 MySQL 数据库
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="edu_prj"
)

# 创建数据库游标
mycursor = mydb.cursor()

# 创建表格 (如果不存在)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS your_table_name (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Level1 TEXT,
  Level2 TEXT,
  Level3 TEXT,
  Level4 TEXT,
  Level5 TEXT,
  Content TEXT
)
""")

# 从第22行开始遍历 DataFrame 并插入数据
for index, row in df.iloc[22:].iterrows():
  # 将 NaN 值替换为空字符串
  row = row.fillna('')
  sql = """
  INSERT INTO your_table_name (Level1, Level2, Level3, Level4, Level5, Content) 
  VALUES (%s, %s, %s, %s, %s, %s)
  """
  val = (row['Level 1'], row['Level 2'], row['Level 3'], row['Level 4'], row['Level 5'], row['Content'])
  mycursor.execute(sql, val)

# 提交更改并关闭连接
mydb.commit()
mycursor.close()
mydb.close()

print("数据已成功插入数据库")