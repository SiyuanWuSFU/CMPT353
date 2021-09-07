import sys
from pyspark.sql import SparkSession, functions, types, Row
import re
from pprint import pprint
spark = SparkSession.builder.appName('correlate logs').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
import math as m

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.3' # make sure we have Spark 2.3+

line_re = re.compile(r"^(\S+) - - \[\S+ [+-]\d+\] \"[A-Z]+ \S+ HTTP/\d\.\d\" \d+ (\d+)$")


def line_to_row(line):

    """
    Take a logfile line and return a Row object with hostname and bytes transferred. Return None if regex doesn't match.
    """
    #pprint(line)
    m = line_re.match(line)

    if m:


        return m.group(1,2)
    else:

        return None


def not_none(row):
    """
    Is this None? Hint: .filter() with it.
    """
    return row is not None


def create_row_rdd(in_directory):
    log_lines = spark.sparkContext.textFile(in_directory)
    rows = log_lines.map(line_to_row).filter(not_none)
    #pprint(rows.take(5))
    #print(rows)


    return rows
    # TODO: return an RDD of Row() objects


def main(in_directory):
    logs = spark.createDataFrame(create_row_rdd(in_directory),['host', 'size'])

    with_bins = logs.select(
            logs['host'],
            logs['size'].cast("int")
        )
    with_bins = with_bins.cache()
    #logs.filter(logs["size").cast("int").isNotNull()).show()
    total_size = with_bins.groupBy(with_bins['host']).sum("size")
    total_count = with_bins.groupBy(with_bins['host']).count()

    joined_data = total_size.join(total_count, on = (total_size['host'] == total_count['host']) ,how = 'left').drop(total_size.host)
    joined_data = joined_data.cache()
    # TODO: calculate r.
    joined_data = joined_data.withColumn('1', functions.lit(1))
    joined_data = joined_data.withColumn('xi', joined_data['count'])
    joined_data = joined_data.withColumn('x^2i', joined_data['count']*joined_data['count'])
    joined_data = joined_data.withColumn('yi', joined_data['sum(size)'])
    joined_data = joined_data.withColumn('y^2i', joined_data['sum(size)']*joined_data['sum(size)'])
    joined_data = joined_data.withColumn('xiyi', joined_data['count'] *joined_data['sum(size)'])
    joined_data =joined_data.groupby().sum()
    joined_data = joined_data.select(
            joined_data['sum(1)'],
            joined_data['sum(xi)'],
            joined_data['sum(x^2i)'],
            joined_data['sum(yi)'],
            joined_data['sum(y^2i)'],
            joined_data['sum(xiyi)']
        )
    #joined_data.show()
    sum_data = joined_data.first()
    #print(sum_data[0])
    n = sum_data[0]
    xi = sum_data[1]
    x2i = sum_data[2]
    yi = sum_data[3]
    y2i = sum_data[4]
    xiyi = sum_data[5]

    numerator = n*xiyi-xi*yi
    denominator = m.sqrt((n*x2i-(xi**2))*(n*y2i-(yi**2)))
    r = numerator/denominator # TODO: it isn't zero.

    print("r = %g\nr^2 = %g" % (r, r**2))


if __name__=='__main__':
    in_directory = sys.argv[1]
    main(in_directory)
