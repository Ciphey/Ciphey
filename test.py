def sortProbTable(probTable):
    """Sorts the probabiltiy table"""
    # for each object: prob table in dictionary
    maxOverall = 0
    maxDictPair = {}
    highestKey = None
    print(probTable)
    for key, value in probTable.items():
        print(key, value)
        maxLocal = 0
        # for each item in that table
        print(value)
        for key2, value2 in value.items():
            maxLocal = maxLocal + value2
        if maxLocal > maxOverall:
            # because the dict doesnt reset
            maxDictPair = {}
            
            maxOverall = maxLocal
            # so eventually, we get the maximum dict pairing?
            maxDictPair[key] = value
            highestKey = key
            print(f"\nChanging maxDictPair from {maxDictPair} to {highestKey}\n because local is {maxLocal}. The key / value are {key} {value}")
    # removes the highest key from the prob table
    del probTable[highestKey]
    # returns the max dict (at the start) with the prob table
    # this way, it should always work on most likely first.#
    d = {**maxDictPair, **probTable}
    print(f"\n\nThe maximum dict pair is {maxDictPair}")
    print("\n\n")
    print("################### d is:")
    print(d)
    return d

sortProbTable({"hash parent": {'md5': 0.01, 'sha1': 0.01, 'sha256': 0.01, 'sha512': 0.01}, "basic parent": {'caesar': 0.1266546}, 
'plaintext': {'plaintext': 0.22581327}, "encoding parent": {'ascii': 0.01, 'base64': 0.22110419, 'binary': 0.91, 'hexadecimal': 0.024687605, 'morse': 0.01, 'reverse': 0.01}})