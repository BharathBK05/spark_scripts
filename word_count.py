words = sc.textFile("/home/bharubk05/words.txt").flatMap(lambda line:line.split(" "))
a = words.map(lambda word: (word,1))
b = a.reduceByKey(lambda a,b:a +b)
b.collect()