def characteristicsProduct(data):
    items = data.findAll('dl', class_="ux-labels-values")

    dataItems = []

    for item in items:
        label = item.find('dt', class_="ux-labels-values__labels").text
        value = item.find('dd', class_="ux-labels-values__values").text

        _items = {
            "label" : label,
            "value" : value
        }

        dataItems.append(_items)

    return dataItems