class Sol:
    def fair_candy_swap(self,aliceSizes,bobSizes):
        sum_alice,sum_bob=sum(aliceSizes),sum(bobSizes)
        half=(sum_bob+sum_alice)//2
        diff_needed=(sum_bob-sum_alice)//2
        for a in aliceSizes:
            if a-diff_needed in bobSizes:
                return [a,a+diff_needed]
if __name__ == '__main__':
    p = Sol()
    print(p.fair_candy_swap(aliceSizes = [2], bobSizes = [1,3]))
