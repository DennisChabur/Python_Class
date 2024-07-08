'''
2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

def find_duplicates(orig_list):
    return list(set([x for x in orig_list if orig_list.count(x) > 1]))

orig_list = [1, 1, 2, 3, 3, 4, 4, 4, 4]
print(find_duplicates(orig_list))


'''
3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии 
или из документации к языку.
'''

import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Yukio Mishima[a] (三島 由紀夫, Mishima Yukio), born Kimitake Hiraoka (平岡 公威, Hiraoka Kimitake, 
14 January 1925 – 25 November 1970), was a Japanese author, poet, playwright, actor, model, Shintoist, 
nationalist, and founder of the Tatenokai (楯の会, "Shield Society"). Mishima is considered one of the most 
important post-war stylists of the Japanese language. He was considered for the Nobel Prize in Literature
 
 five times in the 1960s—including in 1968, but that year the award went to his countryman and benefactor 
 Yasunari Kawabata.[6] His works include the novels Confessions of a Mask and The Temple of the Golden Pavilion,
  and the autobiographical essay Sun and Steel. Mishima's work is characterized by "its luxurious vocabulary and
   decadent metaphors, its fusion of traditional Japanese and modern Western literary styles, and its obsessive 
   assertions of the unity of beauty, eroticism and death",[7] according to author Andrew Rankin.

Mishima's political activities made him a controversial figure, which he remains in modern Japan.[8][9][10][11] 
From his mid-30s, Mishima's right-wing ideology and reactionary beliefs were increasingly evident.[11][12][13] 
He was proud of the traditional culture and spirit of Japan, and opposed what he saw as western-style materialism
, along with Japan's postwar democracy, globalism, and communism, worrying that by embracing these ideas the Japanese 
people would lose their "national essence" (kokutai) and their distinctive cultural heritage (Shinto and Yamato-damashii)
 to become a "rootless" people.[14][15][16][17] Mishima formed the Tatenokai for the avowed purpose of restoring 
 sacredness and dignity to the Emperor of Japan.[15][16][17] On 25 November 1970, Mishima and four members of his 
 militia entered a military base in central Tokyo, took its commandant hostage, and unsuccessfully tried to inspire 
 the Japan Self-Defense Forces to rise up and overthrow Japan's 1947 Constitution (which he called "a constitution
  of defeat").[17][14] After his speech and screaming of "Long live the Emperor!", he committed seppuku."""
print(top_10_words(text))

'''
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть 
один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''

def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {"вилка": 1,
        "ложка": 1,
        "вода": 3,
        "ботинки": 3,
        "куртка": 5,
        "камера": 4,
        "чайник": 4,
        "палатка": 12,
        "еда": 5,
        "джинсы": 4,
        "посуда": 2,
        }
max_weight = 10
print(pack_backpack(items, max_weight))