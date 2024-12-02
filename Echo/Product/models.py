from django.db import models
from itertools import product
from Customer.models import (Tblcompany,Tblcustomer,TblcustomerClass,TblgenUsers,TblaccNominal,
                             TblbusCountries,TblbusSalesPeople)

from Supplier.models import (TblwhoWarehouses,Tblsupplier)

from django.db import IntegrityError


class TblproductCategory1(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category1id = models.IntegerField(db_column='Category1ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_category1'

    # def has_related_objects(self):
    #     # Iterate through related managers and check for existence
    #     for related_model in self._meta.related_objects:
    #         if related_model.field.on_delete != models.CASCADE:  # Only check non-CASCADE
    #             if related_model.model.objects.filter(tblproductcategory1=self).exists():
    #                 return True
    #     return False

    # def delete(self, using=None, keep_parents=False):
    #     if self.has_related_objects():
    #         raise IntegrityError("TblproductCategory1 Cannot delete category due to linked objects.")
    #     return super().delete(using=using, keep_parents=keep_parents)


class TblproductCategory2(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category2id = models.IntegerField(db_column='Category2ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_category2'


class TblproductCategory3(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category3id = models.IntegerField(db_column='Category3ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_category3'


class TblproductClass(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_class'


class TblproductColours(models.Model):
    #id = models.BigIntegerField(db_column='ID')
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    colourid = models.CharField(db_column='ColourID', primary_key=True, max_length=15)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colourcode = models.CharField(db_column='ColourCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_colours'


class TblproductCommoditycodes(models.Model):
    #id = models.BigIntegerField(db_column='ID')
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    commodity_code = models.CharField(db_column='Commodity_Code', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_commoditycodes'


class TblproductCustomerClass(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    fskclassid = models.ForeignKey(TblproductClass, models.DO_NOTHING, db_column='FskClassID')  # Field name made lowercase.
    cusclassid = models.ForeignKey(TblcustomerClass, models.DO_NOTHING, db_column='CusClassID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_customer_class'

class TblproductFits(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    fitid = models.CharField(db_column='FitID', primary_key=True, max_length=5)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_fits'


class TblproductIntrastat(models.Model):
    companyid = models.CharField(db_column='CompanyId', max_length=3, blank=True, null=True)  # Field name made lowercase.
    documentno = models.IntegerField(db_column='DocumentNo', blank=True, null=True)  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lineno = models.IntegerField(db_column='LineNo', blank=True, null=True)  # Field name made lowercase.
    goodsvalue = models.IntegerField(db_column='GoodsValue', blank=True, null=True)  # Field name made lowercase.
    commoditycode = models.CharField(db_column='CommodityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deliveryterms = models.CharField(db_column='DeliveryTerms', max_length=50, blank=True, null=True)  # Field name made lowercase.
    natureofprocess = models.CharField(db_column='NatureOfProcess', max_length=50, blank=True, null=True)  # Field name made lowercase.
    netmasskg = models.IntegerField(db_column='NetMassKg', blank=True, null=True)  # Field name made lowercase.
    supplementaryunits = models.CharField(db_column='SupplementaryUnits', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modeoftransport = models.IntegerField(db_column='ModeOfTransport', blank=True, null=True)  # Field name made lowercase.
    membercode = models.IntegerField(db_column='MemberCode', blank=True, null=True)  # Field name made lowercase.
    trndate = models.DateTimeField(db_column='TrnDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_intrastat'


class TblproductMemo(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('TblproductProducts', models.DO_NOTHING, db_column='ProductID', primary_key=True)  # Field name made lowercase.
    memotext = models.TextField(db_column='MemoText', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(TblgenUsers, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_memo'


class TblproductObsoleteTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    obsoleteid = models.IntegerField(db_column='ObsoleteID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    allow_sale = models.BooleanField(db_column='IsAllow_Sale')  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'tblproduct_obsolete_types'

class TblproductParametersCustomerSetvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.ForeignKey('tblproductParametersSettings', models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_parameters_customer_setvalues'



class TblgenCategories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    moduleid = models.CharField(db_column='ModuleID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblgen_categories'

class TblproductParametersSettings(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.CharField(db_column='SettingID', primary_key=True, max_length=20)  # Field name made lowercase.
    settingname = models.CharField(db_column='SettingName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(TblgenCategories, models.DO_NOTHING, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lookup_text = models.CharField(db_column='Lookup_Text', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iscustomer = models.IntegerField(db_column='IsCustomer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_parameters_settings'


class TblproductParametertsSetvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.ForeignKey(TblproductParametersSettings, models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_parameterts_setvalues'


class TblproductPriceTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    priceid = models.IntegerField(db_column='PriceID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price_type = models.IntegerField(db_column='Price_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_price_types'


class TblproductProductBom(models.Model):
    companyid = models.CharField(db_column='CompanyID', primary_key=True, max_length=3)  # Field name made lowercase. The composite primary key (CompanyID, StyleID, ColourID, StyleID_BOM, ColourID_BOM) found, that is not supported. The first column is selected.
    styleid = models.CharField(db_column='StyleID', max_length=25)  # Field name made lowercase.
    colourid = models.CharField(db_column='ColourID', max_length=15)  # Field name made lowercase.
    styleid_bom = models.CharField(db_column='StyleID_BOM', max_length=25)  # Field name made lowercase.
    colourid_bom = models.CharField(db_column='ColourID_BOM', max_length=15)  # Field name made lowercase.
    rating_bom = models.FloatField(db_column='Rating_BOM', blank=True, null=True)  # Field name made lowercase.
    seqno = models.SmallIntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_bom'
        unique_together = (('companyid', 'styleid', 'colourid', 'styleid_bom', 'colourid_bom'),)


class TblproductProductCostStandardMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdcostmatix = models.JSONField(db_column='StdCostMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_cost_standard_matrix'


    def Update_Product_CostStandard_Matrix(self,company,productid):
        

        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.pricematrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}

        product_price_types = TblproductPriceTypes.objects.filter(companyid = company,price_type=1)

        coststdmatrix = []
        for price_type in product_price_types:
            if len(property_names) != 1 and len(product_prop_id) != 1:
                for i in range(len(product_prop_id)): 
                    property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                    mat[property_names[i]] = property_values
                matt = self.create_cost_standard_Matrix(mat,property_names,price_type.priceid)
                coststdmatrix.append(matt)
                #self.stdcostmatix = matt
                #self.save()

            else:
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
                mat[property_names[0]] = property_values
                matt = self.create_cost_standard_Matrix(mat,property_names,price_type.priceid)
                coststdmatrix.append(matt)
                #self.stdcostmatix = matt
                #self.save()
        flattened_list = [item for sublist in coststdmatrix for item in sublist]
        
        self.stdcostmatix = flattened_list
        self.save()
        

    def create_cost_standard_Matrix(self,property_dic, names,priceid):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["price"] = 0
                combinations["pricetype"] = priceid

                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["pricetype"] = priceid
                temp_property["price"] = 0
                combi_list.append(temp_property)
                count+=1
        return combi_list


class TblproductProductCostSupplierMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    supcostmatix = models.JSONField(db_column='SupCostMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_cost_supplier_matrix'

    def Update_Product_CostSupplier_Matrix(self,company,productid):
        

        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.pricematrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}
        product_price_types = TblproductPriceTypes.objects.filter(companyid = company,price_type=1)

        suppcostmatix = []
        for price_type in product_price_types:
            if len(property_names) != 1 and len(product_prop_id) != 1:
                for i in range(len(product_prop_id)): 
                    property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                    mat[property_names[i]] = property_values
                matt = self.create_cost_supplier_Matrix(mat,property_names,price_type.priceid)
                suppcostmatix.append(matt)
                #self.supcostmatix = matt
                #self.save()

            else:
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
                mat[property_names[0]] = property_values
                matt = self.create_cost_supplier_Matrix(mat,property_names,price_type.priceid)
                suppcostmatix.append(matt)
                #self.supcostmatix = matt
                #self.save()
        flattened_list = [item for sublist in suppcostmatix for item in sublist]
        
        
        self.supcostmatix = flattened_list
        self.save()

    def create_cost_supplier_Matrix(self,property_dic, names,priceid):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["price"] = 0
                combinations["pricetype"] = priceid

                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["pricetype"] = priceid
                temp_property["price"] = 0
                combi_list.append(temp_property)
                count+=1
        return combi_list


class TblproductProductFreetext(models.Model):
    companyid = models.CharField(db_column='CompanyId', primary_key=True, max_length=50)  # Field name made lowercase. The composite primary key (CompanyId, WareHouseId, StyleId, FreeTextType) found, that is not supported. The first column is selected.
    warehouseid = models.CharField(db_column='WareHouseId', max_length=10)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=25)  # Field name made lowercase.
    freetexttype = models.CharField(db_column='FreeTextType', max_length=50)  # Field name made lowercase.
    freetext = models.TextField(db_column='FreeText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_freetext'
        unique_together = (('companyid', 'warehouseid', 'productid', 'freetexttype'),)


class TblproductProductGallery(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    productimage = models.CharField(db_column='ProductImage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is360 = models.IntegerField(db_column='Is360', default=0,blank=True, null=True)  # Field name made lowercase.
    noframes = models.IntegerField(db_column='NoFrames', blank=True, null=True)  # Field name made lowercase.
    nofootages = models.IntegerField(db_column='NoFootages', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_gallery'

class TblproductProductObsoleteMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    obslmatix = models.JSONField(db_column='ObslMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_obsolete_matrix'

    
    ########### Functions for update obslmatrix
    def Update_Product_ObsoleteType_Matrix(self,company,productid):
        
        
        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.obslmatrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}
        if len(property_names) != 1 and len(product_prop_id) != 1:
            for i in range(len(product_prop_id)): 
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                mat[property_names[i]] = property_values
            matt = self.create_Obsolete_Matrix(mat,property_names)
            self.obslmatix = matt
            self.save()

        else:
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
            mat[property_names[0]] = property_values
            matt = self.create_Obsolete_Matrix(mat,property_names)

            self.obslmatix = matt
            self.save()

    def create_Obsolete_Matrix(self,property_dic, names):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["obsoleteID"] = 0
                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["obsoleteID"] = 0
                combi_list.append(temp_property)
                count+=1
        return combi_list



class TblproductProductPriceCustomerMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    cuspricematix = models.JSONField(db_column='CusPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_price_customer_matrix'

    def Update_Product_PriceCustomer_Matrix(self,company,productid):
        

        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.pricematrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}

        product_price_types = TblproductPriceTypes.objects.filter(companyid = company,price_type=2)

        cuspricematix = []
        for price_type in product_price_types:
            if len(property_names) != 1 and len(product_prop_id) != 1:
                for i in range(len(product_prop_id)): 
                    property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                    mat[property_names[i]] = property_values
                matt = self.create_price_customer_Matrix(mat,property_names,price_type.priceid)
                cuspricematix.append(matt)
                # self.cuspricematix = matt
                # self.save()

            else:
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
                mat[property_names[0]] = property_values
                matt = self.create_price_customer_Matrix(mat,property_names,price_type.priceid)
                cuspricematix.append(matt)
        flattened_list = [item for sublist in cuspricematix for item in sublist]
        
        
        self.cuspricematix = flattened_list
        self.save()

    def create_price_customer_Matrix(self,property_dic, names,priceid):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["price"] = 0
                combinations["pricetype"] = priceid

                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["pricetype"] = priceid
                temp_property["price"] = 0
                combi_list.append(temp_property)
                count+=1
        return combi_list
    
class TblproductProductPriceStandardDateMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdpricematix = models.JSONField(db_column='StdPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_price_standard_date_matrix'

class TblproductProductPriceStandardMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdpricematix = models.JSONField(db_column='StdPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_price_standard_matrix'

    def Update_Product_PriceStandard_Matrix(self,company,productid):
        

        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.pricematrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}

        product_price_types = TblproductPriceTypes.objects.filter(companyid = company,price_type=2)

        stdpricematrix = []

        for price_type in product_price_types:

            if len(property_names) != 1 and len(product_prop_id) != 1:
                for i in range(len(product_prop_id)): 
                    property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                    mat[property_names[i]] = property_values
                matt = self.create_price_standard_Matrix(mat,property_names,price_type.priceid)
                stdpricematrix.append(matt)
                #self.stdpricematix = matt
                #self.save()

            else:
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
                mat[property_names[0]] = property_values
                matt = self.create_price_standard_Matrix(mat,property_names,price_type.priceid)
                stdpricematrix.append(matt)
                #self.stdpricematix = matt
                #self.save()

        flattened_list = [item for sublist in stdpricematrix for item in sublist]
        
        self.stdpricematix = flattened_list
        self.save()

    def create_price_standard_Matrix(self,property_dic, names,priceid):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["price"] = 0
                combinations["pricetype"] = priceid

                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["pricetype"] = priceid
                temp_property["price"] = 0
                combi_list.append(temp_property)
                count+=1
        return combi_list


class TblproductProductPriceStandardQtyMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdpricematix = models.JSONField(db_column='StdPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_price_standard_qty_matrix'

class TblproductProductProperties(models.Model):
    product_propid = models.AutoField(db_column='Product_PropId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    propertyid = models.ForeignKey('TblproductPropertyTypes', models.DO_NOTHING, db_column='PropertyId', blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_properties'


class TblproductProductPropertyLevel(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('TblproductProducts', models.DO_NOTHING, db_column='ProductID', primary_key=True)  # Field name made lowercase.
    stockmatrix = models.JSONField(db_column='StockMatrix', blank=True, null=True)  # Field name made lowercase.
    pricematrix = models.JSONField(db_column='PriceMatrix', blank=True, null=True)  # Field name made lowercase.
    stklvlmatrix = models.JSONField(db_column='StkLvlMatrix', blank=True, null=True)  # Field name made lowercase.
    stklocmatrix = models.JSONField(db_column='StkLocMatrix', blank=True, null=True)  # Field name made lowercase.
    stktypematrix = models.JSONField(db_column='StkTypeMatrix', blank=True, null=True)  # Field name made lowercase.
    obslmatrix = models.JSONField(db_column='ObslMatrix', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_property_level'


class TblproductProductPropertyLevelColmatrix(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('TblproductProducts', models.DO_NOTHING, db_column='ProductID', primary_key=True)  # Field name made lowercase.
    stockcolmatrix = models.JSONField(db_column='StockColMatrix', blank=True, null=True)  # Field name made lowercase.
    pricecolmatrix = models.JSONField(db_column='PriceColMatrix', blank=True, null=True)  # Field name made lowercase.
    stklvlcolmatrix = models.JSONField(db_column='StkLvlColMatrix', blank=True, null=True)  # Field name made lowercase.
    stkloccolmatrix = models.JSONField(db_column='StkLocColMatrix', blank=True, null=True)  # Field name made lowercase.
    stktypecolmatrix = models.JSONField(db_column='StkTypeColMatrix', blank=True, null=True)  # Field name made lowercase.
    obslcolmatrix = models.JSONField(db_column='ObslColMatrix', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_property_level_colmatrix'

    def sort_dict_by_value(self,my_dict):

        #print('my_dict = ',my_dict)
        # Use sorted() with items() and a lambda function to sort by value
        sorted_items = sorted(my_dict.items(), key=lambda item: item[1])

        # Extract keys and values from sorted items
        sorted_keys = [item[0] for item in sorted_items]
        sorted_values = [item[1] for item in sorted_items]

        return sorted_keys, sorted_values

    def Update_Product_Property_Level_ColMatrix(self,product_property_level,column_name,productid,companyid):
        stock_matrix = product_property_level
        

        sort_keys , sort_values = self.sort_dict_by_value(stock_matrix[0])

        # print('column_name = ',column_name)
        #product_relations = TblproductProductProperties.objects.filter(productid=productid).select_related('propertyid').order_by('seqno')
        product_relations = TblproductProductProperties.objects.filter(companyid = companyid,
                                                                       productid = productid,
                                                                       propertyid__description__in = sort_keys).order_by('seqno')
        product_prop_id = [rel.product_propid for rel in product_relations]
        sort_keys = [rel.propertyid.description for rel in product_relations]
        #print(sort_keys," = product property id", product_prop_id)

        mat = {}
        remove_property = []
        select_property = []
        for i in range(len(product_prop_id)): 
            if len(sort_keys) == 1:
                property_id = sort_keys[0]
                property_instance = TblproductPropertyTypes.objects.get(companyid=companyid, description=property_id)
                #print(" = product property id", property_instance)
                mat['summary'] = 0
                product_prop_id_ = [rel.product_propid for rel in product_relations if rel.propertyid.propertyid == int(property_instance.propertyid)]
                #product_prop_id_ = [rel.product_propid for rel in product_relations if rel.seqno == int(sort_values[0])]
                sort_keys[0] = ['summary']
                sort_keys.append(property_id)
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id_[0])]
                mat[sort_keys[1]] = property_values
                
                break
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
            mat[sort_keys[i]] = property_values
        #print("Mat ==== ",mat)
        Columngrid = self.UpdatePropertyGridMatrix(mat,sort_keys,column_name)
        
        if column_name =='stockmatrix':
            self.stockcolmatrix = Columngrid
        elif column_name == 'pricematrix':
            self.pricecolmatrix = Columngrid
        elif column_name =='stklvlmatrix':
            self.stklvlcolmatrix = Columngrid
        elif column_name =='stklocmatrix':
            self.stkloccolmatrix = Columngrid
        elif column_name =='stktypematrix':
            self.stktypecolmatrix = Columngrid
        elif column_name =='obslmatrix':
            self.obslcolmatrix = Columngrid

        self.save()

    def UpdatePropertyGridMatrix(self,grid_values,colum_seq,column_name):
        columns_list = []
        
        keys_list = list(grid_values.keys())
        for i in range(len(colum_seq)):
            colum_sequence = {}
            if colum_seq[0] == keys_list[i]:
                colum_sequence["label"] = colum_seq[0]
                colum_sequence["dataField"] = colum_seq[0]
                colum_sequence["dataType"] = "string"
                colum_sequence["allowRowGroup"] =True
                colum_sequence["rowGroup"] =True
                columns_list.append(colum_sequence)
            # elif colum_seq[-1] == keys_list[i]:
            #     for j in grid_values[colum_seq[-1]]:
            #         colum_sequence = {}
            #         #print('j = ',j)
            #         colum_sequence["label"] = j
            #         colum_sequence["dataField"] = j
            #         colum_sequence["dataType"] = "number"
            #         colum_sequence["summary"] ='sum'
            #         columns_list.append(colum_sequence)
            elif colum_seq[-1] == keys_list[i]:
                    colum_sequence["label"] = colum_seq[i]
                    colum_sequence["dataField"] = colum_seq[i]
                    colum_sequence["dataType"] = "string"
                    colum_sequence["allowPivot"] =True
                    colum_sequence["pivot"] =True
                    columns_list.append(colum_sequence)

                    if column_name == 'stklvlmatrix':
                        
                        for j in ['minqty','maxqty','reorderqty']:
                            colum_sequence = {}
                            colum_sequence["label"] = j
                            colum_sequence["dataField"] = j
                            colum_sequence["dataType"] = "number"
                            colum_sequence["summary"] ='sum'
                            columns_list.append(colum_sequence)

                    if column_name == 'stktypematrix':
                            colum_sequence = {}
                            colum_sequence["label"] = 'stocktype'
                            colum_sequence["dataField"] = 'stocktype'
                            colum_sequence["dataType"] = "number"
                            colum_sequence["summary"] ='sum'
                            columns_list.append(colum_sequence)

                    if column_name == 'obslmatrix':
                            colum_sequence = {}
                            colum_sequence["label"] = 'obsolete'
                            colum_sequence["dataField"] = 'obsoleteID'
                            colum_sequence["dataType"] = "number"
                            colum_sequence["summary"] ='sum'
                            columns_list.append(colum_sequence)

                    if column_name == 'pricematrix':
                        
                        for j in ['price','pricetype']:
                            colum_sequence = {}
                            colum_sequence["label"] = j
                            colum_sequence["dataField"] = j
                            colum_sequence["dataType"] = "number"
                            colum_sequence["summary"] ='sum'
                            columns_list.append(colum_sequence)

                    
                    
            else:  
                    colum_sequence["label"] = colum_seq[i]
                    colum_sequence["dataField"] = colum_seq[i]
                    colum_sequence["dataType"] = "string"
                    colum_sequence["allowPivot"] =True
                    colum_sequence["pivot"] =True
                    columns_list.append(colum_sequence)
        



        return columns_list



class TblproductProductPropertyMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    propertymatix = models.JSONField(db_column='PropertyMatix', blank=True, null=True)  # Field name made lowercase.
    propertycolmatrix = models.JSONField(db_column='PropertyColMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_property_matrix'

    def update_PropertyMatix(self, product):
        
        product_relations = TblproductProductProperties.objects.filter(productid=product).select_related('propertyid').order_by('seqno')
      

        property_id = [rel.propertyid.propertyid for rel in product_relations]
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]

        mat = {}

        #print('################## mat',product_prop_id)

        remove_property = []
        select_property = []
        for i in range(len(product_prop_id)): 
            #property_values = [value.Property_Value for value in ProductPropertyValues.objects.filter(ProductID=product,Property = property_id[i])]
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
            if len(property_values) == 0:
                #print(property_names[i],'################## mat',product_prop_id[i])
                remove_property.append(property_names[i])
            else:
                mat[property_names[i]] = property_values
                select_property.append(property_names[i])

        #print('################## mat', mat,select_property)
        matt = self.create_product_properties(mat,select_property)       
        Columngrid = self.UpdatePropertyGridMatrix(mat,select_property)       
        self.propertycolmatrix = Columngrid
        self.propertymatix = matt
        #print('##################propertymatixmat', matt)
        self.save()


    def create_product_properties(self,property_dic, names):
        
        from itertools import product
    
        combinations = {}
        combi_list = []
        count=0
        all_values = [property_dic[name] for name in names]
        for combination in product(*all_values):
            temp = combinations
            temp_property = {}
            for i in range(len(names)):
                
                if i < len(names) - 1:
                    temp_property[names[i]] = combination[i]
                else:
                    temp_property[combination[i]] = 0

                    
                if combination[i] not in temp:
                    temp[combination[i]] = {} if i < len(names) - 1 else 0
                    #print('i=',i,'temp',temp)
                temp = temp[combination[i]]
            combi_list.append(temp_property)
            count+=1
        
        print('Total_count = ',count)
        
        return combi_list
        #return combinations
    
    def UpdatePropertyGridMatrix(self,grid_values,colum_seq):
        columns_list = []
        
        keys_list = list(grid_values.keys())
        for i in range(len(colum_seq)):
            colum_sequence = {}
            if colum_seq[0] == keys_list[i]:
                colum_sequence["label"] = colum_seq[0]
                colum_sequence["dataField"] = colum_seq[0]
                colum_sequence["dataType"] = "string"
                colum_sequence["allowRowGroup"] =True
                colum_sequence["rowGroup"] =True
                columns_list.append(colum_sequence)
            elif colum_seq[-1] == keys_list[i]:
                for j in grid_values[colum_seq[-1]]:
                    colum_sequence = {}
                    #print('j = ',j)
                    colum_sequence["label"] = j
                    colum_sequence["dataField"] = j
                    colum_sequence["dataType"] = "number"
                    colum_sequence["summary"] ='sum'
                    # colum_sequence["summarySettings"] ={
                    #                                         "prefix": 'size',
                    #                                     }
                    columns_list.append(colum_sequence)
            else:  
                    colum_sequence["label"] = colum_seq[i]
                    colum_sequence["dataField"] = colum_seq[i]
                    colum_sequence["dataType"] = "string"
                    colum_sequence["allowPivot"] =True
                    colum_sequence["pivot"] =True
                    columns_list.append(colum_sequence)



        return columns_list


class TblproductProductPropertyValues(models.Model):
    product_prop_value_id = models.AutoField(db_column='Product_Prop_Value_Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    product_propid = models.ForeignKey(TblproductProductProperties, models.DO_NOTHING, db_column='Product_PropId', blank=True, null=True)  # Field name made lowercase.
    product_prop_value = models.CharField(db_column='Product_Prop_Value', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_property_values'


class TblproductProductReps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    repid = models.ForeignKey(TblbusSalesPeople, models.DO_NOTHING, db_column='RepID')  # Field name made lowercase.
    seqno = models.SmallIntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_reps'


class TblproductProductStockinglevelMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stocklevelmatix = models.JSONField(db_column='StockLevelMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_stockinglevel_matrix'

    def Update_Product_StockingLevel_Matrix(self,company,productid,warehouseid=None,old_data=[]):
        
        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.stklvlmatrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}
        if len(property_names) != 1 and len(product_prop_id) != 1:
            for i in range(len(product_prop_id)): 
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                mat[property_names[i]] = property_values
            matt = self.create_Stock_level_Matrix(mat,property_names,warehouseid)
            #print(old_data,'------------------olddata1--------------->',len(old_data))
            if len(old_data) > 0 and old_data !=None :
                self.stocklevelmatix = old_data + matt
                self.save()
                #print(old_data + matt,'-------------update_data1-------------------->',len(old_data + matt))
            else:
                self.stocklevelmatix = matt
                self.save()

        else:
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
            mat[property_names[0]] = property_values
            matt = self.create_Stock_level_Matrix(mat,property_names,warehouseid)
            #print(old_data,'------------------olddata2--------------->')
            if len(old_data) > 0 and old_data !=None :
                self.stocklevelmatix = old_data + matt
                self.save()
                #print(matt,'-------------update_data2-------------------->')
            else:
                self.stocklevelmatix = matt
                self.save()

    def create_Stock_level_Matrix(self,property_dic, names,warehouseid):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations['minqty'] = 0.0
                combinations['maxqty'] = 0.0
                combinations['reorderqty'] = 0.0
                combinations['WarehouseID'] = warehouseid if warehouseid else 'MAX01' ## need to change dynamic

                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property['minqty'] = 0.0
                temp_property['maxqty'] = 0.0
                temp_property['reorderqty'] = 0.0
                temp_property['WarehouseID'] = warehouseid if warehouseid else 'MAX01' ## need to change dynamic
                combi_list.append(temp_property)
                count+=1
        return combi_list

        


class TblproductProductStockingtypeMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stocktypematix = models.JSONField(db_column='StockTypeMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_stockingtype_matrix'

    def Update_Product_StockingType_Matrix(self,company,productid):
        

        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.stktypematrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}
        if len(property_names) != 1 and len(product_prop_id) != 1:
            for i in range(len(product_prop_id)): 
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                mat[property_names[i]] = property_values
            matt = self.create_Stock_Type_Matrix(mat,property_names)
            self.stocktypematix = matt
            self.save()

        else:
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
            mat[property_names[0]] = property_values
            matt = self.create_Stock_Type_Matrix(mat,property_names)

            self.stocktypematix = matt
            self.save()

    def create_Stock_Type_Matrix(self,property_dic, names):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["stocktype"] = "None"
                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["stocktype"] = "None"
                combi_list.append(temp_property)
                count+=1
        return combi_list
    

class TblproductProductSupplierLevel(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    suppliermatrix = models.JSONField(db_column='SupplierMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_supplier_level'


class TblproductProductSupplierLevelColmatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    suppliercolmatrix = models.JSONField(db_column='SupplierColMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_supplier_level_colmatrix'


    def sort_dict_by_value(self,my_dict):

        sorted_items = sorted(my_dict.items(), key=lambda item: item[1])

        # Extract keys and values from sorted items
        sorted_keys = [item[0] for item in sorted_items]
        sorted_values = [item[1] for item in sorted_items]

        return sorted_keys, sorted_values

    def Update_Product_Supplier_Level_ColMatrix(self,supplier_level,column_name,productid,companyid):
        supplier_matrix = supplier_level
        

        sort_keys , sort_values = self.sort_dict_by_value(supplier_matrix[0])

        # print('column_name = ',column_name)
        #product_relations = TblproductProductProperties.objects.filter(productid=productid).select_related('propertyid').order_by('seqno')
        product_relations = TblproductProductProperties.objects.filter(companyid = companyid,
                                                                       productid = productid,
                                                                       propertyid__description__in = sort_keys).order_by('seqno')
        product_prop_id = [rel.product_propid for rel in product_relations]
        sort_keys = [rel.propertyid.description for rel in product_relations]
        #print(sort_keys," = product property id", product_prop_id)

        mat = {}
        remove_property = []
        select_property = []
        for i in range(len(product_prop_id)): 
            if len(sort_keys) == 1:
                property_id = sort_keys[0]
                property_instance = TblproductPropertyTypes.objects.get(companyid=companyid, description=property_id)
                #print(" = product property id", property_instance)
                mat['summary'] = 0
                product_prop_id_ = [rel.product_propid for rel in product_relations if rel.propertyid.propertyid == int(property_instance.propertyid)]
                #product_prop_id_ = [rel.product_propid for rel in product_relations if rel.seqno == int(sort_values[0])]
                sort_keys[0] = ['summary']
                sort_keys.append(property_id)
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id_[0])]
                mat[sort_keys[1]] = property_values
                
                break
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
            mat[sort_keys[i]] = property_values
        #print("Mat ==== ",mat)
        Columngrid = self.UpdateSupplierGridMatrix(mat,sort_keys,column_name)
        
        if column_name =='suppliermatrix':
            self.suppliercolmatrix = Columngrid
        

        self.save()

    def UpdateSupplierGridMatrix(self,grid_values,colum_seq,column_name):
        columns_list = []
        
        keys_list = list(grid_values.keys())
        for i in range(len(colum_seq)):
            colum_sequence = {}
            if colum_seq[0] == keys_list[i]:
                colum_sequence["label"] = colum_seq[0]
                colum_sequence["dataField"] = colum_seq[0]
                colum_sequence["dataType"] = "string"
                colum_sequence["allowRowGroup"] =True
                colum_sequence["rowGroup"] =True
                columns_list.append(colum_sequence)
            elif colum_seq[-1] == keys_list[i]:
                    colum_sequence["label"] = colum_seq[i]
                    colum_sequence["dataField"] = colum_seq[i]
                    colum_sequence["dataType"] = "string"
                    colum_sequence["allowPivot"] =True
                    colum_sequence["pivot"] =True
                    columns_list.append(colum_sequence)

                    if column_name == 'suppliermatrix':
                        
                        for j in ['SupplierCode','LeadTime','WarehouseID','SupplierXRate','IsBulkOrder','Select']:
                            colum_sequence = {}
                            if j in ['SupplierCode','WarehouseID','IsBulkOrder']:
                                colum_sequence["label"] = j
                                colum_sequence["dataField"] = j
                                colum_sequence["dataType"] = "string"
                                colum_sequence["summary"] ='sum'
                                columns_list.append(colum_sequence)
                                continue
                            elif j in ['Select']:
                                colum_sequence = {}
                                colum_sequence["label"] = j
                                colum_sequence["dataField"] = j
                                colum_sequence["dataType"] = "boolean"
                                colum_sequence["summary"] ='sum'
                                columns_list.append(colum_sequence)
                                continue


                            colum_sequence["label"] = j
                            colum_sequence["dataField"] = j
                            colum_sequence["dataType"] = "number"
                            colum_sequence["summary"] ='sum'
                            columns_list.append(colum_sequence)

                    
            else:  
                    colum_sequence["label"] = colum_seq[i]
                    colum_sequence["dataField"] = colum_seq[i]
                    colum_sequence["dataType"] = "string"
                    colum_sequence["allowPivot"] =True
                    colum_sequence["pivot"] =True
                    columns_list.append(colum_sequence)
        



        return columns_list


class TblproductProductSuppliersMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    suppliermatrix = models.JSONField(db_column='SupplierMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_suppliers_matrix'

    def Update_Product_Supplier_Matrix(self,company,productid,supplierid):
        

        product_supplier_level = TblproductProductSupplierLevel.objects.get(companyid=company,productid=productid,supplierid=supplierid)
        pro_stock_ = product_supplier_level.suppliermatrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}
        if len(property_names) != 1 and len(product_prop_id) != 1:
            for i in range(len(product_prop_id)): 
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                mat[property_names[i]] = property_values
            matt = self.create_Supplier_Matrix(mat,property_names,productid.productid)
            #print("================================" , matt)
            self.suppliermatrix = matt
            self.save()

        else:
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
            mat[property_names[0]] = property_values
            matt = self.create_Supplier_Matrix(mat,property_names,productid.productid)
            #print("================================" , matt)
            self.suppliermatrix = matt
            self.save()

    def create_Supplier_Matrix(self,property_dic, names,supplierProductcode):
        combinations = {}
        combi_list = []
        count=0
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["SupplierCode"] = supplierProductcode
                combinations["LeadTime"] = 0
                combinations["WarehouseID"] = "Max01"
                combinations["SupplierXRate"] = 0
                combinations["IsBulkOrder"] = 'No'
                combinations['Select'] = True
                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["SupplierCode"] = supplierProductcode
                temp_property["LeadTime"] = 0
                temp_property["WarehouseID"] = "Max01"
                temp_property["SupplierXRate"] = 0
                temp_property["IsBulkOrder"] = 'No'
                temp_property['Select'] = True

                combi_list.append(temp_property)
                count+=1
        return combi_list


class TblproductProductSuppliers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    warehouseid = models.ForeignKey(TblwhoWarehouses, models.DO_NOTHING, db_column='WarehouseID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    supplierprod_code = models.CharField(db_column='SupplierProd_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_price = models.IntegerField(db_column='Supplier_price', blank=True, null=True)  # Field name made lowercase.
    supplierseq = models.SmallIntegerField(db_column='SupplierSeq', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=10)  # Field name made lowercase.
    leadtime = models.IntegerField(db_column='Leadtime', blank=True, null=True)  # Field name made lowercase.
    isbulkorder = models.IntegerField(db_column='IsBulkOrder', blank=True, null=True)  # Field name made lowercase.
    dutycost = models.DecimalField(db_column='DutyCost', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_suppliers'


class TblproductProductSuppliersWeekdays(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    supplierid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    weekday = models.IntegerField(db_column='WeekDay')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_suppliers_weekdays'


class TblproductProductVatcodeMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    vatcodematix = models.JSONField(db_column='VatCodeMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_product_vatcode_matrix'

    def Update_Product_Vatcode_Matrix(self,company,productid):
        

        product_stock_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=productid)
        pro_stock_ = product_stock_level.pricematrix[0]
        property_names, property_keys = pro_stock_.keys(), pro_stock_.values()
        product_relations = TblproductProductProperties.objects.filter(companyid = company,
                                                                       productid = productid,
                                                                       propertyid__description__in = property_names)
        
        product_prop_id = [rel.product_propid for rel in product_relations]
        property_names = [rel.propertyid.description for rel in product_relations]
        mat = {}
        if len(property_names) != 1 and len(product_prop_id) != 1:
            for i in range(len(product_prop_id)): 
                property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[i])]
                mat[property_names[i]] = property_values
            matt = self.create_vatcode_Matrix(mat,property_names)
            self.vatcodematix = matt
            self.save()

        else:
            property_values = [value.product_prop_value for value in TblproductProductPropertyValues.objects.filter(product_propid = product_prop_id[0])]
            mat[property_names[0]] = property_values
            matt = self.create_vatcode_Matrix(mat,property_names)

            self.vatcodematix = matt
            self.save()

    def create_vatcode_Matrix(self,property_dic, names):
        combinations = {}
        combi_list = []
        count=0
        
        if len(names) == 1:
            for i in range(len(property_dic[names[0]])):
                combinations = {}
                combinations[names[0]] = property_dic[names[0]][i]
                combinations["Vatcode"] = 2

                combi_list.append(combinations)

        else:
            all_values = [property_dic[name] for name in names]
            for combination in product(*all_values):
                temp = combinations
                temp_property = {}
            
                for i in range(len(names)):
                    if i < len(names) - 1:
                        temp_property[names[i]] = combination[i]
                    else:
                        temp_property[names[i]] = combination[i]
                temp_property["Vatcode"] = 2
                combi_list.append(temp_property)
                count+=1
        return combi_list


class TblproductProducts(models.Model):
    companyid = models.ForeignKey(Tblcompany, on_delete=models.PROTECT, db_column='CompanyID')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', primary_key=True, max_length=25)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category1id = models.ForeignKey(TblproductCategory1, on_delete=models.PROTECT, db_column='Category1ID', blank=True, null=True)  # Field name made lowercase.
    category2id = models.ForeignKey(TblproductCategory2, on_delete=models.PROTECT, db_column='Category2ID', blank=True, null=True)  # Field name made lowercase.
    category3id = models.ForeignKey(TblproductCategory3, on_delete=models.PROTECT, db_column='Category3ID', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    supplimentaryunits = models.CharField(db_column='SupplimentaryUnits', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nominal_code = models.ForeignKey(TblaccNominal, on_delete=models.PROTECT, db_column='Nominal_Code', blank=True, null=True)  # Field name made lowercase.
    commodity_code = models.ForeignKey(TblproductCommoditycodes, on_delete=models.PROTECT, db_column='Commodity_Code', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    classid = models.ForeignKey(TblproductClass, on_delete=models.PROTECT, db_column='ClassID', blank=True, null=True)  # Field name made lowercase.
    obsolete_class = models.ForeignKey(TblproductObsoleteTypes, on_delete=models.PROTECT, db_column='Obsolete_Class', default=0)  # Field name made lowercase.
    live = models.BooleanField(db_column='Live',default=False)  # Field name made lowercase. This field type is a guess.
    styleimage = models.CharField(db_column='StyleImage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    batchcontrol = models.BooleanField(db_column='BatchControl',default=False)  # Field name made lowercase. This field type is a guess.
    stockinguom = models.ForeignKey('TblproductTypeofissue', on_delete=models.PROTECT, db_column='StockingUOM', default=1)  # Field name made lowercase.
    issueuom = models.ForeignKey('TblproductUnitofissue', on_delete=models.PROTECT, db_column='IssueUOM', default=1)  # Field name made lowercase.
    stockingtype = models.ForeignKey('TblproductStockingTypes', on_delete=models.PROTECT, db_column='StockingType', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TblbusCountries, on_delete=models.PROTECT, db_column='CountryID', default=0)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_products'


class TblproductPropertyLevelTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    propertylvlid = models.IntegerField(db_column='PropertyLvlID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_property_level_types'

class TblproductPropertyTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    propertyid = models.IntegerField(db_column='PropertyID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isstatic = models.IntegerField(db_column='IsStatic',default=0)

    class Meta:
        #managed = False
        db_table = 'tblproduct_property_types'


class TblproductPropertyTypesValues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    proptypeid = models.ForeignKey(TblproductPropertyTypes, models.DO_NOTHING, db_column='PropTypeID')  # Field name made lowercase.
    proptype_values = models.CharField(db_column='PropType_Values', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_property_types_values'




# class TblproductSizeRanges(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
#     rangeid = models.CharField(db_column='RangeID', max_length=10)  # Field name made lowercase.
#     size_number = models.IntegerField(db_column='Size_Number')  # Field name made lowercase.
#     size_value = models.CharField(db_column='Size_Value', max_length=15, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         #managed = False
#         db_table = 'tblproduct_size_ranges'

class TblproductSizeRangeValues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    rangeid = models.ForeignKey('TblproductSizeRanges', models.DO_NOTHING, db_column='RangeID')  # Field name made lowercase.
    size_number = models.IntegerField(db_column='Size_Number')  # Field name made lowercase.
    size_value = models.CharField(db_column='Size_Value', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_size_range_values'


class TblproductSizeRanges(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    rangeid = models.CharField(db_column='RangeID', max_length=10)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_size_ranges'


class TblproductStockingTypes(models.Model):
    #id = models.IntegerField(db_column='ID')
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    stockingtype = models.CharField(db_column='StockingType', primary_key=True, max_length=1)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_stocking_types'


class TblproductTypeofissue(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    issue_type = models.IntegerField(db_column='Issue_Type', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_typeofissue'


class TblproductUnitofissue(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    issue_units = models.IntegerField(db_column='Issue_Units', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_unitofissue'


class TblproductUnitofmeasure(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitID', primary_key=True)  # Field name made lowercase.
    unitshortcode = models.CharField(db_column='UnitShortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitdescription = models.CharField(db_column='UnitDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='Seqno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_unitofmeasure'


class TblproductUnitofmeasureCustomer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    unitid = models.ForeignKey(TblproductUnitofmeasure, models.DO_NOTHING, db_column='UnitID')  # Field name made lowercase.
    unitshortcode = models.CharField(db_column='UnitShortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_unitofmeasure_customer'


class TblproductUnitofmeasureconversion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    productid = models.ForeignKey(TblproductProducts, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    largerunit = models.IntegerField(db_column='LargerUnit')  # Field name made lowercase.
    smallerunit = models.IntegerField(db_column='SmallerUnit', blank=True, null=True)  # Field name made lowercase.
    ratio = models.IntegerField(db_column='Ratio', blank=True, null=True)  # Field name made lowercase.
    baseratio = models.IntegerField(db_column='BaseRatio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblproduct_unitofmeasureconversion'