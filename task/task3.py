from pyspark.sql import SparkSession
from pyspark.sql.functions import lit


import os
import sys
''' "Подготовительный" этап данного задания занял намного бОльший промежуток времени.
Без данных модулей и парамтеров окружения программа почему то не запускалась в принципе.
Кроме того, на новых версиях Python (12+) pyspark отказывался работать. Пришлось откатывать изменения.
Также, как оказалось, для запуска требуется версия Java 17 или 18+.
По умолчанию она у меня была 8й, и переключение в настройках самой Java ничего не давало, через VSC не удавалось заставить программу работать.
Пришлось ставить виртуальную среду с помощью Pycharm'a, перенастраивать его и только тогда все начало работать.
'''
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create a Spark session
spark = SparkSession.builder.appName("Task3").getOrCreate()
# Creating source dataframes
df1 = spark.createDataFrame([(1, "A", 4), (2, "B", 4), (3, "C", 0), (4, "D", 5)], ["id", "product", "id_cat"])
df2 = spark.createDataFrame([(4, "tools"), (5, "vegetables"), (6, "tea")], ["id", "category"])

#make tempo dataframes with filtered data
temp_df = df1.filter(df1.id_cat == 0)
temp_df2 = df1.join(df2, df1['id_cat'] == df2['id'], "inner")
#remove useless columns
temp_df2 = temp_df2.drop('id', 'id_cat')
temp_df = temp_df.drop('id', 'id_cat')
#add category column to make union works properly
temp_df = temp_df.withColumn("category", lit("null"))

#creating a result dataframe
result = temp_df2.union(temp_df)
result.show()
