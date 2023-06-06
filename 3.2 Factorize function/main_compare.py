import time
import factorize
import multiprocessing_factorize


def main():
    data = (10_520_100, 850_000, 785_200, 55_210_000, 41_250_300, 62_417_895,
            78_500, 45_800, 65_210_333, 78_625, 415_950)

    start_factorize = time.time()
    factorize.factorize(*data)
    end = time.time()
    print("*" * 40)
    print(f"Program runtime: {end - start_factorize} sec\n\n")

    start_multi_pr = time.time()
    multiprocessing_factorize.factorize(*data)
    print("*" * 40)
    print(f"Multiprocessing factorize runtime: {time.time() - start_multi_pr} sec")


if __name__ == '__main__':
    main()
