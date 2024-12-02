import graphene
import json
from django.db import connection
from Product.utils import (bytes_to_boolean,GetProduct_params_value,GetCompany_params_value,
                           GetCustomer_params_value,GetSupplier_params_value)
from AppMessage.utils import JsonDataFrame

from .product_schema import (E4K_TblProductCategory1Node, E4K_TblProductCategory2Node,E4K_TblProductCategory3Node,
                             E4K_TblProductClassNode,E4K_TblproductColoursNode,E4K_TblproductCommoditycodesNode,
                             E4K_TblproductFitsNode,E4K_TblproductObsoleteTypesNode,E4K_TblproductParametersSettingsNode,
                             E4K_TblproductTypeofissueNode,E4K_TblproductUnitofissueNode,E4K_TblproductStockingTypesNode,
                             E4K_Tblproduct_ParametertsSetvalues_Node,E4K_TblproductPriceTypesNode,
                             E4K_TblproductPropertyTypesNode,E4K_TblproductSizeRangesNode,
                             E4K_TblproductSizeRangeValuesNode,E4K_TblProduct_ProductNode,
                             E4K_TblproductProduct_GalleryNode,E4K_TblproductProductPropertiesNode,
                             E4K_TblproductProductPropertyValuesNode,E4K_TblproductProductRepsNode,
                             E4K_TblproductProductPropertyLevelNode,E4K_TblProductProductPropertyLevelColmatrixNode,
                             E4K_TblproductProductPropertyMatrixNode,E4K_TblproductProductStockinglevelMatrixNode,
                             E4K_TblproductProductStockingtypeMatrixNode,E4K_TblproductProductVatcodeMatrixNode,
                             E4K_TblproductProductCostStandardMatrixNode,E4K_TblproductProductCostSupplierMatrixNode,
                             E4K_TblproductProductPriceCustomerMatrixNode,E4K_TblproductProductPriceStandardMatrixNode,
                             E4K_TblproductProductSuppliersWeekdaysNode,E4k_Tblcompany,E4K_TblwhoWarehouses,
                             E4K_TblproductPropertyLevelTypesNode,E4K_TblproductPropertyTypesValuesNode,
                             E4K_TblproductProductObsoleteMatrixNode,
                             E4K_Tblcustomer,E4k_TblSupplier,E4K_TblproductProductSupplierLevelNode,
                             E4K_TblProductProductSupplierLevelColmatrixNode,
                             E4K_TblproductProductSupplierMatrixNode,E4K_TblproductProductPriceStandardDateMatrixNode,
                             E4K_TblproductProductPriceStandardQtyMatrixNode,E4k_TblGen_CategoriesNode)

from .models import (TblproductProductPropertyMatrix,TblproductProducts,TblproductProductPropertyLevel,
                     TblproductProductPropertyLevelColmatrix,TblproductCategory1,TblproductCategory2,
                     TblproductCategory3,TblproductClass,TblproductColours,TblproductCommoditycodes,
                     TblproductFits,TblproductObsoleteTypes,TblproductParametersSettings,
                     TblproductPriceTypes,TblproductPropertyTypes,TblproductStockingTypes,
                     TblproductTypeofissue,TblproductUnitofissue,TblproductSizeRanges,TblproductSizeRangeValues,
                     TblproductProducts,TblproductParametertsSetvalues,TblproductProductGallery,
                     TblproductProductProperties,TblproductProductPropertyValues,TblproductProductReps,
                     TblproductProductSuppliers,TblproductProductStockinglevelMatrix,
                     TblproductProductStockingtypeMatrix,TblproductProductCostStandardMatrix,
                     TblproductProductCostSupplierMatrix,TblproductProductPriceCustomerMatrix,
                     TblproductProductPriceStandardMatrix,TblproductProductVatcodeMatrix,
                     TblproductProductSuppliersWeekdays,TblproductPropertyLevelTypes,
                     TblproductPropertyTypesValues,TblproductProductObsoleteMatrix,
                     TblproductProductSupplierLevel,
                     TblproductProductSupplierLevelColmatrix,TblproductProductSuppliersMatrix,
                     TblproductParametersCustomerSetvalues,TblproductProductPriceStandardDateMatrix,
                     TblproductProductPriceStandardQtyMatrix,TblgenCategories)

from Customer.models import (Tblcompany,TblbusSalesPeople,
                             Tblcustomer) 
from Supplier.models import (Tblsupplier,TblwhoWarehouses)
from graphene_django import DjangoObjectType



######################### Custom error
class CustomErrorType(graphene.ObjectType):
    message = graphene.String()

######################### Image api
class ImageType(graphene.ObjectType):
    url = graphene.String()


################################ Pagination
class PageInfoType(graphene.ObjectType):
    has_next_page = graphene.Boolean()
    end_cursor = graphene.String()

class ProductEdge(graphene.ObjectType):
    node = graphene.Field(E4K_TblProduct_ProductNode)

class E4k_TblProduct_Product_Page_Connection(graphene.ObjectType):
    edges = graphene.List(ProductEdge)
    page_info = graphene.Field(PageInfoType)

####################### TblbusSalesPeople

class E4K_TblbusSalesPeopleNode(DjangoObjectType):
    class Meta:
        model = TblbusSalesPeople
        fields = '__all__'
###########Product class
#################### Custome return Union
class E4k_TblProductCategory1Union(graphene.Union):
    class Meta:
        types = (E4K_TblProductCategory1Node, CustomErrorType)

class E4k_TblProductCategory2Union(graphene.Union):
    class Meta:
        types = (E4K_TblProductCategory2Node, CustomErrorType)

class E4k_TblProductCategory3Union(graphene.Union):
    class Meta:
        types = (E4K_TblProductCategory3Node, CustomErrorType)
    
class E4K_TblProductClassUnion(graphene.Union):
    class Meta:
        types = (E4K_TblProductClassNode, CustomErrorType)

class E4K_TblproductColoursUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductColoursNode, CustomErrorType)

class E4K_TblproductCommoditycodesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductCommoditycodesNode, CustomErrorType)

class E4K_TblproductFitsUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductFitsNode, CustomErrorType)

class E4K_TblproductObsoleteTypesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductObsoleteTypesNode, CustomErrorType)

class E4k_TblproductParametersSettingsUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductParametersSettingsNode, CustomErrorType)


class E4k_TblproductParametersSetValuesUnion(graphene.Union):
    class Meta:
        types = (E4K_Tblproduct_ParametertsSetvalues_Node, CustomErrorType)

class E4K_TblproductPriceTypesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductPriceTypesNode, CustomErrorType)

class E4K_TblproductPropertyTypesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductPropertyTypesNode, CustomErrorType)

############# Property types values 
class E4K_TblproductPropertyTypesValueUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductPropertyTypesValuesNode, CustomErrorType)

class E4K_TblproductSizeRangesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductSizeRangesNode, CustomErrorType)

class E4K_TblproductSizeRangeValuesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductSizeRangeValuesNode, CustomErrorType)

class E4K_TblproductStockingTypesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductStockingTypesNode, CustomErrorType)

class E4K_TblproductTypeOfIssueUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductTypeofissueNode, CustomErrorType)

class E4K_TblproductUnitofissueUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductUnitofissueNode, CustomErrorType)

class E4K_TblProductProductUnion(graphene.Union):
    class Meta:
        types = (E4K_TblProduct_ProductNode, CustomErrorType)

class E4K_TblProductGalleryUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProduct_GalleryNode, CustomErrorType)

class E4K_TblproductProductPropertiesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPropertiesNode, CustomErrorType)

class E4K_TblproductProductPropertyValuesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPropertyValuesNode, CustomErrorType)

class E4K_TblproductProductRepsUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductRepsNode, CustomErrorType)

class E4K_TblproductProductPropertyLevelUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPropertyLevelNode, CustomErrorType)

class E4K_TblproductProductPropertyLevelColmatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblProductProductPropertyLevelColmatrixNode, CustomErrorType)

class E4K_TblproductProductPropertyMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPropertyMatrixNode, CustomErrorType)

class E4K_TblproductProductStockinglevelMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductStockinglevelMatrixNode, CustomErrorType)

class E4K_TblproductProductStockingtypeMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductStockingtypeMatrixNode, CustomErrorType)

class E4K_TblproductProductObsoletetypeMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductObsoleteMatrixNode, CustomErrorType)

class E4K_TblproductProductVatcodeMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductVatcodeMatrixNode, CustomErrorType)

class E4K_TblproductProductCostStandardMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductCostStandardMatrixNode, CustomErrorType)

class E4K_TblproductProductCostSupplierMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductCostSupplierMatrixNode, CustomErrorType)

class E4K_TblproductProductPriceCustomerMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPriceCustomerMatrixNode, CustomErrorType)

class E4K_TblproductProductPriceStandardMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPriceStandardMatrixNode, CustomErrorType)

class E4K_TblproductProductPriceStandardDateMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPriceStandardDateMatrixNode, CustomErrorType)

class E4K_TblproductProductPriceStandardQtyMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductPriceStandardQtyMatrixNode, CustomErrorType)

class E4K_TblproductProductSuppliersWeekdaysUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductSuppliersWeekdaysNode, CustomErrorType)

###################### TblproductPropertyLevelTypes
class E4K_TblproductPropertyLevelTypesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductPropertyLevelTypesNode, CustomErrorType)

############################## E4K_TblbusSalesPeopleNode reps get
class E4k_TblBusSalesPeopleUnion(graphene.Union):
    class Meta:
        types = (E4K_TblbusSalesPeopleNode, CustomErrorType)

################# Company get
class E4K_TblCompanyUnion(graphene.Union):
    class Meta:
        types = (E4k_Tblcompany, CustomErrorType)

class E4K_TblWhoWarehousesUnion(graphene.Union):
    class Meta:
        types = (E4K_TblwhoWarehouses, CustomErrorType)

#################### E4k Tbl CUstomer get

class E4K_TblCustomerUnion(graphene.Union):
    class Meta:
        types = (E4K_Tblcustomer, CustomErrorType)

#################### E4k Tbl Supplier get

class E4K_TblSupplierUnion(graphene.Union):
    class Meta:
        types = (E4k_TblSupplier, CustomErrorType)

#################### E4k Tbl BusSalesPeople get

########################################### E4k Tbl Product Supplier level settings
class E4K_TblproductProductSupplierLevelSetUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductSupplierLevelNode, CustomErrorType)

######################### SupllierCol node
class E4K_TblproductProductSupplierLevelColMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblProductProductSupplierLevelColmatrixNode, CustomErrorType)

######################### Suplliermatrix node
class E4K_TblproductProductSupplierMatrixUnion(graphene.Union):
    class Meta:
        types = (E4K_TblproductProductSupplierMatrixNode, CustomErrorType)
       


#################### E4k Tbl gen categories

class E4K_TblgenCategoriesUnion(graphene.Union):
    class Meta:
        types = (E4k_TblGen_CategoriesNode, CustomErrorType)




class Query(graphene.ObjectType):
    fsk_all_product = graphene.List(E4K_TblProduct_ProductNode)

    ################ TblProduct product category Node
    e4k_tblproduct_product_category1 = graphene.List(E4k_TblProductCategory1Union, 
                                                     companyid=graphene.String())
    e4k_tblproduct_product_category2 = graphene.List(E4k_TblProductCategory2Union,
                                                     companyid=graphene.String())
    e4k_tblproduct_product_category3 = graphene.List(E4k_TblProductCategory3Union,
                                                     companyid=graphene.String())

    ############### TblProduct class
    e4k_tblproduct_product_class = graphene.List(E4K_TblProductClassUnion,
                                                 companyid=graphene.String())

    ############### tblproduct_colours
    e4k_tblproduct_product_colours = graphene.List(E4K_TblproductColoursUnion,
                                           companyid=graphene.String())
    
    ############## tblproduct_commoditycodes
    e4k_tblproduct_product_commoditycodes = graphene.List(E4K_TblproductCommoditycodesUnion,
                                                   companyid=graphene.String())
    
    ############# tblproduct_fits
    e4k_tblproduct_product_fits = graphene.List(E4K_TblproductFitsUnion,
                                           companyid=graphene.String())
    
    ################ tblproduct_obsolete_types
    e4k_tblproduct_product_obsolete_types = graphene.List(E4K_TblproductObsoleteTypesUnion,
                                                   companyid=graphene.String())
    
    ################ tblproduct_parameters_settings
    e4k_tblproduct_product_parameters_settings = graphene.List(of_type=graphene.JSONString,
                                                   companyid=graphene.String(),
                                                   settingid = graphene.String(),
                                                   productid = graphene.String(),
                                                   )
    
    e4k_tblproduct_product_parameters_customer_settings = graphene.List(of_type=graphene.JSONString,
                                                   companyid=graphene.String(),
                                                   settingid = graphene.String(),
                                                   productid = graphene.String(),
                                                   customerid = graphene.String(),
                                                   )

    
    #### ######### tblproduct_parameterts_setvalues
    e4k_tblproduct_product_parameterts_setvalues = graphene.List(E4k_TblproductParametersSetValuesUnion,
                                                   companyid=graphene.String(),
                                                   settingid = graphene.String(),
                                                   productid = graphene.String())
    ############## tblproduct_price_types
    e4k_tblproduct_product_price_types = graphene.List(E4K_TblproductPriceTypesUnion,
                                                   companyid=graphene.String(),
                                                   priceid = graphene.Int())
    
    ############## tblproduct_property_types
    e4k_tblproduct_product_property_types = graphene.List(E4K_TblproductPropertyTypesUnion,
                                                   companyid=graphene.String(),
                                                   propertyid = graphene.Int())
    
    ######################## E4K_TblproductPropertyTypesValueUnion tblproduct_property_types_values
    e4k_tblproduct_product_property_types_values = graphene.List(E4K_TblproductPropertyTypesValueUnion,
                                                   companyid=graphene.String(),
                                                   propertyid = graphene.Int(),
                                                   propertyvalue = graphene.String())

    

    ################### tblproduct_size_ranges E4K_TblproductSizeRangesUnion
    e4k_tblproduct_product_size_ranges = graphene.List(E4K_TblproductSizeRangesUnion,
                                                   companyid=graphene.String(),
                                                   rangeid = graphene.String())
    
    #####################  tblproduct_size_range_values
    
    e4k_tblproduct_product_size_range_values = graphene.List(E4K_TblproductSizeRangeValuesUnion,
                                                   companyid=graphene.String(),
                                                   rangeid = graphene.String(),
                                                   sizenumber = graphene.Int())
    
    ################# tblproduct_stocking_types
    e4k_tblproduct_product_stocking_types = graphene.List(E4K_TblproductStockingTypesUnion,
                                                   companyid=graphene.String(),
                                                   stockingtype = graphene.String())
    
    ################# tblproduct_typeofissue
    e4k_tblproduct_product_typeofissue = graphene.List(E4K_TblproductTypeOfIssueUnion,
                                                   companyid=graphene.String(),
                                                   issue_type = graphene.Int())
    
    ################### tblproduct_unitofissue
    e4k_tblproduct_product_unitofissue = graphene.List(E4K_TblproductUnitofissueUnion,
                                                   companyid=graphene.String(),
                                                   issue_units = graphene.Int())
    
    ############## tblproduct_products
    e4k_tblproduct_product_products = graphene.List(E4K_TblProductProductUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   first=graphene.Int(),
                                                    skip=graphene.Int())
    
    ################ tblproduct_product_gallery
    e4k_tblproduct_product_gallery = graphene.List(E4K_TblProductGalleryUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    ################## tblproduct_product_properties
    e4k_tblproduct_product_properties = graphene.List(E4K_TblproductProductPropertiesUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   propertyid = graphene.Int())

    ################# tblproduct_product_property_values
    e4k_tblproduct_product_property_values = graphene.List(E4K_TblproductProductPropertyValuesUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   propertyid = graphene.Int())
    
    ################# tblproduct_product_reps
    e4k_tblproduct_product_reps = graphene.List(E4K_TblproductProductRepsUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   repid = graphene.Int())
    
    ################### tblproduct_product_property_level
    e4k_tblproduct_product_property_level = graphene.List(E4K_TblproductProductPropertyLevelUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_property_level_colmatrix
    e4k_tblproduct_product_property_level_colmatrix = graphene.List(E4K_TblproductProductPropertyLevelColmatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_property_matrix
    e4k_tblproduct_product_property_matrix = graphene.List(E4K_TblproductProductPropertyMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_stockinglevel_matrix
    e4k_tblproduct_product_stockinglevel_matrix = graphene.List(E4K_TblproductProductStockinglevelMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_stockingtype_matrix
    e4k_tblproduct_product_stockingtype_matrix = graphene.List(E4K_TblproductProductStockingtypeMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    ###### tblproduct_product_obsoletetype_matrix
    e4k_tblproduct_product_obsoletetype_matrix = graphene.List(E4K_TblproductProductObsoletetypeMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_vatcode_matrix
    e4k_tblproduct_product_vatcode_matrix = graphene.List(E4K_TblproductProductVatcodeMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_cost_standard_matrix
    e4k_tblproduct_product_cost_standard_matrix = graphene.List(E4K_TblproductProductCostStandardMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_cost_supplier_matrix
    e4k_tblproduct_product_cost_supplier_matrix = graphene.List(E4K_TblproductProductCostSupplierMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   supplierid = graphene.String())
    
    
    #################### tblproduct_product_price_customer_matrix
    e4k_tblproduct_product_price_customer_matrix = graphene.List(E4K_TblproductProductPriceCustomerMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   customerid=graphene.String())
    
    #################### tblproduct_product_price_standard_matrix
    e4k_tblproduct_product_price_standard_matrix = graphene.List(E4K_TblproductProductPriceStandardMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    ###################################  tblproduct_product_price_standard_date_matrix
    e4k_tblproduct_product_price_standard_date_matrix = graphene.List(E4K_TblproductProductPriceStandardDateMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    ###################################  tblproduct_product_price_standard_qty_matrix
    e4k_tblproduct_product_price_standard_qty_matrix = graphene.List(E4K_TblproductProductPriceStandardQtyMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String())
    
    #################### tblproduct_product_suppliers_weekdays
    e4k_tblproduct_product_suppliers_weekdays = graphene.List(E4K_TblproductProductSuppliersWeekdaysUnion,
                                                   companyid=graphene.String(),
                                                   supplierid = graphene.String())
    
    ################################ Image api
    external_image = graphene.Field(ImageType, image_name=graphene.String())

    e4k_tblproduct_products_page = graphene.Field(E4k_TblProduct_Product_Page_Connection, 
                                                  companyid=graphene.String(),first=graphene.Int(), after=graphene.String())
    
    ######################## E4k_TblBusSalesPeopleUnion
    e4k_tblbus_sales_people = graphene.List(E4k_TblBusSalesPeopleUnion,companyid = graphene.String())
    
    ############### raw query
    e4k_tblproduct_product_all = graphene.List(of_type=graphene.JSONString,companyid=graphene.String())

    ########### comaony get 
    e4k_tblcompany_all = graphene.List(E4K_TblCompanyUnion)

    ########### Product Id Search
    e4k_tblproduct_product_search = graphene.String(companyid=graphene.String(),productid=graphene.String())

    ################ Tbl who warehouse get
    e4k_tblwhowarehouse = graphene.List(E4K_TblWhoWarehousesUnion,companyid=graphene.String(),
                                                                warehouseid=graphene.String())
    
    ####################### Get all customer 
    e4k_tblcustomer_all = graphene.List(E4K_TblCustomerUnion,companyid=graphene.String())

    ############# Get all supplier information
    e4k_tblsupplier_all = graphene.List(E4K_TblSupplierUnion,companyid=graphene.String())

    
    #################### E4K_TblproductPropertyLevelTypesUnion
    e4k_tblproduct_property_level_types = graphene.List(E4K_TblproductPropertyLevelTypesUnion,companyid=graphene.String())


    ############################ Product Supplier Level Settings
    ################### 
    e4k_tblproduct_product_supplier_level = graphene.List(E4K_TblproductProductSupplierLevelSetUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   supplierid = graphene.String())
    
    #################### tblproduct_product_supplier_level_colmatrix
    e4k_tblproduct_product_supplier_level_colmatrix = graphene.List(E4K_TblproductProductSupplierLevelColMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   supplierid = graphene.String())
    
    #################### tblproduct_product_property_matrix
    e4k_tblproduct_product_supplier_matrix = graphene.List(E4K_TblproductProductSupplierMatrixUnion,
                                                   companyid=graphene.String(),
                                                   productid = graphene.String(),
                                                   supplierid = graphene.String())
    
    ################################# Get paramter set default values based on product and settingid
    e4k_tblproduct_product_paramerter_default_value = graphene.List(of_type=graphene.String,
                                                                    companyid=graphene.String(),
                                                                    productid = graphene.String(),
                                                                    settingid = graphene.String(),
                                                                    customerid = graphene.String())
    
    ################################# Get paramter set default values based on companyid and params id

    e4k_tblcompany_params_value = graphene.List(of_type=graphene.String,
                                                companyid=graphene.String(),
                                                paramid = graphene.String())
    

    ################################# Get paramter set default values based on companyid and settingid for custoemr
    
    e4k_tblcustomer_params_default_value = graphene.List(of_type=graphene.String,
                                                companyid=graphene.String(),
                                                customerid = graphene.String(),
                                                settingid = graphene.String())
    
    ################################# Get paramter set default values based on companyid and settingid for supplier
    
    e4k_tblsupplier_params_default_value = graphene.List(of_type=graphene.String,
                                                companyid=graphene.String(),
                                                supplierid = graphene.String(),
                                                settingid = graphene.String())
    

    ############################################### E4K_TblgenCategoriesUnion
    e4k_tblgen_Categories = graphene.List(E4K_TblgenCategoriesUnion,
                                          companyid = graphene.String(),
                                          moduleid = graphene.String(),
                                          iscustomer = graphene.Boolean())


    @staticmethod
    def resolve_e4k_tblproduct_product_category1(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductCategory1.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
    
    @staticmethod
    def resolve_e4k_tblproduct_product_category2(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductCategory2.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_category3(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductCategory3.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
    
    @staticmethod
    def resolve_e4k_tblproduct_product_class(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductClass.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
    
    @staticmethod
    def resolve_e4k_tblproduct_product_colours(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductColours.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_commoditycodes(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductCommoditycodes.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_fits(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductFits.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_obsolete_types(self,info,companyid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            
            return TblproductObsoleteTypes.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
                
    @staticmethod
    def resolve_e4k_tblproduct_product_parameters_settings(self,info,companyid,settingid,productid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            look_return = []
            if productid !='':
                try:
                    product = TblproductProducts.objects.get(companyid = company,productid = productid)
                    if settingid != "":
                        try:
                            return TblproductParametersSettings.objects.get(companyid = company,
                                                                            settingid = settingid)
                            
                        except TblproductParametersSettings.DoesNotExist:
                            error = ErrorDataFrame.get_entry(id=39)
                            return [json.dumps({"message":error['errormessage']})]
                    else:
                        # lookup_data = TblproductParametersSettings.objects.filter(companyid = company,
                        #                                                           iscustomer = 0 ).order_by('category','seqno')
                        lookup_data = TblproductParametersSettings.objects.filter(companyid = company).order_by('category','seqno')
                        
                        for item in lookup_data:
                            
                            if item.settingid:
                                setting = TblproductParametersSettings.objects.get(companyid=company, settingid=item.settingid)
                                lookup_query = setting.lookup_table  # Assuming this is a SQL query string
                                try:
                                    setvalues_setting_compare_product = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                                                            settingid = setting,
                                                                                                                productid = product)
                                    
                                    if not lookup_query:
                                    
                                        if not setvalues_setting_compare_product.value:
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': None,
                                                    'lookup_table': lookup_query,
                                                    'default': item.default,
                                                    'seqno': item.seqno})
                                        else:

                                            item.lookup_value = setvalues_setting_compare_product.value
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': None,
                                                    'lookup_table': lookup_query,
                                                    'default': setvalues_setting_compare_product.value,
                                                    'seqno': item.seqno})
                                    else:
                                        with connection.cursor() as cursor:
                                            cursor.execute(lookup_query)
                                            rows = cursor.fetchall()
                                        
                                        result = [row[0] for row in rows]
                                        item.lookup_value = result
                                        if not setvalues_setting_compare_product.value:
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': result,
                                                    'lookup_table': lookup_query,
                                                    'default': item.default,
                                                    'seqno': item.seqno})
                                        else:

                                            item.lookup_value = setvalues_setting_compare_product.value
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': result,
                                                    'lookup_table': lookup_query,
                                                    'default': setvalues_setting_compare_product.value,
                                                    'seqno': item.seqno})



                                except TblproductParametertsSetvalues.DoesNotExist:
                                    if not lookup_query:
                                        item.lookup_value = None
                                        look_return.append({
                                            'settingid': item.settingid,
                                            'settingname': item.settingname,
                                            'category': item.category_id,
                                            'lookup_value': item.lookup_value,
                                            'lookup_table': lookup_query,
                                            'default': item.default,
                                            'seqno': item.seqno})
                                    else:
                                        with connection.cursor() as cursor:
                                            cursor.execute(lookup_query)
                                            rows = cursor.fetchall()
                                        
                                        result = [row[0] for row in rows]
                                        item.lookup_value = result
                                        look_return.append({
                                                'settingid': item.settingid,
                                                'settingname': item.settingname,
                                                'category': item.category_id,
                                                'lookup_value': result,
                                                'lookup_table': lookup_query,
                                                'default': item.default,
                                                'seqno': item.seqno})
                except TblproductProducts.DoesNotExist:
                    return [json.dumps({"message": "Product Id Not Found"})]
            else:
                if settingid != "":
                    try:
                        return TblproductParametersSettings.objects.get(companyid = company,
                                                                        settingid = settingid)
                        
                    except TblproductParametersSettings.DoesNotExist:
                        error = ErrorDataFrame.get_entry(id=39)
                        return [json.dumps({"message":error['errormessage']})]
                        #return [json.dumps({"message": "Setting Id Not Found"})]
                else:
                    # lookup_data = TblproductParametersSettings.objects.filter(companyid = company,
                    #                                                               iscustomer = 0 ).order_by('category','seqno')
                    lookup_data = TblproductParametersSettings.objects.filter(companyid = company).order_by('category','seqno')
                        
                    
                    for item in lookup_data:

                        if item.settingid:
                            setting = TblproductParametersSettings.objects.get(companyid=company, settingid=item.settingid)
                            lookup_query = setting.lookup_table  # Assuming this is a SQL query string
                            
                            if not lookup_query:
                                item.lookup_value = None
                                look_return.append({
                                    'settingid': item.settingid,
                                    'settingname': item.settingname,
                                    'category': item.category_id,
                                    'lookup_value': None,
                                    'lookup_table': lookup_query,
                                    'default': item.default,
                                    'seqno': item.seqno})
                            else:
                                with connection.cursor() as cursor:
                                    cursor.execute(lookup_query)
                                    rows = cursor.fetchall()
                                
                                result = [row[0] for row in rows]
                                item.lookup_value = result
                                look_return.append({
                                        'settingid': item.settingid,
                                        'settingname': item.settingname,
                                        'category': item.category_id,
                                        'lookup_value': result,
                                        'lookup_table': lookup_query,
                                        'default': item.default,
                                        'seqno': item.seqno})

            return look_return
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [json.dumps({"message":error['errormessage']})]
           #return [json.dumps({"message": "Company Id Not Found"})]
        

    
    ########### paramters settinge look up value

    @staticmethod
    def resolve_e4k_tblproduct_product_parameters_customer_settings(self,info,companyid,settingid,productid,customerid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            look_return = []
            if productid !='':
                try:
                    product = TblproductProducts.objects.get(companyid = company,productid = productid)
                    if settingid != "":
                        try:
                            return TblproductParametersSettings.objects.get(companyid = company,
                                                                            settingid = settingid)
                            
                        except TblproductParametersSettings.DoesNotExist:
                            error = ErrorDataFrame.get_entry(id=39)
                            return [json.dumps({"message":error['errormessage']})]
                    else:
                        lookup_data = TblproductParametersSettings.objects.filter(companyid = company,
                                                                                  iscustomer = 1 ).order_by('category','seqno')
                        
                        customer = Tblcustomer.objects.get(companyid=company,
                                                            businessid = customerid)
                        
                        for item in lookup_data:
                            
                            if item.settingid:
                                setting = TblproductParametersSettings.objects.get(companyid=company, settingid=item.settingid)
                                lookup_query = setting.lookup_table  # Assuming this is a SQL query string
                                
                                try:
                                    setvalues_setting_compare_product = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                                                                                                                settingid = setting,
                                                                                                                productid = product,
                                                                                                                businessid = customer)
                                    if not lookup_query:
                                    
                                        if not setvalues_setting_compare_product.value:
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': None,
                                                    'lookup_table': lookup_query,
                                                    'default': item.default,
                                                    'seqno': item.seqno})
                                        else:

                                            item.lookup_value = setvalues_setting_compare_product.value
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': None,
                                                    'lookup_table': lookup_query,
                                                    'default': setvalues_setting_compare_product.value,
                                                    'seqno': item.seqno})
                                    else:
                                        with connection.cursor() as cursor:
                                            cursor.execute(lookup_query)
                                            rows = cursor.fetchall()
                                        
                                        result = [row[0] for row in rows]
                                        item.lookup_value = result
                                        if not setvalues_setting_compare_product.value:
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': result,
                                                    'lookup_table': lookup_query,
                                                    'default': item.default,
                                                    'seqno': item.seqno})
                                        else:

                                            item.lookup_value = setvalues_setting_compare_product.value
                                            look_return.append({
                                                    'settingid': item.settingid,
                                                    'settingname': item.settingname,
                                                    'category': item.category_id,
                                                    'lookup_value': result,
                                                    'lookup_table': lookup_query,
                                                    'default': setvalues_setting_compare_product.value,
                                                    'seqno': item.seqno})



                                except TblproductParametersCustomerSetvalues.DoesNotExist:
                                    if not lookup_query:
                                        item.lookup_value = None
                                        look_return.append({
                                            'settingid': item.settingid,
                                            'settingname': item.settingname,
                                            'category': item.category_id,
                                            'lookup_value': item.lookup_value,
                                            'lookup_table': lookup_query,
                                            'default': item.default,
                                            'seqno': item.seqno})
                                    else:
                                        with connection.cursor() as cursor:
                                            cursor.execute(lookup_query)
                                            rows = cursor.fetchall()
                                        
                                        result = [row[0] for row in rows]
                                        item.lookup_value = result
                                        look_return.append({
                                                'settingid': item.settingid,
                                                'settingname': item.settingname,
                                                'category': item.category_id,
                                                'lookup_value': result,
                                                'lookup_table': lookup_query,
                                                'default': item.default,
                                                'seqno': item.seqno})
                except TblproductProducts.DoesNotExist:
                    return [json.dumps({"message": "Product Id Not Found"})]
            else:
                if settingid != "":
                    try:
                        return TblproductParametersSettings.objects.get(companyid = company,
                                                                        settingid = settingid)
                        
                    except TblproductParametersSettings.DoesNotExist:
                        error = ErrorDataFrame.get_entry(id=39)
                        return [json.dumps({"message":error['errormessage']})]
                        #return [json.dumps({"message": "Setting Id Not Found"})]
                else:
                    lookup_data = TblproductParametersSettings.objects.filter(companyid = company,
                                                                                  iscustomer = 1 ).order_by('category','seqno')
                        
                    
                    for item in lookup_data:

                        if item.settingid:
                            setting = TblproductParametersSettings.objects.get(companyid=company,
                                                                               settingid=item.settingid)
                            lookup_query = setting.lookup_table  # Assuming this is a SQL query string
                            
                            if not lookup_query:
                                item.lookup_value = None
                                look_return.append({
                                    'settingid': item.settingid,
                                    'settingname': item.settingname,
                                    'category': item.category_id,
                                    'lookup_value': None,
                                    'lookup_table': lookup_query,
                                    'default': item.default,
                                    'seqno': item.seqno})
                            else:
                                with connection.cursor() as cursor:
                                    cursor.execute(lookup_query)
                                    rows = cursor.fetchall()
                                
                                result = [row[0] for row in rows]
                                item.lookup_value = result
                                look_return.append({
                                        'settingid': item.settingid,
                                        'settingname': item.settingname,
                                        'category': item.category_id,
                                        'lookup_value': result,
                                        'lookup_table': lookup_query,
                                        'default': item.default,
                                        'seqno': item.seqno})

            return look_return
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [json.dumps({"message":error['errormessage']})]
           #return [json.dumps({"message": "Company Id Not Found"})]
       

    

        
    @staticmethod
    def resolve_e4k_tblproduct_product_parameterts_setvalues(self,info,companyid,settingid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            product = TblproductProducts.objects.get(companyid = company,productid = productid)
            setting = TblproductParametersSettings.objects.get(companyid = company,
                                                                    settingid = settingid)
            try:
                return TblproductParametertsSetvalues.objects.filter(companyid = company,
                                                                settingid = setting,
                                                                productid = product)
                
            except TblproductParametertsSetvalues.DoesNotExist:
                return [CustomErrorType(message="Set Values Not Found")]
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except TblproductParametersSettings.DoesNotExist:
            return [CustomErrorType(message="Setting Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_price_types(self,info,companyid,priceid):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            if priceid is not None:
                    price =  TblproductPriceTypes.objects.filter(companyid = company,
                                                                    priceid = priceid)
                    if len(price) == 0:
                        error = ErrorDataFrame.get_entry(id=47)
                        return [CustomErrorType(message=error['errormessage'])]
                    return price
            else:
                return TblproductPriceTypes.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           error = ErrorDataFrame.get_entry(id=1)
           return [CustomErrorType(message=error['errormessage'])]
        

    ###################### Not Include Error Message JSon FIle####################################
    @staticmethod
    def resolve_e4k_tblproduct_product_property_types(self,info,companyid,propertyid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if propertyid is not None:
                    property =  TblproductPropertyTypes.objects.filter(companyid = company,
                                                                    propertyid = propertyid)
                    if len(property) == 0:
                        return [CustomErrorType(message="Property Id Not Found")]
                    return property
            else:
                return TblproductPropertyTypes.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_size_ranges(self,info,companyid,rangeid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if rangeid !='':
                    range =  TblproductSizeRanges.objects.filter(companyid = company,
                                                                    rangeid = rangeid)
                    if len(range) == 0:
                        return [CustomErrorType(message="Range Id Not Found")]
                    return range
            else:
                return TblproductSizeRanges.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_size_range_values(self,info,companyid,rangeid,sizenumber):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if rangeid !='':
                try:
                    sizerange = TblproductSizeRanges.objects.get(companyid=company,rangeid=rangeid)
                    if sizenumber is not None:
                        range =  TblproductSizeRangeValues.objects.filter(companyid = company,
                                                                        rangeid = sizerange,
                                                                        size_number = sizenumber)
                        if len(range) == 0:
                            return [CustomErrorType(message="sizenumber Not Found Range id not found")]
                        return range
                    else:
                        return TblproductSizeRangeValues.objects.filter(companyid = company,
                                                                        rangeid = sizerange)
                except TblproductSizeRanges.DoesNotExist:
                    return [CustomErrorType(message="Range Id Not Found")]
            else:
                return TblproductSizeRangeValues.objects.filter(companyid = company).order_by('size_number')
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
    

    @staticmethod
    def resolve_e4k_tblproduct_product_stocking_types(self,info,companyid,stockingtype):
        try:
            ErrorDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid = companyid)
            if stockingtype !="":
                    stocking =  TblproductStockingTypes.objects.filter(companyid = company,
                                                                    stockingtype = stockingtype)
                    if len(stocking) == 0:
                        error = ErrorDataFrame.get_entry(id=14)
                        return [CustomErrorType(message=error['errormessage'])]
                        # return [CustomErrorType(message="Stocking Type Not Found")]
                    return stocking
            else:
                return TblproductStockingTypes.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            error = ErrorDataFrame.get_entry(id=1)
            return [CustomErrorType(message=error['errormessage'])]
           #return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_typeofissue(self,info,companyid,issue_type):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if issue_type is not None:
                    type =  TblproductTypeofissue.objects.filter(companyid = company,
                                                                    issue_type = issue_type)
                    if len(type) == 0:
                        return [CustomErrorType(message="Issue Type Id Not Found")]
                    return type
            else:
                return TblproductTypeofissue.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
    
    @staticmethod
    def resolve_e4k_tblproduct_product_unitofissue(self,info,companyid,issue_units):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if issue_units is not None:
                    units =  TblproductUnitofissue.objects.filter(companyid = company,
                                                                    issue_units = issue_units)
                    if len(units) == 0:
                        return [CustomErrorType(message="Issue Units Id Not Found")]
                    return units
            else:
                return TblproductUnitofissue.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
    
    @staticmethod
    def resolve_e4k_tblproduct_product_products(self,info,companyid,productid,first, skip):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid !='':
                    product =  TblproductProducts.objects.filter(companyid = company,
                                                                    productid = productid)
                    if len(product) == 0:
                        return [CustomErrorType(message="Product Id Not Found")]
                    
                    
                    return product
            else:
                product = TblproductProducts.objects.filter(companyid = company)
                if first is not None:
                    product = product[:first]
                if skip is not None:
                    product = product[skip:]
                return product
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_gallery(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid !="":
                    try:
                        product =  TblproductProducts.objects.get(companyid = company,
                                                                    productid = productid)
                        gallery =  TblproductProductGallery.objects.filter(companyid = company,
                                                                        productid = product)
                        if len(gallery) == 0:
                            return [CustomErrorType(message="Product Id Not Found")]
                        return gallery
                    except TblproductProducts.DoesNotExist:
                        return [CustomErrorType(message="Product Id Not Found")]
            else:
                return TblproductProductGallery.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_properties(self,info,companyid,productid,propertyid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            product = TblproductProducts.objects.get(productid = productid)
            if propertyid is not None:
                    try:
                        property =  TblproductPropertyTypes.objects.get(companyid = company,
                                                                        propertyid = propertyid)
                        product_prop = TblproductProductProperties.objects.filter(companyid = company,
                                                                               productid = product,
                                                                               propertyid = property)
                        if len(product_prop) == 0:
                            return [CustomErrorType(message="Product Property Not Found")]
                        return product_prop
                    except TblproductPropertyTypes.DoesNotExist:
                        return [CustomErrorType(message="Property Id Not Found")]
            else:
                return TblproductProductProperties.objects.filter(companyid = company,productid = product).order_by('seqno')
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_property_values(self,info,companyid,productid,propertyid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            product = TblproductProducts.objects.get(companyid=company,
                                                     productid = productid)
            if propertyid is not None:
                property = TblproductPropertyTypes.objects.get(companyid=company,
                                                               propertyid = propertyid)
                try:
                    product_prop = TblproductProductProperties.objects.filter(companyid = company,
                                                                        productid = product,
                                                                        propertyid = property)
                    product_property_values = TblproductProductPropertyValues.objects.filter(companyid = company,
                                                                                    product_propid =product_prop[0].product_propid).order_by('product_prop_value')
                    
                                                                                            
                    if len(product_property_values) == 0:
                        return [CustomErrorType(message="Product Property Values Not Found")]
                    return product_property_values
                except TblproductProductProperties.DoesNotExist:
                    return [CustomErrorType(message="Product Property Id Not Found")]
            else:
                product_prop = TblproductProductProperties.objects.filter(companyid = company,
                                                                        productid = product)
                product_propid = [product.product_propid for product in product_prop]
                product_property_values = TblproductProductPropertyValues.objects.filter(companyid = company,
                                                                                    product_propid__in =product_propid)

                return product_property_values
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        except TblproductPropertyTypes.DoesNotExist:
            return [CustomErrorType(message="Property Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_reps(self,info,companyid,productid,repid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            product = TblproductProducts.objects.get(companyid=company,
                                                     productid = productid)
            if repid is not None:
                try:
                    rep = TblbusSalesPeople.objects.get(companyid=company,
                                                    repid = repid)
                    try:
                        product_rep = TblproductProductReps.objects.filter(companyid = company,
                                                                            productid = product,
                                                                            repid = rep)
                        if len(product_rep) == 0:
                            return [CustomErrorType(message="Product Rep Not Found")]
                        return product_rep
                    except TblproductProductReps.DoesNotExist:
                        return [CustomErrorType(message="Product Rep Id Not Found")]
                except TblbusSalesPeople.DoesNotExist:
                    return [CustomErrorType(message="Rep Id Not Found")]
            else:
                return TblproductProductReps.objects.filter(companyid = company,
                                                            productid = product)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_property_level(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid !='':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    prop_level = TblproductProductPropertyLevel.objects.filter(companyid = company,
                                                                productid = product)
                    if len(prop_level) == 0:
                        return [CustomErrorType(message="Product Property Level Data Not Found")]

                    return prop_level
                except TblproductProductPropertyLevel.DoesNotExist:
                    return [CustomErrorType(message="Product Property Level Not Found")]
            else:
                return TblproductProductPropertyLevel.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    

    @staticmethod
    def resolve_e4k_tblproduct_product_property_level_colmatrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    level_col = TblproductProductPropertyLevelColmatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(level_col) == 0:
                        return [CustomErrorType(message="Product Property Level Col Matrix Data Not Found")]
                    return level_col
                except TblproductProductPropertyLevelColmatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Property Level Col Matrix Not Found")]
            else:
                return TblproductProductPropertyLevelColmatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_property_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    prop_matrix = TblproductProductPropertyMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(prop_matrix) == 0:
                        return [CustomErrorType(message="Product Property Matrix Data Not Found")]
                    return prop_matrix
                except TblproductProductPropertyMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Property Matrix Not Found")]
            else:
                return TblproductProductPropertyMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_stockinglevel_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    stock_level = TblproductProductStockinglevelMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(stock_level) == 0:
                        return [CustomErrorType(message="Product Stocking Level Matrix Data Not Found")]
                    return stock_level
                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Stocking Level Matrix Not Found")]
            else:
                return TblproductProductStockinglevelMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    

    @staticmethod
    def resolve_e4k_tblproduct_product_stockingtype_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    stock_type = TblproductProductStockingtypeMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(stock_type) == 0:
                        return [CustomErrorType(message="Product Stocking Type Matrix Data Not Found")]
                    return stock_type
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Stocking Type Matrix ID Not Found")]
            else:
                return TblproductProductStockingtypeMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    

    ##################### Obsolete type get method
    @staticmethod
    def resolve_e4k_tblproduct_product_obsoletetype_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    obsolete_type = TblproductProductObsoleteMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(obsolete_type) == 0:
                        return [CustomErrorType(message="Product Obsolete Type Matrix Data Not Found")]
                    return obsolete_type
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Obsolete Type Matrix ID Not Found")]
            else:
                return TblproductProductObsoleteMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]

    

    @staticmethod
    def resolve_e4k_tblproduct_product_vatcode_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    vat_code = TblproductProductVatcodeMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(vat_code) == 0:
                        return [CustomErrorType(message="Product Vat Code Matrix Data Not Found")]
                    return vat_code
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Vat Code Matrix Not Found")]
            else:
                return TblproductProductVatcodeMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_cost_standard_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    cost_standard = TblproductProductCostStandardMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(cost_standard) == 0:
                        return [CustomErrorType(message="Product Cost Standard Matrix No Data")]
                    return cost_standard
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Cost Standard Matrix Not Found")]
            else:
                return TblproductProductCostStandardMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_cost_supplier_matrix(self,info,companyid,productid,supplierid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                                productid = productid)
                if supplierid!='':
                    try:
                        
                        supplier = Tblsupplier.objects.get(companyid=company,
                                                            businessid = supplierid)
                        try:
                            cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid = company,
                                                                        productid = product,
                                                                        businessid = supplier)
                            if len(cost_supplier) == 0:
                                return [CustomErrorType(message="Product Cost Supplier Matrix No Data")]
                            return cost_supplier
                        except TblproductProductCostSupplierMatrix.DoesNotExist:
                            return [CustomErrorType(message="Product Cost Supplier Matrix Not Found")]
                    except TblproductProducts.DoesNotExist:
                        return [CustomErrorType(message="Product Id Not Found")]
                    except Tblsupplier.DoesNotExist:
                        return [CustomErrorType(message="Supplier Id Not Found")]
                else:
                    return TblproductProductCostSupplierMatrix.objects.filter(companyid = company,
                                                                productid = product)
            else:
                if supplierid !='':
                    try:
                        supplier = Tblsupplier.objects.get(companyid=company,
                                                            businessid = supplierid)
                        try:
                            cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid = company,
                                                                        businessid = supplier)
                            if len(cost_supplier) == 0:
                                return [CustomErrorType(message="Product Cost Supplier Matrix No Data")]
                            return cost_supplier
                        except TblproductProductCostSupplierMatrix.DoesNotExist:
                            return [CustomErrorType(message="Product Cost Supplier Matrix Not Found")]
                    except Tblsupplier.DoesNotExist:
                        return [CustomErrorType(message="Supplier Id Not Found")]
                else:
                    return TblproductProductCostSupplierMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_price_customer_matrix(self,info,companyid,productid,customerid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                if customerid!='':
                    try:
                        
                        customer = Tblcustomer.objects.get(companyid=company,
                                                            businessid = customerid)
                        try:
                            price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid = company,
                                                                        productid = product,
                                                                        businessid = customer)
                            if len(price_customer) == 0:
                                return [CustomErrorType(message="Product Price Customer Matrix No Data")]
                            return price_customer
                        except TblproductProductPriceCustomerMatrix.DoesNotExist:
                            return [CustomErrorType(message="Product Price Customer Matrix Not Found")]
                    except Tblcustomer.DoesNotExist:
                        return [CustomErrorType(message="Customer Id Not Found")]
                else:
                    cus_price = TblproductProductPriceCustomerMatrix.objects.filter(companyid = company,
                                                                productid = product)

                    if len(cus_price) == 0:
                                return [CustomErrorType(message="Product Price Customer Matrix No Data")]
                    return cus_price

                     
            else:
                if customerid!='':
                    try:
                        customer = Tblcustomer.objects.get(companyid=company,
                                                            businessid = customerid)
                        try:
                            price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid = company,
                                                                        businessid = customer)
                            if len(price_customer) == 0:
                                return [CustomErrorType(message="Product Price Customer Matrix No Data")]
                            return price_customer
                        except TblproductProductPriceCustomerMatrix.DoesNotExist:
                            return [CustomErrorType(message="Product Price Customer Matrix Not Found")]
                    except Tblcustomer.DoesNotExist:
                        return [CustomErrorType(message="Customer Id Not Found")]
                else:
                    return TblproductProductPriceCustomerMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_price_standard_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    price_standard = TblproductProductPriceStandardMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(price_standard) == 0:
                        return [CustomErrorType(message="Product Price Standard Matrix No Data")]
                    return price_standard
                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Price Standard Matrix Not Found")]
            else:
                return TblproductProductPriceStandardMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_price_standard_date_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    price_standard = TblproductProductPriceStandardDateMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(price_standard) == 0:
                        return [CustomErrorType(message="Product Price Standard Date Matrix No Data")]
                    return price_standard
                except TblproductProductPriceStandardDateMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Price Standard Date Matrix Not Found")]
            else:
                return TblproductProductPriceStandardDateMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        

    @staticmethod
    def resolve_e4k_tblproduct_product_price_standard_qty_matrix(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if productid!= '':
                product = TblproductProducts.objects.get(companyid=company,
                                                        productid = productid)
                try:
                    price_standard = TblproductProductPriceStandardQtyMatrix.objects.filter(companyid = company,
                                                                productid = product)
                    if len(price_standard) == 0:
                        return [CustomErrorType(message="Product Price Standard Qty Matrix No Data")]
                    return price_standard
                except TblproductProductPriceStandardQtyMatrix.DoesNotExist:
                    return [CustomErrorType(message="Product Price Standard Qty Matrix Not Found")]
            else:
                return TblproductProductPriceStandardQtyMatrix.objects.filter(companyid = company)
        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_suppliers_weekdays(self,info,companyid,supplierid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if supplierid!='':
                    try:  
                        supplier = Tblsupplier.objects.get(companyid=company,
                                                            businessid = supplierid)
                        try:
                            suppliers_weekdays = TblproductProductSuppliersWeekdays.objects.filter(companyid = company,
                                                                                supplierid = supplier)
                            if len(suppliers_weekdays) == 0:
                                return [CustomErrorType(message="Product Suppliers Weekdays No Data")]
                            return suppliers_weekdays
                        except TblproductProductSuppliersWeekdays.DoesNotExist:
                            return [CustomErrorType(message="Product Suppliers Weekdays Not Found")]
                    except Tblsupplier.DoesNotExist:
                        return [CustomErrorType(message="Supplier Id Not Found")]
            else:
                    return TblproductProductSuppliersWeekdays.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
                


    @staticmethod
    def resolve_fsk_all_product(self, info, **kwargs):
        return TblproductProducts.objects.all()
    

    ########### read images
    def resolve_external_image(self, info, image_name):
        url = f'product/images/{image_name}/'
        return ImageType(url=url)
    
    @staticmethod
    def resolve_e4k_tblproduct_products_page(self, info,companyid, first=None, after=None):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            queryset = TblproductProducts.objects.filter(companyid=company).order_by('productid')

            if after:
                queryset = queryset.filter(productid__gt=after)

            if first:
                queryset = queryset[:first]

            products = list(queryset)  # Convert queryset to list after slicing
            edges = [ProductEdge(node=product) for product in products]
            end_cursor = products[-1].productid if products else None
            has_next_page = TblproductProducts.objects.filter(productid__gt=end_cursor).exists() if end_cursor else False

            return E4k_TblProduct_Product_Page_Connection(
                edges=edges,
                page_info=PageInfoType(
                    has_next_page=has_next_page,
                    end_cursor=end_cursor
                )
            )
    
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    
    @staticmethod
    def resolve_e4k_tblproduct_product_all(self,info,companyid):
        with connection.cursor() as cursor:
            query = """SELECT t1.CompanyID, t1.ProductID, t1.Description, t2.Description AS Category1ID, 
                t3.Description AS Category2ID, t4.Description AS Category3ID, t5.Description AS ClassID,
                t6.description AS CommodityCode, t7.NomDescription AS Nominal, t8.description AS Obsolete_Class, 
                t11.Description AS StockingType, t10.description AS IssueUOM, t9.description AS StockingUOM, t1.Notes, 
                t1.Weight, t1.Live, t1.BatchControl, t1.StyleImage, t1.SupplimentaryUnits,t12.Country AS CountryID
            FROM tblproduct_products t1
            LEFT JOIN tblproduct_category1 t2 ON t1.CompanyID = t2.CompanyID AND t1.Category1ID = t2.Category1ID
            LEFT JOIN tblproduct_category2 t3 ON t1.CompanyID = t3.CompanyID AND t1.Category2ID = t3.Category2ID
            LEFT JOIN tblproduct_category3 t4 ON t1.CompanyID = t4.CompanyID AND t1.Category3ID = t4.Category3ID
            LEFT JOIN tblproduct_class t5 ON t1.CompanyID = t5.CompanyID AND t1.ClassID = t5.ClassID
            LEFT JOIN tblproduct_commoditycodes t6 ON t1.CompanyID = t6.CompanyID AND t1.Commodity_Code = t6.Commodity_Code
            LEFT JOIN tblacc_nominal t7 ON t1.CompanyID = t7.CompanyID AND t1.Nominal_Code = t7.NomCode
            LEFT JOIN tblproduct_obsolete_types t8 ON t1.CompanyID = t8.CompanyID AND t1.Obsolete_Class = t8.ObsoleteID
            LEFT JOIN tblproduct_typeofissue t9 ON t1.CompanyID = t9.CompanyID AND t1.StockingUOM = t9.Issue_Type
            LEFT JOIN tblproduct_unitofissue t10 ON t1.CompanyID = t10.CompanyID AND t1.IssueUOM = t10.Issue_Units
            LEFT JOIN tblproduct_stocking_types t11 ON t1.CompanyID = t11.CompanyID AND t1.StockingType = t11.StockingType
            LEFT JOIN tblbus_countries t12 ON t1.CompanyID = t12.CompanyID AND t1.CountryID =t12.CountryID
            WHERE t1.CompanyID = '%s'""" % (companyid)
            

            cursor.execute(query)
            result = cursor.fetchall()

            # Convert the result to a list of lists
            columns = ['CompanyID', 'ProductID', 'Description', 'Category1ID', 'Category2ID', 'Category3ID',
           'ClassID', 'CommodityCode', 'Nominal', 'Obsolete_Class', 'StockingType', 'IssueUOM',
           'StockingUOM', 'Notes', 'Weight', 'Live', 'BatchControl', 'StyleImage', 'SupplimentaryUnits','CountryID']

            
            result_dicts = [dict(zip(columns, row)) for row in result]
            for row in result_dicts:
                row['Live'] = bytes_to_boolean(row['Live'])
                row['BatchControl'] = bytes_to_boolean(row['BatchControl'])
            return result_dicts
        

    @staticmethod
    def resolve_e4k_tblcompany_all(self,info):
        try:
            company = Tblcompany.objects.all()
            return company
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_search(self,info,companyid,productid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            product = TblproductProducts.objects.filter(companyid=company, productid=productid)
            if len(product) == 0:
                return "Success"
            else:
                return "Failed"
        except Tblcompany.DoesNotExist:
            return "Companyid not found"
        
    @staticmethod
    def resolve_e4k_tblwhowarehouse(self,info,companyid,warehouseid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if warehouseid!= '':
                warehouses = TblwhoWarehouses.objects.filter(companyid=company,
                                                        warehouseid = warehouseid)
                
                if len(warehouses) == 0:
                    return [CustomErrorType(message="Warehouse id doesn't Exists")]
                return warehouses
                
            else:
                return TblwhoWarehouses.objects.filter(companyid = company)
        except TblwhoWarehouses.DoesNotExist:
            return [CustomErrorType(message="Warehouse id Not Found")]
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_property_level_types(self,info,companyid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            return TblproductPropertyLevelTypes.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblbus_sales_people(self,info,companyid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            return TblbusSalesPeople.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_property_types_values(self,info,companyid,propertyid,propertyvalue):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if propertyid != None:
                if propertyvalue != "" :
                    property_types_values = TblproductPropertyTypesValues.objects.filter(companyid = company, proptypeid = propertyid, proptype_values = propertyvalue)
                    if len(property_types_values) == 0:
                        return [CustomErrorType(message="Property Type Value Not Found")]
                    return property_types_values

                else:

                    property_types_values = TblproductPropertyTypesValues.objects.filter(companyid = company, proptypeid = propertyid)
                    if len(property_types_values) == 0:
                        return [CustomErrorType(message="Property Type Not Found")]
                    return property_types_values
            else:
                return TblproductPropertyTypesValues.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        except TblproductPropertyTypesValues.DoesNotExist:
            return [CustomErrorType(message="Property Type Value Not Found")]
        
    

    @staticmethod
    def resolve_e4k_tblproduct_product_supplier_level(self,info,companyid,productid,supplierid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if supplierid !='':
                supplier = Tblsupplier.objects.get(companyid=company,
                                                 businessid = supplierid)
                if productid !='':
                    product = TblproductProducts.objects.get(companyid=company,
                                                            productid = productid)
                    try:
                        supplier_level = TblproductProductSupplierLevel.objects.filter(companyid = company,
                                                                    productid = product,
                                                                    supplierid = supplier)
                        if len(supplier_level) == 0:
                            return [CustomErrorType(message="Product Supplier Level Data Not Found")]

                        return supplier_level
                    except TblproductProductSupplierLevel.DoesNotExist:
                        return [CustomErrorType(message="Product Supplier Level Not Found")]
                else:
                    return TblproductProductSupplierLevel.objects.filter(companyid = company,
                                                                         supplierid = supplier)
            else:
                if productid !='':
                    product = TblproductProducts.objects.get(companyid=company,
                                                            productid = productid)
                    try:
                        supplier_level = TblproductProductSupplierLevel.objects.filter(companyid = company,
                                                                    productid = product)
                        if len(supplier_level) == 0:
                            return [CustomErrorType(message="Product Supplier Level Data Not Found")]

                        return supplier_level
                    except TblproductProductSupplierLevel.DoesNotExist:
                        return [CustomErrorType(message="Product Supplier Level Not Found")]
                else:
                    return TblproductProductSupplierLevel.objects.filter(companyid = company)

        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblsupplier.DoesNotExist:
            return [CustomErrorType(message="Supplier Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_supplier_level_colmatrix(self,info,companyid,productid,supplierid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if supplierid !='':
                supplier = Tblsupplier.objects.get(companyid=company,
                                                 businessid = supplierid)
                if productid !='':
                    product = TblproductProducts.objects.get(companyid=company,
                                                            productid = productid)
                    try:
                        supplier_level = TblproductProductSupplierLevelColmatrix.objects.filter(companyid = company,
                                                                    productid = product,
                                                                    supplierid = supplier)
                        if len(supplier_level) == 0:
                            return [CustomErrorType(message="Product Supplier Col Level Data Not Found")]

                        return supplier_level
                    except TblproductProductSupplierLevelColmatrix.DoesNotExist:
                        return [CustomErrorType(message="Product Supplier Level Col Not Found")]
                else:
                    return TblproductProductSupplierLevelColmatrix.objects.filter(companyid = company,
                                                                         supplierid = supplier)
            else:
                if productid !='':
                    product = TblproductProducts.objects.get(companyid=company,
                                                            productid = productid)
                    try:
                        supplier_level = TblproductProductSupplierLevelColmatrix.objects.filter(companyid = company,
                                                                    productid = product)
                        if len(supplier_level) == 0:
                            return [CustomErrorType(message="Product Supplier Level Col Data Not Found")]

                        return supplier_level
                    except TblproductProductSupplierLevelColmatrix.DoesNotExist:
                        return [CustomErrorType(message="Product Supplier Level  Col Not Found")]
                else:
                    return TblproductProductSupplierLevelColmatrix.objects.filter(companyid = company)

        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblsupplier.DoesNotExist:
            return [CustomErrorType(message="Supplier Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblproduct_product_supplier_matrix(self,info,companyid,productid,supplierid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            if supplierid !='':
                supplier = Tblsupplier.objects.get(companyid=company,
                                                 businessid = supplierid)
                if productid !='':
                    product = TblproductProducts.objects.get(companyid=company,
                                                            productid = productid)
                    try:
                        supplier_level = TblproductProductSuppliersMatrix.objects.filter(companyid = company,
                                                                    productid = product,
                                                                    supplierid = supplier)
                        if len(supplier_level) == 0:
                            return [CustomErrorType(message="Product Supplier matrix Data Not Found")]

                        return supplier_level
                    except TblproductProductSuppliersMatrix.DoesNotExist:
                        return [CustomErrorType(message="Product Supplier matrix Not Found")]
                else:
                    return TblproductProductSuppliersMatrix.objects.filter(companyid = company,
                                                                         supplierid = supplier)
            else:
                if productid !='':
                    product = TblproductProducts.objects.get(companyid=company,
                                                            productid = productid)
                    try:
                        supplier_level = TblproductProductSuppliersMatrix.objects.filter(companyid = company,
                                                                    productid = product)
                        if len(supplier_level) == 0:
                            return [CustomErrorType(message="Product Supplier Matrix Data Not Found")]

                        return supplier_level
                    except TblproductProductSuppliersMatrix.DoesNotExist:
                        return [CustomErrorType(message="Product Supplier matrix Not Found")]
                else:
                    return TblproductProductSuppliersMatrix.objects.filter(companyid = company)

        except TblproductProducts.DoesNotExist:
            return [CustomErrorType(message="Product Id Not Found")]
        except Tblsupplier.DoesNotExist:
            return [CustomErrorType(message="Supplier Id Not Found")]
        except Tblcompany.DoesNotExist:
           return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblcustomer_all(self,info,companyid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            return Tblcustomer.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        
    @staticmethod
    def resolve_e4k_tblsupplier_all(self,info,companyid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            return Tblsupplier.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]

    @staticmethod
    def resolve_e4k_tblproduct_product_paramerter_default_value(self, info, companyid,productid,settingid,customerid=None):
        default_data = GetProduct_params_value(companyid=companyid,
                                                   productid=productid,
                                                   settingid=settingid,
                                                   customerid=customerid)
        return default_data
    
    @staticmethod
    def resolve_e4k_tblcompany_params_value(self,info, companyid,paramid):
        company_data = GetCompany_params_value(companyid=companyid,
                                                   paramid=paramid)
        return company_data
    
    @staticmethod
    def resolve_e4k_tblcustomer_params_default_value(self,info,companyid,customerid,settingid):
        customer_defaul_data = GetCustomer_params_value(companyid=companyid,
                                                        customerid=customerid,
                                                        settingid=settingid)
        return customer_defaul_data
        
    @staticmethod
    def resolve_e4k_tblsupplier_params_default_value(self,info,companyid,supplierid,settingid):
        supplier_defaul_data = GetSupplier_params_value(companyid=companyid,
                                                        supplierid=supplierid,
                                                        settingid=settingid)
        return supplier_defaul_data
        

    @staticmethod
    def resolve_e4k_tblgen_Categories(self,info,companyid,moduleid,iscustomer):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if iscustomer == False:
                if moduleid !='':
                    return TblgenCategories.objects.filter(companyid=company,
                                                            moduleid=moduleid)
                
                else:
                    return TblgenCategories.objects.filter(companyid=company)
            else:
                if moduleid.lower() == 'product':
                    par_cus_set = TblproductParametersSettings.objects.filter(companyid=company,
                                                                            iscustomer=1).values_list('category',flat=True)
                    params = set(par_cus_set)
                    return TblgenCategories.objects.filter(companyid=company,
                                                            moduleid=moduleid,
                                                            categoryid__in=params)
                else:
                    return []

        except Tblcompany.DoesNotExist:
            return [CustomErrorType(message="Company Id Not Found")]
        