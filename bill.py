print("item price")
item_price=input()
print("quantity")
quantity=input()
print('gst %')
gst_percent=input()

sub_total=float(item_price)*float(quantity)
print('sub_total',sub_total)
gst=float(sub_total)*float(gst_percent)/100
print('gst',gst)
final_result=float(gst)+float(sub_total)
print('final_result',final_result)