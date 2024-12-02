import re
import graphene
from graphene_django.types import DjangoObjectType
from datetime import datetime
from Customer.models import (Tblcompany,TblbusCountries,TblaccNominal,TblbusCurrencies,TblaccVatcodes,
                               TblbusPaymentterms,TblbusAddresstypes,TblbusContactRef,TblgenUsers,
                               TblcustomerAddress,TblgenUsers,
                               )
from .models import (Tblsupplier,TblbusContactRef,TblsupplierAccount,
                     TblsupplierMemo, TblsupplierBalance, TblsupplierTurnover,
                     TblwhoWarehouses, TblsupplierAddress,TblwhoWarehousesTypes,
                     TblsupplierNotes,TblsupplierCategory1,TblsupplierCategory2,
                     TblsupplierCategory3,TblaccNominal,TblsupplierClass,TblbusCountries,
                     TblsupplierContact,TblsupplierSettings,TblsupplierSetvalues)
from django.db import transaction

from Product.utils import NextNo
from graphene_file_upload.scalars import Upload
from django.conf import settings
import os
import base64
import graphene
from decimal import Decimal, InvalidOperation
from graphql import GraphQLError
from datetime import datetime
from  Product.utils import parse_date

   
class TblsupplierCategory1Type(DjangoObjectType):
    class Meta:
        model = TblsupplierCategory1
        fields = '__all__'
 # Customercategory2 tbl query
class Tblsuppliercategory2Type(DjangoObjectType):
    class Meta:
        model = TblsupplierCategory2
        fields = '__all__'
# customercategory3 tbl query class define
class TblsupplierCategory3Type(DjangoObjectType):
    class Meta:
        model = TblsupplierCategory3
        fields = '__all__'

#  Class Tble quer define
class TblsupplierClassType(DjangoObjectType):
    class Meta:
        model = TblsupplierClass
        fields = '__all__'
# contact type query define
class TblsupplierContactType(DjangoObjectType):
    class Meta:
        model = TblsupplierContact
        fields = '__all__'
# Tblsupplier type query define
class TblsupplierType(DjangoObjectType):
    class Meta:
        model = Tblsupplier
        fields = '__all__'
# Note Tbl 
class TblsupplierNotesType(DjangoObjectType):
    class Meta:
        model = TblsupplierNotes
        fields = '__all__'
# Addresses type query define
class TblsupplierAddressType(DjangoObjectType):
    class Meta:
        model = TblsupplierAddress
        fields = '__all__'
# Warehouse Tbl query define 
class TblwhoWarehousesTypesType(DjangoObjectType): 
    class Meta:
        model = TblwhoWarehousesTypes
        fields = '__all__'            

# Memo query define 
class TblsupplierMemoType(DjangoObjectType):
    class Meta:
        model = TblsupplierMemo
        fields = '__all__'
# Turnover query define
class  TblsupplierTurnoverType(DjangoObjectType):
    class Meta:
        model = TblsupplierTurnover
        fields = '__all__'
    
# warehouse type    Tble query
class TblwhoWarehousesType(DjangoObjectType):
    class Meta:
        model = TblwhoWarehouses
        fields = '__all__'
# Balance query define
class  TblsupplierBalanceType(DjangoObjectType):
    class Meta:
        model = TblsupplierBalance
        fields = '__all__'

# Account type query 
class TblsupplierAccountType(DjangoObjectType):
    class Meta:
        model = TblsupplierAccount
        fields = '__all__'
        
class TblbusContactRefType(DjangoObjectType):
    class Meta:
        model = TblbusContactRef
        feilds = '__all__'



# Mutation Class Definition

class E4k_TblsupplierCategory1_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category1name = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.Boolean()
    customer_category1 = graphene.Field(TblsupplierCategory1Type)

    def mutate(self, info, companyid, category1name):
        try:
            # Check if category1name already exists for the company
            if TblsupplierCategory1.objects.filter(companyid=companyid, category1name=category1name).exists():
                return E4k_TblsupplierCategory1_Create(success=False, error=True)

            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblsupplier_category1', field_name='Category1ID', companyid=companyid)
            
            if next_no is None:
                return E4k_TblsupplierCategory1_Create(success=False, error=True)
            
            customer_category1 = TblsupplierCategory1(
                companyid_id=companyid,
                category1id=int(next_no),
                category1name=category1name
            )
            customer_category1.save()
            
            return E4k_TblsupplierCategory1_Create(success=True, error=False, customer_category1=customer_category1)

        except Exception:
            return E4k_TblsupplierCategory1_Create(success=False, error=True)



class E4k_TblsupplierCategory1_Update(graphene.Mutation):
    class Arguments:
        category1id = graphene.Int(required=True)
        category1name = graphene.String()

    success = graphene.Boolean()
    error = graphene.Boolean()
    customer_category1 = graphene.Field(TblsupplierCategory1Type)

    def mutate(self, info, category1id, category1name=None):
        try:
            customer_category1 = TblsupplierCategory1.objects.get(pk=category1id)

            # Check if category1name already exists for the company
            if category1name is not None and TblsupplierCategory1.objects.filter(
                companyid=customer_category1.companyid_id,
                category1name=category1name
            ).exclude(pk=category1id).exists():
                return E4k_TblsupplierCategory1_Update(success=False, error=True)

            if category1name:
                customer_category1.category1name = category1name
                customer_category1.save()
            
            return E4k_TblsupplierCategory1_Update(success=True, error=False, customer_category1=customer_category1)

        except TblsupplierCategory1.DoesNotExist:
            return E4k_TblsupplierCategory1_Update(success=False, error=True)
        except Exception:
            return E4k_TblsupplierCategory1_Update(success=False, error=True)

        

class E4k_TblsupplierCategory1_Delete(graphene.Mutation):
    class Arguments:
        category1id = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid,category1id):
        try:
            customer_category1 = TblsupplierCategory1.objects.get(category1id=category1id,companyid = companyid)
            customer_category1.delete()
            return E4k_TblsupplierCategory1_Delete(success=True)
        except TblsupplierCategory1.DoesNotExist:
            return E4k_TblsupplierCategory1_Delete(success=False)  


#######################################################################################################

class E4k_TblsupplierCategory2_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category2name = graphene.String(required=True)

    customer_category2 = graphene.Field(Tblsuppliercategory2Type)
    success = graphene.Boolean()
    error = graphene.Boolean()

    def mutate(self, info, companyid, category2name):
        # Check if category2name already exists for the company
        if TblsupplierCategory2.objects.filter(companyid=companyid, category2name=category2name).exists():
            raise Exception("Category2 name already exists for the company.")

        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblsupplier_category2', field_name='Category2ID', companyid=companyid)
        
        if next_no is None:
            raise Exception("Failed to generate next category2id")
        
        customer_category2 = TblsupplierCategory2(
            companyid_id=companyid,
            category2id=int(next_no),  # Ensure next_no is an integer
            category2name=category2name
        )
        customer_category2.save()
        
        return E4k_TblsupplierCategory2_Create(customer_category2=customer_category2, success=True)

##################

class E4k_TblsupplierCategory2_Update(graphene.Mutation):
    class Arguments:
        category2id = graphene.Int(required=True)
        category2name = graphene.String()

    customer_category2 = graphene.Field(Tblsuppliercategory2Type)
    success = graphene.Boolean()
    error = graphene.Boolean()

    def mutate(self, info, category2id, category2name=None):
        try:
            customer_category2 = TblsupplierCategory2.objects.get(pk=category2id)
        except TblsupplierCategory2.DoesNotExist:
            raise Exception("Category2 with the provided ID does not exist.")

        if category2name:
           
            
            if TblsupplierCategory2.objects.filter(category2name=category2name).exclude(pk=category2id).exists():
                raise Exception("Category2 name already exists.")

            customer_category2.category2name = category2name
            customer_category2.save()
        
        return E4k_TblsupplierCategory2_Update(customer_category2=customer_category2, success=True)

    

class E4k_TblsupplierCategory2_Delete(graphene.Mutation):
    class Arguments:
        category2id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        # category2name = graphene.String(required=True)
    success = graphene.Boolean()
    def mutate(self, info, category2id,companyid):
        try:
            customer_category2 = TblsupplierCategory2.objects.get(category2id=category2id,companyid = companyid)
            customer_category2.delete()
            return E4k_TblsupplierCategory2_Delete(success=True)
        except TblsupplierCategory2.DoesNotExist:
            return E4k_TblsupplierCategory2_Delete(success=False)
        

#######################################################################################################

class E4k_TblsupplierCategory3_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category3name = graphene.String(required=True)

    customer_category3 = graphene.Field(TblsupplierCategory3Type)
    success = graphene.Boolean()
    error = graphene.Boolean()

    def mutate(self, info, companyid, category3name):
        try:
            # Check if category3name already exists for the company
            if TblsupplierCategory3.objects.filter(companyid=companyid, category3name=category3name).exists():
                return E4k_TblsupplierCategory3_Create(success=False, error=True)

            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblsupplier_category3', field_name='Category3ID', companyid=companyid)
            
            if next_no is None:
                raise Exception("Failed to generate next category3id")
            
            customer_category3 = TblsupplierCategory3(
                companyid_id=companyid,
                category3id=int(next_no),  # Ensure next_no is an integer
                category3name=category3name
            )
            customer_category3.save()

            return E4k_TblsupplierCategory3_Create(customer_category3=customer_category3, success=True, error=False)
        
        except Exception as e:
            return E4k_TblsupplierCategory3_Create(success=False, error=True)


class E4k_TblsupplierCategory3_Update(graphene.Mutation):
    class Arguments:
        category3id = graphene.Int(required=True)
        category3name = graphene.String()

    customer_category3 = graphene.Field(TblsupplierCategory3Type)
    success = graphene.Boolean()
    error = graphene.Boolean()

    def mutate(self, info, category3id, category3name=None):
        try:
            customer_category3 = TblsupplierCategory3.objects.get(pk=category3id)
        except TblsupplierCategory3.DoesNotExist:
            return E4k_TblsupplierCategory3_Update(success=False, error=True)

        if category3name:
            # Check if category3name already exists for other categories
            if TblsupplierCategory3.objects.filter(category3name=category3name).exclude(pk=category3id).exists():
                return E4k_TblsupplierCategory3_Update(success=False, error=True)

            customer_category3.category3name = category3name
            customer_category3.save()

        return E4k_TblsupplierCategory3_Update(customer_category3=customer_category3, success=True, error=False)


class E4k_TblsupplierCategory3_Delete(graphene.Mutation):
    class Arguments:
        category3id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
    success = graphene.Boolean()
    def mutate(self, info, category3id,companyid):
        try:
            customer_category3 = TblsupplierCategory3.objects.get(pk=category3id,companyid=companyid)
            customer_category3.delete()
            return E4k_TblsupplierCategory3_Delete(success=True)
        except TblsupplierCategory3.DoesNotExist:
            return E4k_TblsupplierCategory3_Delete(success=False)
        
##########################################
# class E4k_TblsupplierClass_Create(graphene.Mutation):
#     class Arguments:
#         companyid = graphene.String(required=True)
#         class_name = graphene.String(required=True)

#     supplier_class = graphene.Field(TblsupplierClassType)
#     success =graphene.Boolean()
#     error =graphene.Boolean()

#     def mutate(self, info, companyid, class_name):
#         # Check if class_name already exists for the company
#         if TblsupplierClass.objects.filter(companyid=companyid, class_name=class_name).exists():
#             raise Exception("Class name already exists for the company.")

#         autonumber = NextNo()
#         next_no = autonumber.get_next_no(table_name='tblsupplier_class', field_name='ClassID', companyid=companyid)
        
#         if next_no is None:
#             raise Exception("Failed to generate next classid")

#         supplier_class = TblsupplierClass(
#             companyid_id=companyid,
#             classid=int(next_no),  # Ensure next_no is an integer
#             class_name=class_name
#         )
#         supplier_class.save()
        
#         return E4k_TblsupplierClass_Create(supplier_class=supplier_class)

# class E4k_TblsupplierClass_Update(graphene.Mutation):
#     class Arguments:
#         classid = graphene.Int(required=True)
#         class_name = graphene.String()

#     supplier_class = graphene.Field(TblsupplierClassType)
#     success = graphene.Boolean()
#     error = graphene.Boolean()

#     def mutate(self, info, classid, class_name=None):
#         try:
#             supplier_class = TblsupplierClass.objects.get(classid=classid)
#         except TblsupplierClass.DoesNotExist:
#             raise Exception("Supplier class with the provided ID does not exist.")

#         if class_name:
#             # Check if class_name already exists for other classes
#             if TblsupplierClass.objects.filter(class_name=class_name).exclude(classid=classid).exists():
#                 raise Exception("Class name already exists for other supplier classes.")

#             supplier_class.class_name = class_name
#             supplier_class.save()
        
#         return E4k_TblsupplierClass_Update(supplier_class=supplier_class) 

class E4k_TblsupplierClass_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        class_name = graphene.String(required=True)

    customer_class = graphene.Field(TblsupplierClassType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, class_name):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(pk=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
        
        # Check if class_name already exists for the given company
        if TblsupplierClass.objects.filter(companyid=companyid, class_name=class_name).exists():
            errors.append("Class name already exists for this company.")

        if errors:
            return E4k_TblsupplierClass_Create(success=False, error=", ".join(errors))

        # Generate the next ClassID
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblsupplier_class', field_name='ClassID', companyid=companyid)
        
        if next_no is None:
            return E4k_TblsupplierClass_Create(success=False, error="Failed to generate next ClassID")

        # Create the customer class instance
        try:
            customer_class = TblsupplierClass(
                companyid=company,
                classid=int(next_no),  # Ensure next_no is an integer
                class_name=class_name
            )
            customer_class.save()
            return E4k_TblsupplierClass_Create(customer_class=customer_class, success=True)
        except Exception as e:
            return E4k_TblsupplierClass_Create(success=False, error=str(e))


class E4k_TblsupplierClass_Update(graphene.Mutation):
    class Arguments:
        classid = graphene.Int(required=True)
        class_name = graphene.String()

    customer_class = graphene.Field(TblsupplierClassType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, classid, class_name=None):
        try:
            customer_class = TblsupplierClass.objects.get(classid=classid)
        except TblsupplierClass.DoesNotExist:
            return E4k_TblsupplierClass_Update(success=False, error="ClassID does not exist.")

        if class_name:
            # Check if the new class_name already exists for the same company
            if TblsupplierClass.objects.filter(companyid=customer_class.companyid, class_name=class_name).exists():
                return E4k_TblsupplierClass_Update(success=False, error="Class name already exists for this company.")

            customer_class.class_name = class_name
            try:
                customer_class.save()
                return E4k_TblsupplierClass_Update(customer_class=customer_class, success=True)
            except Exception as e:
                return E4k_TblsupplierClass_Update(success=False, error=str(e))
        else:
            return E4k_TblsupplierClass_Update(success=False, error="No updates provided.")
        
        
class E4k_TblsupplierClass_Delete(graphene.Mutation):
    class Arguments:
        classid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, classid,companyid):
        try:
            supplier_class = TblsupplierClass.objects.get(classid=classid,companyid=companyid)
            supplier_class.delete()
            return E4k_TblsupplierClass_Delete(success=True)
            

        except TblsupplierClass.DoesNotExist:
            return E4k_TblsupplierClass_Delete(success=False)

########################################################################

class E4k_Tblsupplier_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        name = graphene.String()
        countryid = graphene.Int()
        islive = graphene.Boolean()
        category1id = graphene.Int()
        category2id = graphene.Int()
        category3id = graphene.Int()
        classid = graphene.Int()
        default_nominal = graphene.Int()
        isextract = graphene.Boolean()
        isstop = graphene.Boolean()

    customer = graphene.Field(TblsupplierType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, name=None, countryid=None, islive=True, category1id=None, category2id=None, category3id=None, classid=None, default_nominal=None, isextract=False, isstop=None):
        errors = []

        # Check if companyid exists
        if not Tblsupplier.objects.filter(companyid=companyid).exists():
            errors.append("CompanyID does not exist.")

        # Check if countryid exists
        if countryid is not None and not TblbusCountries.objects.filter(countryid=countryid).exists():
            errors.append("CountryID does not exist.")

        # if TblaccNominalCountries.objects.filter(countryid = countryid).exists():
        #     errors.append("CountryID already exists.")
        
        if  Tblsupplier.objects.filter( businessid = businessid).exists():
            errors.append("BusinessID already exists.")

        # Check if category1id exists
        if category1id is not None and not TblsupplierCategory1.objects.filter(category1id=category1id).exists():
            errors.append("Category1ID does not exist.")
        
        # Check if category2id exists
        if category2id is not None and not TblsupplierCategory2.objects.filter(category2id=category2id).exists():
            errors.append("Category2ID does not exist.")
        
        # Check if category3id exists
        if category3id is not None and not TblsupplierCategory3.objects.filter(category3id=category3id).exists():
            errors.append("Category3ID does not exist.")
        
        # Check if classid exists
        if classid is not None and not TblsupplierClass.objects.filter(classid=classid).exists():
            errors.append("ClassID does not exist.")
        
  
        # Check if default_nominal exists
        if default_nominal is not None and not TblaccNominal.objects.filter(nomcode=default_nominal).exists():
            errors.append("Default_Nominal does not exist.")
        
        # If there are errors, return the errors
        if errors:
            return E4k_Tblsupplier_Create(success=False, error=", ".join(errors))

        # Create the customer
        try:
            customer = Tblsupplier(
                companyid_id=companyid,
                businessid=businessid,
                name=name,
                countryid_id=countryid,
                islive=islive,
                category1id_id=category1id,
                category2id_id=category2id,
                category3id_id=category3id,
                classid_id=classid,
                default_nominal_id=default_nominal,
                isextract=isextract,
                isstop=isstop
            )
            customer.save()
            return E4k_Tblsupplier_Create(customer=customer, success=True)
        except Exception as e:
            return E4k_Tblsupplier_Create(success=False, error=str(e))



##############################################################

# class E4k_Tblsupplier_Update(graphene.Mutation):
#     class Arguments:
#         businessid = graphene.String(required=True)
#         companyid = graphene.String()
#         name = graphene.String()
#         countryid = graphene.Int()
#         islive = graphene.Boolean()
#         category1id = graphene.Int()
#         category2id = graphene.Int()
#         category3id = graphene.Int()
#         classid = graphene.Int()
#         default_nominal = graphene.Int()
#         isextract = graphene.Boolean()
#         isstop = graphene.Boolean()

#     customer = graphene.Field(TblsupplierType)
#     success = graphene.Boolean()
#     error = graphene.String()

#     def mutate(self, info, businessid, companyid=None, name=None, countryid=None, islive=None, category1id=None, category2id=None, category3id=None, classid=None, default_nominal=None, isextract=None, isstop=None):
#         try:
#             customer = Tblsupplier.objects.get(businessid=businessid)
            
         

#             # Update the customer fields if provided
#             if companyid is not None:
#                 customer.companyid_id = companyid
#             if name is not None:
#                 customer.name = name
#             if countryid is not None:
#                 customer.countryid_id = countryid
#             if islive is not None:
#                 customer.islive = islive
#             if category1id is not None:
#                 customer.category1id_id = category1id
#             if category2id is not None:
#                 customer.category2id_id = category2id
#             if category3id is not None:
#                 customer.category3id_id = category3id
#             if classid is not None:
#                 customer.classid_id = classid
#             if default_nominal is not None:
#                 customer.default_nominal_id = default_nominal
#             if isextract is not None:
#                 customer.isextract = isextract
#             if isstop is not None:
#                 customer.isstop = isstop

#             customer.save()
#             return E4k_Tblsupplier_Update(customer=customer, success=True)
#         except Tblsupplier.DoesNotExist:
#             return E4k_Tblsupplier_Update(success=False, error="Customer not found.")
#         except Exception as e:
#             return E4k_Tblsupplier_Update(success=False, error=str(e))


class E4k_Tblsupplier_Update(graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        companyid = graphene.String()
        name = graphene.String()
        countryid = graphene.Int()
        islive = graphene.Boolean()
        category1id = graphene.Int()
        category2id = graphene.Int()
        category3id = graphene.Int()
        classid = graphene.Int()
        default_nominal = graphene.Int()
        isextract = graphene.Boolean()
        isstop = graphene.Boolean()

    customer = graphene.Field(TblsupplierType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, businessid, companyid=None, name=None, countryid=None, islive=None, category1id=None, category2id=None, category3id=None, classid=None, default_nominal=None, isextract=None, isstop=None):
        try:
            customer = Tblsupplier.objects.get(businessid=businessid)

            # Set default value of 0 if any of the Int fields are not provided
            if companyid is not None:
                customer.companyid_id = companyid
            if name is not None:
                customer.name = name

            customer.countryid_id = countryid if countryid is not None else 0
            customer.category1id_id = category1id if category1id is not None else 0
            customer.category2id_id = category2id if category2id is not None else 0
            customer.category3id_id = category3id if category3id is not None else 0
            customer.classid_id = classid if classid is not None else 0
            customer.default_nominal_id = default_nominal if default_nominal is not None else 0

            # Update boolean fields if provided
            if islive is not None:
                customer.islive = islive
            if isextract is not None:
                customer.isextract = isextract
            if isstop is not None:
                customer.isstop = isstop

            # Save the updated customer
            customer.save()
            return E4k_Tblsupplier_Update(customer=customer, success=True)

        except Tblsupplier.DoesNotExist:
            return E4k_Tblsupplier_Update(success=False, error="Customer not found.")
        except Exception as e:
            return E4k_Tblsupplier_Update(success=False, error=str(e))


########################################################################################################################################
class E4k_Tblsupplier_Delete(graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info,companyid, businessid):
        try:
            customer = Tblsupplier.objects.get(businessid=businessid,companyid = companyid )
            customer.isextract = customer.isextract  == b'\x01'
            customer.isstop= customer.isstop  == b'\x01'
            customer.islive = customer.isstop == b'\x01'
            customer.save()
            return E4k_Tblsupplier_Delete(success=True)
        except Tblsupplier.DoesNotExist:
            return E4k_Tblsupplier_Delete(success=False, error="Customer not found.")
        except Exception as e:
            return E4k_Tblsupplier_Delete(success=False, error=str(e))

#################################

class E4k_TblsupplierNotes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        note = graphene.String()
        userid = graphene.String()
        # note_date = graphene.DateTime()

    customer_note = graphene.Field(TblsupplierNotesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, note=None, userid=None):
        try:
            # Validation for foreign keys

            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierNotes_Create(success=False, error="CompanyID does not exist.")
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierNotes_Create(success=False, error="BusinessID does not exist.")
            if userid and not TblgenUsers.objects.filter(userid=userid).exists():
                return E4k_TblsupplierNotes_Create(success=False, error="UserID does not exist.")

            # Set the current date and time if note_date is not provided
            note_date = datetime.now()


            customer_note = TblsupplierNotes(
                companyid_id=companyid,
                businessid_id=businessid,
                note=note,
                userid_id=userid,
                note_date=note_date
            )
            customer_note.save()
            return E4k_TblsupplierNotes_Create(customer_note=customer_note, success=True)
        except Exception as e:
            return E4k_TblsupplierNotes_Create(success=False, error=str(e))


#################################################################################################################################################

class E4k_TblsupplierNotes_Update(graphene.Mutation):
    class Arguments:
        noteid = graphene.Int(required=True)
        companyid = graphene.String()
        businessid = graphene.String()
        note = graphene.String()
        userid = graphene.String()

    customer_note = graphene.Field(TblsupplierNotesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, noteid, companyid=None, businessid=None, note=None, userid=None):
        try:
            customer_note = TblsupplierNotes.objects.get(noteid=noteid)
            
            if companyid is not None:
                if not Tblcompany.objects.filter(companyid=companyid).exists():
                    return E4k_TblsupplierNotes_Update(success=False, error="CompanyID does not exist.")
                customer_note.companyid_id = companyid

            if businessid is not None:
                if not Tblsupplier.objects.filter(businessid=businessid).exists():
                    return E4k_TblsupplierNotes_Update(success=False, error="BusinessID does not exist.")
                customer_note.businessid_id = businessid

            if userid is not None:
                if not TblgenUsers.objects.filter(userid=userid).exists():
                    return E4k_TblsupplierNotes_Update(success=False, error="UserID does not exist.")
                customer_note.userid_id = userid

            if note is not None:
                customer_note.note = note

            # Update the note_date to the current date and time
            customer_note.note_date = datetime.now()

            customer_note.save()
            return E4k_TblsupplierNotes_Update(customer_note=customer_note, success=True)
        except TblsupplierNotes.DoesNotExist:
            return E4k_TblsupplierNotes_Update(success=False, error="Customer Note not found.")
        except Exception as e:
            return E4k_TblsupplierNotes_Update(success=False, error=str(e))
        


##############################################################################################
class E4k_TblsupplierNote_Delete(graphene.Mutation):
    class Arguments:
        noteid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info,companyid, noteid):
        
        try:
            customer_note = TblsupplierNotes.objects.get(noteid=noteid,companyid= companyid)
            customer_note.delete()
            return E4k_TblsupplierNote_Delete(success=True)
        except TblsupplierNotes.DoesNotExist:
            return E4k_TblsupplierNote_Delete(success=False, error="Customer Note not found.")
        except Exception as e:
            return E4k_TblsupplierNote_Delete(success=False, error=str(e))

#######################################
class E4k_TblsupplierAddress_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        description = graphene.String()
        address1 = graphene.String()
        address2 = graphene.String()
        address3 = graphene.String()
        city = graphene.String()
        county = graphene.String()
        postcode = graphene.String()
        countrycode = graphene.Int()
        addresstypeid = graphene.Int()

    supplier_address = graphene.Field(TblsupplierAddressType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, description=None, address1=None, address2=None, address3=None, city=None, county=None, postcode=None, countrycode=None, addresstypeid=None):
        try:
            # Get the next auto-generated number
            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblsupplier_address',field_name='AddressID',companyid=companyid)
            print(next_no)
            if not next_no:
                return E4k_TblsupplierAddress_Create(success=False, error="No auto numbers found for the given parameters.")

            # Validation for foreign keys
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierAddress_Create(success=False, error="CompanyID does not exist.")
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierAddress_Create(success=False, error="BusinessID does not exist.")
            if countrycode and not TblbusCountries.objects.filter(countryid=countrycode).exists():
                return E4k_TblsupplierAddress_Create(success=False, error="CountryCode does not exist.")
            if addresstypeid and not TblbusAddresstypes.objects.filter(addresstypeid=addresstypeid).exists():
                return E4k_TblsupplierAddress_Create(success=False, error="AddressTypeID does not exist.")
            # if TblsupplierAddress.objects.filter(addresstypeid=addresstypeid).exists():
            #     return E4k_TblsupplierAddress_Create(success=False, error="AddressTypeID already exists.")

            # Create new address
            supplier_address = TblsupplierAddress(
                companyid_id=companyid,
                businessid_id=businessid,
                description=description,
                address1=address1,
                address2=address2,
                address3=address3,
                addressid=next_no,
                city=city,
                county=county,
                postcode=postcode,
                countrycode_id=countrycode,  # Assuming this is correct based on your schema
                addresstypeid_id=addresstypeid
            )
            supplier_address.save()
            return E4k_TblsupplierAddress_Create(supplier_address=supplier_address, success=True)

        except Exception as e:
            return E4k_TblsupplierAddress_Create(success=False, error=str(e))



# Update customer address


class E4k_TblsupplierAddress_Update(graphene.Mutation):
    class Arguments:
        addressid = graphene.Int(required=True)
        companyid = graphene.String()
        businessid = graphene.String()
        description = graphene.String()
        address1 = graphene.String()
        address2 = graphene.String()
        address3 = graphene.String()
        city = graphene.String()
        county = graphene.String()
        postcode = graphene.String()
        countrycode = graphene.Int()  # Changed from countryid to countrycode
        addresstypeid = graphene.Int()

    customer_address = graphene.Field(TblsupplierAddressType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, addressid, companyid=None, businessid=None, description=None, address1=None, address2=None, address3=None, city=None, county=None, postcode=None, countrycode=None, addresstypeid=None):
        try:
        
            
            customer_address = TblsupplierAddress.objects.get(addressid=addressid)

            if companyid is not None:
                if not Tblcompany.objects.filter(companyid=companyid).exists():
                    return E4k_TblsupplierAddress_Update(success=False, error="CompanyID does not exist.")
                customer_address.companyid_id = companyid

            if businessid is not None:
                if not Tblsupplier.objects.filter(businessid=businessid).exists():
                    return E4k_TblsupplierAddress_Update(success=False, error="BusinessID does not exist.")
                customer_address.businessid_id = businessid

            if countrycode is not None:
                country = TblbusCountries.objects.filter(countryid=countrycode).first()
                if country:
                    customer_address.countrycode = country  
                else:
                    return  E4k_TblsupplierAddress_Update (success=False, error="CountryCode does not exist.")
                       

            if addresstypeid is not None:
                if not TblbusAddresstypes.objects.filter(addresstypeid=addresstypeid).exists():  # Changed from id to addresstypeid
                    return E4k_TblsupplierAddress_Update(success=False, error="AddressTypeID does not exist.")
                customer_address.addresstypeid_id = addresstypeid

            if description is not None:
                customer_address.description = description

            if address1 is not None:
                customer_address.address1 = address1

            if address2 is not None:
                customer_address.address2 = address2

            if address3 is not None:
                customer_address.address3 = address3

            if city is not None:
                customer_address.city = city

            if county is not None:
                customer_address.county = county

            if postcode is not None:
                customer_address.postcode = postcode

            customer_address.save()
            return E4k_TblsupplierAddress_Update(customer_address=customer_address, success=True)
        except TblcustomerAddress.DoesNotExist:
            return E4k_TblsupplierAddress_Update(success=False, error="Customer Address not found.")
        except Exception as e:
            return E4k_TblsupplierAddress_Update(success=False, error=str(e))

class E4k_TblsupplierAddress_Delete(graphene.Mutation):
    class Arguments:
        addressid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, addressid, companyid):
        try:
            customer_address = TblsupplierAddress.objects.get(addressid=addressid,companyid=companyid)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierAddress_Delete(success=False, error="CompanyID does not exist.")
            customer_address.delete()
            return E4k_TblsupplierAddress_Delete(success=True)
        except TblcustomerAddress.DoesNotExist:
            return E4k_TblsupplierAddress_Delete(success=False, error="Customer Address not found.")
        except Exception as e:
            return E4k_TblsupplierAddress_Delete(success=False, error=str(e))

##########################################################
class   E4k_TblwhoWarehousesTypes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        # whtypeid  = graphene.Int()
        whtype = graphene.String()
    
    whtype = graphene.Field(TblwhoWarehousesTypesType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, companyid, whtypeid=None, whtype=None):
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblwho_warehouses_type', field_name='whtypeid', companyid=companyid)
        try:
            company = Tblcompany.objects.get(companyid=companyid);
            
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblwhoWarehousesTypes_Create(success=False, error="CompanyID does not exist.")
            if whtypeid and not TblwhoWarehousesTypes.objects.filter(companyid = company , whtypeid=whtypeid).exists():
                return E4k_TblwhoWarehousesTypes_Create(success=False, error="WHTypeID does not exist.")
          
            
            # Create new address
            whtype = TblwhoWarehousesTypes(
                companyid_id=companyid,
                whtypeid=next_no,
                whtype=whtype
            )
            whtype.save()
            return E4k_TblwhoWarehousesTypes_Create( whtype= whtype, success=True)
        except Exception as e:
            return E4k_TblwhoWarehousesTypes_Create(success=False, error=str(e))
         
class E4k_TblwhoWarehousesTypes_Update(graphene.Mutation):
    class Arguments:
        whtypeid = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        whtype = graphene.String()  # Renamed the input argument to avoid conflict
    
    whtype = graphene.Field(TblwhoWarehousesTypesType)
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, whtypeid, companyid, whtype=None):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            
            whtype_instance = TblwhoWarehousesTypes.objects.get(whtypeid=whtypeid)  # Renamed variable to avoid conflict
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblwhoWarehousesTypes_Update(success=False, error="CompanyID does not exist.")
         
            if whtype is not None:
                whtype_instance.whtype = whtype  # Correctly assign the new whtype value
            whtype_instance.save()
            return E4k_TblwhoWarehousesTypes_Update(companyid = company ,whtype=whtype_instance, success=True)
        except TblwhoWarehousesTypes.DoesNotExist:
            return E4k_TblwhoWarehousesTypes_Update(success=False, error="Warehouse Type not found.")
        except Exception as e:
            return E4k_TblwhoWarehousesTypes_Update(success=False, error=str(e))

        
class E4k_TblwhoWarehousesTypes_Delete(graphene.Mutation):
    class Arguments:
        whtypeid = graphene.Int(required=True)
        companyid = graphene.String(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, whtypeid, companyid):
        try:
            whtype = TblwhoWarehousesTypes.objects.get(whtypeid=whtypeid,companyid=companyid)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblwhoWarehousesTypes_Delete(success=False, error="CompanyID does not exist.")
            whtype.delete()
            return E4k_TblwhoWarehousesTypes_Delete(success=True)
        except TblwhoWarehousesTypes.DoesNotExist:
            return E4k_TblwhoWarehousesTypes_Delete(success=False, error="WareHouse Type not found.")
        except Exception as e:
            return E4k_TblwhoWarehousesTypes_Delete(success=False, error=str(e))

################################################################

class E4k_TblsupplierMemo_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        userid  = graphene.String(required=True)
        memotext = graphene.String()
        # lastupdatedate = graphene.DateTime()
    
    memo = graphene.Field(TblsupplierMemoType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, companyid, businessid, userid,id=None , memotext=None, lastupdatedate=None):
        lastupdatedate =datetime.now()
        
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierMemo_Create(success=False, error="CompanyID does not exist.")
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierMemo_Create(success=False, error="BusinessID does not exist.")
            if not TblgenUsers.objects.filter(userid=userid).exists():
                return E4k_TblsupplierMemo_Create(success=False, error="UserID does not exist.")
            
            # Create new address
            memo = TblsupplierMemo(
                companyid_id=companyid,
                id = id,
                businessid_id=businessid,
                userid_id=userid,
                memotext=memotext,
                lastupdatedate=lastupdatedate
            )
            memo.save()
            return E4k_TblsupplierMemo_Create( memo= memo, success=True)
        except Exception as e:
            return E4k_TblsupplierMemo_Create(success=False, error=str(e))

class E4k_TblsupplierMemo_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        userid  = graphene.String(required=True)
        memotext = graphene.String()
        # lastupdatedate = graphene.DateTime()
    
    memo = graphene.Field(TblsupplierMemoType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, id, companyid, businessid, userid, memotext=None, lastupdatedate=None):
        lastupdatedate =datetime.now()
        try:
            memo_instance = TblsupplierMemo.objects.get(id=id)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierMemo_Update(success=False, error="CompanyID does not exist.")
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierMemo_Update(success=False, error="BusinessID does not exist.")
            if not TblgenUsers.objects.filter(userid=userid).exists():
                return E4k_TblsupplierMemo_Update(success=False, error="UserID does not exist.")
            
            if memotext is not None:
                memo_instance.memotext = memotext
            if lastupdatedate is not None:
                memo_instance.lastupdatedate = lastupdatedate
            memo_instance.save()
            return E4k_TblsupplierMemo_Update(memo=memo_instance, success=True)
        except TblsupplierMemo.DoesNotExist:
            return E4k_TblsupplierMemo_Update(success=False, error="Memo not found.")
        except Exception as e:
            return E4k_TblsupplierMemo_Update(success=False, error=str(e))
        
class E4k_TblsupplierMemo_Delete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, id, companyid):
        try:
            memo = TblsupplierMemo.objects.get(id=id,companyid=companyid)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierMemo_Delete(success=False, error="CompanyID does not exist.")
            memo.delete()
            return E4k_TblsupplierMemo_Delete(success=True)
        except TblsupplierMemo.DoesNotExist:
            return E4k_TblsupplierMemo_Delete(success=False, error="Memo not found.")
        except Exception as e:
            return E4k_TblsupplierMemo_Delete(success=False, error=str(e))

class E4k_TblsupplierContact_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        addressid = graphene.String()
        contacttype_id = graphene.String()
        value = graphene.String()
    
    contact = graphene.Field(TblsupplierContactType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, addressid=None, contacttype_id=None, value=None):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierContact_Create(success=False, error="CompanyID does not exist.")
            if not TblsupplierAddress.objects.filter(addressid=addressid).exists():
                return E4k_TblsupplierContact_Create(success=False, error="AddressID does not exist.")
            if not TblbusContactRef.objects.filter(contacttype_id=contacttype_id).exists():
                return E4k_TblsupplierContact_Create(success=False, error="ContactType does not exist.")

            # Retrieve the contact type instance
            contact_type_instance = TblbusContactRef.objects.get(contacttype_id=contacttype_id)
            
            if contacttype_id =='1':
                 if not re.match(r'^\+?[1-9]\d{0,10}[-.\s]?(\(?\d{1,100}?\)?[-.\s]?|\d{1,100}[-.\s]?)?\d{1,100}[-.\s]?\d{1,100}[-.\s]?\d{1,100}$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Telephone number format.")


            if contacttype_id == '3':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Email format.")
            if contacttype_id == '5':
                 if not re.match(r'^\+?[1-9]\d{0,10}[-.\s]?(\(?\d{1,100}?\)?[-.\s]?|\d{1,100}[-.\s]?)?\d{1,100}[-.\s]?\d{1,100}[-.\s]?\d{1,100}$', value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Mobile number format.")
                
                
            if contacttype_id == '8':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Email format.")
                
            if contacttype_id == '9':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Email format.")
            
            if contacttype_id == '11':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Email format.")
            if contacttype_id == '25':
                if not re.match(r'^[YyNn]$',value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Yes/No format.")
            if contacttype_id == '27':
                if not re.match(r'^[YyNn]$', value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Yes/No format.")
                
            if contacttype_id == '31':
                if not re.match(r'^\+?[1-9]\d{0,10}[-.\s]?(\(?\d{1,100}?\)?[-.\s]?|\d{1,100}[-.\s]?)?\d{1,100}[-.\s]?\d{1,100}[-.\s]?\d{1,100}$', value):
                    return E4k_TblsupplierContact_Create(success=False, error="Invalid Telephone number format.")
            


            # Create new contact
            contact = TblsupplierContact(
                companyid_id=companyid,
                addressid_id=addressid,
                contacttype=contact_type_instance,  # Assign the instance instead of the ID
                value=value
            )
            contact.save()
            return E4k_TblsupplierContact_Create(contact=contact, success=True)
        except Exception as e:
            return E4k_TblsupplierContact_Create(success=False, error=str(e))

        
class E4k_TblsupplierContact_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        addressid = graphene.String()
        contacttype_id = graphene.String()
        value = graphene.String()
    
    contact = graphene.Field(TblsupplierContactType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id, companyid, addressid=None, contacttype_id=None, value=None):
        try:
            contact_instance = TblsupplierContact.objects.get(id=id, companyid=companyid)

            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierContact_Update(success=False, error="CompanyID does not exist.")
            
            if addressid is not None and not TblsupplierAddress.objects.filter(addressid=addressid).exists():
                return E4k_TblsupplierContact_Update(success=False, error="AddressID does not exist.")
            
            if contacttype_id is not None:
                contact_type_instance = TblbusContactRef.objects.get(contacttype_id=contacttype_id)
                
            if contacttype_id =='1':
                if not re.match(r'^\+?[1-9]\d{0,10}[-.\s]?(\(?\d{1,100}?\)?[-.\s]?|\d{1,100}[-.\s]?)?\d{1,100}[-.\s]?\d{1,100}[-.\s]?\d{1,100}$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Telephone number format.")


            if contacttype_id == '3':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Email format.")
            if contacttype_id == '5':
                if not re.match(r'^\+?[1-9]\d{0,10}[-.\s]?(\(?\d{1,100}?\)?[-.\s]?|\d{1,100}[-.\s]?)?\d{1,100}[-.\s]?\d{1,100}[-.\s]?\d{1,100}$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Mobile number format.")
                
                
            if contacttype_id == '8':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Email format.")
                
            if contacttype_id == '9':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Email format.")
            
            if contacttype_id == '11':
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Email format.")
                
            if contacttype_id == '31':
                if not re.match(r'^\+?[1-9]\d{0,10}[-.\s]?(\(?\d{1,100}?\)?[-.\s]?|\d{1,100}[-.\s]?)?\d{1,100}[-.\s]?\d{1,100}[-.\s]?\d{1,100}$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Telphone number format.")
            if contacttype_id == '25':
                if not re.match(r'^[YyNn]$',value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Yes/No format.")
            if contacttype_id == '27':
                if not re.match(r'^[YyNn]$', value):
                    return E4k_TblsupplierContact_Update(success=False, error="Invalid Yes/No format.")

            # Assign values to the contact instance
            if addressid is not None:
                contact_instance.addressid = TblsupplierAddress.objects.get(addressid=addressid)
            if contacttype_id is not None:
                contact_instance.contacttype = contact_type_instance
            if value is not None:
                contact_instance.value = value
            
            contact_instance.save()
            return E4k_TblsupplierContact_Update(contact=contact_instance, success=True)

        except TblsupplierContact.DoesNotExist:
            return E4k_TblsupplierContact_Update(success=False, error="Contact not found.")
        except Exception as e:
            return E4k_TblsupplierContact_Update(success=False, error=str(e))

    

class E4k_TblsupplierContact_Delete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id, companyid):
        try:
            contact = TblsupplierContact.objects.get(id=id,companyid=companyid)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierContact_Delete(success=False, error="CompanyID does not exist.")
            contact.delete()
            return E4k_TblsupplierContact_Delete(success=True)
        except TblsupplierContact.DoesNotExist:
            return E4k_TblsupplierContact_Delete(success=False, error="Contact not found.")
        except Exception as e:
            return E4k_TblsupplierContact_Delete(success=False, error=str(e))

##################    

class E4k_TblsupplierTurnover_Create(graphene.Mutation):
    class Arguments:    
        companyid = graphene.String(required=True)
        businessid = graphene.String() 
        period = graphene.Int()
        year = graphene.Int()
        turnover = graphene.Decimal()

    turnover = graphene.Field(TblsupplierTurnoverType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid=None, period=None, year=None, turnover=None):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierTurnover_Create(success=False, error="CompanyID does not exist.")
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierTurnover_Create(success=False, error="BusinessID does not exist.")

            # Create new turnover instance
            turnover_instance = TblsupplierTurnover(
                companyid_id=companyid,
                businessid_id=businessid,
                period=period,
                year=year,
                turnover=turnover
            )
            turnover_instance.save()
            return E4k_TblsupplierTurnover_Create(turnover=turnover_instance, success=True)
        except Exception as e:
            return E4k_TblsupplierTurnover_Create(success=False, error=str(e))

class E4k_TblsupplierTurnover_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        businessid = graphene.String()
        period = graphene.Int()
        year = graphene.Int()
        turnover = graphene.Decimal()
    
    turnover = graphene.Field(TblsupplierTurnoverType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id, companyid, businessid=None, period=None, year=None, turnover=None):
        try:
            turnover_instance = TblsupplierTurnover.objects.get(id=id)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierTurnover_Update(success=False, error="CompanyID does not exist.")
            if businessid and not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierTurnover_Update(success=False, error="BusinessID does not exist.")

            if businessid is not None:
                turnover_instance.businessid = Tblsupplier.objects.get(businessid=businessid)
            if period is not None:
                turnover_instance.period = period
            if year is not None:
                turnover_instance.year = year
            if turnover is not None:
                turnover_instance.turnover = turnover

            turnover_instance.save()
            return E4k_TblsupplierTurnover_Update(turnover=turnover_instance, success=True)
        except TblsupplierTurnover.DoesNotExist:
            return E4k_TblsupplierTurnover_Update(success=False, error="Turnover not found.")
        except Exception as e:
            return E4k_TblsupplierTurnover_Update(success=False, error=str(e))

        
class E4k_TblsupplierTurnover_Delete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, id, companyid):
        try:
            turnover = TblsupplierTurnover.objects.get(id=id, companyid = companyid)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierTurnover_Delete(success=False, error="CompanyID does not exist.")
            turnover.delete()
            return E4k_TblsupplierTurnover_Delete(success=True)
        except TblsupplierTurnover.DoesNotExist:
            return E4k_TblsupplierTurnover_Delete(success=False, error="Turnover not found.")
        except Exception as e:
            return E4k_TblsupplierTurnover_Delete(success=False, error=str(e))


######################################################################
class E4k_TblwhoWarehouses_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        warehouseid = graphene.String(required=True)
        warehousename = graphene.String(required=True)
        locationcontroled = graphene.Boolean(required=True)
        noofaisles = graphene.Int(required=True)
        noofbays = graphene.Int(required=True)
        noofshelfs = graphene.Int(required=True)
        # datecreated = graphene.Date(required=True)
        createdby = graphene.String()
        updateby  = graphene.String()
        # dateupdated = graphene.Date()   
        address1  = graphene.String()
        address2 = graphene.String()
        address3 = graphene.String()
        address4 = graphene.String()
        postcode = graphene.String()
        live = graphene.Boolean()
        phone = graphene.String()
        fax  = graphene.String()
        email = graphene.String()
        vatno = graphene.String()
        whtypeid = graphene.String()  
    
    TblwhoWarehouses = graphene.Field(TblwhoWarehousesType)
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, companyid, warehouseid, warehousename, locationcontroled, noofaisles, noofbays, noofshelfs, createdby, updateby, address1, address2, address3, address4, postcode, live, phone, fax, email, vatno, whtypeid):
        datecreated = datetime.now()
        dateupdated = datetime.now()
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblwhoWarehouses_Create(success=False, error="CompanyID does not exist.")
            if not TblwhoWarehousesTypes.objects.filter(whtypeid=whtypeid).exists():
                return E4k_TblwhoWarehouses_Create(success=False, error="WarehouseID does not exist.")
            if TblwhoWarehouses.objects.filter(warehouseid=warehouseid).exists():
                return E4k_TblwhoWarehouses_Create(success=False, error="WarehouseID already exists.")
            
            # Create new warehouse instance
            warehouse_instance = TblwhoWarehouses(
                companyid_id=companyid,
                warehouseid=warehouseid,
                warehousename=warehousename,
                locationcontroled=locationcontroled,
                noofaisles=noofaisles,
                noofbays=noofbays,
                noofshelfs=noofshelfs,
                datecreated=datecreated,
                createdby=createdby,
                updateby=updateby,
                dateupdated=dateupdated,
                address1=address1,
                address2=address2,
                address3=address3,
                address4=address4,
                postcode=postcode,
                live=live,
                phone=phone,
                fax=fax,
                email=email,
                vatno=vatno,
                whtypeid_id=whtypeid
            )
            warehouse_instance.save()
            return E4k_TblwhoWarehouses_Create(TblwhoWarehouses=warehouse_instance, success=True)
        except Exception as e:
            return E4k_TblwhoWarehouses_Create(success=False, error=str(e))
         
class E4k_TblwhoWarehouses_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        warehouseid = graphene.String(required=True)
        warehousename = graphene.String()
        locationcontroled = graphene.Boolean()
        noofaisles = graphene.Int()
        noofbays = graphene.Int()
        noofshelfs = graphene.Int()
        createdby = graphene.String()
        updateby = graphene.String()
        address1 = graphene.String()
        address2 = graphene.String()
        address3 = graphene.String()
        address4 = graphene.String()
        postcode = graphene.String()
        live = graphene.Boolean()
        phone = graphene.String()
        fax = graphene.String()
        email = graphene.String()
        vatno = graphene.String()
        whtypeid = graphene.String()

    TblwhoWarehouses = graphene.Field(TblwhoWarehousesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, warehouseid, warehousename=None, locationcontroled=None, noofaisles=None, noofbays=None, noofshelfs=None, createdby=None, updateby=None, address1=None, address2=None, address3=None, address4=None, postcode=None, live=None, phone=None, fax=None, email=None, vatno=None, whtypeid=None):
        try:
            warehouse_instance = TblwhoWarehouses.objects.get(warehouseid=warehouseid)
            
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblwhoWarehouses_Update(success=False, error="CompanyID does not exist.")
            
            if whtypeid and not TblwhoWarehousesTypes.objects.filter(whtypeid=whtypeid).exists():
                return E4k_TblwhoWarehouses_Update(success=False, error="Warehouse Type ID does not exist.")

            if warehousename is not None:
                warehouse_instance.warehousename = warehousename
            if locationcontroled is not None:
                warehouse_instance.locationcontroled = locationcontroled
            if noofaisles is not None:
                warehouse_instance.noofaisles = noofaisles
            if noofbays is not None:
                warehouse_instance.noofbays = noofbays
            if noofshelfs is not None:
                warehouse_instance.noofshelfs = noofshelfs
            if createdby is not None:
                warehouse_instance.createdby = createdby
            if updateby is not None:
                warehouse_instance.updateby = updateby
            if address1 is not None:
                warehouse_instance.address1 = address1
            if address2 is not None:
                warehouse_instance.address2 = address2
            if address3 is not None:
                warehouse_instance.address3 = address3
            if address4 is not None:
                warehouse_instance.address4 = address4
            if postcode is not None:
                warehouse_instance.postcode = postcode
            if live is not None:
                warehouse_instance.live = live
            if phone is not None:
                warehouse_instance.phone = phone
            if fax is not None:
                warehouse_instance.fax = fax
            if email is not None:
                warehouse_instance.email = email
            if vatno is not None:
                warehouse_instance.vatno = vatno
            if whtypeid is not None:
                warehouse_instance.whtypeid_id = whtypeid  # Assuming whtypeid is a foreign key

            warehouse_instance.dateupdated = datetime.now()
            warehouse_instance.save()

            return E4k_TblwhoWarehouses_Update(TblwhoWarehouses=warehouse_instance, success=True)
        except TblwhoWarehouses.DoesNotExist:
            return E4k_TblwhoWarehouses_Update(success=False, error="Warehouse not found.")
        except Exception as e:
            return E4k_TblwhoWarehouses_Update(success=False, error=str(e))


class E4k_TblwhoWarehouses_Delete(graphene.Mutation):
    class Arguments:
        warehouseid = graphene.String(required=True)
        companyid = graphene.String(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, warehouseid, companyid):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblwhoWarehouses_Delete(success=False, error="CompanyID does not exist.")
            warehouse_instance = TblwhoWarehouses.objects.get(warehouseid=warehouseid,companyid=companyid)
            warehouse_instance.delete()
            return E4k_TblwhoWarehouses_Delete(success=True)
        except TblwhoWarehouses.DoesNotExist:
            return E4k_TblwhoWarehouses_Delete(success=False, error="Warehouse not found.")
        except Exception as e:
            return E4k_TblwhoWarehouses_Delete(success=False, error=str(e))
        
#################################################################################################################
class E4k_TblsupplierBalance_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)  # Marked as required
        balance = graphene.Decimal(required=True)  # Marked as required
        foreignbalance = graphene.Decimal(required=True)  # Marked as required
    
    TblsupplierBalance = graphene.Field(TblsupplierBalanceType)
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, companyid, businessid, balance, foreignbalance):
        date_used = datetime.now()
        try:
            # validate company
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierBalance_Create(success=False, error="CompanyID does not exist.")
            
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierBalance_Create(success=False, error="BusinessID does not exist.")

            business_instance = Tblsupplier.objects.get(businessid=businessid)

            supplier_instance = TblsupplierBalance(
                companyid_id=companyid,
                businessid=business_instance,  # Assign the Tblsupplier instance here
                balance=balance,
                date_used=date_used,
                foreignbalance=foreignbalance
            )
            supplier_instance.save()
            return E4k_TblsupplierBalance_Create(TblsupplierBalance=supplier_instance, success=True)
        except Exception as e:
            return E4k_TblsupplierBalance_Create(success=False, error=str(e))

        
class E4k_TblsupplierBalance_Update (graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String()
        balance = graphene.Decimal()
        # date_used = graphene.DateTime()
        foreignbalance = graphene.Decimal()
    
    TblsupplierBalance = graphene.Field(TblsupplierBalanceType)
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, companyid, businessid, balance, foreignbalance):
        date_used= datetime.now()
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierBalance_Update(success=False, error="CompanyID does not exist.")
            supplier_instance = TblsupplierBalance.objects.get(businessid=businessid)
            if balance is not None:
                supplier_instance.balance = balance
            if date_used is not None:
                supplier_instance.date_used = date_used
            if foreignbalance is not None:
                supplier_instance.foreignbalance = foreignbalance
            supplier_instance.save()
            return E4k_TblsupplierBalance_Update(TblsupplierBalance=supplier_instance, success=True)
        except TblsupplierBalance.DoesNotExist:
            return E4k_TblsupplierBalance_Update(success=False, error="Supplier not found.")
        except Exception as e:
            return E4k_TblsupplierBalance_Update(success=False, error=str(e))
        
class E4k_TblsupplierBalance_Delete (graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        companyid = graphene.String(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, businessid, companyid):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierBalance_Delete(success=False, error="CompanyID does not exist.")
            supplier_instance = TblsupplierBalance.objects.get(businessid=businessid,companyid= companyid)
            supplier_instance.delete()
            return E4k_TblsupplierBalance_Delete(success=True)
        except TblsupplierBalance.DoesNotExist:
            return E4k_TblsupplierBalance_Delete(success=False, error="Supplier not found.")
        except Exception as e:
            return E4k_TblsupplierBalance_Delete(success=False, error=str(e))
        

#####################################################################################################################

class E4k_TblsupplierAccount_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        bank_name = graphene.String()
        bank_account_name = graphene.String()
        bank_sort_code = graphene.String()
        bank_account_num = graphene.Int()
        discount = graphene.Int()
        credit_limit = graphene.Decimal()
        currency_code = graphene.Int()
        vatcode = graphene.Int()
        vatflag = graphene.String()
        vatno = graphene.String()
        nominal_code = graphene.String()
        paymenttermsid = graphene.String()
        
        
       
    
    TblsupplierAccount = graphene.Field(TblsupplierAccountType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, bank_name=None, bank_account_name=None, bank_sort_code=None, bank_account_num=None, discount=None, credit_limit=None, currency_code=None, vatcode=None, vatflag=None, vatno=None, nominal_code=None, paymenttermsid=None):
        # getting current date and time
        date_used = datetime.now()
        date_opened = datetime.now()
# validation for foriegn keys fields
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierAccount_Create(success=False, error="CompanyID does not exist.")
            
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierAccount_Create(success=False, error="BusinessID does not exist.")
            
            if not TblbusCurrencies.objects.filter(currency_code=currency_code).exists():
                return E4k_TblsupplierAccount_Create(success=False, error="CurrencyCode does not exist.")

            business_instance = Tblsupplier.objects.get(businessid=businessid)
            currency_instance = TblbusCurrencies.objects.get(currency_code=currency_code)
            companyid_instance = Tblcompany.objects.get(companyid=companyid)
            vatcode_instance = TblaccVatcodes.objects.get(vatcode = vatcode)
            nominal_code_Instance = TblaccNominal.objects.get( nomcode= nominal_code)
            paymenttermsid_instance = TblbusPaymentterms.objects.get(paymenttermsid=paymenttermsid)

            supplier_instance = TblsupplierAccount(
                companyid=companyid_instance,
                businessid=business_instance,  # Assign the Tblsupplier instance here
                bank_name=bank_name,
                bank_account_name=bank_account_name,
                bank_sort_code=bank_sort_code,
                bank_account_num=bank_account_num,
                discount=discount,
                credit_limit=credit_limit,
                currency_code=currency_instance,  # Assign the TblbusCurrencies instance here
                vatcode=vatcode_instance,
                vatflag=vatflag,
                vatno=vatno,
                date_used=date_used,
                date_opened=date_opened,
                nominal_code=nominal_code_Instance ,
                paymenttermsid= paymenttermsid_instance
            )
            supplier_instance.save()
            return E4k_TblsupplierAccount_Create(TblsupplierAccount=supplier_instance, success=True)
        except Exception as e:
            return E4k_TblsupplierAccount_Create(success=False, error=str(e))

        
class E4k_TblsupplierAccount_Update(graphene.Mutation):
    class Arguments:    
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        bank_name = graphene.String()
        bank_account_name = graphene.String()
        bank_sort_code = graphene.String()
        bank_account_num = graphene.Int()
        discount = graphene.Int()
        credit_limit = graphene.Decimal()
        currency_code = graphene.Int()
        vatcode = graphene.Int()
        vatflag = graphene.String()
        vatno = graphene.String()
        nominal_code = graphene.String()
        paymenttermsid = graphene.String()
        date_Opened = graphene.String()
        date_Used = graphene.String()
    
    TblsupplierAccount = graphene.Field(TblsupplierAccountType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, bank_name=None, bank_account_name=None, bank_sort_code=None, bank_account_num=None, discount=None, credit_limit=None, currency_code=None, vatcode=None, vatflag=None, vatno=None, nominal_code=None, paymenttermsid=None, date_Opened = None, date_Used = None):
        try:
            # Check for required instances
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierAccount_Update(success=False, error="CompanyID does not exist.")
            
            if not Tblsupplier.objects.filter(businessid=businessid).exists():
                return E4k_TblsupplierAccount_Update(success=False, error="BusinessID does not exist.")
            
            # Optional instance checks
            currency_instance = TblbusCurrencies.objects.get(currency_code=currency_code) if currency_code else None
            vatcode_instance = TblaccVatcodes.objects.get(vatcode=vatcode) if vatcode else None
            nominal_code_instance = TblaccNominal.objects.get(nomcode=nominal_code) if nominal_code else None
            paymenttermsid_instance = TblbusPaymentterms.objects.get(paymenttermsid=paymenttermsid) if paymenttermsid else None

            # Fetching existing supplier account instance
            business_instance = Tblsupplier.objects.get(businessid=businessid)
            supplier_instance = TblsupplierAccount.objects.get(businessid=business_instance)

            # Updating fields if new values are provided
            if bank_name is not None:
                supplier_instance.bank_name = bank_name
            if bank_account_name is not None:
                supplier_instance.bank_account_name = bank_account_name
            if bank_sort_code is not None:
                supplier_instance.bank_sort_code = bank_sort_code
            if bank_account_num is not None:
                supplier_instance.bank_account_num = bank_account_num
            if discount is not None:
                supplier_instance.discount = discount
            if credit_limit is not None:
                supplier_instance.credit_limit = credit_limit
            if currency_code is not None:
                supplier_instance.currency_code = currency_instance
            if vatcode is not None:
                supplier_instance.vatcode = vatcode_instance
            if vatflag is not None:
                supplier_instance.vatflag = vatflag
            if vatno is not None:
                supplier_instance.vatno = vatno
            if nominal_code is not None:
                supplier_instance.nominal_code = nominal_code_instance
            if paymenttermsid is not None:
                supplier_instance.paymenttermsid = paymenttermsid_instance
            if date_Opened:
                supplier_instance.date_opened = parse_date(date_Opened)
            else:
                supplier_instance.date_opened = datetime.date.today()

            if date_Used:
                supplier_instance.date_used = parse_date(date_Used)
            else:
                supplier_instance.date_used = datetime.date.today()
                
            # supplier_instance.date_used = datetime.now()
            # supplier_instance.date_opened = datetime.now()

            supplier_instance.save()
            return E4k_TblsupplierAccount_Update(TblsupplierAccount=supplier_instance, success=True)
        except TblsupplierAccount.DoesNotExist:
            return E4k_TblsupplierAccount_Update(success=False, error="Supplier not found.")
        except TblbusCurrencies.DoesNotExist:
            return E4k_TblsupplierAccount_Update(success=False, error="Curren cy code does not exist.")
        except TblaccVatcodes.DoesNotExist:
            return E4k_TblsupplierAccount_Update(success=False, error="VAT code does not exist.")
        except TblaccNominal.DoesNotExist:
            return E4k_TblsupplierAccount_Update(success=False, error="Nominal code does not exist.")
        except TblbusPaymentterms.DoesNotExist:
            return E4k_TblsupplierAccount_Update(success=False, error="Payment terms ID does not exist.")
        except Exception as e:
            return E4k_TblsupplierAccount_Update(success=False, error=str(e))


class E4k_TblsupplierAccount_Delete (graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, companyid, businessid):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblsupplierAccount_Delete(success=False, error="CompanyID does not exist.")
            supplier_instance = TblsupplierAccount.objects.get(businessid=businessid,companyid=companyid)
            supplier_instance.delete()
            return E4k_TblsupplierAccount_Delete(success=True)
        except TblsupplierAccount.DoesNotExist:
            return E4k_TblsupplierAccount_Delete(success=False, error="Supplier not found.")
        except Exception as e:
            return E4k_TblsupplierAccount_Delete(success=False, error=str(e))
        
        
class E4k_SupplierDeleteAddressAndContacts(graphene.Mutation):
    class Arguments:
        addressid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, addressid, companyid):
        try:
            # Check if the company exists
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_SupplierDeleteAddressAndContacts(success=False, error="CompanyID does not exist.")

            # Find the customer address
            try:
                Supplier_address = TblsupplierAddress.objects.get(addressid=addressid)
            except TblcustomerAddress.DoesNotExist:
                return E4k_SupplierDeleteAddressAndContacts(success=False, error="supplier Address not found.")

            # Delete associated contacts first
            contacts = TblsupplierContact.objects.filter(addressid=addressid, companyid=companyid)
            if contacts.exists():
                contacts.delete()

            # Delete the customer address
            Supplier_address.delete()

            # Optionally, reduce the ID numbers (if needed)
           

            return E4k_SupplierDeleteAddressAndContacts(success=True)

        except Exception as e:
            return E4k_SupplierDeleteAddressAndContacts(success=False, error=str(e))       
        
            
            

class E4k_SupplierRowContact_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        id = graphene.Int(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self,info, companyid,id ) :
        try:
            contact = TblsupplierContact.objects.get(companyid=companyid , id=id )
            contact.delete()
            return E4k_SupplierRowContact_Delete(success=True)
        except TblsupplierContact.DoesNotExist:
            return E4k_SupplierRowContact_Delete(success=False, error="Contact not found.")
        except Exception as e:
            return E4k_SupplierRowContact_Delete(success=False, error=str(e))
        
        

class E4k_TblSupplier_SetValueUpdate(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        value = graphene.String(required=True)
    customersetvalues = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, businessid, settingid, value):
        try:
            compan = Tblcompany.objects.get(companyid = companyid)
            with transaction.atomic():
                lowercase_input = value.lower()
                if lowercase_input == "true":
                    value = 'True'
                elif lowercase_input == "false":
                    value = "False"
                else:
                    value = value
                businessid = Tblsupplier.objects.get(businessid = businessid)
                customer_settingid = TblsupplierSettings.objects.get(settingid = settingid , companyid = compan)
                try:
                    if customer_settingid.default == value:
                        if customer_settingid.default !=''  and  value != '' :
                            try:
                                setvalues = TblsupplierSetvalues.objects.get(settingid =settingid, companyid = compan , businessid = businessid)
                                setvalues.delete()
                            except TblsupplierSetvalues.DoesNotExist:
                                pass
                        elif customer_settingid.default == '' and value == '':
                            try:
                                setvalues1 = TblsupplierSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                setvalues1.delete()
                                
                            except TblsupplierSetvalues.DoesNotExist:
                                pass
                            
                        elif customer_settingid.default !='' and value =='':
                            try :
                                setvalues2 = TblsupplierSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                setvalues2.delete()
                            except TblsupplierSetvalues.DoesNotExist:
                                pass
                    
                    else :
                        if customer_settingid.default != value:
                            if customer_settingid.default == None and value != '':
                                try:
                                    setvalues  = TblsupplierSetvalues.objects.create(companyid = compan , businessid = businessid , settingid = customer_settingid, value = value)
                                    setvalues.save()
                                except TblsupplierSetvalues.DoesNotExist:
                                    pass
                            elif  value =='' and customer_settingid.default is not None:
                                try:
                                    setvalues1 = TblsupplierSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                    setvalues1.delete()
                                except TblsupplierSetvalues.DoesNotExist:
                                    pass
                            elif value!= '' and customer_settingid.default!= value:
                                try:
                                    setvalues2 = TblsupplierSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                    setvalues2.value = value 
                                    setvalues2.save()
                                except TblsupplierSetvalues.DoesNotExist:
                                    setvalues3 = TblsupplierSetvalues.objects.create(companyid = compan , businessid = businessid , settingid = customer_settingid , value = value) 
                                    
                                    setvalues3.save()
                
                    return  E4k_TblSupplier_SetValueUpdate(customersetvalues ='Success')  
                except TblsupplierSetvalues.DoesNotExist:
                    return  E4k_TblSupplier_SetValueUpdate(customersetvalues ='SettingID does not exist')
        except Tblcompany.DoesNotExist:
            return  E4k_TblSupplier_SetValueUpdate(customersetvalues ='CompanyID does not exist')
        except Tblsupplier.DoesNotExist:
            return  E4k_TblSupplier_SetValueUpdate(customersetvalues ='BusinessID does not exist')
        except Exception as e:
            return  E4k_TblSupplier_SetValueUpdate(customersetvalues = str(e))
        


class E4k_TblSupplierLogo_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        value = graphene.String(required=True)  # This will now hold the image string (Base64-encoded)

    logo = graphene.String()  # This will return the file path after the mutation
    message = graphene.String()
    success = graphene.Boolean()
    error = graphene.Boolean()

    @staticmethod
    def mutate(root, info, companyid, businessid, settingid, value):
        try:
            # Fetch company, business, and setting objects
            company = Tblcompany.objects.get(companyid=companyid)
            business = Tblsupplier.objects.get(businessid=businessid)
            setting = TblsupplierSettings.objects.get(settingid=settingid)

            # Check if the provided value is a valid base64 string
            if value:
                # Decode the base64 image string
                image_data = base64.b64decode(value)
                
                # Define the external directory to save the uploaded image
                file_dir = settings.EXTERNAL_MEDIA_ROOT_SUPPLIER_LOGO
                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)
                
                # Define the file name (e.g., companyid_businessid.png)
                file_name = f"{companyid}_{businessid}.png"  # You can change the extension based on the image format
                file_path = os.path.join(file_dir, file_name)

                # Save the decoded image to the file path
                with open(file_path, 'wb') as image_file:
                    image_file.write(image_data)

                # Store the file path in the value field of TblcustomerSetvalues
                Logo, created = TblsupplierSetvalues.objects.update_or_create(
                    companyid=company,
                    businessid=business,
                    settingid=setting,
                    defaults={'value': file_path}  # Save the external file path
                )

                return E4k_TblSupplierLogo_Create(
                    logo=file_path,
                    message="Logo uploaded and saved successfully.",
                    success = True,
                    error = None
                    
                )
            else:
                return E4k_TblSupplierLogo_Create(
                    logo=None,
                    message="No logo provided.",
                    success=False,
                    error=None
                    
                    
                )

        except Tblcompany.DoesNotExist:
            return E4k_TblSupplierLogo_Create(
                logo=None,
                message=f"Company with ID {companyid} does not exist.",
                success=False,
                error=None
            )
        except Tblsupplier.DoesNotExist:
            return E4k_TblSupplierLogo_Create(
                logo=None,
                message=f"Business with ID {businessid} does not exist.",
                success= False,
                error = None
            )
        except TblsupplierSettings.DoesNotExist:
            return E4k_TblSupplierLogo_Create(
                logo=None,
                message=f"Setting with ID {settingid} does not exist.",
                success=False,
                error=None
            )



class E4k_SupplierAndAccount_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        name = graphene.String()
        countryid = graphene.Int()  # Optional field, can be manually entered or left empty
        islive = graphene.Boolean()  # Optional field
        category1id = graphene.Int()  # Optional field
        category2id = graphene.Int()  # Optional field
        category3id = graphene.Int()  # Optional field
        classid = graphene.Int()  # Optional field
        default_nominal = graphene.Int()  # Optional field
        isextract = graphene.Boolean()  # Optional field
        isstop = graphene.Boolean()  # Optional field
        bank_name = graphene.String()  # Optional field
        bank_account_name = graphene.String()  # Optional field
        bank_sort_code = graphene.String()  # Optional field
        bank_account_num = graphene.Int()  # Optional field, manually entered or left empty
        discount = graphene.Int()  # Optional field, manually entered or left empty
        credit_limit = graphene.Decimal()  # Optional field
        currency_code = graphene.Int()  # Required
        vatcode = graphene.Int()  # Optional field
        vatflag = graphene.String()  # Optional field
        vatno = graphene.String()  # Optional field
        nominal_code = graphene.String()  # Optional field
        paymenttermsid = graphene.String()  # Optional field

    success = graphene.Boolean()
    error = graphene.String()
    @staticmethod
    def mutate(self, info, **kwargs):
        companyid = kwargs.get('companyid')
        businessid = kwargs.get('businessid')

        # Start a transaction to ensure both operations succeed or fail together
        with transaction.atomic():
            try:
                # Create or get the supplier
                supplier, created = Tblsupplier.objects.get_or_create(
                    companyid_id=companyid,
                    businessid=businessid,
                    defaults={
                        'name': kwargs.get('name', None),
                        'countryid_id': kwargs.get('countryid', None),
                        'islive': kwargs.get('islive', None),
                        'category1id_id': kwargs.get('category1id', None),
                        'category2id_id': kwargs.get('category2id', None),
                        'category3id_id': kwargs.get('category3id', None),
                        'classid_id': kwargs.get('classid', None),
                        'default_nominal_id': kwargs.get('default_nominal', None),
                        'isextract': kwargs.get('isextract', None),
                        'isstop': kwargs.get('isstop', None)
                    }
                )

                if not created:
                    return E4k_SupplierAndAccount_Create(success=False, error="Supplier with this BusinessID already exists.")

            except Exception as e:
                return E4k_SupplierAndAccount_Create(success=False, error=f"Supplier creation failed: {str(e)}")

            try:
                # Helper function to convert values to Decimal or set as None if missing
                def convert_decimal(value):
                    if value is None:
                        return None
                    try:
                        return Decimal(value)
                    except (InvalidOperation, ValueError):
                        raise ValueError(f"Invalid decimal value: {value}")

                # Validate paymenttermsid
                paymenttermsid = kwargs.get('paymenttermsid')
                if paymenttermsid:
                    try:
                        payment_terms_instance = TblbusPaymentterms.objects.get(id=paymenttermsid)
                    except TblbusPaymentterms.DoesNotExist:
                        return E4k_SupplierAndAccount_Create(success=False, error="Invalid payment terms ID.")

                # Create or get the supplier account
                supplier_account, account_created = TblsupplierAccount.objects.get_or_create(
                    companyid_id=companyid,
                    businessid_id=businessid,
                    defaults={
                        'bank_name': kwargs.get('bank_name', None),
                        'bank_account_name': kwargs.get('bank_account_name', None),
                        'bank_sort_code': kwargs.get('bank_sort_code', None),
                        'bank_account_num': kwargs.get('bank_account_num', None),
                        'discount': kwargs.get('discount', None),
                        'credit_limit': convert_decimal(kwargs.get('credit_limit', None)),
                        'currency_code_id': kwargs.get('currency_code'),  # Required
                        'vatcode_id': kwargs.get('vatcode', None),
                        'vatflag': kwargs.get('vatflag', None),
                        'vatno': kwargs.get('vatno', None),
                        'nominal_code': kwargs.get('nominal_code', None),
                        'paymenttermsid': payment_terms_instance if paymenttermsid else None,  # Use the instance if valid
                        'date_used': datetime.now(),
                        'date_opened': datetime.now()
                    }
                )

                if not account_created:
                    return E4k_SupplierAndAccount_Create(success=False, error="Supplier Account already exists for this BusinessID.")

                return E4k_SupplierAndAccount_Create(success=True)

            except Exception as e:
                # Rollback transaction if any error occurs
                transaction.set_rollback(True)
                return E4k_SupplierAndAccount_Create(success=False, error=f"Account creation failed: {str(e)}")



    
class SupplierMutation(graphene.ObjectType):

    E4k_TblsupplierCategory1Create = E4k_TblsupplierCategory1_Create.Field()
    E4k_TblsupplierCategory1Update = E4k_TblsupplierCategory1_Update.Field()
    E4k_TblsupplierCategory1Delete = E4k_TblsupplierCategory1_Delete.Field()  

    E4k_TblsupplierCategory2Create = E4k_TblsupplierCategory2_Create.Field()
    E4k_TblsupplierCategory2Update =  E4k_TblsupplierCategory2_Update.Field()
    E4k_TblsupplierCategory2Delete = E4k_TblsupplierCategory2_Delete.Field()
    
    E4k_TblsupplierCategory3Create = E4k_TblsupplierCategory3_Create.Field()
    E4k_TblsupplierCategory3Update = E4k_TblsupplierCategory3_Update.Field()
    E4k_TblsupplierCategory3Delete = E4k_TblsupplierCategory3_Delete.Field()


    E4k_TblsupplierClassCreate = E4k_TblsupplierClass_Create.Field()
    E4k_TblsupplierClassUpdate = E4k_TblsupplierClass_Update.Field()
    E4k_TblsupplierClassDelete = E4k_TblsupplierClass_Delete.Field()

    E4k_Tblsupplier_Create = E4k_Tblsupplier_Create.Field()
    E4k_Tblsupplier_Update = E4k_Tblsupplier_Update.Field()
    E4k_Tblsupplier_Delete = E4k_Tblsupplier_Delete.Field()

    E4k_TblsupplierNotesCreate = E4k_TblsupplierNotes_Create.Field()
    E4k_TblsupplierNotesUpdate = E4k_TblsupplierNotes_Update.Field()
    E4k_TblsupplierNotesDelete = E4k_TblsupplierNote_Delete.Field()

    E4k_TblsupplierAddressCreate = E4k_TblsupplierAddress_Create.Field()
    E4k_TblsupplierAddressUpdate = E4k_TblsupplierAddress_Update.Field()
    E4k_TblsupplierAddressDelete = E4k_TblsupplierAddress_Delete.Field() 

    E4k_TblwhoWarehousesTypesCreate = E4k_TblwhoWarehousesTypes_Create.Field() 
    E4k_TblwhoWarehousesTypesUpdate = E4k_TblwhoWarehousesTypes_Update.Field()
    E4k_TblwhoWarehousesTypesDelete = E4k_TblwhoWarehousesTypes_Delete.Field()

    E4k_TblsupplierMemoCreate = E4k_TblsupplierMemo_Create.Field()
    E4k_TblsupplierMemoUpdate = E4k_TblsupplierMemo_Update.Field()
    E4k_TblsupplierMemoDelete = E4k_TblsupplierMemo_Delete.Field() 

    E4k_TblsupplierContactCreate = E4k_TblsupplierContact_Create.Field()
    E4k_TblsupplierContactUpdate = E4k_TblsupplierContact_Update.Field()
    E4k_TblsupplierContactDelete = E4k_TblsupplierContact_Delete.Field()

    E4k_TblsupplierTurnoverCreate = E4k_TblsupplierTurnover_Create.Field()
    E4k_TblsupplierTurnoverUpdate = E4k_TblsupplierTurnover_Update.Field()
    E4k_TblsupplierTurnoverDelete = E4k_TblsupplierTurnover_Delete.Field()

    E4k_TblwhoWarehousesCreate = E4k_TblwhoWarehouses_Create.Field()
    E4k_TblwhoWarehousesUpdate = E4k_TblwhoWarehouses_Update.Field()
    E4k_TblwhoWarehousesDelete = E4k_TblwhoWarehouses_Delete.Field()

    E4k_TblsupplierBalanceCreate = E4k_TblsupplierBalance_Create.Field()
    E4k_TblsupplierBalanceUpdate = E4k_TblsupplierBalance_Update.Field()
    E4k_TblsupplierBalanceDelete = E4k_TblsupplierBalance_Delete.Field()

    E4k_TblsupplierAccountCreate = E4k_TblsupplierAccount_Create.Field()
    E4k_TblsupplierAccountUpdate = E4k_TblsupplierAccount_Update.Field()
    E4k_TblsupplierAccountDelete = E4k_TblsupplierAccount_Delete.Field()
    
    
    E4k_SupplierDeleteAddressAndContacts = E4k_SupplierDeleteAddressAndContacts.Field()
    E4k_SupplierRowContact_Delete = E4k_SupplierRowContact_Delete.Field()
    E4k_TblSupplierSetValueUpdate =E4k_TblSupplier_SetValueUpdate.Field()
    
    
    E4k_TblSupplierLogo_Create = E4k_TblSupplierLogo_Create.Field()
    E4k_SupplierAndAccount_Create = E4k_SupplierAndAccount_Create.Field()



