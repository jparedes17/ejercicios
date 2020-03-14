def total(basket):
   results = {}
   count = 0
   while basket != []:
        books = []
        count += 1
        results[f'basket_{count}'] = {}
        for x in set(basket):
            basket.remove(x), books.append(x)
            results[f'basket_{count}'] = books
   baskets = []
   for item in results.keys():
        baskets.append(len(results[item]))
   while 3 in baskets and 5 in baskets:
        baskets.remove(5), baskets.remove(3)
        baskets.append(4), baskets.append(4)
   total = 0
   for item in baskets:
            if item == 1:
                total += 800
            elif item == 2:
               total += 1520
            elif item == 3:
               total += 2160
            elif item == 4:
                total += 2560
            elif item == 5:
                total += 3000
   return total
