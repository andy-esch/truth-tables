from collections import OrderedDict

#
## OR operator
#  | a & b | t | f |
#  |-------|-------|
#  |     t | t | f |
#  |-------|---|---|
#  |     f | f | f |
#  |-------|---|---|
#
## AND operator
#  | a | b | t | f |
#  |-------|-------|
#  |     t | t | t |
#  |-------|---|---|
#  |     f | t | f |
#  |-------|---|---|
#

class TruthTable:
    """Construct truth tables given arbitrary inputs."""
    all_elements = []
    variables = []
    operators = []

    def __init__(self, statement):
        self.statement = self.clean(statement)
        self.all_elements = self.break_up(self.statement)
        self.operators = self.get_operators()
        self.num_variables = len(self.all_elements) - len(self.operators)

    def summary(self):
        print('statement: %s' % self.statement)
        print('all_elements: %s' % str(self.all_elements))
        print('operators: %s' % str(self.operators))
        print('num_variables: %d' % self.num_variables)

    def clean(self, in_str):
        return in_str.strip().replace(' ','')

    def break_up(self, in_str):
        return list(in_str)

    def get_operators(self):
        ops = {'&', '|', '~'}
        ops_in = []
        for e in self.all_elements:
            if e in ops:
                ops_in.append(e)
        return ops_in

    def classify_operation(self):
        # for everything in self.all_elements, classify it
        operators = {'&', '|', '~'}
        od = OrderedDict([(e, 'v') if e not in operators
                                   else (e, 'o')
                                   for e in self.all_elements])
        print(str(od))
        return od

def print_table(elements):
    print('')

if __name__ == '__main__':

    t1 = 'a & b'
    t2 = 'a & (b | c)'
    tt = TruthTable(t1)

    tt.summary()
    tt.classify_operation()
