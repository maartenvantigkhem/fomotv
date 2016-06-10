"""
Importing category tree from csv file
"""
import csv
import os
from main.models import Category

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fomotv.settings.local")


def csv_load_file(file_name):
    """
    Read from csv file
    """
    res = list()
    with open(file_name, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for r in reader:
            res.append(r)
    return res


def import_categories():
    res = csv_load_file(os.path.dirname(os.path.abspath (__file__)) + "/categories.csv")
    #print res

    parent_categories = dict()

    for r in res:
        if r[1] == '':
            continue
        level = int(r[1])

        cat = Category.objects.filter(pk=r[0])
        if cat.count() == 0:
            print cat
            item = Category()
            item.id = r[0]
            item.name = r[2]

            if level == 1:
                print item

                item = Category.add_root(name=r[2], id=r[0])
                parent_categories[level] = item
            else:
                item = parent_categories[level-1].add_child(name=r[2], id=r[0])
                parent_categories[level] = item
        else:
            parent_categories[level] = cat[0]




import_categories()
