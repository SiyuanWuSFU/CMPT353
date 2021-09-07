import sys
from pyspark.sql import SparkSession, functions, types, Row
import string, re
from pyspark.sql.functions import lower, col
  # regex that matches spaces and/or punctuation
spark = SparkSession.builder.appName('wordcount').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '3.1' # make sure we have Spark 2.3+



def main(in_directory, out_directory):
    wordbreak = r'[%s\s]+' % (re.escape(string.punctuation),)

    textFile = spark.read.text(in_directory)
    #textFile.show()


    wordfile = textFile.select(
        functions.explode(functions.split(lower('value'), wordbreak)).alias("word")
    )
    #wordfile.show()
    wordcount = wordfile.groupBy("word").count()
    wordcount_sort = wordcount.sort(wordcount['count'].desc(),wordcount['word'])
    #wordcount_sort.show()
    final_word = wordcount_sort.filter("word != ''")
    #final_word.show()
    final_word.write.csv(out_directory, mode='overwrite')
if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)
