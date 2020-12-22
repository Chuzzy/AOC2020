from copy import copy

inp = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

inp = open('input21.txt', 'r').read().splitlines()

ingredients, allergens = [], []
for l in inp:
    ing, al = l.split('(')
    #print(ing, al)
    ingredients.append(ing[:-1].split(' '))
    allergens.append(al[9:-1].split(', '))

all_allergens = set(x for xs in allergens for x in xs)
all_ingredients = set(x for xs in ingredients for x in xs)
#print(*list(zip(ingredients, allergens)), sep = '\n')


all_poss = {al: copy(all_ingredients) for al in all_allergens}

#print(all_poss)
#print('\n\n')
#for allergen in all_allergens:
#    all_poss[allergen] = set.intersection()

for ing, als in zip(ingredients, allergens):
    for al in als:
        #print(al, set(ing))
        all_poss[al].intersection_update(set(ing))
        #print(all_poss[al], '\n')

never_allergen = all_ingredients - set.union(*all_poss.values())

count = 0
for ing in ingredients:
    for ing2 in never_allergen:
        count += ing.count(ing2)

print('Silver:', count)

to_be_done = set(all_poss.keys())

aller = {}

while len(to_be_done) > 0:
    rem_al, rem_ing = None, None

    print('\n\n', all_poss)
    for al in to_be_done:
        if len(all_poss[al]) == 1:
            rem_ing = all_poss[al].pop()
            rem_al = al
            
            #aller[al] = rem_ing
            #del(all_poss[al])

            break

    #print(rem)
    to_be_done.remove(rem_al)
    aller[rem_al] = rem_ing
    del(all_poss[al])

    for al2 in to_be_done:
        if rem_ing in all_poss[al2]:
            all_poss[al2].remove(rem_ing)

print(aller)

print(','.join([y[1] for y in sorted(aller.items(), key = lambda x: x[0])]))