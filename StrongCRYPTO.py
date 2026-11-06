
algorithms = ["MD5", "SHA1", "SHA256", "SHA512", "AES"]

weak_algorithms = ["MD5", "SHA1"]

for algorithm in algorithms:
    if algorithm in weak_algorithms:
        print(algorithm, "is WEAK! Replace it.")
    else:
        print(algorithm, "is STRONG.")
