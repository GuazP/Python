def main(args):
    print(empty_buckets(3))
    return 0

def empty_buckets(n):
    if n > 0:
        buckets = [[]]
        return buckets + empty_buckets(n-1)
    else:
        return []

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
