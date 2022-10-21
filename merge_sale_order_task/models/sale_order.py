from odoo import fields, models,api,_
from datetime import date
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
   _inherit='sale.order'

   def merge_orders(self):
    print("____________",self)
    name_list=[]
    insert_products=[]
    for customer_name in self:
        name_list.append(customer_name.partner_id.name)
        

    for record in self:
        if record.state=='sale' or name_list.count(name_list[0])!=len(name_list):
            raise ValidationError("Customers are not Same or You have selected The sale Order state")
        for so_line in record.order_line:
            insert_products.append((
            0,0,{'product_id':so_line.product_id.id,'product_uom_qty':so_line.product_uom_qty,'price_unit':so_line.price_unit})
            )
        record.action_cancel()  

    
    print("______________",insert_products)
    new_sale_order=self.env['sale.order'].create({
        'partner_id':record.partner_id.id
    })

          
    new_sale_order.write(
    {'order_line':insert_products,
    })

    new_sale_order.action_confirm()



