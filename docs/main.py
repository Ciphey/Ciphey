        """
        this method calls 1 level of decrypt
        The idea is that so long as decrypt doesnt return the plaintext
        to carry on decrypting all subsets of the text until we find one that does decrypt properly
        maybe only 2 levels

        The way probability distribution works is something like this:
        {Encoding: {"Binary": 0.137, "Base64": 0.09, "Hexadecimal": 0.00148}, Hashes: {"SHA1": 0.0906, "MD5": 0.>
        If an item in the dictionary is == 0.00 then write it down as 0.001
        Each parental dictiony object (eg encoding, hashing) is the actual object
        So each decipherment class has a parent that controls all of it
        sha1, sha256, md5, sha512 etc all belong to the object "hashes"
        Ciphey passes each probability to these classes
        Sort the dictionary
                                                                                                                >


        """
