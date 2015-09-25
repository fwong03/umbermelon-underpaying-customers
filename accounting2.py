def find_underpaid(file_path):
    price_per_melon = 1.00
    log_file = open(file_path)

    for line in log_file:
        line = line.rstrip()
        cust_order_info = line.split("|")
        
        num_melons = int(cust_order_info[2])
        amount_paid = float(cust_order_info[3])

        expected_amount = num_melons * price_per_melon

        if expected_amount != amount_paid:
            customer_name = cust_order_info[1]
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, amount_paid, expected_amount)


find_underpaid("customer-orders.txt")