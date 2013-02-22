# Frequently used functions

def cfor(i, condition_func, update_func):
    while condition_func(i):
        yield i
        i = update_func(i)


# IO functions ===========================================

def read_listfile(fn):
    l = []
    fh = open(fn, 'r')
    for line in fh:
        i = line.rstrip()
        if i:
            l.append(i)
    return l

#--------------------------------------
def read_tablefile(fn, d='\t'):
    from csv import reader
    t = []
    fh = open(fn, 'rb')
    rd = reader(fh, delimiter=d)
    for row in rd:
        t.append(row)
    fh.close()
    return t

def read_tab_table(fn):
    return read_tablefile(fn)

def read_csv_table(fn):
    return read_tablefile(fn, ',')

#--------------------------------------
def write_tablefile(fn, tab, d='\t'):
    from csv import writer
    of = open(fn, 'wb')
    wt  = writer(of, delimiter=d)
    for i in tab:
        wt.writerow(i)
    return of.close()

def write_tab_table(fn, tab):
    return write_tablefile(fn, tab)

def write_csv_table(fn, tab):
    return write_tablefile(fn, tab, ',')

# http://code.activestate.com/recipes/189972-zip-and-pickle/
def pickle_dump(obj, fn, p=2):
    import cPickle, bz2
    f = bz2.BZ2File(fn, 'wb')
    f.write(cPickle.dumps(obj, p))
    f.close()
    return

def pickle_load(fn):
    import cPickle, bz2
    f = bz2.BZ2File(fn, 'rb')
    tmps = ""
    while 1:
        data = f.read()
        if data == "":
            break
        tmps += data
    obj = cPickle.loads(tmps)
    f.close()
    return obj

# Improved Datatypes ================================

def makehash():
    # autovivification like hash in perl
    # http://stackoverflow.com/questions/651794/whats-the-best-way-to-initialize-a-dict-of-dicts-in-python
    from collections import defaultdict
    return defaultdict(makehash)

#--------------------------------------
def list_dedup(iterable, idfunc=lambda x:x, nonFalse=False):
    # return a deduped order-preserving list
    # http://www.peterbe.com/plog/uniqifiers-benchmark
    seen = set()
    ddList = [seen.add(idfunc(x)) or x for x in iterable if idfunc(x) not in seen]
    if nonFalse: # 2012-09-11
        return filter(lambda x:x, ddList)
    else:
        return ddList




# Calculation =======================================
def calc_pvalue_halfnorm(v, sample):
    from scipy.stats import halfnorm
    ## half-normal survival function
    l, s = halfnorm.fit(sample)
    return halfnorm.sf(v, loc=l, scale=s)

def calc_pvalue_normal(v, sample):
    from scipy.stats import norm
    # normal distribution survival function ( 1 - cdf )
    l, s = norm.fit(sample)
    return norm.sf(v, loc=l, scale=s) * 2 # two-tail



# Misc ==============================================
# def __hidden_import():
    # for PyInstaller packaging
    # import scipy.sparse.csgraph._validation
