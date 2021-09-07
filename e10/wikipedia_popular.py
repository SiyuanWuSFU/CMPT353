import sys
from pyspark.sql import SparkSession, functions, types
import re

spark = SparkSession.builder.appName('popular').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.3' # make sure we have Spark 2.3+

wiki_schema = types.StructType([
    types.StructField('language', types.StringType()),
    types.StructField('title', types.StringType()),
    types.StructField('view_count', types.IntegerType()),
    types.StructField('size', types.IntegerType()),

])

def convert_name(file_path):

    x = re.findall("pagecounts-[0-9]+-[0-9]+", file_path)
    name = re.findall("[0-9]+-[0-9]{2}", x[0])
    return name[0]

def find_date(file_path):
    x = convert_name(file_path)
    y = re.findall("[0-9]{2}-", x)
    date = re.findall("[0-9]{2}", y[0])
    return date[0]

def find_hour(file_path):
    x = convert_name(file_path)
    y = re.findall("-[0-9]{2}", x)
    hour = re.findall("[0-9]{2}", y[0])
    return hour[0]






def main(in_directory, out_directory):
    path_to_hour = functions.udf(convert_name, returnType=types.StringType())
    get_date = functions.udf(find_date, returnType=types.StringType())
    get_hour = functions.udf(find_hour, returnType=types.StringType())




    #file_name.show()
    wikidata = spark.read.csv(in_directory,sep = ' ',schema=wiki_schema).withColumn('filename', functions.input_file_name())




    wikidata = wikidata.filter(wikidata.language == 'en')
    wikidata = wikidata.filter(wikidata.title != 'Main_Page')
    no_special = "^(?!Special:)"
    wikidata = wikidata.filter(wikidata.title.rlike(no_special))

    wikidata = wikidata.cache()
    list_title = wikidata.select(
    wikidata['view_count'],
    wikidata['title'],
    path_to_hour(wikidata.filename).alias('filename'),
    )


    find_max = wikidata.groupby('filename').max('view_count')
    max_join = find_max.select(
    find_max['max(view_count)'].alias('view_count1'),
    path_to_hour(find_max.filename).alias('filename1'))



    joined_data = max_join.join(list_title, on = (list_title['view_count'] == max_join['view_count1']) & (list_title['filename'] == max_join['filename1']),how = 'left')

    #joined_data = joined_data.drop("date").show()



    joined_data = joined_data.select(
    joined_data['filename'],
    joined_data['title'],
    joined_data['view_count']
    )
    joined_data.sort("filename")


    joined_data.write.csv(out_directory + '-output', mode='overwrite')
    #d = joined_data.groupby('filename').show()


















if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)
