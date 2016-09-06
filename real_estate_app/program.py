import csv
import os
try:
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics

from real_estate_app.data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    # print(filename)
    data = load_file(filename)
    query_data(data)
    # print(data)


def print_header():
    print('----------------------------------')
    print('         REAL ESTATE APP')
    print('----------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row), row)
            # print("Bed count: {}, type: {}".format(row['beds'], type(row['beds'])))
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        # print(purchases[0].__dict__)
        return purchases

        # header = fin.readline().strip()
        # reader =csv.reader(fin, delimiter=',')
        # for row in reader:
        #     print(type(row), row)
        #     beds = row[4]
        #     print(beds)


# def load_file_basic(filename):
#    with open(filename, 'r', encoding='utf-8') as fin:
#        header = fin.readline().strip()
#        print('Found header: ' + header)
#
#        lines = []
#        for line in fin:
#            line_data = line.strip().split(',')
#            lines.append(line_data)
#
#        print(lines[:5])
# def get_price(p):
#     return p.price


def query_data(data): # : list[Purchase]):
    # data.sort(key=get_price)
    # most expensive house?
    data.sort(key= lambda p: p.price)

    high_purchase = data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths".format(high_purchase.price, high_purchase.beds, high_purchase.baths))
    # lease expensive house
    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".format(low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house?
    # prices = list()  # []
    # for pur in data:
    #     prices.append(pur.price)

    prices = (
        p.price  # projection or items
        for p in data  # the set to process
    )

    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(ave_price)))

    # average price of 2 bedroom houses


    prices = []
    baths = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print("The average home price of a two bedroom home is ${:,}".format(int(ave_price)))


if __name__ == '__main__':
    main()
