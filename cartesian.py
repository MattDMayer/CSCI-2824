class CartesianProduct:
    def get_cartesian_product(self,A,B,C):
        product = []
        for i in A:
            for j in B:
                for k in C:
                    product += list(i,j,k)
        return product