
def shuffle_file(path, buff=10000000, has_header=False):
    import random
    from datetime import datetime
    start = datetime.now()

    header = ''
    with open(path) as f:
        for linecount, line in enumerate(f):
            if linecount == 0 and has_header:
                header = line
    f.close()

    if has_header:
        linecount -= 1
    print 'Found ' + str(linecount) + ' lines'
    shuffled = range(linecount+1)
    random.shuffle(shuffled)

    with open(path + '.shuffled', 'a') as fw:
        if has_header:
            fw.write(header)

        for k in range(len(shuffled)/buff+1):
            print '...processing from line ' + str(k*buff) + ' to line ' + str((k+1)*buff-1)

            segment = shuffled[k*buff:(k+1)*buff]
            segment_set = set(segment) # for quicker lookup

            db = {}
            with open(path) as fr:
                for j, line in enumerate(fr):
                    if has_header:
                        if j == 0:
                            continue
                        j -= 1
                    if j in segment_set:
                        db[str(j)] = line
            fr.close()

            for i in segment:
                fw.write(db[str(i)])
    fw.close()
    print 'Elapsed: ' + str(datetime.now() - start)


if __name__ == "__main__":
    shuffle_file('data/train')