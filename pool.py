class Pool:
    def __init__(self, address='no', capacity_in_liters=0,
                 max_number_of_concurrent_visitors=0):
        self.address = address
        self.capacity_in_liters = capacity_in_liters
        self.max_number_of_concurrent_visitors = max_number_of_concurrent_visitors

    def __str__(self):
        return 'Pool(Address = ' + self.address + \
               ', Capacity = ' + str(self.capacity_in_liters) + \
                ', Visitors = ' + str(self.max_number_of_concurrent_visitors) + ')'
