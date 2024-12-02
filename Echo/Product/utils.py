from Customer.models import (TblgenAutonumbers,Tblcompany,Tblcustomer,TblgenParameters,
                             TblcmpDefaults,TblcustomerSettings,TblcustomerSetvalues)

from Supplier.models import (TblsupplierSettings,TblsupplierSetvalues,Tblsupplier)
import os
import random
from datetime import date, datetime,timedelta

from Product.models import (TblproductParametersSettings,TblproductParametertsSetvalues,
                            TblproductParametersCustomerSetvalues,TblproductProducts,)

class NextNo:
    def __init__(self):
        pass

    def get_next_no(self,table_name=None,field_name=None,companyid=None):
        previd_query = TblgenAutonumbers.objects.filter(companyid=companyid,
                                                field_name=field_name,
                                                table_name=table_name).values('autonumber').first()

        if previd_query:
            previd = previd_query['autonumber']
            next_id = previd + 1

            table_obj = TblgenAutonumbers.objects.get(field_name=field_name,
                                                    companyid=companyid,
                                                    table_name=table_name,
                                                    )

            table_obj.autonumber = next_id
            table_obj.save()
        else:
            print("No matching record found.")
        return previd
    
def get_random_image_path(folder_path):
    """
    This function reads a folder and returns the path to a random image within it.

    Args:
        folder_path (str): The path to the folder containing images.

    Returns:
        str: The path to a randomly chosen image file in the folder, 
            or None if the folder is empty or there are no image files.
    """

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter for image files (can be customized for specific extensions)
    image_files = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not image_files:
        # No image files found
        return None

    # Choose a random image from the filtered list
    random_image = random.choice(image_files)

    # Construct the full path to the image
    image_path = os.path.join(folder_path, random_image)

    return image_path

def bytes_to_boolean(data):
    if isinstance(data, bytes):
        return data == b'\x01'  # Convert bytes to boolean (adjust condition as per your data)
    else:
        return data
    

def GetProduct_params_value(companyid,settingid,productid,customerid=None):
    try:
        company = Tblcompany.objects.get(companyid = companyid)
        if settingid !='':
            if productid !='':
                try:
                    product = TblproductProducts.objects.get(companyid=company,productid = productid)
                    try:
                        setting = TblproductParametersSettings.objects.get(companyid=company, settingid = settingid)
                        if customerid !='':
                            try:
                                    customer = Tblcustomer.objects.get(companyid=company,businessid = customerid)
                                    
                                    try:
                                        customer_parameter_setting_set_val = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                                                                                                                        settingid=setting,
                                                                                                                        productid=product,
                                                                                                                        businessid=customer)
                                        
                                        if customer_parameter_setting_set_val.value:
                                            return [customer_parameter_setting_set_val.value]
                                    except TblproductParametersCustomerSetvalues.DoesNotExist:
                                        return [setting.default]
                            except Tblcustomer.DoesNotExist:
                                    return ["Customer ID Not Exists"]
                            else:
                               return  [TblproductParametersSettings.objects.get(companyid=company, settingid = settingid).default]
                        else:
                            try:
                                paremeter_setting_set_val = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                                                    settingid=setting,
                                                                                                    productid=product)
                                
                                if paremeter_setting_set_val.value:
                                    return [paremeter_setting_set_val.value]
                            except TblproductParametertsSetvalues.DoesNotExist:
                                return [setting.default]
                    except TblproductParametersSettings.DoesNotExist:
                        return ['Product Param Default:, <{}> has not been set up.  Please contact system administrator to set this up.'.format(settingid)]
                    # else:
                    #     if settingid in TblproductParametersSettings.objects.filter(companyid=company,iscustomer = 1).values_list('settingid',flat=True):
                    #         if customerid !='':
                    #             setting = TblproductParametersSettings.objects.get(companyid=company, settingid = settingid)
                    #             try:
                    #                 customer = Tblcustomer.objects.get(companyid=company,businessid = customerid)
                                    
                    #                 try:
                    #                     customer_parameter_setting_set_val = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                    #                                                                                                     settingid=setting,
                    #                                                                                                     productid=product,
                    #                                                                                                     businessid=customer)
                                        
                    #                     if customer_parameter_setting_set_val.value:
                    #                         return [customer_parameter_setting_set_val.value]
                    #                 except TblproductParametersCustomerSetvalues.DoesNotExist:
                    #                     return [setting.default]
                    #             except Tblcustomer.DoesNotExist:
                    #                 return ["Customer ID Not Exists"]
                    #         else:
                    #            return  [TblproductParametersSettings.objects.get(companyid=company, settingid = settingid).default]
                except TblproductProducts.DoesNotExist:
                    return ["Product ID Not Exists"]
            else:
                ["Productid is must be specified"]
        else:
            return ["Setting is is must be specified"]
    except Tblcompany.DoesNotExist:
        return ['Company ID Not Exists']
    
def GetCompany_params_value(companyid,paramid):
    try:
        company = Tblcompany.objects.get(companyid = companyid)
        if paramid !='':
            try:
                param = TblgenParameters.objects.get(companyid=company, paramid = paramid)
                try:
                    cmp_default = TblcmpDefaults.objects.get(companyid=company, paramid = paramid)
                    if cmp_default.value:
                        return [cmp_default.value]
                except TblcmpDefaults.DoesNotExist:
                    return [param.default]
            except TblgenParameters.DoesNotExist:
                return ['Company Param Default:, <{}> has not been set up.  Please contact system administrator to set this up.'.format(paramid)]
        else:
            return ["Param ID is must be specified"]
    except Tblcompany.DoesNotExist:
        return ['Company ID Not Exists']
    
def GetCustomer_params_value(companyid,customerid,settingid):
    try:
        company = Tblcompany.objects.get(companyid=companyid)
        if customerid!='':
            try:
                customer = Tblcustomer.objects.get(companyid=company,businessid=customerid)
                if settingid!='':
                    try:
                        setting = TblcustomerSettings.objects.get(companyid = company,settingid = settingid)
                        try:
                            customer_default = TblcustomerSetvalues.objects.get(companyid=company, businessid = customer,settingid = setting)
                            if customer_default.value:
                                return [customer_default.value]
                        except TblcustomerSetvalues.DoesNotExist:
                            return [setting.default]

                    except TblcustomerSettings.DoesNotExist:
                        return ['Customer Param Default:, <{}> has not been set up.  Please contact system administrator to set this up.'.format(settingid)]

            except Tblcustomer.DoesNotExist:
                return ["Customer ID Not Exists"]
        else:
            return ['Customer id must be specified']
    except Tblcompany.DoesNotExist:
        return ['Company ID Not Exists']
    

def GetSupplier_params_value(companyid,supplierid,settingid):
    try:
        company = Tblcompany.objects.get(companyid=companyid)
        if supplierid !='':
            try:
                supplier = Tblsupplier.objects.get(companyid = company,businessid=supplierid)
                if settingid!='':
                    try:
                        setting = TblsupplierSettings.objects.get(companyid=company,settingid=settingid)
                        try:
                            supplier_default = TblsupplierSetvalues.objects.get(companyid=company, businessid=supplier, settingid=setting)
                            if supplier_default.value:
                                return [supplier_default.value]
                        except TblsupplierSetvalues.DoesNotExist:
                            return [setting.default]

                    except TblsupplierSettings.DoesNotExist:
                        return ['Supplier Param Default:, <{}> has not been set up.  Please contact system administrator to set this up.'.format(settingid)]
            except Tblsupplier.DoesNotExist:
                return ["Supplier ID Not Exists"]
        else:
            return ["Supplier ID is must be specified"]
    except Tblcompany.DoesNotExist:
        return ['Company ID Not Exists']







@staticmethod
def parse_date(date_str):
    """Parse date from various formats to a date object."""
    allowed_formats = [
        "%m/%d/%Y",  # MM/DD/YYYY
        "%d/%m/%Y",  # DD/MM/YYYY
        "%Y-%m-%d",  # YYYY-MM-DD (ISO format)
        "%d-%m-%Y",  # DD-MM-YYYY
        "%m-%d-%Y"   # MM-DD-YYYY
        
    ]
    
    for date_format in allowed_formats:
        try:
            return datetime.strptime(date_str, date_format).date()
        except ValueError:
            continue
    
    # If none of the formats match, raise an error
    raise ValueError(f"Invalid date format: {date_str}. Expected formats: {', '.join(allowed_formats)}")
