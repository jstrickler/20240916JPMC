from logtimestampclass import LogTimestamp

@LogTimestamp
def spam(n):   # spam = show_timestamp(spam)
    print("SPAM!" * n)

@LogTimestamp
def ham():
    print("HAM!")

spam(5)
ham()

