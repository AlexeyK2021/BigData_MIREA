import scipy

if __name__ == '__main__':
    data = [97, 98, 109, 95, 97, 104]
    print(scipy.stats.chisquare(data))
