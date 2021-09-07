import sys
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('reddit relative scores').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.3' # make sure we have Spark 2.3+

comments_schema = types.StructType([
    types.StructField('archived', types.BooleanType()),
    types.StructField('author', types.StringType()),
    types.StructField('author_flair_css_class', types.StringType()),
    types.StructField('author_flair_text', types.StringType()),
    types.StructField('body', types.StringType()),
    types.StructField('controversiality', types.LongType()),
    types.StructField('created_utc', types.StringType()),
    types.StructField('distinguished', types.StringType()),
    types.StructField('downs', types.LongType()),
    types.StructField('edited', types.StringType()),
    types.StructField('gilded', types.LongType()),
    types.StructField('id', types.StringType()),
    types.StructField('link_id', types.StringType()),
    types.StructField('name', types.StringType()),
    types.StructField('parent_id', types.StringType()),
    types.StructField('retrieved_on', types.LongType()),
    types.StructField('score', types.LongType()),
    types.StructField('score_hidden', types.BooleanType()),
    types.StructField('subreddit', types.StringType()),
    types.StructField('subreddit_id', types.StringType()),
    types.StructField('ups', types.LongType()),
    #types.StructField('year', types.IntegerType()),
    #types.StructField('month', types.IntegerType()),
])


def main(in_directory, out_directory):
    comments = spark.read.json(in_directory, schema=comments_schema)
    comments = comments.cache()
    with_bins = comments.select(
            comments['subreddit'],
            comments['score']
        )
    grouped = with_bins.groupBy(comments['subreddit']).avg('score')
    averages_by_score = grouped.sort(grouped['avg(score)'])
    averages_by_score = averages_by_score.filter(grouped['avg(score)'] >0)
    averages_by_score = averages_by_score.hint('broadcast')
    #averages_by_score.show()
    #comments.show(n=5)
    # TODO

    joined_data = comments.join(averages_by_score, on = (comments['subreddit'] == averages_by_score['subreddit']) ,how = 'left').drop(averages_by_score.subreddit)
    joined_data = joined_data.cache()
    joined_data = joined_data.withColumn('relative_score', joined_data['score'] /joined_data['avg(score)'])
    highest = joined_data.groupBy("subreddit").max("relative_score")
    highest = highest.hint('broadcast')
    highest_data = joined_data.select(
                joined_data['subreddit'],
                joined_data['author'],
                joined_data['relative_score'].alias('rel_score')
            )
    highest_data = highest_data.cache()
    highest_data = highest_data.join(highest, on = ((highest_data['subreddit'] == highest['subreddit']) & (highest_data['rel_score'] == highest['max(relative_score)'])),how = 'right').drop(highest.subreddit)
    best_author = highest_data.drop('max(relative_score)')
    best_author.write.json(out_directory, mode='overwrite')
    #best_author.show()

if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)
