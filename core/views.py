from django.shortcuts import render

# Create your views here.

def home(request):
  api_infos = [
    {'name':'Auth'},
    {'name':'Vendors','gp':'/vendors/','gppd':'/vendors/vendor_id}/'},
    {'name':'Purchase Orders','gp':'/purchase_orders/','gppd':'/purchase_orders/{po_id}/'},
    {'name':'Historical Performance','gp':'/vendors/{vendor_id}/performance/','gppd':'/vendors/{vendor_id}/performance/{performance_id}/'},
    {'name':'Acknowledge'}
  ]
  return render(request,'index.html',context={'api_infos':api_infos})