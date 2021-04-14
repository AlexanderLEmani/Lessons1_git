catalog_item = {
	"type":"phone",
	"vendor":"Apple",
	"model":"Iphone 12",
	"price":37

}
print (catalog_item)

catalog_item['audio_jack']=False
catalog_item['price'] = 70

print (catalog_item['price'])


item_name = catalog_item['vendor']+ ' ' + format(catalog_item['price'])
print (item_name)

catalog_item.get('discount', 'Скидок нет!')
print ('discount' not in catalog_item)

del catalog_item['price']
print(catalog_item)