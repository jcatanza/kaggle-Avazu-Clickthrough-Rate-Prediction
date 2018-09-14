
def shuffle_file(path, buff=10000000):
    import random
    from datetime import datetime
    start = datetime.now()

    with open(path) as f:
        for linecount, line in enumerate(f):
            pass
    f.close()

    print 'Found ' + str(linecount) + ' lines'
    shuffled = range(linecount+1)
    random.shuffle(shuffled)

    with open(path + '.shuffled', 'a') as fw:
        for k in range(len(shuffled)/buff+1):
            print '...processing from line ' + str(k*buff) + ' to line ' + str((k+1)*buff-1)

            segment = shuffled[k*buff:(k+1)*buff]
            segment_set = set(segment) # for quicker lookup

            db = {}
            with open(path) as fr:
                for j, line in enumerate(fr):
                    if j in segment_set:
                        db[str(j)] = line
            fr.close()

            for i in segment:
                fw.write(db[str(i)])
    fw.close()
    print 'Elapsed: ' + str(datetime.now() - start)


if __name__ == "__main__":
    shuffle_file('data/train')