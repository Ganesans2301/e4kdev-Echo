import graphene
import json
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
#from graphene_django.filter import DjangoFilterConnectionField
from django.db import connection,transaction,IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
import base64
from django.core.files.base import ContentFile
import os
from django.shortcuts import get_object_or_404
from django.conf import settings
from AppMessage.utils import JsonDataFrame

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
                     TblproductPropertyTypesValues,TblproductProductObsoleteMatrix,TblproductProductSupplierLevel,
                     TblproductProductSupplierLevelColmatrix,TblproductProductSuppliersMatrix,
                     TblproductParametersCustomerSetvalues,TblproductProductPriceStandardDateMatrix,
                     TblproductProductPriceStandardQtyMatrix,TblgenCategories)

from Customer.models import (TblaccNominal,TblbusCountries,Tblcompany,TblbusSalesPeople,
                             Tblcustomer) 
from Supplier.models import (Tblsupplier,TblsupplierSettings,TblsupplierSetvalues,TblwhoWarehouses)
from .utils import NextNo ,get_random_image_path

class E4k_TblSupplier(DjangoObjectType):
    class Meta:
        model = Tblsupplier
        fields = '__all__'

class E4k_TblSupplier_settings(DjangoObjectType):
    class Meta:
        model = TblsupplierSettings
        fields = '__all__'

class E4k_TblSupplier_set_values(DjangoObjectType):
    class Meta:
        model = TblsupplierSetvalues
        fields = '__all__'


class E4K_Tblcustomer(DjangoObjectType):
    class Meta:
        model = Tblcustomer
        fields = '__all__'

class E4K_TblwhoWarehouses(DjangoObjectType):
    class Meta:
        model = TblwhoWarehouses
        fields = '__all__'

class E4K_TblaccNominalNode(DjangoObjectType):
    class Meta:
        model = TblaccNominal
        fields = '__all__'

class E4k_TblGen_CategoriesNode(DjangoObjectType):
    class Meta:
        model = TblgenCategories
        fields = '__all__'

class E4K_TblbusCountriesNode(DjangoObjectType):
    class Meta:
        model = TblbusCountries
        fields = '__all__'
class E4k_Tblcompany(DjangoObjectType):
    class Meta:
        model = Tblcompany
        fields = '__all__'
########################## TblproductPropertyLevelTypes

class E4K_TblproductPropertyLevelTypesNode(DjangoObjectType):
    class Meta:
        model = TblproductPropertyLevelTypes
        fields = '__all__'

###########Product class

class E4K_TblProductCategory1Node(DjangoObjectType):
    class Meta:
        model = TblproductCategory1
        fields = '__all__'

class E4K_TblProductCategory2Node(DjangoObjectType):
    class Meta:
        model = TblproductCategory2
        fields = '__all__'

class E4K_TblProductCategory3Node(DjangoObjectType):
    class Meta:
        model = TblproductCategory3
        fields = '__all__'

class E4K_TblProductClassNode(DjangoObjectType):
    class Meta:
        model = TblproductClass
        fields = '__all__'

################################################ End of Product Category and class Node

############################TblproductColours
class E4K_TblproductColoursNode(DjangoObjectType):
    class Meta:
        model = TblproductColours
        fields = '__all__'

###########################TblproductCommoditycodes
class E4K_TblproductCommoditycodesNode(DjangoObjectType):
    class Meta:
        model = TblproductCommoditycodes
        fields = '__all__'

########################################TblproductFits

class E4K_TblproductFitsNode(DjangoObjectType):
    class Meta:
        model = TblproductFits
        fields = '__all__'

######################TblproductObsoleteTypes

class E4K_TblproductObsoleteTypesNode(DjangoObjectType):
    class Meta:
        model = TblproductObsoleteTypes
        fields = '__all__'
    
    allow_sale = graphene.Boolean()

    def resolve_allow_sale(self, info):
        # Assuming the database stores it as a BIT field that Django reads as a boolean
        byte_value = self.allow_sale
        if isinstance(byte_value, bytes):
            return byte_value == b'\x01'
        return byte_value

################################TblproductParametersSettings

class E4K_TblproductParametersSettingsNode(DjangoObjectType):
    class Meta:
        model = TblproductParametersSettings
        fields = '__all__'

###############################tblproduct_pricetypes

class E4K_TblproductPriceTypesNode(DjangoObjectType):
    class Meta:
        model = TblproductPriceTypes
        fields = '__all__'

############################# TblproductPropertyTypes

class E4K_TblproductPropertyTypesNode(DjangoObjectType):
    class Meta:
        model = TblproductPropertyTypes
        fields = '__all__'

#########################################TblproductPropertyTypesValues

class E4K_TblproductPropertyTypesValuesNode(DjangoObjectType):
    class Meta:
        model = TblproductPropertyTypesValues
        fields = '__all__'



################################TblproductStockingTypes

class E4K_TblproductStockingTypesNode(DjangoObjectType):
    class Meta:
        model = TblproductStockingTypes
        fields = '__all__'
################################################ TblproductTypeofissue

class E4K_TblproductTypeofissueNode(DjangoObjectType):
    class Meta:
        model = TblproductTypeofissue
        fields = '__all__'

############################################### TblproductUnitofissue

class E4K_TblproductUnitofissueNode(DjangoObjectType):
    class Meta:
        model = TblproductUnitofissue
        fields = '__all__'

############################################### TblproductSizeRanges
class E4K_TblproductSizeRangesNode(DjangoObjectType):
    class Meta:
        model = TblproductSizeRanges
        fields = '__all__'

############################################### TblproductSizeRanges values
class E4K_TblproductSizeRangeValuesNode(DjangoObjectType):
    class Meta:
        model = TblproductSizeRangeValues
        fields = '__all__'

############################################### E4K_TblProduct_ProductNode 
class E4K_TblProduct_ProductNode(DjangoObjectType):
    class Meta:
        model = TblproductProducts
        fields = '__all__'
    
    live = graphene.Boolean()
    batchcontrol = graphene.Boolean()

    def resolve_live(self, info):
        # Assuming the database stores it as a BIT field that Django reads as a boolean
        byte_value = self.live
        if isinstance(byte_value, bytes):
            return byte_value == b'\x01'
        return byte_value
    
    def resolve_batchcontrol(self, info):
        # Assuming the database stores it as a BIT field that Django reads as a boolean
        byte_value = self.batchcontrol
        if isinstance(byte_value, bytes):
            return byte_value == b'\x01'
        return byte_value

############################################### TblproductParametertsSetvalues

class E4K_Tblproduct_ParametertsSetvalues_Node(DjangoObjectType):
    class Meta:
        model = TblproductParametertsSetvalues
        fields = '__all__'

##################################################TblproductProductGallery

class E4K_TblproductProduct_GalleryNode(DjangoObjectType):
    class Meta:
        model = TblproductProductGallery
        fields = '__all__'

####################################################TblproductProductProperties 

class E4K_TblproductProductPropertiesNode(DjangoObjectType):
    class Meta:
        model = TblproductProductProperties
        fields = '__all__'

######################################################## TblproductProductPropertyValues

class E4K_TblproductProductPropertyValuesNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPropertyValues
        fields = '__all__'

########################################################## TblproductProductReps

class E4K_TblproductProductRepsNode(DjangoObjectType):
    class Meta:
        model = TblproductProductReps
        fields = '__all__'

###########################################################TblproductProductPropertyLevel


class E4K_TblproductProductPropertyLevelNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPropertyLevel
        fields = '__all__'



###########################################################TblproductProductSupplier Level



class E4K_TblproductProductSupplierLevelNode(DjangoObjectType):
    class Meta:
        model = TblproductProductSupplierLevel
        fields = '__all__'
###############################################################TblproductProductSuppliers

class E4K_TblproductProductSuppliersNode(DjangoObjectType):
    class Meta:
        model = TblproductProductSuppliers
        fields = '__all__'

############################################################# TblproductProductStockinglevelMatrix 

class E4K_TblproductProductStockinglevelMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductStockinglevelMatrix
        fields = '__all__'
##################################################################TblproductProductStockingtypeMatrix 

class E4K_TblproductProductStockingtypeMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductStockingtypeMatrix
        fields = '__all__'

class E4K_TblproductProductObsoleteMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductObsoleteMatrix
        fields = '__all__'


################################################################ TblproductProductCostStandardMatrix

class E4K_TblproductProductCostStandardMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductCostStandardMatrix
        fields = '__all__'

################################################################# TblproductProductCostSupplierMatrix

class E4K_TblproductProductCostSupplierMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductCostSupplierMatrix
        fields = '__all__'

############################################################## TblproductProductPriceCustomerMatrix

class E4K_TblproductProductPriceCustomerMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPriceCustomerMatrix
        fields = '__all__'

############################################################## TblproductProductPriceStandardDateMatrix 

class E4K_TblproductProductPriceStandardDateMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPriceStandardDateMatrix
        fields = '__all__'



############################################################## TblproductProductPriceStandardMatrix 

class E4K_TblproductProductPriceStandardMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPriceStandardMatrix
        fields = '__all__'


############################################################## TblproductProductPriceStandardQtyMatrix 

class E4K_TblproductProductPriceStandardQtyMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPriceStandardQtyMatrix
        fields = '__all__'

############################################################# TblproductProductVatcodeMatrix

class E4K_TblproductProductVatcodeMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductVatcodeMatrix
        fields = '__all__'

###########################################################TblproductProductSuppliersWeekdays

class E4K_TblproductProductSuppliersWeekdaysNode(DjangoObjectType):
    class Meta:
        model = TblproductProductSuppliersWeekdays
        fields = '__all__'

############################################################## End of tables one more table exits tblproduct_product_freetext

class E4K_TblproductProductPropertyMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPropertyMatrix
        fields = '__all__'


######################################################### E4K_TblProductProductPropertyLevelColmatrix

class E4K_TblProductProductPropertyLevelColmatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductPropertyLevelColmatrix
        fields = '__all__'



######################################################### E4K_TblProductProductSupplierLevelColmatrix

class E4K_TblProductProductSupplierLevelColmatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductSupplierLevelColmatrix
        fields = '__all__'


################################################################ TblproductProductSupplierMatrix

class E4K_TblproductProductSupplierMatrixNode(DjangoObjectType):
    class Meta:
        model = TblproductProductSuppliersMatrix
        fields = '__all__'

################################### TblproductCategory1 CRUD operations
####### Create a new TblproductCategory1
class E4K_TblProduct_ProductCategory1_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category = graphene.String(required=True)
        image_path = graphene.String(required=True)
        filename = graphene.String(required=True)

    category1id = graphene.String()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, category, image_path=None,filename=None):
        """
            This function is used to create a new product category1 in the database.

            Parameters:
            root (graphene.ResolveInfo): The root resolver object.
            info (graphene.ResolveInfo): The resolver info object.
            companyid (str): The ID of the company for which the category is being created.
            category (str): The name of the product category.
            image_path (str, optional): The path to the image representing the category1.

            Returns:
            E4K_TblProduct_ProductCategory1_Create: An instance of the mutation class with a status message indicating success or failure.
        """
        try:
            MessageDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    category = TblproductCategory1.objects.get(companyid=company,
                                                               description = category)
                    error = MessageDataFrame.get_entry(id=2)
                    return E4K_TblProduct_ProductCategory1_Create(category1id="Failed",message=error['successmessage'])
                    
                except TblproductCategory1.DoesNotExist:
                    next_category = NextNo()
                    category1id = next_category.get_next_no(
                        table_name="tblproduct_category1",
                        field_name='Category1ID',
                        companyid=companyid
                    )

                    ########### convert base image to image 
                    if image_path =="":
                        category1 = TblproductCategory1.objects.create(
                        companyid=company,
                        category1id=category1id,  # Corrected field name
                        description=category,
                        imagepath=None
                        )
                        category1.save()
                    else:
                        format, imgstr = image_path.split(';base64,')
                        ext = format.split('/')[-1]
                        data = ContentFile(base64.b64decode(imgstr), name=f'{filename}.{ext}')
                        
                        unique_filename = os.path.join('Category1', data.name)
                        full_path = os.path.join(settings.EXTERNAL_FRONDEND_IMAGES_DIR, unique_filename)

                        # Ensure the directory exists
                        os.makedirs(os.path.dirname(full_path), exist_ok=True)

                        # Save the image to the media directory
                        with open(full_path, 'wb') as f:
                            f.write(data.read())


                        category1 = TblproductCategory1.objects.create(
                            companyid=company,
                            category1id=category1id,  # Corrected field name
                            description=category,
                            imagepath=full_path
                        )
                        category1.save()  # This line is not strictly necessary as create() already saves the instance
                    
                    message_return = MessageDataFrame.get_entry(id=3)
                    return E4K_TblProduct_ProductCategory1_Create(category1id="Success",message=message_return['successmessage'])
        except Tblcompany.DoesNotExist:
            error = MessageDataFrame.get_entry(id=1)
            return E4K_TblProduct_ProductCategory1_Create(category1id="Failed",message=error['errormessage'])
        except Exception as e:
            # print(f"An error occurred: {e}")  # Print the error for debugging
            # return E4K_TblProduct_ProductCategory1_Create(category1id=f"Failed: {e}")
            error = MessageDataFrame.get_entry(id=3)
            return E4K_TblProduct_ProductCategory1_Create(category1id="Failed",message=error['errormessage'])

######## Update the product category

class E4K_TblProduct_ProductCategory1_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category1id = graphene.Int(required=True)
        category = graphene.String(required=True)
        image_path = graphene.String(required=True)
        filename = graphene.String()

    category1id = graphene.String()
    message = graphene.String()

    @staticmethod
    def mutate(root, info,companyid, category1id, category, image_path,filename=None):
        """
            Update a product category1.

            Parameters:
            root (graphene.ResolveInfo): The root resolver.
            info (graphene.ResolveInfo): The resolver info.
            companyid (str): The company ID.
            category1id (int): The category1 ID.
            category (str): The new category name.
            image_path (str): The new image path.

            Returns:
            E4K_TblProduct_ProductCategory1_Update: An instance of the mutation with the result status.
        """
        try:
            MessageDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():

                category_instance = TblproductCategory1.objects.get(companyid=company, category1id=category1id)
                
                # If a new image is provided, delete the old image
                if image_path and filename:
                    old_image_path = category_instance.imagepath
                    if old_image_path is not None:
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    
                    # Convert base64 image to image file
                    # print('####################################image_path',image_path.split(';base64,'))
                    format, imgstr = image_path.split(';base64,')
                    
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr), name=f'{filename}.{ext}')
                    # Generate unique filename to avoid overwriting existing files
                    unique_filename = os.path.join('Category1', data.name)

                    # Build the full file path
                    #full_path = os.path.join(settings.EXTERNAL_IMAGES_DIR, unique_filename)
                    full_path = os.path.join(settings.EXTERNAL_FRONDEND_IMAGES_DIR, unique_filename)

                    # Ensure the directory exists
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)

                    # Save the image to the media directory
                    with open(full_path, 'wb') as f:
                        f.write(data.read())

                    category_instance.imagepath = full_path
                else:
                    if category_instance.imagepath is not None:
                        directory, original_filename = os.path.split(category_instance.imagepath)
                        file_name_old, file_extension_old = os.path.splitext(original_filename)

                        ##new name for category instance image
                        new_file_name = f"{category}{file_extension_old}"
                        new_path = os.path.join(directory, new_file_name)
                        os.rename(category_instance.imagepath, new_path)
                        category_instance.imagepath = new_path


                category_instance.description = category
                category_instance.save()
                message_return = MessageDataFrame.get_entry(id=4)
                return E4K_TblProduct_ProductCategory1_Update(category1id="Success",message=message_return['successmessage'])
        except Tblcompany.DoesNotExist:
            message_return = MessageDataFrame.get_entry(id=1)
            return E4K_TblProduct_ProductCategory1_Update(category1id="Failed",message=message_return['errormessage'])
        except TblproductCategory1.DoesNotExist:
            message_return = MessageDataFrame.get_entry(id=2)
            return E4K_TblProduct_ProductCategory1_Update(category1id="Failed",message = message_return['errormessage'])
        except Exception as e:
            #print(f"An error occurred: {e}")
            message_return = MessageDataFrame.get_entry(id=4)
            #return E4K_TblProduct_ProductCategory1_Update(category1id=f"Failed: {e}")
            return E4K_TblProduct_ProductCategory1_Update(category1id="Failed",message = message_return['errormessage'])

######## Delete Product Category

class E4K_TblProduct_ProductCategory1_Delete(graphene.Mutation):
    """
        Mutation to delete a product category1.
    """
    class Arguments:
        companyid = graphene.String(required=True)
        category1id = graphene.Int(required=True)

    category1id = graphene.String()
    message = graphene.String()

    @staticmethod
    def mutate(root, info,companyid, category1id):
        """
            Delete a product category1.

            Parameters:
            - companyid (str): The ID of the company.
            - category1id (int): The ID of the product category1 to delete.

            Returns:
            - E4K_TblProduct_ProductCategory1_Delete: A mutation object with the result of the deletion.

            Raises:
            - Tblcompany.DoesNotExist: If the company with the given ID does not exist.
            - TblproductCategory1.DoesNotExist: If the product category1 with the given ID does not exist.
        """
        try:
            MessageDataFrame = JsonDataFrame()
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                category1 = TblproductCategory1.objects.get(companyid = company,category1id=category1id)
                if category1.imagepath:
                    old_image_path = category1.imagepath
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                
                # Delete the record from the database
                category1.delete()
                message_return = MessageDataFrame.get_entry(id=5)  # Fetch the message from the message data frame for successful deletion.
                return E4K_TblProduct_ProductCategory1_Delete(category1id="Success", message = message_return['successmessage'])
        except Tblcompany.DoesNotExist:
            message_return = MessageDataFrame.get_entry(id=1)
            return E4K_TblProduct_ProductCategory1_Delete(category1id='Failed',message=message_return['errormessage'])
        except TblproductCategory1.DoesNotExist:
            message_return = MessageDataFrame.get_entry(id=2)
            return E4K_TblProduct_ProductCategory1_Delete(category1id='Failed', message= message_return['errormessage'])
        except Exception as e:
            message_return = MessageDataFrame.get_entry(id=5)
            return E4K_TblProduct_ProductCategory1_Delete(category1id='Failed', message= message_return['errormessage'])
            #return E4K_TblProduct_ProductCategory1_Delete(category1id=f"Failed Unable To Delete \n\n Exception \n: {e}")
        

################################### TblproductCategory2 CRUD operations
####### Create a new TblproductCategory2
class E4K_TblProduct_ProductCategory2_Create(graphene.Mutation):
    """
        Mutation to create a new product category 2.

    """
    class Arguments:
        companyid = graphene.String(required=True)
        category = graphene.String(required=True)
        image_path = graphene.String()
        filename = graphene.String()

    category2id = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, category, image_path=None, filename=None):
        """
            Create a new product category 2.

            Args:
                root: The root mutation.
                info: The information about the mutation.
                companyid (str): The ID of the company.
                category (str): The name of the product category.
                image_path (str, optional): The path of the image related to the category.

            Returns:
                E4K_TblProduct_ProductCategory2_Create: An instance of the mutation with the result.
        """
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    category2 = TblproductCategory2.objects.get(companyid=company,
                                                               description = category)
                
                    return E4K_TblProduct_ProductCategory2_Create(category2id='Failed , Category2 Already Exists')
                except TblproductCategory2.DoesNotExist:
                        next_category = NextNo()
                        category2id = next_category.get_next_no(
                            table_name="tblproduct_category2",
                            field_name='Category2ID',
                            companyid=companyid
                        )

                        if image_path =="":
                            category2 = TblproductCategory2.objects.create(
                                companyid=company,
                                category2id=category2id,  # Corrected field name
                                description=category,
                                imagepath=None
                            )
                            category2.save()
                        else:

                            ########### convert base image to image 
                            format, imgstr = image_path.split(';base64,')
                            ext = format.split('/')[-1]
                            data = ContentFile(base64.b64decode(imgstr), name=f'{filename}.{ext}')

                        
                            # Generate unique filename to avoid overwriting existing files
                            unique_filename = os.path.join('Category2', data.name)

                            # Build the full file path
                            full_path = os.path.join(settings.EXTERNAL_FRONDEND_IMAGES_DIR, unique_filename)

                            # Ensure the directory exists
                            os.makedirs(os.path.dirname(full_path), exist_ok=True)

                            # Save the image to the media directory
                            with open(full_path, 'wb') as f:
                                f.write(data.read())


                            category2 = TblproductCategory2.objects.create(
                                companyid=company,
                                category2id=category2id,  # Corrected field name
                                description=category,
                                imagepath=full_path
                            )
                            category2.save()
                        return E4K_TblProduct_ProductCategory2_Create(category2id='Success')
        
        except Exception as e:
            return E4K_TblProduct_ProductCategory2_Create(category2id=f"Failed: {e}")
        except Tblcompany.DoesNotExist:
            return E4K_TblProduct_ProductCategory2_Create(category2id='Company id not found')


######## Update the product category2

class E4K_TblProduct_ProductCategory2_Update(graphene.Mutation):
    """
        Mutation to update a product category 2.

        Parameters:
        companyid (str): The ID of the company.
        category2id (int): The ID of the product category 2.
        category (str): The new description of the product category 2.
        image_path (str): The new image path of the product category 2.

        Returns:
        E4K_TblProduct_ProductCategory2_Update: A mutation object with the result of the update operation.
    """
    class Arguments:
        companyid = graphene.String(required=True)
        category2id = graphene.Int(required=True)
        category = graphene.String(required=True)
        image_path = graphene.String(required=True)
        filename = graphene.String()

    category2id = graphene.String()

    @staticmethod
    def mutate(root, info,companyid, category2id, category, image_path=None, filename=None):
        try:
            company  = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                category2 = TblproductCategory2.objects.get(companyid = company,category2id=category2id)
                
                if image_path and filename:
                    old_image_path = category2.imagepath
                    if old_image_path is not None:
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    # old_image_path = category2.imagepath
                    # if os.path.exists(old_image_path):
                    #     os.remove(old_image_path)
                    
                    # Convert base64 image to image file
                    format, imgstr = image_path.split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr), name=f'{filename}.{ext}')
                   
                    # Generate unique filename to avoid overwriting existing files
                    unique_filename = os.path.join('Category2', data.name)

                    # Build the full file path
                    full_path = os.path.join(settings.EXTERNAL_FRONDEND_IMAGES_DIR, unique_filename)

                    # Ensure the directory exists
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)

                    # Save the image to the media directory
                    with open(full_path, 'wb') as f:
                        f.write(data.read())

                    category2.imagepath = full_path
                else:
                    if category2.imagepath is not None:
                        directory, original_filename = os.path.split(category2.imagepath)
                        file_name_old, file_extension_old = os.path.splitext(original_filename)

                        ##new name for category instance image
                        new_file_name = f"{category}{file_extension_old}"
                        new_path = os.path.join(directory, new_file_name)
                        os.rename(category2.imagepath, new_path)
                        category2.imagepath = new_path

                category2.description = category
                category2.save()
                return E4K_TblProduct_ProductCategory2_Update(category2id='Success')
        except Tblcompany.DoesNotExist:
            return E4K_TblProduct_ProductCategory2_Update(category2id="Company id not found")
        except TblproductCategory2.DoesNotExist:
            return E4K_TblProduct_ProductCategory2_Update(category2id='product category2id not found')
        except Exception as e:
            return E4K_TblProduct_ProductCategory2_Update(category2id=f"Failed: {e}")

######## Delete Product Category2

class E4k_TblProduct_ProductCategory2_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category2id = graphene.Int(required=True)

    category2id = graphene.String()

    @staticmethod
    def mutate(root, info, companyid,category2id):
        """
            Deletes a product category 2 record from the database.

            Parameters:
            root (graphene.ResolveInfo): The root resolver.
            info (graphene.ResolveInfo): Additional information about the resolver.
            companyid (str): The ID of the company.
            category2id (int): The ID of the product category 2.

            Returns:
            E4k_TblProduct_ProductCategory2_Delete: A mutation object with a success message or an error message.
        """
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                category2 = TblproductCategory2.objects.get(companyid = company,category2id=category2id)
                if category2.imagepath:
                    old_image_path = category2.imagepath
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                category2.delete()
                return E4k_TblProduct_ProductCategory2_Delete(category2id='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductCategory2_Delete(category2id='Company id not found')
        except TblproductCategory2.DoesNotExist:
            return E4k_TblProduct_ProductCategory2_Delete(category2id='product category not found')
        except Exception as e:
            return E4k_TblProduct_ProductCategory2_Delete(category2id=f"Failed Unable To Delete \n\n Exception \n: {e}")
        


################################### TblproductCategory3 CRUD operations
####### Create a new TblproductCategory3
class E4k_TblProduct_ProductCategory3_Create(graphene.Mutation):
    """
        Mutation to create a new product category 3.

        Parameters:
        - companyid (str): The ID of the company.
        - category (str): The description of the product category 3.

        Returns:
        - category3id (str): The ID of the newly created product category 3.
        Returns 'Success' if the creation is successful.
        Returns 'Failed, Category3 Already Exists' if the category already exists.
        Returns 'Company id not found' if the company ID does not exist.
        Returns 'Failed to create product category' if any other error occurs.
    """
    class Arguments:
        companyid = graphene.String(required=True)
        category = graphene.String(required=True)

    category3id = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, category):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    category3 = TblproductCategory3.objects.get(companyid=company,
                                                               description = category)
                    
                    return E4k_TblProduct_ProductCategory3_Create(category3id='Failed , Category3 Already Exists')
                except TblproductCategory3.DoesNotExist:
                    next_category = NextNo()
                    category3id = next_category.get_next_no(
                        table_name="tblproduct_category3",
                        field_name='Category3ID',
                        companyid=companyid
                    )
                    category3 = TblproductCategory3.objects.create(
                        companyid=company,
                        category3id=category3id,
                        description=category
                    )
                    category3.save()

                return E4k_TblProduct_ProductCategory3_Create(category3id="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductCategory3_Create(category3id='Company id not found')
        except Exception as e:
            return E4k_TblProduct_ProductCategory3_Create(category3id=f"Failed: {e}")

######## Update the product category3

class E4k_TblProduct_ProductCategory3_Update(graphene.Mutation):
    """
        Mutation class for updating a product category 3.

        Attributes:
        companyid (str): The company ID.
        category3id (str): The category 3 ID.
        category (str): The new category description.

        Returns:
        E4k_TblProduct_ProductCategory3_Update: A mutation object with the result of the update operation.
    """
    class Arguments:
        companyid = graphene.String(required=True)
        category3id = graphene.Int(required=True)
        category = graphene.String(required=True)
        
    category3id = graphene.String()

    @staticmethod
    def mutate(root, info, companyid,category3id, category):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                category3 = TblproductCategory3.objects.get(companyid=company,category3id=category3id)
                category3.description = category
                category3.save()
                return E4k_TblProduct_ProductCategory3_Update(category3id='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductCategory3_Update(category3id='Company id not found')
        except TblproductCategory3.DoesNotExist:
            return E4k_TblProduct_ProductCategory3_Update(category3id='ProductCategory not found')
        except Exception as e:
            return E4k_TblProduct_ProductCategory3_Update(category3id='Failed to update product category')

######## Delete Product Category2

class E4k_TblProduct_ProductCategory3_Delete(graphene.Mutation):
    """
        Mutation class for deleting a product category 3.

        Attributes:
        companyid (str): The company ID.
        category3id (str): The category 3 ID.

        Returns:
        E4k_TblProduct_ProductCategory3_Delete: A mutation object with the result of the deletion operation.
    """
    class Arguments:
        companyid = graphene.String(required=True)
        category3id = graphene.Int(required=True)

    category3id = graphene.String()

    @staticmethod
    def mutate(root, info, companyid,category3id):
        """
            Method to delete a product category 3.

            Parameters:
            root (graphene.ResolveInfo): The root resolver.
            info (graphene.ResolveInfo): The resolver info.
            companyid (str): The company ID.
            category3id (str): The category 3 ID.

            Returns:
            E4k_TblProduct_ProductCategory3_Delete: A mutation object with the result of the deletion operation.
        """
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                category3 = TblproductCategory3.objects.get(companyid=company,category3id=category3id)
                category3.delete()
                return E4k_TblProduct_ProductCategory3_Delete(category3id='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductCategory3_Delete(category3id="Company ID not found")
        except TblproductCategory3.DoesNotExist:
            return E4k_TblProduct_ProductCategory3_Delete(category3id='Product ID not found')
        except Exception as e:
            return E4k_TblProduct_ProductCategory3_Delete(category3id=f"Failed Unable To Delete \n\n Exception \n: {e}")
        


################################### TblproductClass CRUD operations
####### Create a new TblproductClass
class E4k_TblProduct_ProductClass_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        class_name = graphene.String(required=True)

    class_ = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, class_name):
        """
            This function is used to create a new product class in the database.

            Parameters:
            root (graphene.ResolveInfo): The root resolver object.
            info (graphene.ResolveInfo): The resolver info object.
            companyid (str): The ID of the company.
            class_name (str): The name of the product class.

            Returns:
            E4k_TblProduct_ProductClass_Create: A mutation object with the result of the operation.
            If the operation is successful, the 'class_' field will be 'Success'.
            If the operation fails due to a unique constraint violation, the 'class_' field will be 'Failed Product Class already exists'.
            If the operation fails due to a company not found error, the 'class_' field will be 'Company id not found'.
            If any other error occurs, the 'class_' Failed to create product class.
        """
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    productclass = TblproductClass.objects.get(companyid=company,description=class_name)
                    return E4k_TblProduct_ProductClass_Create(class_='Failed Product Class already exists')
                except TblproductClass.DoesNotExist:
                    next_category = NextNo()
                    classid = next_category.get_next_no(
                        table_name="tblproduct_class",
                        field_name='ClassID',
                        companyid=companyid
                    )
                
                    product_class = TblproductClass.objects.create(
                        companyid=company,
                        classid=classid,
                        description=class_name
                    )
                    product_class.save()

                    return E4k_TblProduct_ProductClass_Create(class_='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductClass_Create(class_='Company id not found')
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_ProductClass_Create(class_="Failed to create product class")

######## Update the product class

class E4k_TblProduct_ProductClass_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        classid = graphene.Int(required=True)
        description = graphene.String(required=True)
        
    class_id = graphene.String()

    @staticmethod
    def mutate(root, info,companyid, classid, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                classid_update = TblproductClass.objects.get(companyid = company,classid=classid)
                classid_update.description = description
                classid_update.save()
                return E4k_TblProduct_ProductClass_Update(class_id='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductClass_Update(class_id='Company id not found')
        except TblproductClass.DoesNotExist:
            return E4k_TblProduct_ProductClass_Update(class_id='Product class not found')
        except Exception as e:
            return E4k_TblProduct_ProductClass_Update(class_id='Failed to update')

######## Delete Product Class

class E4k_TblProduct_ProductClass_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        classid = graphene.Int(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info,companyid, classid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                class_delete = TblproductClass.objects.get(companyid=company,classid=classid)
                class_delete.delete()
                return E4k_TblProduct_ProductClass_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductClass_Delete(success='Company id not found')
        except TblproductClass.DoesNotExist:
            return E4k_TblProduct_ProductClass_Delete(success='Product class not found')
        except Exception as e:
            return E4k_TblProduct_ProductClass_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")



####################################### TblproductColoursNode create_product_colours

#################### Tbl Product colour create
class E4k_TblProduct_ProductColours_Create(graphene.Mutation):

    class Arguments:
        companyid = graphene.String(required=True)
        colourid = graphene.String(required=True)
        description = graphene.String(required=True)
        colourcode = graphene.String()
    
    colour = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, colourid, description, colourcode:None):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    colour_id = TblproductColours.objects.get(companyid=company,colourid = colourid)
                    return E4k_TblProduct_ProductColours_Create(colour='Failed colourid already exists')
                except TblproductColours.DoesNotExist:
                    try:
                        colourcode_ = TblproductColours.objects.create(
                        companyid=company,
                        colourid=colourid,  # Corrected field name
                        description=description,
                        colourcode=colourcode if colourcode else ''
                        )
                        colourcode_.save()
                        return E4k_TblProduct_ProductColours_Create(colour='Success')
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductColours_Create(colour='Failed to create colourid ')
                    
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductColours_Create(colour='Company ID not found')
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_ProductColours_Create(colour='Failed to create colourid')
        
#################### Tbl Product colour Update
class E4k_TblProduct_ProductColours_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        colourid = graphene.String(required=True)
        description = graphene.String(required=True)
        colourcode = graphene.String()
        
    colour_id = graphene.String()

    @staticmethod
    def mutate(root, info,companyid, colourid, description,colourcode:None):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                colourid_update = TblproductColours.objects.get(companyid=company,colourid=colourid)
                colourid_update.description = description
                colourid_update.colourcode = colourcode if colourcode else ''
                colourid_update.save()
                return E4k_TblProduct_ProductColours_Update(colour_id='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductColours_Update(colour_id='Company id not found')
        except TblproductColours.DoesNotExist:
            return E4k_TblProduct_ProductColours_Update(colour_id='Product colourid not found')
        except Exception as e:
            return E4k_TblProduct_ProductColours_Update(colour_id='failed to update product colour')

######## Delete Product Colour

class E4k_TblProduct_ProductColours_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        colourid = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid,colourid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                colour_delete = TblproductColours.objects.get(companyid=company,colourid=colourid)
                colour_delete.delete()
                return E4k_TblProduct_ProductColours_Delete(success='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductColours_Delete(success='Company ID does not exist')
        except TblproductColours.DoesNotExist:
            return E4k_TblProduct_ProductColours_Delete(success='Product colour ID does not exist')
        except Exception as e:
            return E4k_TblProduct_ProductColours_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")

########################################### E4K_TblproductCommoditycodes Create

class E4k_TblProduct_CommodityCodes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        commoditycode = graphene.String(required=True)
        description = graphene.String(required=True)

    commoditycode = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, commoditycode, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    commoditycode_id = TblproductCommoditycodes.objects.get(companyid=company,
                                                                            commodity_code=commoditycode)
                    return E4k_TblProduct_CommodityCodes_Create(commoditycode='Failed commoditycode already exists')
                except TblproductCommoditycodes.DoesNotExist:
                    try:
                        commoditycode_ = TblproductCommoditycodes.objects.create(
                                                                    companyid=company,
                                                                    commodity_code=commoditycode,
                                                                    description=description
                                                                    )
                        commoditycode_.save()
                        return E4k_TblProduct_CommodityCodes_Create(commoditycode='Success')
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_CommodityCodes_Create(commoditycode='Failed to create product commodity code')

        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_CommodityCodes_Create(commoditycode='Company id not found')
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_CommodityCodes_Create(commoditycode='Failed to create product commodity code')

######################### E4K_TblProduct_CommodotityCodes_update

class E4k_TblProduct_CommodityCodes_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        commoditycode = graphene.String(required=True)
        description = graphene.String(required=True)
    
    commoditycode = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, commoditycode, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                commoditycode_update = TblproductCommoditycodes.objects.get(companyid = company,
                                                                            commodity_code=commoditycode)
                commoditycode_update.description = description
                commoditycode_update.save()
                return E4k_TblProduct_CommodityCodes_Update(commoditycode='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_CommodityCodes_Update(commoditycode='Company id not found')
        except TblproductCommoditycodes.DoesNotExist:
            return E4k_TblProduct_CommodityCodes_Update(commoditycode='Product commodity code not found')
        except Exception as e:
            return E4k_TblProduct_CommodityCodes_Update(commoditycode='Failed to update product commodity code')
        
################################ tbl product commodity codes delete

class E4k_TblProduct_CommodityCodes_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        commoditycode = graphene.String(required=True)
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, commoditycode):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                commoditycode_delete = TblproductCommoditycodes.objects.get(companyid=company,
                                                                            commodity_code=commoditycode)
                commoditycode_delete.delete()
                return E4k_TblProduct_CommodityCodes_Delete(success='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_CommodityCodes_Delete(success="Company id not found")
        except TblproductCommoditycodes.DoesNotExist:
            return E4k_TblProduct_CommodityCodes_Delete(success='COMODITY codes not found')
        except Exception as e:
            return E4k_TblProduct_CommodityCodes_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")


#########################################TblproductFitsNode

#################### Tbl Product Fits create

class E4k_TblProduct_ProductFits_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        fitid = graphene.String(required=True)
        description = graphene.String(required=True)

    fit = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, fitid, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    fitid_key = TblproductFits.objects.get(companyid=company,fitid=fitid)
                    return E4k_TblProduct_ProductFits_Create(fit=fitid_key)
                
                except TblproductFits.DoesNotExist:
                    try:
                        fitid_ = TblproductFits.objects.create(
                        companyid=company,
                        fitid=fitid,
                        description=description
                        )
                        fitid_.save()
                        return E4k_TblProduct_ProductFits_Create(fit="Success")
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductFits_Create(fit='Failed to create product fits')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductFits_Create(fit='Company id not found')
        
#######################tbl fsk product fit update

class E4k_TblProduct_ProductFits_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        fitid = graphene.String(required=True)
        description = graphene.String(required=True)
    
    fit_id = graphene.String()

    @staticmethod
    def mutate(root, info, companyid,fitid, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                fitid_update = TblproductFits.objects.get(companyid=company,fitid=fitid)
                fitid_update.description = description
                fitid_update.save()
                return E4k_TblProduct_ProductFits_Update(fit_id="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductFits_Update(fit_id='Company id not found')
        except TblproductFits.DoesNotExist:
            return E4k_TblProduct_ProductFits_Update(fit_id='Product fitid not found')
        except Exception as e:
            return E4k_TblProduct_ProductFits_Update(fit_id='Failed to update product fit')
        
###################### Tbl Fsk_Product_Fits_Delete #################

class E4k_TblProduct_ProductFits_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        fitid = graphene.String(required=True)

    success = graphene.String()
    
    @staticmethod
    def mutate(root, info,companyid, fitid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                fit_delete = TblproductFits.objects.get(companyid=company,fitid=fitid)
                fit_delete.delete()
                return E4k_TblProduct_ProductFits_Delete(success='Success')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductFits_Delete(success="Company does not exist")
        except TblproductFits.DoesNotExist:
            return E4k_TblProduct_ProductFits_Delete(success="TBlProductFits does not exist")
        except Exception as e:
            return E4k_TblProduct_ProductFits_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        
################################### TblproductObsoleteTypes Create

class E4k_TblProduct_ProductObsoleteTypes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        description = graphene.String(required=True)
        allow_sale = graphene.Boolean(required=True)

    obsolete_type = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, description, allow_sale):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    
                    obsolete_class_key = TblproductObsoleteTypes.objects.get(companyid=company,
                                                                             description=description)
                    return E4k_TblProduct_ProductObsoleteTypes_Create(obsolete_type="Failed Already Exists")
                except TblproductObsoleteTypes.DoesNotExist:
                        try:
                            obsoleteid_ = NextNo()
                            obsoleteid = obsoleteid_.get_next_no(
                                                table_name="tblproduct_obsolete_types",
                                                field_name='ObsoleteID',
                                                companyid=companyid
                                            )
                        
                            obsolete_class_ = TblproductObsoleteTypes.objects.create(
                                companyid=company,
                                obsoleteid = obsoleteid,
                                description=description,
                                allow_sale=allow_sale
                            )
                            obsolete_class_.save()
                            return E4k_TblProduct_ProductObsoleteTypes_Create(obsolete_type='Success')
                        except Exception as e:
                            print("Error occurred during object creation:", e)
                            return E4k_TblProduct_ProductObsoleteTypes_Create(obsolete_type='Failed')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductObsoleteTypes_Create(obsolete_type="company id not found")
        except Exception as e:
            return E4k_TblProduct_ProductObsoleteTypes_Create(obsolete_type='Failed')
        
##################################### Tbl_FSK_Product_ObsoleteTypes_update

class E4k_TblProduct_ProductObsoleteTypes_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        obsoleteid = graphene.Int(required=True)
        description = graphene.String(required=True)
        allow_sale = graphene.Boolean(required=True)
    
    obsolete_type = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, obsoleteid, description, allow_sale):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():

                obsolete_update = TblproductObsoleteTypes.objects.get(companyid=company,obsoleteid=obsoleteid)
                obsolete_update.description = description
                obsolete_update.allow_sale = allow_sale
                obsolete_update.save()
                return E4k_TblProduct_ProductObsoleteTypes_Update(obsolete_type="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductObsoleteTypes_Update(obsolete_type='Company id not found')
        except TblproductObsoleteTypes.DoesNotExist:
            return E4k_TblProduct_ProductObsoleteTypes_Update(obsolete_type='product obsolete type id not found')
        except Exception as e:
            return E4k_TblProduct_ProductObsoleteTypes_Update(obsolete_type='failed to update product obsolete type')
        
############################# Tbl_FSK_Product_ObsoleteTypes_Delete

class E4k_TblProduct_ProductObsoleteTypes_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        obsoleteid = graphene.Int(required=True)
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info,companyid, obsoleteid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                obsolete_delete = TblproductObsoleteTypes.objects.get(companyid=company,obsoleteid=obsoleteid)
                obsolete_delete.delete()
                return E4k_TblProduct_ProductObsoleteTypes_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductObsoleteTypes_Delete(success="Company id not found")
        except TblproductObsoleteTypes.DoesNotExist:
            return E4k_TblProduct_ProductObsoleteTypes_Delete(success="Obsolete type id not found")
        except Exception as e:
            return E4k_TblProduct_ProductObsoleteTypes_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        
####################################### TblproductParametersSettings create

class E4k_TblProduct_ProductParameterSettings_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        settingname = graphene.String(required=True)
        default = graphene.String()
        seqno = graphene.Int(required=True)
        lookup_table = graphene.String()
        lookup_text = graphene.String()

    setting = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, settingid, settingname, default, seqno, lookup_table:None, lookup_text:None):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    settings_id = TblproductParametersSettings.objects.get(companyid=company,settingid = settingid)
                    return E4k_TblProduct_ProductParameterSettings_Create(setting="Setting id already exists")
                except TblproductParametersSettings.DoesNotExist:
                    try:
                        settings_ = TblproductParametersSettings.objects.create(
                        companyid=company,
                        settingid=settingid,  # Corrected field name
                        settingname=settingname,
                        default = default if default else '',
                        seqno = seqno,
                        lookup_table=lookup_table if lookup_table else '',
                        lookup_text=lookup_text if lookup_text else '',
                        )
                        settings_.save()
                        return E4k_TblProduct_ProductParameterSettings_Create(setting="Success")
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductParameterSettings_Create(setting='Failed to id')            
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductParameterSettings_Create(setting="Company id not found")
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_ProductParameterSettings_Create(setting='Failed to create settings id')

######################################## TblproductParametersSettings Update

class E4k_TblProduct_ProductParameterSettings_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        settingname = graphene.String(required=True)
        default = graphene.String()
        seqno = graphene.Int(required=True)
        lookup_table = graphene.String()
        lookup_text = graphene.String()

    setting = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, settingid, settingname, default, seqno, lookup_table:None, lookup_text:None):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                setting_update = TblproductParametersSettings.objects.get(companyid=company,settingid=settingid)
                setting_update.settingname = settingname
                setting_update.default = default if default else ''
                setting_update.seqno = seqno
                setting_update.lookup_table = lookup_table if lookup_table else ''
                setting_update.lookup_text = lookup_text if lookup_text else ''
                setting_update.save()
                return E4k_TblProduct_ProductParameterSettings_Update(setting="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductParameterSettings_Update(setting="Company id not found")
        except TblproductParametersSettings.DoesNotExist:
            return E4k_TblProduct_ProductParameterSettings_Update(setting='Setting id not found')
        except Exception as e:
            return E4k_TblProduct_ProductParameterSettings_Update(setting="Failed to update setting id")
        
####################################### TblproductParametersSettings Delete

class E4k_TblProduct_ProductParameterSettings_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        settingid = graphene.String(required=True)
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info,companyid,settingid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                setting_delete = TblproductParametersSettings.objects.get(companyid=company,settingid=settingid)
                setting_delete.delete()
                return E4k_TblProduct_ProductParameterSettings_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductParameterSettings_Delete(success="Company id not found")
        except TblproductParametersSettings.DoesNotExist:
            return E4k_TblProduct_ProductParameterSettings_Delete(success="Setting id not found")
        except Exception as e:
            return E4k_TblProduct_ProductParameterSettings_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")


######################################## TblproductPriceTypes create

class E4k_TblProduct_ProductPriceTypes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        description = graphene.String(required=True)
        price_type = graphene.Int()

    price_type = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, description, price_type:1):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    price_type_id = TblproductPriceTypes.objects.get(companyid=company,description = description)
                    return E4k_TblProduct_ProductPriceTypes_Create(price_type="Price type id already exists")
                except TblproductPriceTypes.DoesNotExist:
                    try:
                        price_type_ = NextNo()
                        price_id_ = price_type_.get_next_no(
                                                table_name="tblproduct_price_types",
                                                field_name='PriceID',
                                                companyid=companyid
                                            )
                        price_type_ = TblproductPriceTypes.objects.create(
                                                    companyid=company,
                                                    description=description,
                                                    price_type=price_type,
                                                    priceid = price_id_
                                                    )
                        price_type_.save()
                        return E4k_TblProduct_ProductPriceTypes_Create(price_type = "Success")
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductPriceTypes_Create(price_type="Failed to create product price type")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductPriceTypes_Create(price_type="Company id not found")
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_ProductPriceTypes_Create(price_type="Failed to create product price type")
        
########################### TblproductPriceTypes Update

class E4k_TblProduct_ProductPriceTypes_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        priceid = graphene.Int(required=True)
        description = graphene.String(required=True)
        price_type = graphene.Int()

    price_type = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, priceid, description, price_type):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                price_type_update = TblproductPriceTypes.objects.get(companyid=company,priceid=priceid)
                price_type_update.description = description
                price_type_update.price_type = price_type if price_type else 1
                price_type_update.save()
                return E4k_TblProduct_ProductPriceTypes_Update(price_type="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductPriceTypes_Update(price_type="Company id not found")
        except TblproductPriceTypes.DoesNotExist:
            return E4k_TblProduct_ProductPriceTypes_Update(price_type="Price id not found")
        except Exception as e:
            return E4k_TblProduct_ProductPriceTypes_Update(price_type="Failed to update price type")
        
##############################################Tbl product prices delete method################################
class E4k_TblProduct_ProductPriceTypes_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        priceid = graphene.Int(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, priceid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                price_type_delete = TblproductPriceTypes.objects.get(companyid=company,priceid=priceid)
                price_type_delete.delete()
                return E4k_TblProduct_ProductPriceTypes_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductPriceTypes_Delete(success="Company id not found")
        except TblproductPriceTypes.DoesNotExist:
            return E4k_TblProduct_ProductPriceTypes_Delete(success="Price type not found")
        except Exception as e:
            return E4k_TblProduct_ProductPriceTypes_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        


################################### TblproductPropertyTypes Create

class E4k_TblProduct_ProductPropertyTypes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        description = graphene.String(required=True)
    
    property_type = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    property_type_id = TblproductPropertyTypes.objects.get(companyid = company,
                                                                           description = description)
                    return E4k_TblProduct_ProductPropertyTypes_Create(property_type="Property type id already exists")
                except TblproductPropertyTypes.DoesNotExist:
                    try:
                        property_type_ = NextNo()
                        property_id_ = property_type_.get_next_no(
                                                table_name="tblproduct_property_types",
                                                field_name='PropertyID',
                                                companyid=companyid
                                            )
                        property_type_ = TblproductPropertyTypes.objects.create(
                                                    companyid=company,
                                                    description=description,
                                                    propertyid = property_id_
                                                    )
                        property_type_.save()
                        return E4k_TblProduct_ProductPropertyTypes_Create(property_type = "Success")
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductPropertyTypes_Create(property_type="Failed to create product property type")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductPropertyTypes_Create(property_type="Company id not found")
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_ProductPropertyTypes_Create(property_type="Failed to create product property type")



################################### TblproductPropertyTypes Update
class E4k_TblProduct_ProductPropertyTypes_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        description = graphene.String(required=True)

    property_type = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, propertyid, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                property_type_update = TblproductPropertyTypes.objects.get(companyid=company,propertyid=propertyid)
                property_type_update.description = description
                property_type_update.save()
                return E4k_TblProduct_ProductPropertyTypes_Update(property_type="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductPropertyTypes_Update(property_type="Company id not found")
        except TblproductPropertyTypes.DoesNotExist:
            return E4k_TblProduct_ProductPropertyTypes_Update(property_type="PropertyType not found")
        except Exception as e:
            return E4k_TblProduct_ProductPropertyTypes_Update(property_type="failed to update product property type")
        
################################# Tbl Product Property Types Delete

class E4k_TblProduct_ProductPropertyTypes_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, propertyid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                property_type_delete = TblproductPropertyTypes.objects.get(companyid=company,propertyid=propertyid)
                property_type_delete.delete()
                return E4k_TblProduct_ProductPropertyTypes_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductPropertyTypes_Delete(success="Company id not found")
        except TblproductPropertyTypes.DoesNotExist:
            return E4k_TblProduct_ProductPropertyTypes_Delete(success="Property type not found")
        except Exception as e:
            return E4k_TblProduct_ProductPropertyTypes_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        

###################################TblproductStockingTypes Create

class E4k_TblProduct_ProductStockingTypes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        stockingtype = graphene.String(required=True)
        description = graphene.String(required=True)

    stocking_type = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, stockingtype, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    stocking_type_id = TblproductStockingTypes.objects.get(companyid = company,
                                                                           stockingtype = stockingtype)
                    return E4k_TblProduct_ProductStockingTypes_Create(stocking_type="Stocking type id already exists")
                except TblproductStockingTypes.DoesNotExist:
                    try:
                        stocking_type_ = TblproductStockingTypes.objects.create(
                                                    companyid=company,
                                                    stockingtype=stockingtype,
                                                    description=description,
                                                    )
                        stocking_type_.save()
                    
                        return E4k_TblProduct_ProductStockingTypes_Create(stocking_type = "Success")
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductStockingTypes_Create(stocking_type="Failed to create product stocking type")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductStockingTypes_Create(stocking_type="Company id not found")
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_ProductStockingTypes_Create(stocking_type="Failed to create product stocking type")
        
####################################### Tbl_FSK_Product_StockingTypes Update

class E4k_TblProduct_ProductStockingTypes_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        stockingtype = graphene.String(required=True)
        description = graphene.String(required=True)

    stocking_type = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, stockingtype, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                stocking_type_update = TblproductStockingTypes.objects.get(companyid=company,
                                                                           stockingtype=stockingtype)
                stocking_type_update.description = description
                stocking_type_update.save()
                return E4k_TblProduct_ProductStockingTypes_Update(stocking_type="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductStockingTypes_Update(stocking_type="Company id not found")
        except TblproductStockingTypes.DoesNotExist:
            return E4k_TblProduct_ProductStockingTypes_Update(stocking_type="Stocking type not found")
        except Exception as e:
            return E4k_TblProduct_ProductStockingTypes_Update(stocking_type="failed to update product stocking type")

####################################### Tbl_FSK_Product_StockingTypes_Delete

class E4k_TblProduct_ProductStockingTypes_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        stockingtype = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, stockingtype):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                stocking_type_delete = TblproductStockingTypes.objects.get(companyid=company,
                                                                           stockingtype=stockingtype)
                stocking_type_delete.delete()
                return E4k_TblProduct_ProductStockingTypes_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductStockingTypes_Delete(success="Company id not found")
        except TblproductStockingTypes.DoesNotExist:
            return E4k_TblProduct_ProductStockingTypes_Delete(success="Stocking type not found")
        except Exception as e:
            return E4k_TblProduct_ProductStockingTypes_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        
######################################## TblproductTypeofissue Create

class E4k_TblProduct_ProductTypeofissue_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        description = graphene.String(required=True)

    type_of_issue = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    type_of_issue_id = TblproductTypeofissue.objects.get(companyid = company,
                                                                         description = description)
                    return E4k_TblProduct_ProductTypeofissue_Create(type_of_issue="Issue type id already exists")
                except TblproductTypeofissue.DoesNotExist:
                    try:
                        issue_type = NextNo()
                        issueid = issue_type.get_next_no(
                            table_name='tblproduct_typeofissue',
                            field_name='Issue_Type',
                            companyid=companyid
                        )
                        type_of_issue_ = TblproductTypeofissue.objects.create(
                                                    companyid=company,
                                                    issue_type=issueid,
                                                    description=description,
                                                    )
                        type_of_issue_.save()
                    
                        return E4k_TblProduct_ProductTypeofissue_Create(type_of_issue = "Success")
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductTypeofissue_Create(type_of_issue="Failed to create type of issue")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductTypeofissue_Create(type_of_issue="Company not found")
        except Exception as e:
            print("An error occurred:", e)
            return E4k_TblProduct_ProductTypeofissue_Create(type_of_issue="Failed to create type of issue")
        
#################################### tbl_product_type_of_issue update

class E4k_TblProduct_ProductTypeofissue_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        issue_type = graphene.Int(required=True)
        description = graphene.String(required=True)

    type_of_issue = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, issue_type, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                type_of_issue_update = TblproductTypeofissue.objects.get(companyid=company,issue_type=issue_type)
                type_of_issue_update.description = description
                type_of_issue_update.save()
                return E4k_TblProduct_ProductTypeofissue_Update(type_of_issue="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductTypeofissue_Update(type_of_issue="Company not found")
        except TblproductTypeofissue.DoesNotExist:
            return E4k_TblProduct_ProductTypeofissue_Update(type_of_issue="Product Type of Issue not found")
        except Exception as e:
            return E4k_TblProduct_ProductTypeofissue_Update(type_of_issue="Failed to update product type of issue")
        
######################################## Tbl_FSK_Product_Typeofissue Delete

class E4k_TblProduct_ProductTypeofissue_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        issue_type = graphene.Int(required=True)

    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, issue_type):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                type_of_issue_delete = TblproductTypeofissue.objects.get(companyid=company,issue_type=issue_type)
                type_of_issue_delete.delete()
                return E4k_TblProduct_ProductTypeofissue_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductTypeofissue_Delete(success="Company id not found")
        except TblproductTypeofissue.DoesNotExist:
            return E4k_TblProduct_ProductTypeofissue_Delete(success="Issue type not found")
        except Exception as e:
            return E4k_TblProduct_ProductTypeofissue_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}") 
        
######################################## TblproductUnitofissue create

class E4k_TblProduct_ProductUnitofissue_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        description = graphene.String(required=True)

    unit_of_issue = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    unit_of_issue_id = TblproductUnitofissue.objects.get(companyid = company,
                                                                         description = description)
                    return E4k_TblProduct_ProductUnitofissue_Create(unit_of_issue="Units type id already exists")
                except TblproductUnitofissue.DoesNotExist:
                    try:
                        units_type = NextNo()
                        unitsid = units_type.get_next_no(
                            table_name='tblproduct_unitofissue',
                            field_name='Issue_Units',
                            companyid=companyid
                        )
                        units_of_issue_ = TblproductUnitofissue.objects.create(
                                                    companyid=company,
                                                    issue_units=unitsid,
                                                    description=description,
                                                    )
                        units_of_issue_.save()
                    
                        return E4k_TblProduct_ProductUnitofissue_Create(unit_of_issue = "Success")
                    except Exception as e:
                        print("Error occurred during object creation:", e)
                        return E4k_TblProduct_ProductUnitofissue_Create(unit_of_issue="Failed to create product unit of issue")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductUnitofissue_Create(unit_of_issue="Company id not found")
        except Exception as e:
            return E4k_TblProduct_ProductUnitofissue_Create(unit_of_issue="Failed to create product unit of issue")


######################################## Tbl_FSK_Product_unitofissue Update

class E4k_TblProduct_ProductUnitofissue_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        issue_units = graphene.Int(required=True)
        description = graphene.String(required=True)

    unit_of_issue = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, issue_units, description):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                units_of_issue_update = TblproductUnitofissue.objects.get(companyid=company,
                                                                          issue_units=issue_units)
                units_of_issue_update.description = description
                units_of_issue_update.save()
                return E4k_TblProduct_ProductUnitofissue_Update(unit_of_issue="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductUnitofissue_Update(unit_of_issue="Company id not found")
        except TblproductUnitofissue.DoesNotExist:
            return E4k_TblProduct_ProductUnitofissue_Update(unit_of_issue="Unit of issue not found")
        except Exception as e:
            return E4k_TblProduct_ProductUnitofissue_Update(unit_of_issue="Failed to Update")
        
######################################## Tbl_FSK_Product_unitofissue Delete

class E4k_TblProduct_ProductUnitofissue_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        issue_units = graphene.Int(required=True)
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, issue_units):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                units_of_issue_delete = TblproductUnitofissue.objects.get(companyid=company,issue_units=issue_units)
                units_of_issue_delete.delete()
                return E4k_TblProduct_ProductUnitofissue_Delete(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductUnitofissue_Delete(success="Company id not found")
        except TblproductUnitofissue.DoesNotExist:
            return E4k_TblProduct_ProductUnitofissue_Delete(success="Unit of issue not found")
        except Exception as e:
            return E4k_TblProduct_ProductUnitofissue_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        

#########################################
class E4k_TblProduct_ProductSizeRangeValues_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        size_number = graphene.Int(required=True)
        size_value = graphene.String(required=True)

    size_ranges = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, rangeid, size_number, size_value):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            sizerange = TblproductSizeRanges.objects.get(companyid=company,
                                                            rangeid=rangeid)
            with transaction.atomic():
                try:
                    size_ranges_id = TblproductSizeRangeValues.objects.get(companyid = company,
                                                                      rangeid = sizerange,
                                                                      size_number=size_number,
                                                                      size_value=size_value)
                    return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges="Range id and size number already exists")
                except TblproductSizeRangeValues.DoesNotExist:
                    try:
                        sizerange_list = TblproductSizeRangeValues.objects.filter(companyid=company,
                                                                                  rangeid = sizerange).values_list('size_value',flat=True)
                        sizenumber_list = TblproductSizeRangeValues.objects.filter(companyid=company,
                                                                                  rangeid = sizerange).values_list('size_number',flat=True)
                        if (size_value not in sizerange_list) and (size_number not in sizenumber_list):
                            size_range = TblproductSizeRangeValues.objects.create(
                            companyid=company,
                            rangeid=sizerange,
                            size_number=size_number,
                            size_value = size_value,
                            )
                            size_range.save()
                            return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges = "Success")
                        else:
                            return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges="Already exists")
                                         
                    except Exception as e:
                        print("Must Provide Unique Size Number and Size Value:", e)
                        return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges=f'Failed : {e}')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges='Company id is not found')
        except TblproductSizeRanges.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges="Range id not found")
        except Exception as e:
            return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges="Failed to create product size ranges")

######################################## Tbl Product Size Ranges update single

class E4k_TblProduct_ProductSizeRangeValues_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        size_number = graphene.Int(required=True)
        #size_value = graphene.String(required=True)
        new_size_number = graphene.Int()
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, rangeid, size_number, new_size_number):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            sizerange = TblproductSizeRanges.objects.get(companyid=company,
                                                            rangeid=rangeid)
            with transaction.atomic():
                try:                   
                    
                    with transaction.atomic():
                        relation_instance = TblproductSizeRangeValues.objects.get(
                            companyid=company, 
                            rangeid=sizerange, 
                            size_number=size_number
                        )
                        
                        # Adjust sequence numbers if the new sequence number is different
                        if relation_instance.size_number != new_size_number:
                            E4k_TblProduct_ProductSizeRangeValues_Update._adjust_sequences_for_update(
                                company,
                                sizerange, 
                                relation_instance.size_number, 
                                new_size_number
                            )
                            relation_instance.size_number = new_size_number
                            #relation_instance.size_value = size_value
                            relation_instance.save()

                    
                        return E4k_TblProduct_ProductSizeRangeValues_Update(success="Success")

                except TblproductSizeRangeValues.DoesNotExist:
                    return E4k_TblProduct_ProductSizeRangeValues_Update(success="Product size range values not found")
                
                except Exception as e:
                    print("Must Provide Unique Size Number and Size Value:", e)
                    return E4k_TblProduct_ProductSizeRangeValues_Update(success='Failed : {e}')
        except TblproductSizeRanges.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValues_Create(size_ranges="Range id not found")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValues_Update(success="Company id not found")

    @staticmethod
    def _adjust_sequences_for_update(company,sizerange, old_seq_no, new_seq_no):
        """ Adjust sequence numbers of existing range id relations for update. """
        if new_seq_no > old_seq_no:
            TblproductSizeRangeValues.objects.filter(
                companyid = company,
                rangeid=sizerange,
                size_number__gt=old_seq_no,
                size_number__lte=new_seq_no
            ).update(size_number=F('size_number') - 1)
        elif new_seq_no < old_seq_no:
            TblproductSizeRangeValues.objects.filter(
                companyid = company,
                rangeid=sizerange,
                size_number__gte=new_seq_no,
                size_number__lt=old_seq_no
            ).update(size_number=F('size_number') + 1)

    
######################################## tbl ProductSizeRangeValues size value update 
class E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        size_number = graphene.Int(required=True)
        size_value = graphene.String(required=True)

    size_ranges = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, rangeid, size_number, size_value):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            sizerange = TblproductSizeRanges.objects.get(companyid=company,
                                                            rangeid=rangeid)
            with transaction.atomic():
                try:       
                    sizerange_list = TblproductSizeRangeValues.objects.filter(companyid=company,
                                                                                rangeid = sizerange).values_list('size_value',flat=True)
                    if (size_value not in sizerange_list):
                        size_range = TblproductSizeRangeValues.objects.get(
                        companyid=company,
                        rangeid=sizerange,
                        size_number=size_number,
                        
                        )
                        size_range.size_value = size_value
                        size_range.save()
                        return E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update(size_ranges = "Success")
                    else:
                        return E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update(size_ranges="Size Value Already exists")
                                         
                except Exception as e:
                        print("Must Provide Unique Size Number and Size Value:", e)
                        return E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update(size_ranges=f'Failed : {e}')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update(size_ranges='Company id is not found')
        except TblproductSizeRanges.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update(size_ranges="Range id not found")
        except Exception as e:
            return E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update(size_ranges=f"Failed : {e}")


#######################################
class E4k_TblProduct_ProductSizeRangeValues_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        size_number = graphene.Int(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, rangeid, size_number):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            sizerange = TblproductSizeRanges.objects.get(companyid=company,
                                                            rangeid=rangeid)
            with transaction.atomic():
                # Find the existing property relation
                relation_instance = TblproductSizeRangeValues.objects.get(
                    companyid=company, 
                    rangeid=sizerange, 
                    size_number=size_number
                )
                old_seq_no = relation_instance.size_number

                relation_instance.delete()

                # Adjust sequence numbers of the remaining properties
                E4k_TblProduct_ProductSizeRangeValues_Delete._adjust_sequences_after_deletion(company, 
                                                                                              sizerange, 
                                                                                              old_seq_no)
                
                return E4k_TblProduct_ProductSizeRangeValues_Delete(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValues_Delete(success="Company id not found")
        except TblproductSizeRanges.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangeValues_Delete(success="Failed To delete")
        except Exception as e:
            return E4k_TblProduct_ProductSizeRangeValues_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        
    @staticmethod
    def _adjust_sequences_after_deletion(company,sizerange, old_seq_no):
        """ Adjust sequence numbers of existing property relations after deletion. """
        TblproductSizeRangeValues.objects.filter(
            companyid=company, 
            rangeid=sizerange,
            size_number__gt=old_seq_no
        ).update(size_number=F('size_number') - 1)
 
        
######################################## Tbl product size ranges Create

class E4k_TblProduct_ProductSizeRanges_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        

    size_ranges = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, rangeid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    size_ranges_id = TblproductSizeRanges.objects.get(companyid = company,rangeid = rangeid)
                    return E4k_TblProduct_ProductSizeRanges_Create(size_ranges="Range id already exists")
                except TblproductSizeRanges.DoesNotExist:
                    try:
                        rangeid_ = TblproductSizeRanges.objects.create(
                        companyid=company,
                        rangeid=rangeid,
                        
                        )
                        rangeid_.save()
                        return E4k_TblProduct_ProductSizeRanges_Create(size_ranges = "Success")
                    except Exception as e:
                        print("Must Provide Unique Size Number and Size Value:", e)
                        return E4k_TblProduct_ProductSizeRanges_Create(size_ranges=f'Failed : {e}')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRanges_Create(size_ranges='Company id is not found')
        except Exception as e:
            return E4k_TblProduct_ProductSizeRanges_Create(size_ranges=f"Failed {e}")

######################################## Tbl Product Size Ranges update

class E4k_TblProduct_ProductSizeRanges_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        id = graphene.Int(required=True)
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, rangeid, id):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    ranges_list = TblproductSizeRanges.objects.filter(companyid=company).values_list('rangeid',flat=True)
                    if (rangeid not in ranges_list):
                        ranges_= TblproductSizeRanges.objects.get(companyid=company,
                                                                pk=id)
                        ranges_.rangeid = rangeid
                        ranges_.save()
                    else:
                        return E4k_TblProduct_ProductSizeRanges_Update(success="Range id already exists")
                    return E4k_TblProduct_ProductSizeRanges_Update(success="Success")

                except TblproductSizeRanges.DoesNotExist:
                    return E4k_TblProduct_ProductSizeRanges_Update(success="Product rangeid not found")
                
                except Exception as e:
                    return E4k_TblProduct_ProductSizeRanges_Update(success=f'Failed : {e}')

        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRanges_Update(success="Company id not found")

            
######################################## tbl product size ranges delete

class E4k_TblProduct_ProductSizeRanges_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        ##id = graphene.Int(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, rangeid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    sizerange = TblproductSizeRanges.objects.get(companyid=company, rangeid=rangeid)

                    size_value_ranges = TblproductSizeRangeValues.objects.filter(companyid=company, rangeid=sizerange)
                    if len(size_value_ranges)>0:
                        size_value_ranges.delete()
                        sizerange.delete()
                        return E4k_TblProduct_ProductSizeRanges_Delete(success = "Success")
                    else:
                        return E4k_TblProduct_ProductSizeRanges_Delete(success="No Size Ranges Values Found")
                except TblproductSizeRanges.DoesNotExist:
                    return E4k_TblProduct_ProductSizeRanges_Delete(success="Product rangeid not found") 
                except TblproductSizeRangeValues.DoesNotExist:
                    return E4k_TblProduct_ProductSizeRanges_Delete(success="Size Ranges Values Not Found")
                
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRanges_Delete(success="Company id not found")
        except TblproductSizeRanges.DoesNotExist:
            return E4k_TblProduct_ProductSizeRanges_Delete(success="Failed To delete")
        except Exception as e:
            return E4k_TblProduct_ProductSizeRanges_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        
######################################## E4K_TblProduct_ProductNode Create

class E4k_TblProduct_Product_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        description = graphene.String()
        category1id = graphene.Int()
        category2id = graphene.Int()
        category3id = graphene.Int()
        weight = graphene.Float()
        supplimentaryunits = graphene.String()
        nominal_code = graphene.String()
        commodity_code = graphene.String()
        notes = graphene.String()
        classid = graphene.Int()
        obsolete_class = graphene.Int()
        live = graphene.Boolean()
        styleimage = graphene.String()
        batchcontrol = graphene.Boolean()
        stockinguom = graphene.Int()
        issueuom = graphene.Int()
        stockingtype = graphene.String()
        countryid = graphene.Int()

    product_id = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, description, category1id, category2id, 
               category3id, weight, supplimentaryunits, nominal_code, commodity_code,
                 notes, classid, obsolete_class, live, styleimage, batchcontrol, 
                 stockinguom, issueuom, stockingtype, countryid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            try:
                    product = TblproductProducts.objects.get(companyid=company, productid=productid)
                    return E4k_TblProduct_Product_Create(product_id="Product id already exists")
            except TblproductProducts.DoesNotExist:
                with transaction.atomic():
                    if (category1id == None and category2id == None and category3id == None 
                        and weight == None and supplimentaryunits =='' and nominal_code == '' and commodity_code =='' and
                        notes =='' and classid == None and obsolete_class == None and live == False and 
                        styleimage == '' and batchcontrol == False and stockinguom == None and 
                        issueuom == None and stockingtype == '' and countryid == None):
                           #print('@@@@@@@@@@@@@@@@@@@new product')
                            product = TblproductProducts.objects.create(
                            companyid=company,
                            productid=productid,
                            description=description,
                            # category1id=category1id,
                            # category2id=category2id,
                            # category3id=category3id,
                            # weight= weight if weight else '',
                            # supplimentaryunits=supplimentaryunits if supplimentaryunits else '',
                            # nominal_code=nominal_code,
                            # commodity_code=commodity_code,
                            # notes=notes if notes else '',
                            # classid=classid,
                            # obsolete_class=obsolete_class,
                            # live=live,
                            # styleimage=None,
                            # batchcontrol=batchcontrol,
                            # stockinguom=stockinguom,
                            # issueuom=issueuom,
                            # stockingtype=stockingtype,
                            # countryid=countryid,
                            )
                            product.save()
                            return E4k_TblProduct_Product_Create(product_id="Success")
                    else :

                        category1id = TblproductCategory1.objects.get(companyid=company,category1id=category1id)
                        category2id = TblproductCategory2.objects.get(companyid=company,category2id=category2id)
                        category3id = TblproductCategory3.objects.get(companyid=company,category3id=category3id)
                        nominal_code = TblaccNominal.objects.get(companyid=company,nomcode=nominal_code)
                        commodity_code = TblproductCommoditycodes.objects.get(companyid=company,commodity_code=commodity_code)
                        classid = TblproductClass.objects.get(companyid=company,classid=classid)
                        obsolete_class = TblproductObsoleteTypes.objects.get(companyid=company,obsoleteid=obsolete_class)
                        countryid = TblbusCountries.objects.get(companyid=company,countryid=countryid)
                        stockinguom = TblproductTypeofissue.objects.get(companyid=company,issue_type=stockinguom)
                        issueuom = TblproductUnitofissue.objects.get(companyid=company,issue_units=issueuom)
                        stockingtype = TblproductStockingTypes.objects.get(companyid=company,stockingtype=stockingtype)
                        #print('################################',styleimage)
                        if styleimage=="":
                            #print('##########ctrer######################',styleimage)
                            product = TblproductProducts.objects.create(
                            companyid=company,
                            productid=productid,
                            description=description,
                            category1id=category1id,
                            category2id=category2id,
                            category3id=category3id,
                            weight= weight if weight else '',
                            supplimentaryunits=supplimentaryunits if supplimentaryunits else '',
                            nominal_code=nominal_code,
                            commodity_code=commodity_code,
                            notes=notes if notes else '',
                            classid=classid,
                            obsolete_class=obsolete_class,
                            live=live,
                            styleimage=None,
                            batchcontrol=batchcontrol,
                            stockinguom=stockinguom,
                            issueuom=issueuom,
                            stockingtype=stockingtype,
                            countryid=countryid,
                            )
                            product.save()
                        else:
                            ext = 'png'#format.split('/')[-1]
                            data = ContentFile(base64.b64decode(styleimage), name=f'{productid}.{ext}')
                            full_path = os.path.join(settings.EXTERNAL_FRONDEND_IMAGES_DIR, data.name)
                            os.makedirs(os.path.dirname(full_path), exist_ok=True)
                            # Save the image to the media directory
                            #print(full_path,'##########ctrer######################',styleimage)
                            with open(full_path, 'wb') as f:
                                f.write(data.read())


                            product = TblproductProducts.objects.create(
                                companyid=company,
                                productid=productid,
                                description=description,
                                category1id=category1id,
                                category2id=category2id,
                                category3id=category3id,
                                weight= weight if weight else '',
                                supplimentaryunits=supplimentaryunits if supplimentaryunits else '',
                                nominal_code=nominal_code,
                                commodity_code=commodity_code,
                                notes=notes if notes else '',
                                classid=classid,
                                obsolete_class=obsolete_class,
                                live=live,
                                styleimage=full_path,
                                batchcontrol=batchcontrol,
                                stockinguom=stockinguom,
                                issueuom=issueuom,
                                stockingtype=stockingtype,
                                countryid=countryid,
                            )
                            product.save()
                        return E4k_TblProduct_Product_Create(product_id="Success")

        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Company id not found")
        except TblproductCategory1.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Category1 id not found")
        except TblproductCategory2.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Category2 id not found")
        except TblproductCategory3.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Category3 id not found")
        except TblaccNominal.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Nominal code not found")
        except TblproductCommoditycodes.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Commodity code not found")
        except TblproductClass.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Class id not found")
        except TblproductObsoleteTypes.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Obsolete class id not found")
        except TblbusCountries.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Country id not found")
        except TblproductTypeofissue.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Stocking type id not found")
        except TblproductUnitofissue.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Issue type id not found")
        except TblproductStockingTypes.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Stocking type id not found")
        except Exception as e:
            return E4k_TblProduct_Product_Create(product_id="Failed")


####################################### Tbl productid update

class E4k_UpdateProductInput(graphene.InputObjectType):
    description = graphene.String()
    category1id = graphene.Int()
    category2id = graphene.Int()
    category3id = graphene.Int()
    weight = graphene.Float()
    supplimentaryunits = graphene.String()
    nominal_code = graphene.String()
    commodity_code = graphene.String()
    notes = graphene.String()
    classid = graphene.Int()
    obsolete_class = graphene.Int()
    live = graphene.Boolean()
    styleimage = graphene.String()
    batchcontrol = graphene.Boolean()
    stockinguom = graphene.Int()
    issueuom = graphene.Int()
    stockingtype = graphene.String()
    countryid = graphene.Int()

class E4k_TblProduct_Product_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        description = graphene.String()
        category1id = graphene.Int()
        category2id = graphene.Int()
        category3id = graphene.Int()
        weight = graphene.Float()
        supplimentaryunits = graphene.String()
        nominal_code = graphene.String()
        commodity_code = graphene.String()
        notes = graphene.String()
        classid = graphene.Int()
        obsolete_class = graphene.Int()
        live = graphene.Boolean()
        styleimage = graphene.String()
        batchcontrol = graphene.Boolean()
        stockinguom = graphene.Int()
        issueuom = graphene.Int()
        stockingtype = graphene.String()
        countryid = graphene.Int()

    product_update = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, description, category1id, category2id, 
                            category3id, weight, supplimentaryunits, nominal_code, commodity_code,
                                notes, classid, obsolete_class, live, styleimage, batchcontrol, 
                                stockinguom, issueuom, stockingtype, countryid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    product = TblproductProducts.objects.get(companyid=company, productid=productid)
                    # Update the fields
                    if description != '':
                        product.description = description
                    product.live = live
                    product.batchcontrol = batchcontrol
                    if weight > 0:
                        product.weight = weight
                    if category1id != None:
                        category1id =TblproductCategory1.objects.get(companyid=company,category1id=category1id)
                        product.category1id = category1id
                    if category2id != None:
                        category2id =TblproductCategory2.objects.get(companyid=company,category2id=category2id)
                        product.category2id = category2id
                    if category3id != None:
                        category3id =TblproductCategory3.objects.get(companyid=company,category3id=category3id)
                        product.category3id = category3id
                    if supplimentaryunits !='':
                        product.supplimentaryunits = supplimentaryunits
                    if nominal_code !='':
                        nominal_code = TblaccNominal.objects.get(companyid=company,nomcode=nominal_code)
                        product.nominal_code = nominal_code
                    if commodity_code !='':
                        commodity_code = TblproductCommoditycodes.objects.get(companyid=company,commodity_code=commodity_code)
                        product.commodity_code = commodity_code
                    if notes !='':
                        product.notes = notes
                    if classid != None:
                        classid = TblproductClass.objects.get(companyid=company,classid=classid)
                        product.classid = classid
                    if obsolete_class != None:
                        obsolete_class = TblproductObsoleteTypes.objects.get(companyid=company,obsoleteid=obsolete_class)
                        product.obsolete_class = obsolete_class
                    if styleimage !='':

                        ext = 'png'#format.split('/')[-1]
                        data = ContentFile(base64.b64decode(styleimage), name=f'{productid}.{ext}')

                        full_path = os.path.join(settings.EXTERNAL_FRONDEND_IMAGES_DIR, data.name)
                        os.makedirs(os.path.dirname(full_path), exist_ok=True)

                        # Save the image to the media directory
                        with open(full_path, 'wb') as f:
                            f.write(data.read())

                        product.styleimage = full_path
                    if stockinguom != None:
                        stockinguom = TblproductTypeofissue.objects.get(companyid=company,issue_type=stockinguom)
                        product.stockinguom = stockinguom
                    if issueuom != None:
                        issueuom = TblproductUnitofissue.objects.get(companyid=company,issue_units=issueuom)
                        product.issueuom = issueuom
                    if stockingtype !=None:
                        stockingtype = TblproductStockingTypes.objects.get(companyid=company,stockingtype=stockingtype)
                        product.stockingtype = stockingtype
                    if countryid != None:
                        countryid = TblbusCountries.objects.get(companyid=company,countryid=countryid)
                        product.countryid = countryid
                    
                    product.save()
                    return E4k_TblProduct_Product_Update(product_update="Success")
                except TblproductProducts.DoesNotExist:
                    return E4k_TblProduct_Product_Update(product_update="Product id not found")
                except Exception as e:
                    print(e)
                    return E4k_TblProduct_Product_Update(product_update="Failed to update product ")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Company id not found")
        except TblproductCategory1.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Category1 id not found")
        except TblproductCategory2.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Category2 id not found")
        except TblproductCategory3.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Category3 id not found")
        except TblaccNominal.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Nominal code not found")
        except TblproductCommoditycodes.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Commodity code not found")
        except TblproductClass.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Class id not found")
        except TblproductObsoleteTypes.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Obsolete class id not found")
        except TblbusCountries.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Country id not found")
        except TblproductTypeofissue.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Stocking type id not found")
        except TblproductUnitofissue.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Issue type id not found")
        except TblproductStockingTypes.DoesNotExist:
            return E4k_TblProduct_Product_Create(product_id="Stocking type id not found")
        except Exception as e:
            return E4k_TblProduct_Product_Create(product_id="Failed")


######################################## Tblproduct productid delete

# class E4k_TblProduct_Product_Delete(graphene.Mutation):
#     class Arguments:
#         companyid = graphene.String(required=True)
#         productid = graphene.String(required=True)

#     Success = graphene.String()

#     @staticmethod
#     def mutate(root, info, companyid, productid):
#         try:
#             company = Tblcompany.objects.get(companyid=companyid)
#             with transaction.atomic():
#                 try:
#                     product = TblproductProducts.objects.get(companyid=company, productid=productid)
#                     #### temporary product delete will be like this Need to change in future development once stock level is coming
#                     product.live = False
#                     if not isinstance(product.live, bool):
#                         print(f"Expected a boolean value for 'live', but got {type(product.live)}: {product.live}")
#                         raise ValueError(f"Expected a boolean value for 'live', but got {type(product.live)}: {product.live}")
                
#                     product.save()
#                     return E4k_TblProduct_Product_Delete(Success="Success")
#                 except TblproductProducts.DoesNotExist:
#                     return E4k_TblProduct_Product_Delete(Success="Productid not found")
#         except Tblcompany.DoesNotExist:
#             return E4k_TblProduct_Product_Delete(Success="Company id not found")
#         except Exception as e:
#             return E4k_TblProduct_Product_Delete(Success=f"Failed Unable To Delete \n\n Exception \n: {e}")

class E4k_TblProduct_Product_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    Success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    product = TblproductProducts.objects.get(companyid=company, productid=productid)
                    product.live = False
                    product.batchcontrol = product.batchcontrol == b'\x01'
                    product.save()
                    return E4k_TblProduct_Product_Delete(Success="Success")

                except TblproductProducts.DoesNotExist:
                    return E4k_TblProduct_Product_Delete(Success="Productid not found")
                except Exception as e:
                    # General exception handling for any other errors
                    return E4k_TblProduct_Product_Delete(Success=f"Failed Unable To Delete - Exception: {e}")

        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_Product_Delete(Success="Company id not found")
        except Exception as e:
            return E4k_TblProduct_Product_Delete(Success=f"Failed Unable To Delete - Exception: {e}")



####################################### E4K_Tblproduct_ParametertsSetvalues Create

class E4k_Tblproduct_ParametertsSetvalues_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        value = graphene.String(required=True)
    
    parameter_set = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, settingid, value):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    parameter = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                        settingid=settingid,
                                                                        productid=productid)
                    return E4k_Tblproduct_ParametertsSetvalues_Create(parameter_set="parameter set values already exists")
                except TblproductParametertsSetvalues.DoesNotExist:
                    try:
                        productid_ = TblproductProducts.objects.get(companyid=company,productid=productid)
                        settingid_ = TblproductParametersSettings.objects.get(companyid=company,settingid=settingid)
                        parameter = TblproductParametertsSetvalues.objects.create(companyid=company,
                                                                                settingid=settingid_,
                                                                                productid=productid_,
                                                                                value=value)
                        parameter.save()
                        return E4k_Tblproduct_ParametertsSetvalues_Create(parameter_set="Success")
                    except TblproductProducts.DoesNotExist:
                        return E4k_Tblproduct_ParametertsSetvalues_Create(parameter_set="product id not found")
                    except TblproductParametersSettings.DoesNotExist:
                        return E4k_Tblproduct_ParametertsSetvalues_Create(parameter_set="setting id not found")
                    
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ParametertsSetvalues_Create(parameter_set="company id not found")
        except Exception as e:
            print(e)
            return E4k_Tblproduct_ParametertsSetvalues_Create(parameter_set="Failed to create parameter set values")
        
####################################### E4K_Tblproduct_ParametertsSetvalues Update

class E4k_Tblproduct_ParametertsSetvalues_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        value = graphene.String(required=True)
    
    parameter_set = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, settingid, value):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if settingid in TblproductParametersSettings.objects.filter(companyid=company,iscustomer = 0).values_list('settingid',flat=True):
                with transaction.atomic():
                    lowercase_input = value.lower()
                    if lowercase_input == "true":
                        value = 'True'
                    elif lowercase_input == "false":
                        value = "False"
                    else:
                        value = value
                    product = TblproductProducts.objects.get(companyid=company,productid=productid)
                    default_parametersettings = TblproductParametersSettings.objects.get(companyid=company,
                                                                                settingid=settingid)
                    try:
                        if default_parametersettings.default == value:
                            if default_parametersettings.default !='' and value !='':
                                try:
                                    parameter = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                                        settingid=settingid,
                                                                                        productid=productid)
                                    parameter.delete()
                                except TblproductParametertsSetvalues.DoesNotExist:
                                    pass
                            elif default_parametersettings.default =='' and value =='':
                                try:
                                    parameter3 = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product)
                                    parameter3.delete()
                                except TblproductParametertsSetvalues.DoesNotExist:
                                    pass
                            elif default_parametersettings.default!= '' and value =='':
                                try:
                                    parameter3 = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product)
                                    parameter3.delete()
                                except TblproductParametertsSetvalues.DoesNotExist:
                                    pass
                            
                            # elif value!= '' and default_parametersettings.default!= value:
                            #     try:
                            #         paramerte = TblproductParametertsSetvalues.objects.get(companyid=company,
                            #                                                                         settingid=default_parametersettings,
                            #                                                                         productid=product)
                                    
                            #         paramerte.value = value
                                    
                            #         paramerte.save()
                            #     except TblproductParametertsSetvalues.DoesNotExist:
                            #         parameter2 = TblproductParametertsSetvalues.objects.create(companyid=company,
                            #                                                                         settingid=default_parametersettings,
                            #                                                                         productid=product,
                            #                                                                         value=value)
                            #         parameter2.save()

                        else:
                            if default_parametersettings.default !=value:
                                if default_parametersettings.default == None and value !='':

                                    parameter1 = TblproductParametertsSetvalues.objects.create(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product,
                                                                                                    value=value)
                                    parameter1.save()
                                elif value =='' and default_parametersettings.default is not None:
                                    try:
                                        parameter3 = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                                                        settingid=default_parametersettings,
                                                                                                        productid=product)
                                        parameter3.delete()
                                    except TblproductParametertsSetvalues.DoesNotExist:
                                        pass
                                elif value!= '' and default_parametersettings.default!= value:
                                    try:
                                        paramerte = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product)
                                        
                                        paramerte.value = value
                                        
                                        paramerte.save()
                                    except TblproductParametertsSetvalues.DoesNotExist:

                                        parameter2 = TblproductParametertsSetvalues.objects.create(companyid=company,
                                                                                                        settingid=default_parametersettings,
                                                                                                        productid=product,
                                                                                                        value=value)
                                        parameter2.save()
                                
                        return E4k_Tblproduct_ParametertsSetvalues_Update(parameter_set="Success")
                    except TblproductParametertsSetvalues.DoesNotExist:
                        
                            return E4k_Tblproduct_ParametertsSetvalues_Update(parameter_set="TblproductParametertsSetvalues Does not exist")
                    except TblproductParametersSettings.DoesNotExist:
                        return E4k_Tblproduct_ParametertsSetvalues_Update(parameter_set="Setting id not found")
            else:
                return E4k_Tblproduct_ParametertsSetvalues_Update(parameter_set="Setting {} not relate to general product settings".format(settingid))
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ParametertsSetvalues_Update(parameter_set="company_id not found")
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ParametertsSetvalues_Update(parameter_set="Product id not found")
        except Exception as e:
            print(e)
            return E4k_Tblproduct_ParametertsSetvalues_Update(parameter_set="Failed to update parameter set values")
        

############################################# E4k Tbl Product Parameter Customer Setting Value Update 
class E4k_Tblproduct_ParametertsCustomersSetvalues_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        customerid = graphene.String(required=True)
        value = graphene.String(required=True)
    
    parameter_customer_set = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, settingid, customerid,value):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if settingid in TblproductParametersSettings.objects.filter(companyid=company,iscustomer = 1).values_list('settingid',flat=True):
                with transaction.atomic():
                    lowercase_input = value.lower()
                    if lowercase_input == "true":
                        value = 'True'
                    elif lowercase_input == "false":
                        value = "False"
                    else:
                        value = value
                    product = TblproductProducts.objects.get(companyid=company,productid=productid)
                    default_parametersettings = TblproductParametersSettings.objects.get(companyid=company,
                                                                                settingid=settingid)
                    customer = Tblcustomer.objects.get(companyid=company,
                                                        businessid=customerid,
                                                        )
                    try:
                        if default_parametersettings.default == value:
                            if default_parametersettings.default !='' and value !='':
                                try:
                                    parameter = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                                                                                        settingid=settingid,
                                                                                        productid=productid,
                                                                                        businessid = customer)
                                    parameter.delete()
                                except TblproductParametersCustomerSetvalues.DoesNotExist:
                                    pass
                            elif default_parametersettings.default =='' and value =='':
                                try:
                                    parameter3 = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product,
                                                                                                    businessid = customer)
                                    parameter3.delete()
                                except TblproductParametersCustomerSetvalues.DoesNotExist:
                                    pass
                            elif default_parametersettings.default!= '' and value =='':
                                try:
                                    parameter3 = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product,
                                                                                                    businessid = customer)
                                    parameter3.delete()
                                except TblproductParametersCustomerSetvalues.DoesNotExist:
                                    pass

                        else:
                            if default_parametersettings.default !=value:
                                if default_parametersettings.default == None and value !='':

                                    parameter1 = TblproductParametersCustomerSetvalues.objects.create(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product,
                                                                                                    businessid = customer,
                                                                                                    value=value)
                                    parameter1.save()
                                elif value =='' and default_parametersettings.default is not None:
                                    try:
                                        parameter3 = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                                                                                                        settingid=default_parametersettings,
                                                                                                        productid=product,
                                                                                                        businessid = customer)
                                        parameter3.delete()
                                    except TblproductParametersCustomerSetvalues.DoesNotExist:
                                        pass
                                elif value!= '' and default_parametersettings.default!= value:
                                    try:
                                        paramerte = TblproductParametersCustomerSetvalues.objects.get(companyid=company,
                                                                                                    settingid=default_parametersettings,
                                                                                                    productid=product,
                                                                                                    businessid = customer)
                                        
                                        paramerte.value = value
                                        
                                        paramerte.save()
                                    except TblproductParametersCustomerSetvalues.DoesNotExist:

                                        parameter2 = TblproductParametersCustomerSetvalues.objects.create(companyid=company,
                                                                                                        settingid=default_parametersettings,
                                                                                                        productid=product,
                                                                                                        value=value,
                                                                                                        businessid = customer)
                                        parameter2.save()
                                
                        return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="Success")
                    except TblproductParametersCustomerSetvalues.DoesNotExist:
                        
                            return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="TblproductParametertsSetvalues Does not exist")
                    except TblproductParametersSettings.DoesNotExist:
                        return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="Setting id not found")
            else :
                return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="Setting {} not relate to product customer settingsid".format(settingid))
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="company_id not found")
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="Product id not found")
        except Tblcustomer.DoesNotExist:
            return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="Customer id not found")
        except Exception as e:
            print(e)
            return E4k_Tblproduct_ParametertsCustomersSetvalues_Update(parameter_customer_set="Failed to update parameter set values")

####################################### E4K_Tblproduct_ParametertsSetvalues Delete

class E4k_Tblproduct_ParametertsSetvalues_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        settingid = graphene.String(required=True)

    Success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, productid, settingid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    parameter = TblproductParametertsSetvalues.objects.get(companyid=company,
                                                                        settingid=settingid,
                                                                        productid=productid)
                    parameter.delete()
                    return E4k_Tblproduct_ParametertsSetvalues_Delete(Success="Success")
                except TblproductParametertsSetvalues.DoesNotExist:
                    return E4k_Tblproduct_ParametertsSetvalues_Delete(Success="Id not found")
            
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ParametertsSetvalues_Delete(Success="Company id not found")
        except Exception as e:
            return E4k_Tblproduct_ParametertsSetvalues_Delete(Success=f"Failed Unable To Delete \n\n Exception \n: {e}")

############################################ TblproductProductGallery Create

class E4k_Tblproduct_ProductGallery_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        productimage = graphene.String(required=True)
        is360 = graphene.Int()
        noframes = graphene.Int()
        nofootages = graphene.Int()

    product_gallery = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, productimage, is360, noframes, nofootages):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    product = TblproductProducts.objects.get(companyid=company, productid=productid)
                    product_gallery = TblproductProductGallery.objects.create(
                        companyid=company,
                        productid=product,
                        productimage=productimage,
                        is360=is360 if is360 else 0,
                        noframes=noframes if noframes else 0,
                        nofootages=nofootages if nofootages else 0
                    )
                    product_gallery.save()
                    return E4k_Tblproduct_ProductGallery_Create(product_gallery="Success")
                except TblproductProducts.DoesNotExist:
                    return E4k_Tblproduct_ProductGallery_Create(product_gallery="Product id not found")
                except Exception as e:
                    return E4k_Tblproduct_ProductGallery_Create(product_gallery="Failure to create product gallery")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductGallery_Create(product_gallery="Company id not found")
        except Exception as e:
            return E4k_Tblproduct_ProductGallery_Create(product_gallery='Failure to create product gallery')

######################################## Tblproduct product Gallery Update

class E4k_ProductGallery_update(graphene.InputObjectType):
    productimage = graphene.String()
    is360 = graphene.Int()
    noframes = graphene.Int()
    nofootages = graphene.Int()


class E4k_Tblproduct_ProductGallery_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        input_data = E4k_ProductGallery_update(required=True)

    product_gallery = graphene.String()
    
    @staticmethod
    def mutate(root, info, id, companyid, productid, input_data):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    product = TblproductProducts.objects.get(companyid=company, productid=productid)
                    product_gallery = TblproductProductGallery.objects.get(companyid=company,
                                                                            productid=product,
                                                                            id=id)
                    try: 
                        # Update the fields
                        if "productimage" in input_data:
                            product_gallery.productimage = input_data.productimage
                        if "is360" in input_data:
                            product_gallery.is360 = input_data.is360
                        if "noframes" in input_data:
                            product_gallery.noframes = input_data.noframes
                        if "nofootages" in input_data:
                            product_gallery.nofootages = input_data.nofootages
                        product_gallery.save()

                        return E4k_Tblproduct_ProductGallery_Update(product_gallery="Success")
                    except TblproductProductGallery.DoesNotExist:
                        return E4k_Tblproduct_ProductGallery_Update(product_gallery="TblproductProductGallery Id not found")

                except TblproductProducts.DoesNotExist:
                    return E4k_Tblproduct_ProductGallery_Update(product_gallery="Product id not found")
                except Exception as e:
                    return E4k_Tblproduct_ProductGallery_Update(product_gallery="Failed to update product gallery")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductGallery_Update(product_gallery="Company id not found")
        except Exception as e:
            return E4k_Tblproduct_ProductGallery_Update(product_gallery="Failed to update product gallery")
        
####################################### Tblproduct Gallery Delete

class E4k_Tblproduct_ProductGallery_Delete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
    
    Success = graphene.String()
    
    @staticmethod
    def mutate(root, info, id, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    product = TblproductProducts.objects.get(companyid=company, productid=productid)
                    product_gallery = TblproductProductGallery.objects.get(companyid=company,
                                                                            productid=product,
                                                                            id=id)
                    product_gallery.delete()
                    return E4k_Tblproduct_ProductGallery_Delete(Success="Success")
                except TblproductProductGallery.DoesNotExist:
                    return E4k_Tblproduct_ProductGallery_Delete(Success="Gallery Id not found")
                except TblproductProducts.DoesNotExist:
                    return E4k_Tblproduct_ProductGallery_Delete(Success="Product id not found")
            
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductGallery_Delete(Success="Company id not found")
        except Exception as e:
            return E4k_Tblproduct_ProductGallery_Delete(Success=f"Failed Unable To Delete \n\n Exception \n: {e}")
        
######################################### E4K_TblproductProductProperties Create

class E4k_Tblproduct_ProductProperties_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        seq_no = graphene.Int(required=True)
    
    product_properties = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, propertyid, seq_no):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            try:
                product = TblproductProducts.objects.get(companyid=company, productid=productid)
                property = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)
                
                existing_seq_nos = list(
                    TblproductProductProperties.objects.filter(companyid=company,
                                                            productid=product).values_list('seqno', flat=True))
                with transaction.atomic():
                    # If the provided seq_no already exists, adjust existing sequences
                    if seq_no in existing_seq_nos:
                        E4k_Tblproduct_ProductProperties_Create._adjust_existing_sequences(company,product, seq_no)
                    
                    product_prop = TblproductProductProperties.objects.create(
                                                                    companyid=company,
                                                                    productid=product,
                                                                    propertyid=property,
                                                                    seqno=seq_no
                                                                    )
                    product_prop.save()
                    return E4k_Tblproduct_ProductProperties_Create(product_properties="Success")

            except TblproductProducts.DoesNotExist:
                return E4k_Tblproduct_ProductProperties_Create(product_properties="Product id not found")
            except TblproductPropertyTypes.DoesNotExist:
                return E4k_Tblproduct_ProductProperties_Create(product_properties="Property id not found")
            except Exception as e:
                return E4k_Tblproduct_ProductProperties_Create(product_properties=e)
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Create(product_properties="Company id not found")
        
    @staticmethod
    def _adjust_existing_sequences(company_instance,product_instance, seq_no):
        """ Adjusts the sequence numbers of existing property relations. """
        existing_relations = TblproductProductProperties.objects.filter(companyid = company_instance,
                                                                        productid=product_instance, 
                                                                        seqno__gte=seq_no).order_by('seqno')

        for relation in existing_relations:
            relation.seqno = F('seqno') + 1
            relation.save()

######################################## tblproductproductproperties update

class E4k_Tblproduct_ProductProperties_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        new_seq_no = graphene.Int(required=True)

    Update_property = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, productid, propertyid, new_seq_no):
        try:
            # Get the product and property instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid =company, productid=productid)
            property_instance = TblproductPropertyTypes.objects.get(companyid=company, 
                                                                    propertyid=propertyid)

            with transaction.atomic():
                # Find the existing property relation
                relation_instance = TblproductProductProperties.objects.get(
                    companyid=company, 
                    productid=product_instance, 
                    propertyid=property_instance
                )
                
                # Adjust sequence numbers if the new sequence number is different
                if relation_instance.seqno != new_seq_no:
                    E4k_Tblproduct_ProductProperties_Update._adjust_sequences_for_update(
                        company,
                        product_instance, 
                        relation_instance.seqno, 
                        new_seq_no
                    )
                    relation_instance.seqno = new_seq_no
                    relation_instance.save()
                #print('################### Update ',relation_instance)

                # Update the property matrix
                # try:
                #     pro_mat = TblproductProductPropertyMatrix.objects.get(companyid= company,
                #                                                           productid=product_instance)
                    
                #     pro_mat.update_PropertyMatix(product_instance)
                # Update the property matrix
                try:

                    product_property_level_instance = TblproductProductPropertyLevel.objects.get(
                                                                    companyid=company,
                                                                    productid=product_instance
                                                                )
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance)
                    



                    ################ Update the Property level sequence inside the json
                    # Retrieve the updated properties and sequence numbers
                    relation_instance = TblproductProductProperties.objects.get(
                        companyid=company, 
                        productid=product_instance, 
                        propertyid=property_instance
                    )

                    # Example format: {'Size': 1, 'Colour': 2}
                    updated_properties = {
                        relation_instance.propertyid.description: relation_instance.seqno
                    }

                    # Update the Property level sequence inside the json
                    for field in product_property_level_instance._meta.fields:
                        column_name = field.attname

                        if column_name not in ['companyid_id', 'productid_id']:
                            # Ensure the attribute exists and is a list of dictionaries containing the property name
                            if hasattr(product_property_level_instance, column_name):
                                column_list = getattr(product_property_level_instance, column_name, [])
                                if isinstance(column_list, list):
                                    updated_list = []
                                    for dict_item in column_list:
                                        if isinstance(dict_item, dict):
                                            for property_name, new_sequence_number in updated_properties.items():
                                                if property_name in dict_item:
                                                    # Update the sequence number for the specified property
                                                    dict_item[property_name] = new_sequence_number
                                        updated_list.append(dict_item)
                                    
                                    setattr(product_property_level_instance, column_name, updated_list)
                    product_property_level_instance.save()


                
                    for field in product_property_level_instance._meta.fields:
                        
                        column_name = field.attname

                        if column_name not in ['companyid_id', 'productid_id']:
                            column_value = getattr(product_property_level_instance, column_name)
                            property_level_col.Update_Product_Property_Level_ColMatrix(
                                product_property_level=column_value,
                                column_name=column_name,
                                productid=product_property_level_instance.productid,
                                companyid = company
                            )
                except (TblproductProductPropertyLevel.DoesNotExist, 
                    TblproductProductPropertyLevelColmatrix.DoesNotExist):
                    pass
                
                ############### Supplier Level Update 

                try:
                    product_supplier_level_instance = TblproductProductSupplierLevel.objects.filter(
                                                                        companyid=company,
                                                                        productid=product_instance
                                                                    )
                    


                    for level in product_supplier_level_instance:
                        # Update the Property level sequence inside the json
                        for field in level._meta.fields:
                            column_name = field.attname

                            if column_name not in ['id','companyid_id', 'productid_id','supplierid_id']:
                                # Ensure the attribute exists and is a list of dictionaries containing the property name
                                if hasattr(level, column_name):
                                    column_list = getattr(level, column_name, [])
                                    if isinstance(column_list, list):
                                        updated_list = []
                                        for dict_item in column_list:
                                            if isinstance(dict_item, dict):
                                                for property_name, new_sequence_number in updated_properties.items():
                                                    if property_name in dict_item:
                                                        # Update the sequence number for the specified property
                                                        dict_item[property_name] = new_sequence_number
                                            updated_list.append(dict_item)
                                        
                                        setattr(level, column_name, updated_list)
                        level.save()
                        
                        supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                                productid=product_instance,
                                                                                                supplierid=level.supplierid)
                        for field in level._meta.fields:
                            
                            column_name = field.attname

                            if column_name not in ['id','companyid_id', 'productid_id','supplierid_id']:
                                column_value = getattr(level, column_name)
                                supplier_level_col.Update_Product_Supplier_Level_ColMatrix(
                                    supplier_level=column_value,
                                    column_name=column_name,
                                    productid=level.productid,
                                    companyid = company
                                )
                except (TblproductProductSupplierLevel.DoesNotExist, 
                    TblproductProductSupplierLevelColmatrix.DoesNotExist):
                    pass

                try:
                    ################## Update the sticking type
                    product_suppliermatrix_type = TblproductProductSuppliersMatrix.objects.filter(companyid=company,
                                                                                productid=product_instance)
                    
                    for product_supplier in product_suppliermatrix_type:

                        product_supplier.Update_Product_Supplier_Matrix(company=company,
                                                                productid=product_instance,
                                                                supplierid=product_supplier.supplierid)
                except TblproductProductSuppliersMatrix.DoesNotExist:
                    pass

                try:
                    pro_mat = TblproductProductPropertyMatrix.objects.get(companyid=company,
                                                                          productid=product_instance)
                    
                    pro_mat.update_PropertyMatix(product_instance)
                except TblproductProductPropertyMatrix.DoesNotExist:
                    pass

                try:
                    ########Update the Stoking Level
                    product_stoking_level=  TblproductProductStockinglevelMatrix.objects.get(
                                                        companyid=company,
                                                        productid=product_instance,)
                    product_stoking_level.Update_Product_StockingLevel_Matrix(company=company,
                                                                              productid=product_instance,
                                                                              warehouseid=None,old_data=[])
                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    pass

                try:
                    ################## Update the sticking type
                    product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_stocking_type.Update_Product_StockingType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    pass

                try:
                    ################## Update the sticking type
                    product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_obsolete_type.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    pass
            
                try:
                    
                    ######################### Update the vatcode
                    product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_vatcode.Update_Product_Vatcode_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    pass

                try:
                    
                    ######################### Update the price standard
                    product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_price_standard.Update_Product_PriceStandard_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    pass
                    
                try:
                    ########################## Update the Cost standard
                    product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_cost_standard.Update_Product_CostStandard_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    pass
                    
                    ########################## Update the Cost Supplier
                try:
                    # Update cost_supplier
                    cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=companyid, 
                                                                                        productid=product_instance)
                    if cost_supplier.exists():
                        if len(cost_supplier) == 1:
                            cost_supplier.first().Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                        else:
                            for cost_supplier_instance in cost_supplier:
                                cost_supplier_instance.Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                except TblproductProductCostSupplierMatrix.DoesNotExist:
                    pass

                try:
                    # Update price_customer
                    price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company,
                                                                                        productid=product_instance)
                    if price_customer.exists():
                        if len(price_customer) == 1:
                            price_customer.first().Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                        else:
                            for price_customer_instance in price_customer:
                                price_customer_instance.Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                    
                
                except TblproductProductPriceCustomerMatrix.DoesNotExist:
                    pass 
                except TblproductProductPropertyMatrix.DoesNotExist:
                    E4k_Tblproduct_ProductProperties_Update(Update_property="Property matrix Not updated")

                

            return E4k_Tblproduct_ProductProperties_Update(Update_property='Success')
        
        except (TblproductProducts.DoesNotExist, TblproductPropertyTypes.DoesNotExist, 
                TblproductProductProperties.DoesNotExist, Tblcompany.DoesNotExist) as e:
            return E4k_Tblproduct_ProductProperties_Update(Update_property=f'Failed: {str(e)}')
        
    
    @staticmethod
    def _adjust_sequences_for_update(company,product_instance, old_seq_no, new_seq_no):
        """ Adjust sequence numbers of existing property relations for update. """
        if new_seq_no > old_seq_no:
            TblproductProductProperties.objects.filter(
                companyid = company,
                productid=product_instance,
                seqno__gt=old_seq_no,
                seqno__lte=new_seq_no
            ).update(seqno=F('seqno') - 1)
        elif new_seq_no < old_seq_no:
            TblproductProductProperties.objects.filter(
                companyid = company,
                productid=product_instance,
                seqno__gte=new_seq_no,
                seqno__lt=old_seq_no
            ).update(seqno=F('seqno') + 1)
 


####################################### Tbl product properties delete

class E4k_Tblproduct_ProductProperties_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        product_prop_id = graphene.Int(required=True)

    delete_properties = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, propertyid, product_prop_id):
        try:
            # Get the product and property instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            property_instance = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)

            with transaction.atomic():
                # Find the existing property relation
                property_list_length = TblproductProductProperties.objects.filter(companyid=company,
                                                                                   productid=product_instance)
                print('Property list length', len(property_list_length))
                if len(property_list_length) == 1:
                    print('Property list length', len(property_list_length))
                    relation_instance = TblproductProductProperties.objects.get(
                        companyid=company, 
                        productid=product_instance, 
                        propertyid=property_instance,
                        product_propid=product_prop_id
                    )
                    old_seq_no = relation_instance.seqno

                    # Delete the property relation with values first
                    existing_values = TblproductProductPropertyValues.objects.filter(
                        companyid=company,
                        product_propid=relation_instance
                    )
                    existing_values.delete()
                    relation_instance.delete()
                   # TblproductProductPropertyMatrix.objects.get(companyid=company, productid=product_instance).delete()
                    
                    
                    
                    try:
                        pro_mat = TblproductProductPropertyMatrix.objects.get(companyid=company, productid=product_instance)
                        pro_mat.delete()
                    except TblproductProductPropertyMatrix.DoesNotExist:
                        pass

                    try:
                        product_property_level_instance = TblproductProductPropertyLevel.objects.get(companyid=company, productid=product_instance)
                        product_property_level_instance.delete()
                    except TblproductProductPropertyLevel.DoesNotExist:
                        pass

                    try:
                         property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid=company, productid=product_instance)
                         property_level_col.delete()
                    except TblproductProductPropertyLevelColmatrix.DoesNotExist:
                        pass

                    try:
                        product_stocking_level = TblproductProductStockinglevelMatrix.objects.get(companyid=company, productid=product_instance)
                        product_stocking_level.delete()
                    except TblproductProductStockinglevelMatrix.DoesNotExist:
                        pass

                    ################### Delete supplier level
                    try:
                        product_supplier_level_instance = TblproductProductSupplierLevel.objects.filter(companyid=company, productid=product_instance)
                        product_supplier_level_instance.delete()
                    except TblproductProductSupplierLevel.DoesNotExist:
                        pass

                    try:
                         supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.filter(companyid=company, productid=product_instance)
                         supplier_level_col.delete()
                    except TblproductProductSupplierLevelColmatrix.DoesNotExist:
                        pass

                    try:
                        product_supplier_level_matrix = TblproductProductSuppliersMatrix.objects.filter(companyid=company, productid=product_instance)
                        product_supplier_level_matrix.delete()
                    except TblproductProductSuppliersMatrix.DoesNotExist:
                        pass

                    # Update the stocking type
                    try:
                        product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company, productid=product_instance)
                        product_stocking_type.delete()
                    except TblproductProductStockingtypeMatrix.DoesNotExist:
                        pass

                    # Update the Obsolete type
                    try:
                        product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company, productid=product_instance)
                        product_obsolete_type.delete()
                    except TblproductProductObsoleteMatrix.DoesNotExist:
                        pass

                    # Update the VAT code
                    try:
                        product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company, productid=product_instance)
                        product_vatcode.delete()
                    except TblproductProductVatcodeMatrix.DoesNotExist:
                        pass

                    # Update the price standard
                    try:
                        product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company, productid=product_instance)
                        product_price_standard.delete()
                    except TblproductProductPriceStandardMatrix.DoesNotExist:
                        pass

                    # Update the cost standard
                    try:
                        product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company, productid=product_instance)
                        product_cost_standard.delete()
                    except TblproductProductCostStandardMatrix.DoesNotExist:
                        pass

                    # Update cost supplier
                    try:
                        cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=company, productid=product_instance)
                        if cost_supplier.exists():
                            for cost_supplier_instance in cost_supplier:
                                cost_supplier_instance.delete()
                    except TblproductProductCostSupplierMatrix.DoesNotExist:
                        pass

                    # Update price customer
                    try:
                        price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company, productid=product_instance)
                        if price_customer.exists():
                            for price_customer_instance in price_customer:
                                price_customer_instance.delete()
                    except TblproductProductPriceCustomerMatrix.DoesNotExist:
                        pass
                else:
                    print('product delete')
                    relation_instance = TblproductProductProperties.objects.get(
                        companyid=company, 
                        productid=product_instance, 
                        propertyid=property_instance,
                        product_propid=product_prop_id
                    )
                    old_seq_no = relation_instance.seqno

                    # Delete the property relation with values first
                    existing_values = TblproductProductPropertyValues.objects.filter(
                        companyid=company,
                        product_propid=relation_instance
                    )
                    existing_values.delete()
                    relation_instance.delete()

                    # Adjust sequence numbers of the remaining properties
                    E4k_Tblproduct_ProductProperties_Delete._adjust_sequences_after_deletion(company, product_instance, old_seq_no)

                    # Update the property matrix
                    try:
                        pro_mat = TblproductProductPropertyMatrix.objects.get(companyid=company, productid=product_instance)
                        pro_mat.update_PropertyMatix(product_instance)
                    except TblproductProductPropertyMatrix.DoesNotExist:
                        pass

                    # Update the property level
                    
                    # try:
                    #     product_property_level_instance = TblproductProductPropertyLevel.objects.get(companyid=company, productid=product_instance)
                    #     property_name = property_instance.description
                    #     property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid=company, productid=product_instance)
                    #     #print('################## Propertlevel deelte instance,',property_name)
                    #     # for field in product_property_level_instance._meta.fields:
                    #     #     column_name = field.attname
                            
                    #     #     if column_name not in ['companyid_id', 'productid_id']:
                    #     #         print('################## Propertlevel column_name column_name,',column_name)
                    #     #         if hasattr(product_property_level_instance, column_name) and property_name in getattr(product_property_level_instance, column_name, {}):
                    #     #             column_dict = getattr(product_property_level_instance, column_name)
                    #     #             print('################## column_dict column_dict column_dict,',column_dict)
                    #     #             del column_dict[property_name]
                    #     #             setattr(product_property_level_instance, column_name, column_dict)

                    #     for field in product_property_level_instance._meta.fields:
                    #         column_name = field.attname

                    #         if column_name not in ['companyid_id', 'productid_id']:
                                

                    #             # Ensure the attribute exists and is a list of dictionaries containing the property name
                    #             if hasattr(product_property_level_instance, column_name):
                    #                 column_list = getattr(product_property_level_instance, column_name, [])
                    #                 if isinstance(column_list, list):
                    #                     updated_list = []
                    #                     for dict_item in column_list:
                    #                         if isinstance(dict_item, dict) and property_name in dict_item:
                                                
                    #                             del dict_item[property_name]
                    #                             # Reorder the remaining properties
                    #                             sorted_items = sorted(dict_item.items(), key=lambda x: x[1])  # Sort by value
                    #                             reordered_dict = {k: i + 1 for i, (k, _) in enumerate(sorted_items)}  # Reorder values
                    #                             dict_item = reordered_dict
                                                
                    #                         updated_list.append(dict_item)
                                        
                    #                     setattr(product_property_level_instance, column_name, updated_list)
                                        

                    #     product_property_level_instance.save()
                    #     #product_property_level_instance = TblproductProductPropertyLevel.objects.get(companyid=company, productid=product_instance)
                    #     for field in product_property_level_instance._meta.fields:
                    #         column_name = field.attname
                    #         if column_name not in ['companyid_id', 'productid_id']:
                    #             column_value = getattr(product_property_level_instance, column_name)
                    #             property_level_col.Update_Product_Property_Level_ColMatrix(
                    #                 product_property_level=column_value,
                    #                 column_name=column_name,
                    #                 productid=product_property_level_instance.productid,
                    #                 companyid=company
                    #             )

                    #     # for field in product_property_level_instance._meta.fields:
                    #     #     column_name = field.attname
                    #     #     if column_name not in ['companyid_id', 'productid_id']:
                    #     #         column_value = getattr(product_property_level_instance, column_name)
                    #     #         property_level_col.Update_Product_Property_Level_ColMatrix(
                    #     #             product_property_level=column_value,
                    #     #             column_name=column_name,
                    #     #             productid=product_property_level_instance.productid,
                    #     #             companyid = company
                    #     #         )

                        
                    # except (TblproductProductPropertyLevel.DoesNotExist, 
                    #         TblproductProductPropertyLevelColmatrix.DoesNotExist):
                    #     pass


                    try:
                        # Fetch the product property level instance
                        product_property_level_instance = TblproductProductPropertyLevel.objects.get(companyid=company, productid=product_instance)
                        property_name = property_instance.description
                        property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid=company, productid=product_instance)

                        # Step 1: Gather all properties and their sequences across all records
                        all_properties = {}

                        for field in product_property_level_instance._meta.fields:
                            column_name = field.attname

                            if column_name not in ['companyid_id', 'productid_id']:
                                if hasattr(product_property_level_instance, column_name):
                                    column_list = getattr(product_property_level_instance, column_name, [])
                                    if isinstance(column_list, list):
                                        for dict_item in column_list:
                                            if isinstance(dict_item, dict):
                                                for prop, seq in dict_item.items():
                                                    if prop not in all_properties:
                                                        all_properties[prop] = seq

                        # Step 2: Remove the property to be deleted and sort the remaining properties
                        if property_name in all_properties:
                            del all_properties[property_name]

                        # Reorder properties after deletion
                        sorted_properties = sorted(all_properties.items(), key=lambda x: x[1])
                        new_order = {prop: i + 1 for i, (prop, _) in enumerate(sorted_properties)}

                        # Step 3: Update all records based on the new order
                        for field in product_property_level_instance._meta.fields:
                            column_name = field.attname

                            if column_name not in ['companyid_id', 'productid_id']:
                                if hasattr(product_property_level_instance, column_name):
                                    column_list = getattr(product_property_level_instance, column_name, [])
                                    if isinstance(column_list, list):
                                        updated_list = []
                                        for dict_item in column_list:
                                            if isinstance(dict_item, dict):
                                                # Remove the property if it exists
                                                if property_name in dict_item:
                                                    del dict_item[property_name]
                                                
                                                # Update the sequence based on new global order
                                                reordered_dict = {prop: new_order[prop] for prop in new_order if prop in dict_item}
                                                dict_item = reordered_dict

                                            updated_list.append(dict_item)

                                        setattr(product_property_level_instance, column_name, updated_list)

                        product_property_level_instance.save()

                        # Update the product property level column matrix after reordering
                        for field in product_property_level_instance._meta.fields:
                            column_name = field.attname
                            if column_name not in ['companyid_id', 'productid_id']:
                                column_value = getattr(product_property_level_instance, column_name)
                                property_level_col.Update_Product_Property_Level_ColMatrix(
                                    product_property_level=column_value,
                                    column_name=column_name,
                                    productid=product_property_level_instance.productid,
                                    companyid=company
                                )

                    except (TblproductProductPropertyLevel.DoesNotExist, TblproductProductPropertyLevelColmatrix.DoesNotExist):
                        pass


                    # Update the stocking level
                    try:
                        product_stocking_level = TblproductProductStockinglevelMatrix.objects.get(companyid=company, productid=product_instance)
                        product_stocking_level.Update_Product_StockingLevel_Matrix(company=company, productid=product_instance)
                    except TblproductProductStockinglevelMatrix.DoesNotExist:
                        pass

                    # Update the stocking type
                    try:
                        product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company, productid=product_instance)
                        product_stocking_type.Update_Product_StockingType_Matrix(company=company, productid=product_instance)
                    except TblproductProductStockingtypeMatrix.DoesNotExist:
                        pass

                    # update obsolete type 
                    try:
                        product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company,
                                                                                    productid=product_instance)
                        product_obsolete_type.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                    productid=product_instance)
                    except TblproductProductObsoleteMatrix.DoesNotExist:
                        pass


                    # Update the VAT code
                    try:
                        product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company, productid=product_instance)
                        product_vatcode.Update_Product_Vatcode_Matrix(company=company, productid=product_instance)
                    except TblproductProductVatcodeMatrix.DoesNotExist:
                        pass

                    # Update the price standard
                    try:
                        product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company, productid=product_instance)
                        product_price_standard.Update_Product_PriceStandard_Matrix(company=company, productid=product_instance)
                    except TblproductProductPriceStandardMatrix.DoesNotExist:
                        pass

                    # Update the cost standard
                    try:
                        product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company, productid=product_instance)
                        product_cost_standard.Update_Product_CostStandard_Matrix(company=company, productid=product_instance)
                    except TblproductProductCostStandardMatrix.DoesNotExist:
                        pass

                    # Update cost supplier
                    try:
                        cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=company, productid=product_instance)
                        if cost_supplier.exists():
                            for cost_supplier_instance in cost_supplier:
                                cost_supplier_instance.Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                    except TblproductProductCostSupplierMatrix.DoesNotExist:
                        pass

                    # Update price customer
                    try:
                        price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company, productid=product_instance)
                        if price_customer.exists():
                            for price_customer_instance in price_customer:
                                price_customer_instance.Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                    except TblproductProductPriceCustomerMatrix.DoesNotExist:
                        pass

                    # Update the supplier level
                    try:
                        # Fetch the product supplier level instances
                        product_supplier_level_instance = TblproductProductSupplierLevel.objects.filter(companyid=company, productid=product_instance)

                        # Step 1: Gather all properties and their sequences across all records
                        all_properties = {}

                        for supplier_level in product_supplier_level_instance:
                            for field in supplier_level._meta.fields:
                                column_name = field.attname

                                if column_name not in ['id', 'companyid_id', 'productid_id', 'supplierid_id']:
                                    if hasattr(supplier_level, column_name):
                                        column_list = getattr(supplier_level, column_name, [])
                                        if isinstance(column_list, list):
                                            for dict_item in column_list:
                                                if isinstance(dict_item, dict):
                                                    for prop, seq in dict_item.items():
                                                        if prop not in all_properties:
                                                            all_properties[prop] = seq

                        # Step 2: Remove the property to be deleted and sort the remaining properties
                        if property_name in all_properties:
                            del all_properties[property_name]

                        # Reorder properties after deletion
                        sorted_properties = sorted(all_properties.items(), key=lambda x: x[1])
                        new_order = {prop: i + 1 for i, (prop, _) in enumerate(sorted_properties)}

                        # Step 3: Update all records based on the new order
                        for supplier_level in product_supplier_level_instance:
                            for field in supplier_level._meta.fields:
                                column_name = field.attname

                                if column_name not in ['id', 'companyid_id', 'productid_id', 'supplierid_id']:
                                    if hasattr(supplier_level, column_name):
                                        column_list = getattr(supplier_level, column_name, [])
                                        if isinstance(column_list, list):
                                            updated_list = []
                                            for dict_item in column_list:
                                                if isinstance(dict_item, dict):
                                                    # Remove the property if it exists
                                                    if property_name in dict_item:
                                                        del dict_item[property_name]
                                                    
                                                    # Update the sequence based on new global order
                                                    reordered_dict = {prop: new_order[prop] for prop in new_order if prop in dict_item}
                                                    dict_item = reordered_dict

                                                updated_list.append(dict_item)

                                            setattr(supplier_level, column_name, updated_list)

                            supplier_level.save()

                            supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid=company,
                                                                                                     productid=product_instance,
                                                                                                     supplierid = supplier_level.supplierid)

                            # Update the supplier level column matrix after reordering
                            for field in supplier_level._meta.fields:
                                column_name = field.attname
                                if column_name not in ['id', 'companyid_id', 'productid_id', 'supplierid_id']:
                                    column_value = getattr(supplier_level, column_name)
                                    supplier_level_col.Update_Product_Supplier_Level_ColMatrix(
                                        supplier_level=column_value,
                                        column_name=column_name,
                                        productid=supplier_level.productid,
                                        companyid=company
                                    )

                    except (TblproductProductSupplierLevel.DoesNotExist, TblproductProductSupplierLevelColmatrix.DoesNotExist):
                        pass


                    # Update Supplier Matrix
                    try:
                        supplier_matrix = TblproductProductSuppliersMatrix.objects.filter(companyid=company, productid=product_instance)
                        if supplier_matrix.exists():
                            for supplier_matrix_instance in supplier_matrix:
                                supplier_matrix_instance.Update_Product_Supplier_Matrix(company=company, 
                                                                                        productid=product_instance,
                                                                                        supplierid=supplier_matrix_instance.supplierid)
                    except TblproductProductSuppliersMatrix.DoesNotExist:
                        pass




            return E4k_Tblproduct_ProductProperties_Delete(delete_properties='Success')
        except (TblproductProducts.DoesNotExist, TblproductPropertyTypes.DoesNotExist, 
                Tblcompany.DoesNotExist, TblproductProductProperties.DoesNotExist) as e:
            return E4k_Tblproduct_ProductProperties_Delete(delete_properties=f'Failed: {str(e)}')
        except Exception as e:
            return E4k_Tblproduct_ProductProperties_Delete(delete_properties=f"Failed Unable To Delete \n\n Exception \n: {e}")


    @staticmethod
    def _adjust_sequences_after_deletion(company,product_instance, old_seq_no):
        """ Adjust sequence numbers of existing property relations after deletion. """
        TblproductProductProperties.objects.filter(
            companyid=company, 
            productid=product_instance,
            seqno__gt=old_seq_no
        ).update(seqno=F('seqno') - 1)



######################################## Tbl ProductProperties Values Create
class E4k_Tblproduct_ProductProperties_Values_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        product_prop_value = graphene.List(required=True, of_type=graphene.String)

    create_property_values = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, propertyid, product_prop_value):
        try:
            # Get the company, product, and property instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            property_instance = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)
            product_prop_instance = TblproductProductProperties.objects.get(
                companyid=company,
                productid=product_instance,
                propertyid=property_instance
            )

            with transaction.atomic():
                # Fetch existing property values for the given product property
                existing_values = TblproductProductPropertyValues.objects.filter(
                    companyid=company,
                    product_propid=product_prop_instance
                ).values_list('product_prop_value', flat=True)

                # Create new property values if they do not already exist
                product_props_create = [
                    TblproductProductPropertyValues(companyid=company, product_propid=product_prop_instance, 
                                                    product_prop_value=value)
                    for value in product_prop_value if value not in existing_values
                ]

                if product_props_create:
                    TblproductProductPropertyValues.objects.bulk_create(product_props_create)

                
                    
                # Update the property matrix
                try:

                    product_property_level_instance = TblproductProductPropertyLevel.objects.get(
                                                                    companyid=company,
                                                                    productid=product_instance
                                                                )
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance)
                    
                
                    for field in product_property_level_instance._meta.fields:
                        
                        column_name = field.attname

                        if column_name not in ['companyid_id', 'productid_id']:
                            column_value = getattr(product_property_level_instance, column_name)
                            property_level_col.Update_Product_Property_Level_ColMatrix(
                                product_property_level=column_value,
                                column_name=column_name,
                                productid=product_property_level_instance.productid,
                                companyid = company
                            )
                except (TblproductProductPropertyLevel.DoesNotExist, 
                    TblproductProductPropertyLevelColmatrix.DoesNotExist):
                    pass


                ######## Update Supplier level
                
                try:

                    product_supplier_level_instance = TblproductProductSupplierLevel.objects.filter(
                                                                    companyid=company,
                                                                    productid=product_instance
                                                                )
                    for supplier_product in product_supplier_level_instance:
                        property_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                                productid=product_instance,
                                                                                                supplierid = supplier_product.supplierid)
                        
                    
                        for field in supplier_product._meta.fields:
                            
                            column_name = field.attname

                            if column_name not in ['id', 'companyid_id', 'productid_id', 'supplierid_id']:
                                column_value = getattr(supplier_product, column_name)
                                property_level_col.Update_Product_Supplier_Level_ColMatrix(
                                    supplier_level=column_value,
                                    column_name=column_name,
                                    productid=supplier_product.productid,
                                    companyid = company
                                )
                except (TblproductProductSupplierLevel.DoesNotExist, 
                    TblproductProductSupplierLevelColmatrix.DoesNotExist):
                    pass
                
                ###### Supplir matrix Update
                try:
                    pro_sup_mat = TblproductProductSuppliersMatrix.objects.filter(companyid=company,
                                                                          productid=product_instance)
                    if pro_sup_mat.exists():
                        for supp_pro_mat in pro_sup_mat:
                            supp_pro_mat.Update_Product_Supplier_Matrix(company=company, 
                                                                        productid=product_instance,
                                                                        supplierid=supp_pro_mat.supplierid)
                    
                    
                except TblproductProductSuppliersMatrix.DoesNotExist:
                    pass


                try:
                    pro_mat = TblproductProductPropertyMatrix.objects.get(companyid=company,
                                                                          productid=product_instance)
                    
                    pro_mat.update_PropertyMatix(product_instance)
                except TblproductProductPropertyMatrix.DoesNotExist:
                    pass

                try:
                    ########Update the Stoking Level
                    product_stoking_level=  TblproductProductStockinglevelMatrix.objects.get(
                                                        companyid=company,
                                                        productid=product_instance,)
                    product_stoking_level.Update_Product_StockingLevel_Matrix(company=company,
                                                                              productid=product_instance)
                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    pass

                try:
                    ################## Update the sticking type
                    product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_stocking_type.Update_Product_StockingType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    pass

                # update obsolete type 
                try:
                    product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_obsolete_type.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    pass
            
                try:
                    
                    ######################### Update the vatcode
                    product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_vatcode.Update_Product_Vatcode_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    pass

                try:
                    
                    ######################### Update the price standard
                    product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_price_standard.Update_Product_PriceStandard_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    pass
                    
                try:
                    ########################## Update the Cost standard
                    product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_cost_standard.Update_Product_CostStandard_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    pass
                    
                    ########################## Update the Cost Supplier
                try:
                    # Update cost_supplier
                    cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=companyid, 
                                                                                        productid=product_instance)
                    if cost_supplier.exists():
                        if len(cost_supplier) == 1:
                            cost_supplier.first().Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                        else:
                            for cost_supplier_instance in cost_supplier:
                                cost_supplier_instance.Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                except TblproductProductCostSupplierMatrix.DoesNotExist:
                    pass

                try:
                    # Update price_customer
                    price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company,
                                                                                        productid=product_instance)
                    if price_customer.exists():
                        if len(price_customer) == 1:
                            price_customer.first().Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                        else:
                            for price_customer_instance in price_customer:
                                price_customer_instance.Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                    
                
                except TblproductProductPriceCustomerMatrix.DoesNotExist:
                    pass 
                except TblproductProductPropertyMatrix.DoesNotExist:
                    productmatrix_instance = TblproductProductPropertyMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        propertymatix={"value": None},
                        propertycolmatrix = {"value": None}
                    )
                    productmatrix_instance.save()
                    productmatrix_instance.update_PropertyMatix(product_instance)

                

                return E4k_Tblproduct_ProductProperties_Values_Create(create_property_values="Success")
        
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Create(create_property_values='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Create(create_property_values='Failed: Product does not exist')
        except TblproductPropertyTypes.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Create(create_property_values='Failed: Property does not exist')
        except TblproductProductProperties.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Create(create_property_values='Failed: Product Property does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductProperties_Values_Create(create_property_values=f'Failed: {str(e)}')

######################################### Tbl Product Properties Value Update

class E4k_Tblproduct_ProductProperties_Values_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        product_prop_values = graphene.List(required=True, of_type=graphene.String)

    update_property_values = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, propertyid, product_prop_values):
        try:
            # Get the company, product, and property instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            property_instance = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)
            product_prop_instance = TblproductProductProperties.objects.get(
                companyid=company,
                productid=product_instance,
                propertyid=property_instance
            )

            with transaction.atomic():
                # Fetch existing property values for the given product property
                existing_values = TblproductProductPropertyValues.objects.filter(
                    companyid=company,
                    product_propid=product_prop_instance
                )

                # Create a mapping of existing values for quick lookup
                existing_values_dict = {v.product_prop_value: v for v in existing_values}

                update_values = []
                seen_values = set()

                # Track which existing values are matched
                existing_values_matched = set()

                # Iterate over the new property values
                for new_value in product_prop_values:
                    if new_value in existing_values_dict:
                        # Mark the existing value as matched
                        existing_value = existing_values_dict[new_value]
                        existing_values_matched.add(existing_value.product_prop_value_id)
                        # Only update if the value is different
                        if existing_value.product_prop_value != new_value:
                            existing_value.product_prop_value = new_value
                            update_values.append(existing_value)
                    else:
                        # Add new values that do not exist yet
                        if new_value not in seen_values:
                            new_prop_value = TblproductProductPropertyValues(
                                companyid=company,
                                product_propid=product_prop_instance,
                                product_prop_value=new_value
                            )
                            update_values.append(new_prop_value)
                            seen_values.add(new_value)

                # Find values to delete if there are more existing values than new ones
                values_to_delete = TblproductProductPropertyValues.objects.filter(
                    companyid=company,
                    product_propid=product_prop_instance
                ).exclude(product_prop_value_id__in=existing_values_matched)

                values_to_delete.delete()

                # Bulk update the existing values
                if update_values:
                    existing_update_values = [v for v in update_values if v.product_prop_value_id is not None]
                    if existing_update_values:
                        TblproductProductPropertyValues.objects.bulk_update(existing_update_values, ['product_prop_value'])

                    # Bulk create the new values
                    new_create_values = [v for v in update_values if v.product_prop_value_id is None]
                    if new_create_values:
                        TblproductProductPropertyValues.objects.bulk_create(new_create_values)

                # Update the property matrix
                try:

                    product_property_level_instance = TblproductProductPropertyLevel.objects.get(
                                                                    companyid=company,
                                                                    productid=product_instance
                                                                )
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance)
                    
                
                    for field in product_property_level_instance._meta.fields:
                        
                        column_name = field.attname

                        if column_name not in ['companyid_id', 'productid_id']:
                            column_value = getattr(product_property_level_instance, column_name)
                            property_level_col.Update_Product_Property_Level_ColMatrix(
                                product_property_level=column_value,
                                column_name=column_name,
                                productid=product_property_level_instance.productid,
                                companyid = company
                            )
                except (TblproductProductPropertyLevel.DoesNotExist, 
                    TblproductProductPropertyLevelColmatrix.DoesNotExist):
                    pass


                ######## Update Supplier level
                
                try:

                    product_supplier_level_instance = TblproductProductSupplierLevel.objects.filter(
                                                                    companyid=company,
                                                                    productid=product_instance
                                                                )
                    for supplier_product in product_supplier_level_instance:
                        property_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                                productid=product_instance,
                                                                                                supplierid = supplier_product.supplierid)
                        
                    
                        for field in supplier_product._meta.fields:
                            
                            column_name = field.attname

                            if column_name not in ['id', 'companyid_id', 'productid_id', 'supplierid_id']:
                                column_value = getattr(supplier_product, column_name)
                                property_level_col.Update_Product_Supplier_Level_ColMatrix(
                                    supplier_level=column_value,
                                    column_name=column_name,
                                    productid=supplier_product.productid,
                                    companyid = company
                                )
                except (TblproductProductSupplierLevel.DoesNotExist, 
                    TblproductProductSupplierLevelColmatrix.DoesNotExist):
                    pass
                
                ###### Supplir matrix Update
                try:
                    pro_sup_mat = TblproductProductSuppliersMatrix.objects.filter(companyid=company,
                                                                          productid=product_instance)
                    if pro_sup_mat.exists():
                        for supp_pro_mat in pro_sup_mat:
                            supp_pro_mat.Update_Product_Supplier_Matrix(company=company, 
                                                                        productid=product_instance,
                                                                        supplierid=supp_pro_mat.supplierid)
                    
                    
                except TblproductProductSuppliersMatrix.DoesNotExist:
                    pass

                try:
                    pro_mat = TblproductProductPropertyMatrix.objects.get(companyid=company,
                                                                          productid=product_instance)
                    
                    pro_mat.update_PropertyMatix(product_instance)
                except TblproductProductPropertyMatrix.DoesNotExist:
                    pass

                try:
                    ########Update the Stoking Level
                    product_stoking_level=  TblproductProductStockinglevelMatrix.objects.get(
                                                        companyid=company,
                                                        productid=product_instance,)
                    product_stoking_level.Update_Product_StockingLevel_Matrix(company=company,
                                                                              productid=product_instance)
                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    pass

                try:
                    ################## Update the sticking type
                    product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_stocking_type.Update_Product_StockingType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    pass

                # update obsolete type 
                try:
                    product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_obsolete_type.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    pass
            
                try:
                    
                    ######################### Update the vatcode
                    product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_vatcode.Update_Product_Vatcode_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    pass

                try:
                    
                    ######################### Update the price standard
                    product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_price_standard.Update_Product_PriceStandard_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    pass
                    
                try:
                    ########################## Update the Cost standard
                    product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_cost_standard.Update_Product_CostStandard_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    pass
                    
                    ########################## Update the Cost Supplier
                try:
                    # Update cost_supplier
                    cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=companyid, 
                                                                                        productid=product_instance)
                    if cost_supplier.exists():
                        if len(cost_supplier) == 1:
                            cost_supplier.first().Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                        else:
                            for cost_supplier_instance in cost_supplier:
                                cost_supplier_instance.Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                except TblproductProductCostSupplierMatrix.DoesNotExist:
                    pass

                try:
                    # Update price_customer
                    price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company,
                                                                                        productid=product_instance)
                    if price_customer.exists():
                        if len(price_customer) == 1:
                            price_customer.first().Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                        else:
                            for price_customer_instance in price_customer:
                                price_customer_instance.Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                    
                
                except TblproductProductPriceCustomerMatrix.DoesNotExist:
                    pass 
                return E4k_Tblproduct_ProductProperties_Values_Update(update_property_values="Success")
        
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Update(update_property_values='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Update(update_property_values='Failed: Product does not exist')
        except TblproductPropertyTypes.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Update(update_property_values='Failed: Property does not exist')
        except TblproductProductProperties.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Update(update_property_values='Failed: Product Property does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductProperties_Values_Update(update_property_values=f'Failed: {str(e)}')

######################################## Tblproduct Properties value delete

class E4k_Tblproduct_ProductProperties_Values_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        product_prop_value = graphene.String(required=True)

    delete_property_values = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, propertyid,product_prop_value):
        try:
            # Get the company, product, and property instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            property_instance = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)
            product_prop_instance = TblproductProductProperties.objects.get(
                companyid=company,
                productid=product_instance,
                propertyid=property_instance
            )
            with transaction.atomic():
                # Fetch existing property values for the given product property
                existing_values = TblproductProductPropertyValues.objects.get(
                    companyid=company,
                    product_propid=product_prop_instance,
                    product_prop_value=product_prop_value
                )
                existing_values.delete()
                try:

                    pro_mat = TblproductProductPropertyMatrix.objects.get(companyid = company,
                                                                          productid=product_instance)
                    
                    pro_mat.update_PropertyMatix(product_instance)
                except TblproductProductPropertyMatrix.DoesNotExist:
                    pass

                try:

                    ##### update the property level col matrix
                    product_property_level_instance = TblproductProductPropertyLevel.objects.get(
                                                                    companyid=company,
                                                                    productid=product_instance
                                                                )
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance)
                    
                
                    for field in product_property_level_instance._meta.fields:
                        
                        column_name = field.attname

                        if column_name not in ['companyid_id', 'productid_id']:
                            column_value = getattr(product_property_level_instance, column_name)
                            property_level_col.Update_Product_Property_Level_ColMatrix(
                                product_property_level=column_value,
                                column_name=column_name,
                                productid=product_property_level_instance.productid,
                                companyid = company
                            )

                except (TblproductProductPropertyLevel.DoesNotExist,TblproductProductPropertyLevelColmatrix.DoesNotExist):
                    pass

                ######## Update Supplier level
                
                try:

                    product_supplier_level_instance = TblproductProductSupplierLevel.objects.filter(
                                                                    companyid=company,
                                                                    productid=product_instance
                                                                )
                    for supplier_product in product_supplier_level_instance:
                        property_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                                productid=product_instance,
                                                                                                supplierid = supplier_product.supplierid)
                        
                    
                        for field in supplier_product._meta.fields:
                            
                            column_name = field.attname

                            if column_name not in ['id', 'companyid_id', 'productid_id', 'supplierid_id']:
                                column_value = getattr(supplier_product, column_name)
                                property_level_col.Update_Product_Supplier_Level_ColMatrix(
                                    supplier_level=column_value,
                                    column_name=column_name,
                                    productid=supplier_product.productid,
                                    companyid = company
                                )
                except (TblproductProductSupplierLevel.DoesNotExist, 
                    TblproductProductSupplierLevelColmatrix.DoesNotExist):
                    pass
                
                ###### Supplir matrix Update
                try:
                    pro_sup_mat = TblproductProductSuppliersMatrix.objects.filter(companyid=company,
                                                                          productid=product_instance)
                    if pro_sup_mat.exists():
                        for supp_pro_mat in pro_sup_mat:
                            supp_pro_mat.Update_Product_Supplier_Matrix(company=company, 
                                                                        productid=product_instance,
                                                                        supplierid=supp_pro_mat.supplierid)
                    
                    
                except TblproductProductSuppliersMatrix.DoesNotExist:
                    pass
                
                try:
                    ########Update the Stoking Level
                    ########Update the Stoking Level
                    product_stoking_level=  TblproductProductStockinglevelMatrix.objects.get(
                                                        companyid=company,
                                                        productid=product_instance,)
                    product_stoking_level.Update_Product_StockingLevel_Matrix(company=company,
                                                                              productid=product_instance)
                except (TblproductProductStockinglevelMatrix.DoesNotExist):
                    pass

                try:
                    ################## Update the sticking type
                    product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_stocking_type.Update_Product_StockingType_Matrix(company=company,
                                                                                productid=product_instance)
                except (TblproductProductStockingtypeMatrix.DoesNotExist):
                    pass
                
                # update obsolete type 
                try:
                    product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_obsolete_type.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    pass

                try:
                    ######################### Update the vatcode
                    product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_vatcode.Update_Product_Vatcode_Matrix(company=company,
                                                                                productid=product_instance)
                except (TblproductProductVatcodeMatrix.DoesNotExist):
                    pass

                try:
                    ######################### Update the price standard
                    product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_price_standard.Update_Product_PriceStandard_Matrix(company=company,
                                                                                productid=product_instance)
                except (TblproductProductPriceStandardMatrix.DoesNotExist):
                    pass

                try:
                    ########################## Update the Cost standard
                    product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_cost_standard.Update_Product_CostStandard_Matrix(company=company,
                                                                                productid=product_instance)
                    
                except (TblproductProductCostStandardMatrix.DoesNotExist):
                    pass

                try:
                    # Update cost_supplier
                    cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=companyid, 
                                                                                        productid=product_instance)
                    if cost_supplier.exists():
                        if len(cost_supplier) == 1:
                            cost_supplier.first().Update_Product_CostSupplier_Matrix(company=company, 
                                                                                     productid=product_instance)
                        else:
                            for cost_supplier_instance in cost_supplier:
                                cost_supplier_instance.Update_Product_CostSupplier_Matrix(company=company, 
                                                                                          productid=product_instance)
                except (TblproductProductCostSupplierMatrix.DoesNotExist):
                    pass

                try:

                    # Update price_customer
                    price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company,
                                                                                        productid=product_instance)
                    if price_customer.exists():
                        if len(price_customer) == 1:
                            price_customer.first().Update_Product_PriceCustomer_Matrix(company=company, 
                                                                                       productid=product_instance)
                        else:
                            for price_customer_instance in price_customer:
                                price_customer_instance.Update_Product_PriceCustomer_Matrix(company=company, 
                                                                                            productid=product_instance)
                except (TblproductProductPriceCustomerMatrix.DoesNotExist):
                    pass
                return E4k_Tblproduct_ProductProperties_Values_Delete(delete_property_values='Success')
        except TblproductProductPropertyValues.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Delete(delete_property_values='Failed: Product Property Value does not exist')  
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Delete(delete_property_values='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Delete(delete_property_values='Failed: Product does not exist')
        except TblproductPropertyTypes.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Delete(delete_property_values='Failed: Property does not exist')
        except TblproductProductProperties.DoesNotExist:
            return E4k_Tblproduct_ProductProperties_Values_Delete(delete_property_values='Failed: Product Property does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductProperties_Values_Delete(delete_property_values=f"Failed Unable To Delete \n\n Exception \n: {e}")

########################################################## TblproductProductReps Create

class E4k_Tblproduct_ProductReps_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        repid = graphene.Int(required=True)
        seq_no = graphene.Int(required=True)

    create_product_rep = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, repid, seq_no):
        try:
            # Get the company and product instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            rep_instance = TblbusSalesPeople.objects.get(companyid=company, repid=repid)
            with transaction.atomic():
                # Create the product rep instance
                existing_seq_nos = list(
                    TblproductProductReps.objects.filter(companyid=company,
                                                            productid=product_instance).values_list('seqno', flat=True))
                if seq_no in existing_seq_nos:
                        E4k_Tblproduct_ProductReps_Create._adjust_existing_sequences(company,
                                                                                     product_instance,
                                                                                       seq_no)
                    
                product_reps = TblproductProductReps.objects.create(
                                                                companyid=company,
                                                                productid=product_instance,
                                                                repid=rep_instance,
                                                                seqno=seq_no
                                                                )
                product_reps.save()
                
                return E4k_Tblproduct_ProductReps_Create(create_product_rep="Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Create(create_product_rep='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Create(create_product_rep='Failed: Product does not exist')
        except TblbusSalesPeople.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Create(create_product_rep='Failed: Rep does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductReps_Create(create_product_rep=f'Failed: {str(e)}')
        
    @staticmethod
    def _adjust_existing_sequences(company_instance,product_instance, seq_no):
        """ Adjusts the sequence numbers of existing property relations. """
        existing_relations = TblproductProductReps.objects.filter(companyid = company_instance,
                                                                        productid=product_instance, 
                                                                        seqno__gte=seq_no).order_by('seqno')

        for relation in existing_relations:
            relation.seqno = F('seqno') + 1
            relation.save()
        
#################################################### TblproductProductReps Update

class E4k_Tblproduct_ProductReps_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        repid = graphene.Int(required=True)
        new_seq_no = graphene.Int(required=True)

    update_product_rep = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, repid, new_seq_no):
        try:
            # Get the company and product instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            rep_instance = TblbusSalesPeople.objects.get(companyid=company, repid=repid)
            with transaction.atomic():
                # Update the product rep instance
                
                relation_instance = TblproductProductReps.objects.get(
                    companyid=company, 
                    productid=product_instance, 
                    repid=rep_instance, 
                )
                
                # Adjust sequence numbers if the new sequence number is different
                if relation_instance.seqno != new_seq_no:
                    E4k_Tblproduct_ProductReps_Update._adjust_sequences_for_update(
                        company,
                        product_instance, 
                        rep_instance,
                        relation_instance.seqno, 
                        new_seq_no
                    )
                    relation_instance.seqno = new_seq_no
                    relation_instance.save()
                return E4k_Tblproduct_ProductReps_Update(update_product_rep="Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Update(update_product_rep='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Update(update_product_rep='Failed: Product does not exist')
        except TblbusSalesPeople.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Update(update_product_rep='Failed: Rep does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductReps_Update(update_product_rep=f'Failed: {str(e)}')
    
    @staticmethod
    def _adjust_sequences_for_update(company,product_instance,rep_instance, old_seq_no, new_seq_no):
        """ Adjust sequence numbers of existing property relations for update. """
        if new_seq_no > old_seq_no:
            TblproductProductReps.objects.filter(
                companyid = company,
                productid=product_instance,
                
                seqno__gt=old_seq_no,
                seqno__lte=new_seq_no
            ).update(seqno=F('seqno') - 1)
        elif new_seq_no < old_seq_no:
            TblproductProductReps.objects.filter(
                companyid = company,
                productid=product_instance,
                
                seqno__gte=new_seq_no,
                seqno__lt=old_seq_no
            ).update(seqno=F('seqno') + 1)
        
################################################## TblproductProductReps Delete

class E4k_Tblproduct_ProductReps_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        id = graphene.Int(required=True)

    delete_product_rep = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, id):
        try:
            # Get the company and product instances
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            with transaction.atomic():
                # Delete the product rep instance

                relation_instance = TblproductProductReps.objects.get(
                    companyid=company, 
                    productid=product_instance,
                    id=id
                )
                old_seq_no = relation_instance.seqno

                relation_instance.delete()

                # Adjust sequence numbers of the remaining properties
                E4k_Tblproduct_ProductReps_Delete._adjust_sequences_after_deletion(company, product_instance, old_seq_no)

                return E4k_Tblproduct_ProductReps_Delete(delete_product_rep="Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Delete(delete_product_rep='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductReps_Delete(delete_product_rep='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductReps_Delete(delete_product_rep=f"Failed Unable To Delete \n\n Exception \n: {e}")
        
    @staticmethod
    def _adjust_sequences_after_deletion(company,product_instance, old_seq_no):
        """ Adjust sequence numbers of existing property relations after deletion. """
        TblproductProductReps.objects.filter(
            companyid=company, 
            productid=product_instance,
            seqno__gt=old_seq_no
        ).update(seqno=F('seqno') - 1)


######################################################## E4K_TblproductProductPropertyLevel Create


class E4k_Tblproduct_ProductPropertyLevel_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stockmatrix = graphene.JSONString(required=True)
        pricematrix = graphene.JSONString(required=True)
        stklvlmatrix = graphene.JSONString(required=True)
        stklocmatrix = graphene.JSONString(required=True)
        stktypematrix = graphene.JSONString(required=True)
        obslmatrix = graphene.JSONString(required=True)
    create_product_property_level = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, stockmatrix, 
               pricematrix, stklvlmatrix, stklocmatrix, stktypematrix,obslmatrix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            with transaction.atomic():

                product_property_level_instance = TblproductProductPropertyLevel.objects.create(
                    companyid=company,
                    productid=product_instance,
                    stockmatrix= [stockmatrix],
                    pricematrix=[pricematrix],
                    stklvlmatrix=[stklvlmatrix],
                    stklocmatrix=[stklocmatrix],
                    stktypematrix=[stktypematrix],
                    obslmatrix=[obslmatrix]
                )
                
                product_property_level_instance.save()
                
                # Update the property level col matrix instance
                try:
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance)
                    property_level = TblproductProductPropertyLevel.objects.get(companyid=company,productid=product_instance)

                    return E4k_Tblproduct_ProductPropertyLevel_Create(create_product_property_level="Failed to Create already Exists")
                except TblproductProductPropertyLevelColmatrix.DoesNotExist:
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        stockcolmatrix={"value": None},
                        pricecolmatrix={"value": None},
                        stklvlcolmatrix={"value": None},
                        stkloccolmatrix={"value": None},
                        stktypecolmatrix={"value": None},
                        obslcolmatrix={"value": None},
                    )
                    property_level_col.save()
                except TblproductProductPropertyLevel.DoesNotExist:
                    property_level = TblproductProductPropertyLevel.objects.create(
                        companyid=company,
                        productid=product_instance,
                        stockmatrix={"value": None},
                        pricematrix={"value": None},
                        stklvlmatrix={"value": None},
                        stklocmatrix={"value": None},
                        stktypematrix={"value": None},
                        obslmatrix={"value": None},
                    )
                    property_level.save()
                
                for field in product_property_level_instance._meta.fields:
                    
                    column_name = field.attname

                    if column_name not in ['companyid_id', 'productid_id']:
                        column_value = getattr(product_property_level_instance, column_name)
                        property_level_col.Update_Product_Property_Level_ColMatrix(
                            product_property_level=column_value,
                            column_name=column_name,
                            productid=product_property_level_instance.productid,
                            companyid = company
                        )
                
                try:
                
                    product_stoking_level=  TblproductProductStockinglevelMatrix.objects.get(
                                                            companyid=company,
                                                            productid=product_instance,)
                    product_stoking_level.Update_Product_StockingLevel_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    product_stock_matrix = TblproductProductStockinglevelMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        stocklevelmatix=[{"value": 0}],
                        
                    )
                    product_stock_matrix.save()
                    product_stock_matrix.Update_Product_StockingLevel_Matrix(company=company,
                                                                              productid=product_instance)
                try:
                    
                    product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_stocking_type.Update_Product_StockingType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    product_stock_type_matrix = TblproductProductStockingtypeMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        stocktypematix=[{"value": 0}],
                        
                    )
                    product_stock_type_matrix.save()
                    product_stock_type_matrix.Update_Product_StockingType_Matrix(company=company,
                                                                                productid=product_instance)
                
                ######### Obsolete type
                try:
                    
                    product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_obsolete_type.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                productid=product_instance)
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    product_obsolete_type_matrix = TblproductProductObsoleteMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        obslmatix=[{"value": 0}],
                        
                    )
                    product_obsolete_type_matrix.save()
                    product_obsolete_type_matrix.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                productid=product_instance)

                try:
                    
                    cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company,
                                                                                    productid=product_instance)
                    cost_standard.Update_Product_CostStandard_Matrix(company=company,
                                                                                    productid=product_instance)
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    product_cost_standard_matrix = TblproductProductCostStandardMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        stdcostmatix=[{"value": 0}],
                        
                    )
                    product_cost_standard_matrix.save()
                    product_cost_standard_matrix.Update_Product_CostStandard_Matrix(company=company,
                                                                                    productid=product_instance)
                try:
                    
                    price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company,
                                                                                        productid=product_instance)
                    price_standard.Update_Product_PriceStandard_Matrix(company=company,
                                                                                        productid=product_instance)
                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    product_price_standard_matrix = TblproductProductPriceStandardMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        stdpricematix=[{"value": 0}],
                        
                    )
                    product_price_standard_matrix.save()
                    product_price_standard_matrix.Update_Product_PriceStandard_Matrix(company=company,
                                                                                      productid=product_instance)
                try:
                    
                    vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company,
                                                                            productid=product_instance)
                    vatcode.Update_Product_Vatcode_Matrix(company=company,
                                                            productid=product_instance)
                
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    product_vat_code_matrix = TblproductProductVatcodeMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        vatcodematix=[{"value": 0}],
                        
                    )
                    product_vat_code_matrix.save()
                    product_vat_code_matrix.Update_Product_Vatcode_Matrix(company=company,
                                                                            productid=product_instance)
                

                return E4k_Tblproduct_ProductPropertyLevel_Create(create_product_property_level="Success")
            
        

        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Create(create_product_property_level='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Create(create_product_property_level='Failed: Product does not exist')
        except IntegrityError as e:
            print(f"IntegrityError: {str(e)}")
            return E4k_Tblproduct_ProductPropertyLevel_Create(create_product_property_level=f'Failedsave: {str(e)}')
        except Exception as e:
            print(f"Exception: {str(e)}")
            return E4k_Tblproduct_ProductPropertyLevel_Create(create_product_property_level=f'Failedsave: {str(e)}')
        
############################################## TblproductProductPropertyLevel Update


class E4k_Tblproduct_ProductPropertyLevel_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stockmatrix = graphene.JSONString(required=True)
        pricematrix = graphene.JSONString(required=True)
        stklvlmatrix = graphene.JSONString(required=True)
        stklocmatrix = graphene.JSONString(required=True)
        stktypematrix = graphene.JSONString(required=True)
        obslmatrix = graphene.JSONString(required=True)
    
    update_product_property_level = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, stockmatrix, 
               pricematrix, stklvlmatrix, stklocmatrix, stktypematrix,obslmatrix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            with transaction.atomic():
                product_property_level_instance = TblproductProductPropertyLevel.objects.get(
                    companyid=company,
                    productid=product_instance
                )
                product_property_level_instance.stockmatrix=[stockmatrix]
                product_property_level_instance.pricematrix=[pricematrix]
                product_property_level_instance.stklvlmatrix=[stklvlmatrix]
                product_property_level_instance.stklocmatrix=[stklocmatrix]
                product_property_level_instance.stktypematrix = [stktypematrix]
                product_property_level_instance.obslmatrix = [obslmatrix]
                product_property_level_instance.save()
                product_property_level_instance = TblproductProductPropertyLevel.objects.get(
                    companyid=company,
                    productid=product_instance
                )
                property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance)
                    
                
                for field in product_property_level_instance._meta.fields:
                    
                    column_name = field.attname

                    if column_name not in ['companyid_id', 'productid_id']:
                        column_value = getattr(product_property_level_instance, column_name)
                        property_level_col.Update_Product_Property_Level_ColMatrix(
                            product_property_level=column_value,
                            column_name=column_name,
                            productid=product_property_level_instance.productid,
                            companyid = company
                        )
                ########Update the Stoking Level
                product_stoking_level=  TblproductProductStockinglevelMatrix.objects.get(
                                                    companyid=company,
                                                    productid=product_instance,)
                product_stoking_level.Update_Product_StockingLevel_Matrix(company=company,
                                                                            productid=product_instance,
                                                                            warehouseid=None,old_data=[])
                ################## Update the sticking type
                product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company,
                                                                            productid=product_instance)
                product_stocking_type.Update_Product_StockingType_Matrix(company=company,
                                                                            productid=product_instance)

                ################## Update the Obsoleten type
                product_obsolete_type = TblproductProductObsoleteMatrix.objects.get(companyid=company,
                                                                            productid=product_instance)
                product_obsolete_type.Update_Product_ObsoleteType_Matrix(company=company,
                                                                            productid=product_instance)
                



                ######################### Update the vatcode
                product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company,
                                                                            productid=product_instance)
                product_vatcode.Update_Product_Vatcode_Matrix(company=company,
                                                                            productid=product_instance)
                
                ######################### Update the price standard
                product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company,
                                                                            productid=product_instance)
                product_price_standard.Update_Product_PriceStandard_Matrix(company=company,
                                                                            productid=product_instance)
                
                ########################## Update the Cost standard
                product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company,
                                                                            productid=product_instance)
                product_cost_standard.Update_Product_CostStandard_Matrix(company=company,
                                                                            productid=product_instance)
                
                ########################## Update the Cost Supplier

                # Update cost_supplier
                cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=companyid, 
                                                                                    productid=product_instance)
                if cost_supplier.exists():
                    if len(cost_supplier) == 1:
                        cost_supplier.first().Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)
                    else:
                        for cost_supplier_instance in cost_supplier:
                            cost_supplier_instance.Update_Product_CostSupplier_Matrix(company=company, productid=product_instance)

                # Update price_customer
                price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company,
                                                                                    productid=product_instance)
                if price_customer.exists():
                    if len(price_customer) == 1:
                        price_customer.first().Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                    else:
                        for price_customer_instance in price_customer:
                            price_customer_instance.Update_Product_PriceCustomer_Matrix(company=company, productid=product_instance)
                    
                                                                            

                return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "Success")
            
        except TblproductProductCostSupplierMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductCostSupplierMatrix not found")
        except TblproductProductPriceCustomerMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductPriceCustomerMatrix not found")
            
        except TblproductProductStockinglevelMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductStockinglevelMatrix not found")
        except TblproductProductStockingtypeMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductStockingtypeMatrix not found")
        except TblproductProductVatcodeMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductVatcodeMatrix not found")
        except TblproductProductPriceStandardMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductPriceStandardMatrix not found")
        except TblproductProductCostStandardMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductCostStandardMatrix not found")
        

        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level='Failed: Product does not exist')
        except Exception as e:
            print(f"Exception: {str(e)}")
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level=f'Failedsave: {str(e)}')
        except TblproductProductPropertyLevelColmatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Update(update_product_property_level = "TblproductProductPropertyLevelColmatrix not found")
                

################################################# Tbl product property level Delete

class E4k_Tblproduct_ProductPropertyLevel_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    delete_product_property_level = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            with transaction.atomic():
                product_property_level_col_instance = TblproductProductPropertyLevelColmatrix.objects.get(
                    companyid=company,
                    productid=product_instance
                )
                product_property_level_col_instance.delete()
                product_property_level_instance = TblproductProductPropertyLevel.objects.get(
                    companyid=company,
                    productid=product_instance
                )
                product_property_level_instance.delete()


                ########Delete the Stoking Level
                try:
                    product_stoking_level=  TblproductProductStockinglevelMatrix.objects.get(
                                                        companyid=company,
                                                        productid=product_instance,)
                    product_stoking_level.delete()
                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    pass

                try:
                ################## Delete the sticking type
                    product_stocking_type = TblproductProductStockingtypeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_stocking_type.delete()
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    pass

                try:
                
                    ######################### Delete the vatcode
                    product_vatcode = TblproductProductVatcodeMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_vatcode.delete()
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    pass

                try:
                
                ######################### Delete the price standard
                    product_price_standard = TblproductProductPriceStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_price_standard.delete()

                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    pass

                try:
                
                    ########################## Delete the Cost standard
                    product_cost_standard = TblproductProductCostStandardMatrix.objects.get(companyid=company,
                                                                                productid=product_instance)
                    product_cost_standard.delete()
                
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    pass

                try:
                
                    ########################## Delete the Cost Supplier

                    # Delete cost_supplier
                    cost_supplier = TblproductProductCostSupplierMatrix.objects.filter(companyid=companyid, 
                                                                                        productid=product_instance)
                    if cost_supplier.exists():
                        if len(cost_supplier) == 1:
                            cost_supplier.first().delete()
                        else:
                            for cost_supplier_instance in cost_supplier:
                                cost_supplier_instance.delete()

                except TblproductProductCostSupplierMatrix.DoesNotExist:
                    pass

                try:

                    # Delete price_customer
                    price_customer = TblproductProductPriceCustomerMatrix.objects.filter(companyid=company,
                                                                                        productid=product_instance)
                    if price_customer.exists():
                        if len(price_customer) == 1:
                            price_customer.first().delete()
                        else:
                            for price_customer_instance in price_customer:
                                price_customer_instance.delete()
                
                except TblproductProductPriceCustomerMatrix.DoesNotExist:
                    pass

                return E4k_Tblproduct_ProductPropertyLevel_Delete(delete_product_property_level = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Delete(delete_product_property_level='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Delete(delete_product_property_level='Failed: Product does not exist')
        except TblproductProductPropertyLevelColmatrix.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyLevel_Delete(delete_product_property_level = "TblproductProductPropertyLevelColmatrix not found")
        except Exception as e:
            print(f"Exception: {str(e)}")
            return E4k_Tblproduct_ProductPropertyLevel_Delete(delete_product_property_level=f"Failed Unable To Delete \n\n Exception \n: {e}")

########################################### E4K_TblproductProductSuppliers Create

class E4k_Tblproduct_ProductSuppliers_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        warehouseid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        supplierprod_code = graphene.String(required=True)
        supplier_price = graphene.Int(required=True)
        supplierseq = graphene.Int(required=True)
        sizeid = graphene.String(required=True)
        leadtime = graphene.Int(required=True)
        isbulkorder = graphene.Int(required=True)
        dutycost = graphene.Float()

    create_product_suppliers = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, warehouseid, supplierid, supplierprod_code, 
               supplier_price, supplierseq, sizeid, leadtime, isbulkorder, dutycost):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            supplier = Tblsupplier.objects.get(companyid=company,businessid = supplierid)
            warehouse = TblwhoWarehouses.objects.get(companyid = company,warehouseid=warehouseid)
            product_supplier = TblproductProductSuppliers.objects.create(companyid=company,
                                                                        warehouseid=warehouse,
                                                                        productid=product,
                                                                        supplierid=supplier,
                                                                        supplierprod_code=supplierprod_code,
                                                                        supplier_price=supplier_price,
                                                                        supplierseq=supplierseq,
                                                                        sizeid=sizeid,
                                                                        leadtime=leadtime,
                                                                        isbulkorder=isbulkorder if isbulkorder else 0,
                                                                        dutycost=dutycost if dutycost else 0,
                                                                        )
            product_supplier.save()
            return E4k_Tblproduct_ProductSuppliers_Create(create_product_suppliers = "Success")

        except Exception as e:
            print(f"Exception: {str(e)}")
            return E4k_Tblproduct_ProductSuppliers_Create(create_product_suppliers=f'Failedsave: {str(e)}')
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliers_Create(create_product_suppliers='Failed: Company does not exist')
        except TblwhoWarehouses.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliers_Create(create_product_suppliers='Failed: Warehouse does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliers_Create(create_product_suppliers='Failed: Product does not exist') 
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliers_Create(create_product_suppliers='Failed: Supplier does not exist')

################################################# E4K_TblproductProductStockinglevelMatrix Mutation


class E4k_Tblproduct_ProductStockinglevelMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        warehouseid = graphene.String()
    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid,warehouseid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_stockinglevel_matrix_instance = TblproductProductStockinglevelMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    if (product_stockinglevel_matrix_instance) :
                        product_stock_level_data = product_stockinglevel_matrix_instance.stocklevelmatix
                        product_stockinglevel_matrix_instance.Update_Product_StockingLevel_Matrix(company=company,
                                                                                            productid=product,
                                                                                            warehouseid = warehouseid,
                                                                                            old_data = product_stock_level_data)
                        return E4k_Tblproduct_ProductStockinglevelMatrix_Create(success = "Success")
                    else:
                        return E4k_Tblproduct_ProductStockinglevelMatrix_Create(success = "Failed to create product Stocking level")

                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    product_stockinglevel_matrix_instance = TblproductProductStockinglevelMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        stocklevelmatix = [{"value":0}]
                    )
                    product_stockinglevel_matrix_instance.save()

                    product_stockinglevel_matrix_instance = TblproductProductStockinglevelMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                
                    product_stockinglevel_matrix_instance.Update_Product_StockingLevel_Matrix(company=company,
                                                                                            productid=product
                                                                                            )
                return E4k_Tblproduct_ProductStockinglevelMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductStockinglevelMatrix_Create(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductStockinglevelMatrix_Create(success='Failed: Product does not exist')


########################################### tbl Product Stocking Level Matrix Update

class E4k_Tblproduct_ProductStockinglevelMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stocklevelmatix = graphene.List(required = True,of_type=graphene.JSONString)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, stocklevelmatix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_stockinglevel_matrix_instance = TblproductProductStockinglevelMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    exclude_keys = ["maxqty", "minqty",'reorderqty']
                    stocklevel_data = product_stockinglevel_matrix_instance.stocklevelmatix
                    stock_levl_matix_update =[]
                    for j in range(len(stocklevelmatix)):  
                        update_data_dict_keys = {key: value for key, value in stocklevelmatix[j].items() if key not in exclude_keys}
                        for i in range(len(stocklevel_data)):
                            filtered_dict = {key: value for key, value in stocklevel_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                stocklevel_data[i]['maxqty']=float(stocklevelmatix[j]['maxqty'])
                                stocklevel_data[i]['minqty']=float(stocklevelmatix[j]['minqty'])
                                stocklevel_data[i]['reorderqty']=float(stocklevelmatix[j]['reorderqty'])
                                stocklevel_data[i]['WarehouseID']=str(stocklevelmatix[j]['WarehouseID'])
                                stock_levl_matix_update.append(stocklevel_data[i])
                    product_stockinglevel_matrix_instance.stocklevelmatix = stock_levl_matix_update
                    product_stockinglevel_matrix_instance.save()
                    return E4k_Tblproduct_ProductStockinglevelMatrix_Update(success = "Success")

                except TblproductProductStockinglevelMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductStockinglevelMatrix_Update(success = "Stocking level Not found")
                
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductStockinglevelMatrix_Update(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductStockinglevelMatrix_Update(success='Failed: Product does not exist')


#################################################E4K_TblproductProductStockingtypeMatrix Create

class E4k_Tblproduct_ProductStockingtypeMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_stockingtype_matrix_instance = TblproductProductStockingtypeMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    return E4k_Tblproduct_ProductStockingtypeMatrix_Create(success = "Failed to create product Stocking type")
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    product_stockingtype_matrix_instance = TblproductProductStockingtypeMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        stocktypematix = [{"value":0}]
                    )
                    product_stockingtype_matrix_instance.save()
                    product_stockingtype_matrix_instance = TblproductProductStockingtypeMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    product_stockingtype_matrix_instance.Update_Product_StockingType_Matrix(company=company,
                                                                                            productid=product
                                                                                            )
                    return E4k_Tblproduct_ProductStockingtypeMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductStockingtypeMatrix_Create(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductStockingtypeMatrix_Create(success='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductStockingtypeMatrix_Create(success='Failed: '+str(e))
        

#################################################### 

############################################## E4K_TblproductProductStockingtypeMatrix update

class E4k_Tblproduct_ProductStockingtypeMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stocktypematix = graphene.List(required = True,of_type=graphene.JSONString)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, stocktypematix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_stockingtype_matrix_instance = TblproductProductStockingtypeMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    exclude_keys = ["stocktype"]
                    stocktype_data = product_stockingtype_matrix_instance.stocktypematix
                    stocking_type_matix_update =[]
                    for j in range(len(stocktypematix)):
                        update_data_dict_keys = {key: value for key, value in stocktypematix[j].items() if key not in exclude_keys}
                        for i in range(len(stocktype_data)):
                            filtered_dict = {key: value for key, value in stocktype_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                stocktype_data[i]['stocktype']=str(stocktypematix[j]['stocktype'])
                                stocking_type_matix_update.append(stocktype_data[i])
                    product_stockingtype_matrix_instance.stocktypematix = stocking_type_matix_update
                    product_stockingtype_matrix_instance.save()
                    return E4k_Tblproduct_ProductStockingtypeMatrix_Update(success = "Success")
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductStockingtypeMatrix_Update(success = "Product Stocking type Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductStockingtypeMatrix_Update(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductStockingtypeMatrix_Update(success='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductStockingtypeMatrix_Update(success='Failed: '+str(e))
                

#################################################E4K_TblproductProductObsoleteMatrix Create

class E4k_Tblproduct_ProductObsoletetypeMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    return E4k_Tblproduct_ProductObsoletetypeMatrix_Create(success = "Failed to create product Obsolete Type")
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        obslmatix = [{"value":0}]
                    )
                    product_obsoletetype_matrix_instance.save()
                    product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    product_obsoletetype_matrix_instance.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                            productid=product
                                                                                            )
                    return E4k_Tblproduct_ProductObsoletetypeMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductObsoletetypeMatrix_Create(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductObsoletetypeMatrix_Create(success='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductObsoletetypeMatrix_Create(success='Failed: '+str(e))

############################################## E4K_TblproductProductObsoletetypeMatrix update

class E4k_Tblproduct_ProductObsoletetypeMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        obslmatix = graphene.List(required = True,of_type=graphene.JSONString)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, obslmatix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    exclude_keys = ["obsoleteID"]
                    obsoletetype_data = product_obsoletetype_matrix_instance.obslmatix
                    obsolete_type_matix_update =[]
                    for j in range(len(obslmatix)):
                        update_data_dict_keys = {key: value for key, value in obslmatix[j].items() if key not in exclude_keys}
                        for i in range(len(obsoletetype_data)):
                            filtered_dict = {key: value for key, value in obsoletetype_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                obsoletetype_data[i]['obsoleteID']=int(obslmatix[j]['obsoleteID'])
                                obsolete_type_matix_update.append(obsoletetype_data[i])
                    product_obsoletetype_matrix_instance.obslmatix = obsolete_type_matix_update
                    product_obsoletetype_matrix_instance.save()
                    return E4k_Tblproduct_ProductObsoletetypeMatrix_Update(success = "Success")
                except TblproductProductObsoleteMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductObsoletetypeMatrix_Update(success = "Product Obsolete type Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductObsoletetypeMatrix_Update(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductObsoletetypeMatrix_Update(success='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductObsoletetypeMatrix_Update(success='Failed: '+str(e))


####################################################### E4K_TblproductProductCostStandardMatrix Create

class E4k_Tblproduct_ProductCostStandardMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_cost_standard_matrix_instance = TblproductProductCostStandardMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    return E4k_Tblproduct_ProductCostStandardMatrix_Create(success = "Failed to create product Cost Standard")
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    product_cost_standard_matrix_instance = TblproductProductCostStandardMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        stdcostmatix = [{"value":0}]
                    )
                    product_cost_standard_matrix_instance.save()
                    product_cost_standard_matrix_instance = TblproductProductCostStandardMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    product_cost_standard_matrix_instance.Update_Product_CostStandard_Matrix(company=company,
                                                                                             productid=product)
                    return E4k_Tblproduct_ProductCostStandardMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductCostStandardMatrix_Create(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductCostStandardMatrix_Create(success='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductCostStandardMatrix_Create(success='Failed: '+str(e))
        
######################################### E4k_Tblproduct_ProductCostStandardMatrix Update

class E4k_Tblproduct_ProductCostStandardMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stdcostmatix = graphene.List(required = True,of_type=graphene.JSONString)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, stdcostmatix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_cost_standard_matrix_instance = TblproductProductCostStandardMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    exclude_keys = ["price"]
                    stdcost_data = product_cost_standard_matrix_instance.stdcostmatix
                    standard_cost_matix_update =[]
                    for j in range(len(stdcostmatix)):  
                        update_data_dict_keys = {key: value for key, value in stdcostmatix[j].items() if key not in exclude_keys}
                        for i in range(len(stdcost_data)):
                            filtered_dict = {key: value for key, value in stdcost_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                stdcost_data[i]['price']=float(stdcostmatix[j]['price'])
                                stdcost_data[i]['pricetype']=int(stdcostmatix[j]['pricetype'])
                                standard_cost_matix_update.append(stdcost_data[i])
                    product_cost_standard_matrix_instance.stdcostmatix = standard_cost_matix_update
                    product_cost_standard_matrix_instance.save()
                    return E4k_Tblproduct_ProductCostStandardMatrix_Update(success = "Success")
                except TblproductProductCostStandardMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductCostStandardMatrix_Update(success = "Product Cost Standard Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductCostStandardMatrix_Update(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductCostStandardMatrix_Update(success='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductCostStandardMatrix_Update(success='Failed: '+str(e))
        
############################################################# E4K_TblproductProductCostSupplierMatrix create

class E4k_Tblproduct_ProductCostSupplierMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        supplierid = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid,supplierid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            supplier = Tblsupplier.objects.get(companyid = company,businessid=supplierid)
            with transaction.atomic():
                try:
                    product_cost_supplier_matrix_instance = TblproductProductCostSupplierMatrix.objects.get(
                        companyid=company,
                        productid=product,
                        businessid = supplier
                    )
                    return E4k_Tblproduct_ProductCostSupplierMatrix_Create(success = "Failed to create product Cost Supplier")
                except TblproductProductCostSupplierMatrix.DoesNotExist:
                    product_cost_supplier_matrix_instance = TblproductProductCostSupplierMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        businessid = supplier,
                        supcostmatix = [{"value":0}]
                    )
                    product_cost_supplier_matrix_instance.save()
                    product_cost_supplier_matrix_instance = TblproductProductCostSupplierMatrix.objects.get(
                        companyid=company,
                        productid=product,
                        businessid=supplier
                    )
                    product_cost_supplier_matrix_instance.Update_Product_CostSupplier_Matrix(company=company,
                                                                                             productid=product)
                    return E4k_Tblproduct_ProductCostSupplierMatrix_Create(success = "Success")
                except Exception as e:
                    return E4k_Tblproduct_ProductCostSupplierMatrix_Create(success='Failed: '+str(e))
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Create(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Create(success='Failed: Product ID does not exist')
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Create(success='Failed: Supplier ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Create(success='Failed: '+str(e))


################################################## E4K_TblproductProductCostSupplierMatrix Update

class E4k_Tblproduct_ProductCostSupplierMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        supcostmatix = graphene.List(required = True,of_type=graphene.JSONString)

    
    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, supplierid, supcostmatix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            supplier = Tblsupplier.objects.get(companyid = company,businessid=supplierid)
            with transaction.atomic():
                try:
                    product_cost_supplier_matrix_instance = TblproductProductCostSupplierMatrix.objects.get(
                        companyid=company,
                        productid=product,
                        businessid = supplier
                    )
                    exclude_keys = ["price"]
                    supcost_data = product_cost_supplier_matrix_instance.supcostmatix
                    supplier_cost_matix_update = []
                    for j in range(len(supcostmatix)):
                        update_data_dict_keys = {key: value for key, value in supcostmatix[j].items() if key not in exclude_keys}
                        for i in range(len(supcost_data)):
                            filtered_dict = {key: value for key, value in supcost_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                supcost_data[i]['price']=float(supcostmatix[j]['price'])
                                supcost_data[i]['pricetype']=int(supcostmatix[j]['pricetype'])
                                supplier_cost_matix_update.append(supcost_data[i])
                    product_cost_supplier_matrix_instance.supcostmatix = supplier_cost_matix_update
                    product_cost_supplier_matrix_instance.save()
                    return E4k_Tblproduct_ProductCostSupplierMatrix_Update(success = "Success")
                except TblproductProductCostSupplierMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductCostSupplierMatrix_Update(success = "Product Cost Supplier Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Update(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Update(success='Failed: Product does not exist')
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Update(success='Failed: Supplier does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductCostSupplierMatrix_Update(success='Failed: '+str(e))

############################################################### TblproductProductPriceCustomerMatrix Create

class E4k_Tblproduct_ProductPriceCustomerMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        customerid = graphene.String(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, customerid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            customer = Tblcustomer.objects.get(companyid = company,businessid=customerid)
            with transaction.atomic():
                try:
                    product_price_customer_matrix_instance = TblproductProductPriceCustomerMatrix.objects.get(
                        companyid=company,
                        productid=product,
                        businessid = customer
                    )
                    return E4k_Tblproduct_ProductPriceCustomerMatrix_Create(success = "Failed to create product Price Customer")
                except TblproductProductPriceCustomerMatrix.DoesNotExist:
                    product_price_customer_matrix_instance = TblproductProductPriceCustomerMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        businessid = customer,
                        cuspricematix = [{"value":0}]
                    )
                    product_price_customer_matrix_instance.save()
                    product_price_customer_matrix_instance = TblproductProductPriceCustomerMatrix.objects.get(
                        companyid=company,
                        productid=product,
                        businessid=customer
                    )
                    product_price_customer_matrix_instance.Update_Product_PriceCustomer_Matrix(company=company,
                                                                                             productid=product)
                    return E4k_Tblproduct_ProductPriceCustomerMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Create(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Create(success='Failed: Product ID does not exist')
        except Tblcustomer.DoesNotExist:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Create(success='Failed: Customer ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Create(success='Failed: '+str(e))
        
######################################################## Tblproduct_ProductPriceCustomerMatrix Update

class E4k_Tblproduct_ProductPriceCustomerMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        customerid = graphene.String(required=True)
        cuspricematix = graphene.List(required = True,of_type=graphene.JSONString)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, customerid, cuspricematix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            customer = Tblcustomer.objects.get(companyid = company,businessid=customerid)
            with transaction.atomic():
                try:
                    product_price_customer_matrix_instance = TblproductProductPriceCustomerMatrix.objects.get(
                        companyid=company,
                        productid=product,
                        businessid = customer
                    )
                    exclude_keys = ["price"]
                    cuspric_data = product_price_customer_matrix_instance.cuspricematix
                    customer_price_matix_update =[]
                    for j in range(len(cuspricematix)):
                        update_data_dict_keys = {key: value for key, value in cuspricematix[j].items() if key not in exclude_keys}
                        for i in range(len(cuspric_data)):
                            filtered_dict = {key: value for key, value in cuspric_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                cuspric_data[i]['price']=float(cuspricematix[j]['price'])
                                cuspric_data[i]['pricetype']=int(cuspricematix[j]['pricetype'])
                                customer_price_matix_update.append(cuspric_data[i])
                    product_price_customer_matrix_instance.cuspricematix = customer_price_matix_update
                    product_price_customer_matrix_instance.save()
                    return E4k_Tblproduct_ProductPriceCustomerMatrix_Update(success = "Success")
                except TblproductProductPriceCustomerMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductPriceCustomerMatrix_Update(success = "Product Price Customer Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Update(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Update(success='Failed: Product does not exist')
        except Tblcustomer.DoesNotExist:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Update(success='Failed: Customer does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceCustomerMatrix_Update(success='Failed: '+str(e))

##################################################### E4K_TblproductProductPriceStandardMatrix Create

class E4k_Tblproduct_ProductPriceStandardMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_price_standard_matrix_instance = TblproductProductPriceStandardMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    return E4k_Tblproduct_ProductPriceStandardMatrix_Create(success = "Failed to create product Price Standard")
                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    product_price_standard_matrix_instance = TblproductProductPriceStandardMatrix.objects.create(
                        companyid=company,
                        productid=product
                    )
                    product_price_standard_matrix_instance.save()
                    product_price_standard_matrix_instance.Update_Product_PriceStandard_Matrix(company=company,
                                                                                               productid=product)
                    return E4k_Tblproduct_ProductPriceStandardMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardMatrix_Create(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardMatrix_Create(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandardMatrix_Create(success='Failed: '+str(e))

############################################################ E4K_TblproductProductPriceStandardMatrix Update

class E4k_Tblproduct_ProductPriceStandardMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stdpricematix = graphene.List(required = True,of_type=graphene.JSONString)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, stdpricematix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_price_standard_matrix_instance = TblproductProductPriceStandardMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    exclude_keys = ["price"]
                    stdpric_data = product_price_standard_matrix_instance.stdpricematix
                    standard_price_matix_update = []
                    for j in range(len(stdpricematix)):
                        update_data_dict_keys = {key: value for key, value in stdpricematix[j].items() if key not in exclude_keys}
                        for i in range(len(stdpric_data)):
                            filtered_dict = {key: value for key, value in stdpric_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                stdpric_data[i]['price']=float(stdpricematix[j]['price'])
                                stdpric_data[i]['pricetype']=int(stdpricematix[j]['pricetype'])
                                product_price_standard_matrix_instance.stdpricematix = stdpric_data
                                standard_price_matix_update.append(stdpric_data[i])
                    product_price_standard_matrix_instance.stdpricematix = standard_price_matix_update
                    product_price_standard_matrix_instance.save()
                    return E4k_Tblproduct_ProductPriceStandardMatrix_Update(success = "Success")
                except TblproductProductPriceStandardMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductPriceStandardMatrix_Update(success = "Product Price Standard ID Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardMatrix_Update(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardMatrix_Update(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandardMatrix_Update(success='Failed: '+str(e))


######################################################################################### E4k_tblProductProductStandardDateMatrix
class E4k_Tblproduct_ProductPriceStandardDateMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_price_standard_date_matrix_instance = TblproductProductPriceStandardDateMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    return E4k_Tblproduct_ProductPriceStandardDateMatrix_Create(success = "Failed to create product Price Standard")
                except TblproductProductPriceStandardDateMatrix.DoesNotExist:
                    product_price_standard_date_matrix_instance = TblproductProductPriceStandardDateMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        stdpricematix = []
                    )
                    product_price_standard_date_matrix_instance.save()
                    # product_price_standard_date_matrix_instance.Update_Product_PriceStandard_Matrix(company=company,
                    #                                                                            productid=product)
                    return E4k_Tblproduct_ProductPriceStandardDateMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardDateMatrix_Create(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardDateMatrix_Create(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandardDateMatrix_Create(success='Failed: '+str(e))


######################################################################
############################################################ E4K_TblproductProductPriceStandardDateMatrix Update

# class E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(graphene.Mutation):
#     class Arguments:
#         companyid = graphene.String(required=True)
#         productid = graphene.String(required=True)
#         stdpricematix = graphene.List(required=True, of_type=graphene.JSONString)

#     success = graphene.String()

#     @staticmethod
#     def mutate(root, info, companyid, productid, stdpricematix):
#         try:
#             # Retrieve the company and product instances
#             company = Tblcompany.objects.get(companyid=companyid)
#             product = TblproductProducts.objects.get(companyid=company, productid=productid)

#             with transaction.atomic():
#                 try:
#                     matrix_instance, created = TblproductProductPriceStandardDateMatrix.objects.get_or_create(
#                         companyid=company,
#                         productid=product
#                     )

#                     # Extract existing data from matrix
#                     stdpric_data = matrix_instance.stdpricematix or []

#                     # Initialize lists for updated data and duplicates
#                     updated_data = []
#                     duplicates = []

#                     # Create a set to track unique entries using all fields dynamically
#                     seen_entries = set()

#                     def sort_dict_keys(d):
#                         sorted_items = sorted(d.items())
#                         return dict(sorted_items)

#                     def create_entry_key(entry):
#                         """Create a unique key for an entry by combining its fields into a hashable string."""
#                         return '|'.join([f"{key}:{entry.get(key, '')}" for key in entry.keys()])

#                     # Process new items
#                     for entry in stdpricematix:
#                         # Create a unique key based on all fields dynamically
#                         entry_key = create_entry_key(entry)
#                         if entry_key in seen_entries:
#                             duplicates.append(entry)
#                         else:
#                             # Mark entry as seen
#                             seen_entries.add(entry_key)

#                             # Check if the entry already exists in the current matrix
#                             updated = False
#                             for existing_entry in stdpric_data:
#                                 existing_entry_key = create_entry_key(existing_entry)
#                                 #print(create_entry_key(sort_dict_keys(existing_entry)) == create_entry_key(sort_dict_keys(entry)))
#                                 # If existing entry matches the new entry based on key, update it
#                                 if entry_key == existing_entry_key:
#                                     existing_entry.update({
#                                         'price': float(entry.get('price', 0)),
#                                         'pricetype': int(entry.get('pricetype', 0)),
#                                         'fromdate': str(entry.get('fromdate', '')),
#                                         'todate': str(entry.get('todate', ''))
#                                     })
#                                     updated_data.append(existing_entry)
#                                     updated = True
#                                     print("Updated existing entry:", existing_entry)
#                                     break

#                             # If not updated, it's a new entry
#                             if not updated:
#                                 #print(f"Adding new entry: {entry}")
#                                 entry['price'] = float(entry.get('price', 0))
#                                 entry['pricetype'] = int(entry.get('pricetype', 0))
#                                 entry['fromdate'] = str(entry.get('fromdate', ''))
#                                 entry['todate'] = str(entry.get('todate', ''))
#                                 updated_data.append(entry)

#                     # Include non-updated existing data that weren't in the new entries
#                     #updated_data.extend([item for item in stdpric_data if create_entry_key(item) not in seen_entries])


#                     # Print duplicate data summary if any
#                     # if duplicates:
#                     #     print(f"Total duplicate entries: {len(duplicates)}")
#                     #     for dup in duplicates:
#                     #         print("Duplicate entry:", dup)
#                     if len(duplicates) == 0:
#                         matrix_instance.stdpricematix = updated_data
#                         matrix_instance.save()
#                         return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Success")
#                     else:
#                         return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Failed : Duplicate Record Found")


#                 except TblproductProductPriceStandardDateMatrix.DoesNotExist:
#                     return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Product Price Standard Date matrix data Not found")

#         except Tblcompany.DoesNotExist:
#             return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Failed: Company ID does not exist")
#         except TblproductProducts.DoesNotExist:
#             return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Failed: Product ID does not exist")
#         except Exception as e:
#             return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success=f"Failed: {str(e)}")

class E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stdpricematix = graphene.List(required=True, of_type=graphene.JSONString)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, stdpricematix):
        try:
            # Retrieve the company and product instances
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company, productid=productid)

            with transaction.atomic():
                try:
                    matrix_instance, created = TblproductProductPriceStandardDateMatrix.objects.get_or_create(
                        companyid=company,
                        productid=product
                    )

                    # Extract existing data from matrix
                    stdpric_data = matrix_instance.stdpricematix or []

                    # Initialize lists for updated data and duplicates
                    updated_data = []
                    duplicates = []

                    # Create a set to track unique entries using all fields dynamically
                    seen_entries = set()
                    exclude_keys = ['price']

                    def sort_dict_keys(d):
                        sorted_items = sorted(d.items())
                        return dict(sorted_items)

                    def create_entry_key(entry):
                        """Create a unique key for an entry by combining its fields into a hashable string."""
                        return '|'.join([f"{key}:{entry.get(key, '')}" for key in entry.keys()])
                        #return '|'.join([f"{key}" for key in entry.keys()])

                    # Process new items
                    for entry in stdpricematix:
                        # Create a unique key based on all fields dynamically
                        entry_key = create_entry_key(sort_dict_keys(entry))
                        update_data_dict_keys = {key: value for key, value in entry.items() if key not in exclude_keys}
                        update_data_dict_keys['pricetype'] = int(update_data_dict_keys['pricetype'])
                        update_data_dict_keys['fromdate'] = str(update_data_dict_keys['fromdate'])
                        update_data_dict_keys['todate'] = str(update_data_dict_keys['todate'])
                        if entry_key in seen_entries:
                            duplicates.append(entry)
                        else:
                            # Mark entry as seen
                            seen_entries.add(entry_key)

                            # Check if the entry already exists in the current matrix
                            updated = False
                            for existing_entry in stdpric_data:
                                existing_entry_key = create_entry_key(sort_dict_keys(existing_entry))
                                filtered_dict_keys = {key: value for key, value in existing_entry.items() if key not in exclude_keys}
                                #if entry_key == existing_entry_key:
                                if set(update_data_dict_keys.values()) == set(filtered_dict_keys.values()):
                                    existing_entry.update({
                                        'price': float(entry.get('price', 0)),
                                        'pricetype': int(entry.get('pricetype', 0)),
                                        'fromdate': str(entry.get('fromdate', '')),
                                        'todate': str(entry.get('todate', ''))
                                    })
                                    updated_data.append(existing_entry)
                                    updated = True
                                    #print("Updated existing entry:", existing_entry)
                                    #break
                            if updated == False:
                                #print(f"Adding new entry: {entry}")
                                entry['price'] = float(entry.get('price', 0))
                                entry['pricetype'] = int(entry.get('pricetype', 0))
                                entry['fromdate'] = str(entry.get('fromdate', ''))
                                entry['todate'] = str(entry.get('todate', ''))
                                updated_data.append(entry)

                            # # If not updated, it's a new entry
                            # if not updated:
                            #     #print(f"Adding new entry: {entry}")
                            #     entry['price'] = float(entry.get('price', 0))
                            #     entry['pricetype'] = int(entry.get('pricetype', 0))
                            #     entry['fromdate'] = float(entry.get('fromdate', ''))
                            #     entry['todate'] = float(entry.get('todate', ''))
                            #     updated_data.append(entry)

                    # Include non-updated existing data that weren't in the new entries
                    #updated_data.extend([item for item in stdpric_data if create_entry_key(item) not in seen_entries])


                    #Print duplicate data summary if any
                    # if duplicates:
                    #     print(f"Total duplicate entries: {len(duplicates)}")
                    #     for dup in duplicates:
                    #         print("Duplicate entry:", dup)

                    update_std_price_data = []
                    for record in updated_data:
                        update_std_price_data.append(dict(sorted(record.items())))

                    if len(duplicates) == 0:
                        matrix_instance.stdpricematix = update_std_price_data
                        matrix_instance.save()
                        return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Success")
                    else:
                        return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Failed : Duplicate Record Found")


                except TblproductProductPriceStandardDateMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Product Price Standard Qty data Not found")

        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Failed: Company ID does not exist")
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success="Failed: Product ID does not exist")
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandardDateMatrix_Update(success=f"Failed: {str(e)}")
        

################################################ E4K_TblproductProductPriceStandardQtyMatrix  Delete

class E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        deletedateprice = graphene.JSONString(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid,deletedateprice):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_price_standard_qty_matrix_instance = TblproductProductPriceStandardDateMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    
                    #deleteqtyprice_data = json.loads(deletedateprice)
                    
                    deletedateprice['price'] = float(deletedateprice['price'])
                    deletedateprice['pricetype'] = float(deletedateprice['pricetype'])
                    deletedateprice['fromdate'] = str(deletedateprice['fromdate'])
                    deletedateprice['todate'] = str(deletedateprice['todate'])
                    strprice_existing_data = product_price_standard_qty_matrix_instance.stdpricematix
                    if len(strprice_existing_data) > 0 and deletedateprice:
                        strprice_existing_data.remove(deletedateprice)
                        product_price_standard_qty_matrix_instance.stdpricematix = strprice_existing_data
                        product_price_standard_qty_matrix_instance.save()
                        return E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete(success = "Success")
                    else:
                        return E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete(success = "Failed: No Data to Delete")
                except TblproductProductPriceStandardDateMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete(success = "Failed Product Price Standard date data Not found")
                    
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete(success='Failed: '+str(e))
        



################################################ E4K_TblproductProductPriceStandardQtyMatrix  create

class E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_price_standard_qty_matrix_instance = TblproductProductPriceStandardQtyMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create(success = "Failed to create product Price Standard")
                except TblproductProductPriceStandardQtyMatrix.DoesNotExist:
                    product_price_standard_qty_matrix_instance = TblproductProductPriceStandardQtyMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        stdpricematix = []
                    )
                    product_price_standard_qty_matrix_instance.save()
                    return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create(success='Failed: '+str(e))
        


###################################################### E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update



class E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        stdpricematix = graphene.List(required=True, of_type=graphene.JSONString)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, stdpricematix):
        try:
            # Retrieve the company and product instances
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company, productid=productid)

            with transaction.atomic():
                try:
                    matrix_instance, created = TblproductProductPriceStandardQtyMatrix.objects.get_or_create(
                        companyid=company,
                        productid=product
                    )

                    # Extract existing data from matrix
                    stdpric_data = matrix_instance.stdpricematix or []

                    # Initialize lists for updated data and duplicates
                    updated_data = []
                    duplicates = []

                    # Create a set to track unique entries using all fields dynamically
                    seen_entries = set()
                    exclude_keys = ['price']

                    def sort_dict_keys(d):
                        sorted_items = sorted(d.items())
                        return dict(sorted_items)

                    def create_entry_key(entry):
                        """Create a unique key for an entry by combining its fields into a hashable string."""
                        return '|'.join([f"{key}:{entry.get(key, '')}" for key in entry.keys()])
                        #return '|'.join([f"{key}" for key in entry.keys()])

                    # Process new items
                    for entry in stdpricematix:
                        # Create a unique key based on all fields dynamically
                        entry_key = create_entry_key(sort_dict_keys(entry))
                        update_data_dict_keys = {key: value for key, value in entry.items() if key not in exclude_keys}
                        update_data_dict_keys['pricetype'] = int(update_data_dict_keys['pricetype'])
                        update_data_dict_keys['fromqty'] = float(update_data_dict_keys['fromqty'])
                        update_data_dict_keys['toqty'] = float(update_data_dict_keys['toqty'])
                        if entry_key in seen_entries:
                            duplicates.append(entry)
                        else:
                            # Mark entry as seen
                            seen_entries.add(entry_key)

                            # Check if the entry already exists in the current matrix
                            updated = False
                            for existing_entry in stdpric_data:
                                existing_entry_key = create_entry_key(sort_dict_keys(existing_entry))
                                filtered_dict_keys = {key: value for key, value in existing_entry.items() if key not in exclude_keys}
                                #print(update_data_dict_keys,'77777777777777777777',filtered_dict_keys)
                                #if entry_key == existing_entry_key:
                                if set(update_data_dict_keys.values()) == set(filtered_dict_keys.values()):
                                    existing_entry.update({
                                        'price': float(entry.get('price', 0)),
                                        'pricetype': int(entry.get('pricetype', 0)),
                                        'fromqty': float(entry.get('fromqty', '')),
                                        'toqty': float(entry.get('toqty', ''))
                                    })
                                    updated_data.append(existing_entry)
                                    updated = True
                                    #print("Updated existing entry:", existing_entry)
                                    #break
                            if updated == False:
                                #print(f"Adding new entry: {entry}")
                                entry['price'] = float(entry.get('price', 0))
                                entry['pricetype'] = int(entry.get('pricetype', 0))
                                entry['fromqty'] = float(entry.get('fromqty', ''))
                                entry['toqty'] = float(entry.get('toqty', ''))
                                updated_data.append(entry)

                            # # If not updated, it's a new entry
                            # if not updated:
                            #     #print(f"Adding new entry: {entry}")
                            #     entry['price'] = float(entry.get('price', 0))
                            #     entry['pricetype'] = int(entry.get('pricetype', 0))
                            #     entry['fromqty'] = float(entry.get('fromqty', ''))
                            #     entry['toqty'] = float(entry.get('toqty', ''))
                            #     updated_data.append(entry)

                    # Include non-updated existing data that weren't in the new entries
                    #updated_data.extend([item for item in stdpric_data if create_entry_key(item) not in seen_entries])


                    #Print duplicate data summary if any
                    # if duplicates:
                    #     print(f"Total duplicate entries: {len(duplicates)}")
                    #     for dup in duplicates:
                    #         print("Duplicate entry:", dup)

                    # Update the matrix instance with sorted
                    update_std_price_data = []
                    for record in updated_data:
                        update_std_price_data.append(dict(sorted(record.items())))

                    if len(duplicates) == 0:
                        matrix_instance.stdpricematix = update_std_price_data
                        matrix_instance.save()
                        return E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update(success="Success")
                    else:
                        return E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update(success="Failed : Duplicate Record Found")


                except TblproductProductPriceStandardQtyMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update(success="Product Price Standard Qty data Not found")

        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update(success="Failed: Company ID does not exist")
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update(success="Failed: Product ID does not exist")
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update(success=f"Failed: {str(e)}")




################################################ E4K_TblproductProductPriceStandardQtyMatrix  Delete

class E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        deleteqtyprice = graphene.JSONString(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid,deleteqtyprice):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_price_standard_qty_matrix_instance = TblproductProductPriceStandardQtyMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    #deleteqtyprice_data = json.loads(deleteqtyprice)
                    deleteqtyprice['price'] = float(deleteqtyprice['price'])
                    deleteqtyprice['pricetype'] = float(deleteqtyprice['pricetype'])
                    deleteqtyprice['fromqty'] = float(deleteqtyprice['fromqty'])
                    deleteqtyprice['toqty'] = float(deleteqtyprice['toqty'])
                    strprice_existing_data = product_price_standard_qty_matrix_instance.stdpricematix
                    if len(strprice_existing_data) > 0 and deleteqtyprice:
                        strprice_existing_data.remove(deleteqtyprice)
                        product_price_standard_qty_matrix_instance.stdpricematix = strprice_existing_data
                        product_price_standard_qty_matrix_instance.save()
                        return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete(success = "Success")
                    else:
                        return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete(success = "Failed: No Data to Delete")
                except TblproductProductPriceStandardQtyMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete(success = "Failed Product Price Standard Qty data Not found")
                    
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete(success='Failed: '+str(e))
        


################################################ E4K_TblproductProductVatcodeMatrix Create

class E4k_Tblproduct_ProductVatcodeMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_vatcode_matrix_instance = TblproductProductVatcodeMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    return E4k_Tblproduct_ProductVatcodeMatrix_Create(success = "Failed to create product Vatcode")
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    product_vatcode_matrix_instance = TblproductProductVatcodeMatrix.objects.create(
                        companyid=company,
                        productid=product
                    )
                    product_vatcode_matrix_instance.save()
                    product_vatcode_matrix_instance.Update_Product_Vatcode_Matrix(company=company,
                                                                                    productid=product)
                    return E4k_Tblproduct_ProductVatcodeMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductVatcodeMatrix_Create(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductVatcodeMatrix_Create(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductVatcodeMatrix_Create(success='Failed: '+str(e))
        
############################################################# E4k_Tblproduct_ProductVatcodeMatrix Update

class E4k_Tblproduct_ProductVatcodeMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        vatcodematix = graphene.List(required = True,of_type=graphene.JSONString)
    
    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, vatcodematix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            with transaction.atomic():
                try:
                    product_vatcode_matrix_instance = TblproductProductVatcodeMatrix.objects.get(
                        companyid=company,
                        productid=product
                    )
                    exclude_keys = ["Vatcode"]
                    vatcode_data = product_vatcode_matrix_instance.vatcodematix
                    update_data_dict_keys = {key: value for key, value in vatcodematix[0].items() if key not in exclude_keys}
                    for i in range(len(vatcode_data)):
                        filtered_dict = {key: value for key, value in vatcode_data[i].items() if key not in exclude_keys}
                        if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                            vatcode_data[i]['Vatcode']=int(vatcodematix[0]['Vatcode'])
                            product_vatcode_matrix_instance.vatcodematix = vatcode_data
                            product_vatcode_matrix_instance.save()
                            return E4k_Tblproduct_ProductVatcodeMatrix_Update(success = "Success")
                except TblproductProductVatcodeMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductVatcodeMatrix_Update(success = "Product Vatcode ID Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductVatcodeMatrix_Update(success='Failed: Company ID does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductVatcodeMatrix_Update(success='Failed: Product ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductVatcodeMatrix_Update(success='Failed: '+str(e))
        
######################################################## E4K_TblproductProductSuppliersWeekdaysNode Create

class E4k_Tblproduct_ProductSuppliersWeekdays_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        weekday = graphene.Int(required = True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, supplierid, weekday):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            supplier = Tblsupplier.objects.get(companyid=company,businessid=supplierid)
            with transaction.atomic():
                try:
                    product_suppliers_weekdays_node_instance = TblproductProductSuppliersWeekdays.objects.get(
                        companyid=company,
                        supplierid=supplier,
                        weekday=weekday
                    )
                    return E4k_Tblproduct_ProductSuppliersWeekdays_Create(success = "Failed to create product suppliers weekdays node")
                except TblproductProductSuppliersWeekdays.DoesNotExist:
                    product_suppliers_weekdays_node_instance = TblproductProductSuppliersWeekdays.objects.create(
                        companyid=company,
                        supplierid=supplier,
                        weekday=weekday
                    )
                    product_suppliers_weekdays_node_instance.save()

                    return E4k_Tblproduct_ProductSuppliersWeekdays_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Create(success='Failed: Company ID does not exist')
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Create(success='Failed: Supplier ID does not exist')

######################################################## E4k_Tblproduct_ProductSuppliersWeekdays Update

class E4k_Tblproduct_ProductSuppliersWeekdays_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        weekday = graphene.Int(required = True)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, supplierid, weekday):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            supplier = Tblsupplier.objects.get(companyid=company,businessid=supplierid)
            with transaction.atomic():
                try:
                    product_suppliers_weekdays_node_instance = TblproductProductSuppliersWeekdays.objects.get(
                        companyid=company,
                        supplierid=supplier,   
                    )
                    product_suppliers_weekdays_node_instance.weekday=weekday
                    product_suppliers_weekdays_node_instance.save()
                    return E4k_Tblproduct_ProductSuppliersWeekdays_Update(success = "Success")
                except TblproductProductSuppliersWeekdays.DoesNotExist:
                    return E4k_Tblproduct_ProductSuppliersWeekdays_Update(success = "Product suppliers weekdays node ID Not found")
            
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Update(success='Failed: Company ID does not exist')
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Update(success='Failed: Supplier ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Update(success='Failed: '+str(e))

#################################################### E4k_Tblproduct_ProductSuppliersWeekdays Delete

class E4k_Tblproduct_ProductSuppliersWeekdays_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        
    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, supplierid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            supplier = Tblsupplier.objects.get(companyid=company,businessid=supplierid)
            with transaction.atomic():
                try:
                    product_suppliers_weekdays_node_instance = TblproductProductSuppliersWeekdays.objects.get(
                        companyid=company,
                        supplierid=supplier
                    )
                    product_suppliers_weekdays_node_instance.delete()

                    return E4k_Tblproduct_ProductSuppliersWeekdays_Delete(success = "Success")
                except TblproductProductSuppliersWeekdays.DoesNotExist:
                    return E4k_Tblproduct_ProductSuppliersWeekdays_Delete(success = "Product suppliers weekdays node ID Not found")
        
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Delete(success='Failed: Company ID does not exist')
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Delete(success='Failed: Supplier ID does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductSuppliersWeekdays_Delete(success=f"Failed Unable To Delete \n\n Exception \n: {e}")



######################################## Product properties matrix 
class Tbl_FSK_ProductPropertyLevel(graphene.Mutation):
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info):
        try:
            company = Tblcompany.objects.get(companyid='001')
            property_levels = TblproductProductPropertyLevel.objects.all()
            for property_level in property_levels:
                product_id = property_level.productid
                try:
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.get(productid=product_id)
                except TblproductProductPropertyLevelColmatrix.DoesNotExist:
                    property_level_col = TblproductProductPropertyLevelColmatrix.objects.create(
                        companyid=company,
                        productid=product_id,
                        stockcolmatrix={"value": None},
                        pricecolmatrix={"value": None},
                        stklvlcolmatrix={"value": None},
                        stkloccolmatrix={"value": None},
                        stktypecolmatrix={"value": None},
                    )
                
                for field in property_level._meta.fields:
                    column_name = field.attname
                    if column_name not in ['companyid_id', 'productid_id']:
                        column_value = getattr(property_level, column_name)
                        property_level_col.Update_Product_Property_Level_ColMatrix(
                            product_property_level=column_value,
                            column_name=column_name,
                            productid=product_id,
                            companyid = company
                        )

            return Tbl_FSK_ProductPropertyLevel(success=True)

        except Tblcompany.DoesNotExist:
            return Tbl_FSK_ProductPropertyLevel(success=False)
        except Exception as e:
            print(f"An error occurred: {e}")
            return Tbl_FSK_ProductPropertyLevel(success=False)


class TblFSK_All_Product_Property_Matrix(graphene.Mutation):
    
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info):
        try:
            # get the product
            product_instances = TblproductProducts.objects.all()
            company = Tblcompany.objects.get(companyid='001')
            for product in product_instances:
                try:
                    pro_mat = TblproductProductPropertyMatrix.objects.get(productid=product)
                    
                    pro_mat.update_PropertyMatix(product)
                except TblproductProductPropertyMatrix.DoesNotExist:
                    productmatrix_instance = TblproductProductPropertyMatrix.objects.create(
                        companyid=company,
                        productid=product,
                        propertymatix={"value": None},
                        propertycolmatrix = {"value": None}
                    )
                    productmatrix_instance.save()
            return TblFSK_All_Product_Property_Matrix(success=True)
        except ObjectDoesNotExist:
            return TblFSK_All_Product_Property_Matrix(success=False)
        
################################# Product image update code 
class E4k_TblProduct_Products_image_update_code(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                product_instances = TblproductProducts.objects.all()
                for product in product_instances:
                    try:
                        # product_image_instance = TblproductProducts.objects.get(companyid=company,
                        #                                                         productid=product)
                        product.styleimage = get_random_image_path("D:\E4K_Echo\Frontend\design1\public\product")
                        product.live = True
                        product.batchcontrol = True
                        
                        product.save()
                        print(product.styleimage)
                    except TblproductProducts.DoesNotExist:
                        return E4k_TblProduct_Products_image_update_code(success="Failed")
                        
            return E4k_TblProduct_Products_image_update_code(success="Success")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_Products_image_update_code(success='Failed: Company ID does not exist')

######################################## Tbl product size ranges bulk Create

class E4k_TblProduct_ProductSizeRangesValues_Bulk_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        size_number = graphene.List(required=True,of_type=  graphene.Int)
        size_value = graphene.List(required=True,of_type= graphene.String)

    size_ranges = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, rangeid, size_number, size_value):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    sizerange = TblproductSizeRanges.objects.get(companyid=company,
                                                            rangeid=rangeid)
                    try:
                        size_ranges_id = TblproductSizeRangeValues.objects.get(companyid = company,rangeid = sizerange)
                        return E4k_TblProduct_ProductSizeRangesValues_Bulk_Create(size_ranges="Range id already exists")
                    except TblproductSizeRangeValues.DoesNotExist:
                        try:
                            
                            size_number_, size_value_ = tuple(set(size_number)), tuple(set(size_value))
                            assert len(size_number_) == len(size_value_)
                            product_sizes = [
                                    TblproductSizeRangeValues(companyid=company,rangeid=sizerange, size_number=size, size_value=size_value)
                                    for size, size_value in zip(size_number, size_value)
                                ]

                            Size_range = TblproductSizeRangeValues.objects.bulk_create(product_sizes)
                            
                        
                            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Create(size_ranges = "Success")
                        except Exception as e:
                            print("Must Provide Unique Size Number and Size Value:", e)
                            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Create(size_ranges=f"Failed Unable To Create \n\n Exception \n: {e}")
                except TblproductSizeRanges.DoesNotExist:
                    return E4k_TblProduct_ProductSizeRangesValues_Bulk_Create(size_ranges='Range id does not exist')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Create(size_ranges='Company id is not found')
        except Exception as e:
            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Create(size_ranges="Failed to create product size ranges")

######################################## Tbl Product Size Ranges update

class E4k_TblProduct_ProductSizeRangesValues_Bulk_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        size_number = graphene.List(required=True,of_type=  graphene.Int)
        size_value = graphene.List(required=True,of_type= graphene.String)
    
    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, rangeid, size_number, size_value):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    sizerange = TblproductSizeRanges.objects.get(companyid=company, rangeid=rangeid)
                    
                    # Ensure size_number and size_value are unique and match in length
                    size_number_, size_value_ = list(dict.fromkeys(size_number)), list(dict.fromkeys(size_value))
                    if len(size_number_) != len(size_value_):
                        raise ValueError("Size number and size value must have the same length")
                    
                    existing_sizes = TblproductSizeRangeValues.objects.filter(companyid=company, rangeid=sizerange)
                    existing_size_numbers = [ps.size_number for ps in existing_sizes]
                    existing_size_values = {ps.size_number: ps.size_value for ps in existing_sizes}
                    
                    new_size_value_map = dict(zip(size_number_, size_value_))
                    
                    # Update or create records while maintaining order
                    updated_sizes = []
                    new_sizes_to_create = []
                    
                    for sn, sv in zip(size_number_, size_value_):
                        if sn in existing_size_numbers:
                            existing_size_values[sn] = sv
                        else:
                            new_sizes_to_create.append(TblproductSizeRangeValues(companyid=company, rangeid=sizerange, size_number=sn, size_value=sv))
                    
                    for product_size in existing_sizes:
                        if product_size.size_number in new_size_value_map:
                            product_size.size_value = new_size_value_map[product_size.size_number]
                            updated_sizes.append(product_size)
                    
                    TblproductSizeRangeValues.objects.bulk_update(updated_sizes, ['size_value'])
                    TblproductSizeRangeValues.objects.bulk_create(new_sizes_to_create)
                    
                    # Delete old records not in new size numbers
                    size_numbers_to_delete = set(existing_size_numbers) - set(size_number_)
                    TblproductSizeRangeValues.objects.filter(companyid=company, rangeid=sizerange, size_number__in=size_numbers_to_delete).delete()
                    
                    return E4k_TblProduct_ProductSizeRangesValues_Bulk_Update(success="Success")
                
                except TblproductSizeRanges.DoesNotExist:
                    return E4k_TblProduct_ProductSizeRangesValues_Bulk_Update(success="Product rangeid not found")
                
                except Exception as e:
                    print("Error:", e)
                    return E4k_TblProduct_ProductSizeRangesValues_Bulk_Update(success=f"Failed to update: {e}")

        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Update(success="Company id not found")

############################ Bulk delete
class E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        rangeid = graphene.String(required=True)
        

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, rangeid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                    try:
                        sizerange = TblproductSizeRanges.objects.get(companyid=company, rangeid=rangeid)

                        size_value_ranges = TblproductSizeRangeValues.objects.filter(companyid=company, rangeid=sizerange)
                        if len(size_value_ranges)>0:
                            size_value_ranges.delete()
                            ##sizerange.delete()
                            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(success = "Success")
                        else:
                            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(success="No Size Ranges Values Found")
                    except TblproductSizeRanges.DoesNotExist:
                        return E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(success="Product rangeid not found") 
                    except TblproductSizeRangeValues.DoesNotExist:
                        return E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(success="Size Ranges Values Not Found")
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(success="Company id not found")
        except TblproductSizeRanges.DoesNotExist:
            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(success="Failed To delete")
        except Exception as e:
            return E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete(success="Failed : %s" % e.message)


#################### Tbl Product property types values add
######################################## Tbl ProductProperties Values Create
class E4k_Tblproduct_ProductPropertyType_Values_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        proptype_values = graphene.List(required=True, of_type=graphene.String)

    create_property_type_values = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, propertyid, proptype_values):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    property_type = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)
                    existing_values = TblproductPropertyTypesValues.objects.filter(companyid=company, proptypeid=property_type)
                    existing_values_set = set(existing_value.proptype_values for existing_value in existing_values)
                    
                    # Find new values that are not in existing values
                    new_values = [value for value in proptype_values if value not in existing_values_set]
                    
                    # Bulk create only new values
                    TblproductPropertyTypesValues.objects.bulk_create([
                        TblproductPropertyTypesValues(companyid=company, proptypeid=property_type, proptype_values=value) 
                        for value in new_values
                    ])
                    
                    return E4k_Tblproduct_ProductPropertyType_Values_Create(create_property_type_values="Success")
                except TblproductPropertyTypes.DoesNotExist:
                    return E4k_Tblproduct_ProductPropertyType_Values_Create(create_property_type_values="Product property id not found")
                except Exception as e:
                    return E4k_Tblproduct_ProductPropertyType_Values_Create(create_property_type_values="Failed to create: %s" % e)
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyType_Values_Create(create_property_type_values="Company id not found")


class E4k_Tblproduct_ProductPropertyType_Values_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        proptype_values = graphene.List(required=True, of_type=graphene.String)

    create_or_update_property_type_values = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, propertyid, proptype_values):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    property_type = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)
                    existing_values = TblproductPropertyTypesValues.objects.filter(companyid=company, proptypeid=property_type)
                    existing_values_dict = {existing_value.proptype_values: existing_value for existing_value in existing_values}

                    new_values = set(proptype_values)
                    existing_values_set = set(existing_values_dict.keys())

                    # Values to be added (new values that are not in existing values)
                    values_to_add = new_values - existing_values_set

                    # Update the existing values
                    for value in new_values & existing_values_set:
                        record = existing_values_dict[value]
                        record.proptype_values = value
                        record.save()

                    # Bulk create new values
                    TblproductPropertyTypesValues.objects.bulk_create([
                        TblproductPropertyTypesValues(companyid=company, proptypeid=property_type, proptype_values=value)
                        for value in values_to_add
                    ])

                    return E4k_Tblproduct_ProductPropertyType_Values_Update(create_or_update_property_type_values="Success")
                except TblproductPropertyTypes.DoesNotExist:
                    return E4k_Tblproduct_ProductPropertyType_Values_Update(create_or_update_property_type_values="Product property id not found")
                except Exception as e:
                    return E4k_Tblproduct_ProductPropertyType_Values_Update(create_or_update_property_type_values="Failed to update: %s" % e)
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductPropertyType_Values_Update(create_or_update_property_type_values="Company id not found")



class E4k_TblProduct_ProductPropertyType_Values_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        propertyid = graphene.Int(required=True)
        proptype_values = graphene.String(required=True)
        
    delete_property_type_value = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, propertyid, proptype_values):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            with transaction.atomic():
                try:
                    property_type = TblproductPropertyTypes.objects.get(companyid=company, propertyid=propertyid)
                    value_to_delete = TblproductPropertyTypesValues.objects.get(companyid=company, proptypeid=property_type, proptype_values=proptype_values)
                    value_to_delete.delete()
                    return E4k_TblProduct_ProductPropertyType_Values_Delete(delete_property_type_value="Success")
                except TblproductPropertyTypes.DoesNotExist:
                    return E4k_TblProduct_ProductPropertyType_Values_Delete(delete_property_type_value="Product property id not found")
                except TblproductPropertyTypesValues.DoesNotExist:
                    return E4k_TblProduct_ProductPropertyType_Values_Delete(delete_property_type_value ="Product property id not found")
        except Exception as e:
            return E4k_TblProduct_ProductPropertyType_Values_Delete(delete_property_type_value="Failed to delete: %s" % e)
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_ProductPropertyType_Values_Delete(delete_property_type_value="Company id not found")


################ Obsolete matrix table create 
class AllE4k_Tblproduct_ProductObsoletetypeMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.filter(companyid=company)
            with transaction.atomic():
                for product_id in product:
                    #print('###### Product = %s' % product_id.productid)
                    try:
                        product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.get(
                            companyid=company,
                            productid=product_id
                        )
                    except TblproductProductObsoleteMatrix.DoesNotExist:
                        product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.create(
                            companyid=company,
                            productid=product_id,
                            obslmatix = [{"value":0}]
                        )
                        product_obsoletetype_matrix_instance.save()
                        product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.get(
                            companyid=company,
                            productid=product_id
                        )
                        product_obsoletetype_matrix_instance.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                                productid=product_id
                                                                                                )
                return AllE4k_Tblproduct_ProductObsoletetypeMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return AllE4k_Tblproduct_ProductObsoletetypeMatrix_Create(success='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return AllE4k_Tblproduct_ProductObsoletetypeMatrix_Create(success='Failed: Product does not exist')
        except Exception as e:
            return AllE4k_Tblproduct_ProductObsoletetypeMatrix_Create(success='Failed: '+str(e))
        

########################### E4k tbl product Suplliers level create################################################################################################################
class E4k_Tblproduct_ProductSupplierLevel_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        suppliermatrix = graphene.JSONString(required=True)
        
    create_product_supplier_level = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid,supplierid, suppliermatrix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            supplier = Tblsupplier.objects.get(companyid=company, businessid = supplierid)
            with transaction.atomic():

                product_supplier_level_instance = TblproductProductSupplierLevel.objects.create(
                    companyid=company,
                    productid=product_instance,
                    supplierid= supplier,
                    suppliermatrix=[suppliermatrix],
                    
                )
                
                product_supplier_level_instance.save()
                
                # Update the property level col matrix instance
                try:
                    supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance,
                                                                                             supplierid=supplier,
                                                                                             )
                    property_level = TblproductProductSupplierLevel.objects.get(companyid=company,
                                                                                productid=product_instance,
                                                                                supplierid=supplier,
                                                                                )

                    return E4k_Tblproduct_ProductPropertyLevel_Create(create_product_supplier_level="Failed to Create already Exists")
                except TblproductProductSupplierLevelColmatrix.DoesNotExist:
                    supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        supplierid=supplier,
                        suppliercolmatrix={"value": None},
                        
                    )
                    supplier_level_col.save()
                except TblproductProductSupplierLevel.DoesNotExist:
                    supplier_level = TblproductProductSupplierLevel.objects.create(
                        companyid=company,
                        productid=product_instance,
                        supplierid=supplier,
                        suppliermatrix={"value": None},
                    )
                    supplier_level.save()
                
                for field in product_supplier_level_instance._meta.fields:
                    
                    column_name = field.attname

                    if column_name not in ['id','companyid_id', 'productid_id','supplierid_id']:
                        column_value = getattr(product_supplier_level_instance, column_name)
                        supplier_level_col.Update_Product_Supplier_Level_ColMatrix(
                            supplier_level=column_value,
                            column_name=column_name,
                            productid=product_supplier_level_instance.productid,
                            companyid = company
                        )
                
                try:
                
                    product_stoking_level=  TblproductProductSuppliersMatrix.objects.get(
                                                            companyid=company,
                                                            productid=product_instance,
                                                            supplierid=supplier)
                    product_stoking_level.Update_Product_Supplier_Matrix(company=company,
                                                                                productid=product_instance,
                                                                                supplierid=supplier)
                except TblproductProductSuppliersMatrix.DoesNotExist:
                    product_stock_matrix = TblproductProductSuppliersMatrix.objects.create(
                        companyid=company,
                        productid=product_instance,
                        supplierid=supplier,
                        suppliermatrix=[{"value":0}]
                        
                    )
                    product_stock_matrix.save()
                    product_stock_matrix.Update_Product_Supplier_Matrix(company=company,
                                                                              productid=product_instance,
                                                                              supplierid=supplier)
                

                return E4k_Tblproduct_ProductSupplierLevel_Create(create_product_supplier_level="Success")
            
        
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Create(create_product_supplier_level='Failed: Supplier does not exist')
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Create(create_product_supplier_level='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Create(create_product_supplier_level='Failed: Product does not exist')
        except IntegrityError as e:
            print(f"IntegrityError: {str(e)}")
            return E4k_Tblproduct_ProductSupplierLevel_Create(create_product_supplier_level=f'Failedsave: {str(e)}')
        except Exception as e:
            print(f"Exception: {str(e)}")
            return E4k_Tblproduct_ProductSupplierLevel_Create(create_product_supplier_level=f'Failedsave: {str(e)}')
        



####################################################################### Product Supplier level Update

class E4k_Tblproduct_ProductSupplierLevel_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        suppliermatrix = graphene.JSONString(required=True)
        
    
    update_product_supplier_level = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid, supplierid, suppliermatrix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            supplier = Tblsupplier.objects.get(companyid=company, businessid = supplierid)
            with transaction.atomic():
                product_supplier_level_instance = TblproductProductSupplierLevel.objects.get(
                    companyid=company,
                    productid=product_instance,
                    supplierid=supplier,
                )
                product_supplier_level_instance.suppliermatrix=[suppliermatrix]
               
                product_supplier_level_instance.save()
                product_supplier_level_instance = TblproductProductSupplierLevel.objects.get(
                    companyid=company,
                    productid=product_instance,
                    supplierid=supplier,
                )
                supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance,
                                                                                             supplierid=supplier,
                                                                                             )
                    
                
                for field in product_supplier_level_instance._meta.fields:
                    
                    column_name = field.attname

                    if column_name not in ['id','companyid_id', 'productid_id','supplierid_id']:
                        column_value = getattr(product_supplier_level_instance, column_name)
                        supplier_level_col.Update_Product_Supplier_Level_ColMatrix(
                            supplier_level=column_value,
                            column_name=column_name,
                            productid=product_supplier_level_instance.productid,
                            companyid = company
                        )
                ########Update the Stoking Level
                product_suppliermatrix_level=  TblproductProductSuppliersMatrix.objects.get(
                                                    companyid=company,
                                                    productid=product_instance,
                                                    supplierid=supplier)
                product_suppliermatrix_level.Update_Product_Supplier_Matrix(company=company,
                                                                            productid=product_instance,
                                                                            supplierid=supplier)
                


                                                      

                return E4k_Tblproduct_ProductSupplierLevel_Update(update_product_supplier_level = "Success")
            
        except TblproductProductSuppliersMatrix.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Update(update_product_supplier_level = "TblproductProductSuppliersMatrix not found")
       
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Update(update_product_supplier_level='Failed: Supplier does not exist')

        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Update(update_product_supplier_level='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Update(update_product_supplier_level='Failed: Product does not exist')
        except Exception as e:
            print(f"Exception: {str(e)}")
            return E4k_Tblproduct_ProductSupplierLevel_Update(update_product_supplier_level=f'Failedsave: {str(e)}')
        except TblproductProductSupplierLevelColmatrix.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Update(update_product_supplier_level = "TblproductProductSupplierLevelColmatrix not found")
            

################################################## Product Supplier level delete 
class E4k_Tblproduct_ProductSupplierLevel_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        
        
    delete_product_supplier_level = graphene.String()

    @staticmethod
    def mutate(root, info, companyid, productid,supplierid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product_instance = TblproductProducts.objects.get(companyid=company, productid=productid)
            supplier = Tblsupplier.objects.get(companyid=company, businessid = supplierid)
            with transaction.atomic():

                product_supplier_level_instance = TblproductProductSupplierLevel.objects.get(
                    companyid=company,
                    productid=product_instance,
                    supplierid= supplier
                    
                )
                
                
                
                # Update the property level col matrix instance
                try:
                    supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                             productid=product_instance,
                                                                                             supplierid=supplier,
                                                                                             )
                    supplier_level_col.delete()

                except TblproductProductSupplierLevelColmatrix.DoesNotExist:
                    pass
                
                
                try:
                
                    product_stoking_level=  TblproductProductSuppliersMatrix.objects.get(
                                                            companyid=company,
                                                            productid=product_instance,
                                                            supplierid=supplier)
                    product_stoking_level.delete()
                except TblproductProductSuppliersMatrix.DoesNotExist:
                    pass

                product_supplier_level_instance.delete()
                

                return E4k_Tblproduct_ProductSupplierLevel_Delete(delete_product_supplier_level="Success")
            
        
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Delete(delete_product_supplier_level='Failed: Supplier does not exist')
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Delete(delete_product_supplier_level='Failed: Company does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierLevel_Delete(delete_product_supplier_level='Failed: Product does not exist')
        except IntegrityError as e:
            print(f"IntegrityError: {str(e)}")
            return E4k_Tblproduct_ProductSupplierLevel_Delete(delete_product_supplier_level=f'Failedsave: {str(e)}')
        except Exception as e:
            print(f"Exception: {str(e)}")
            return E4k_Tblproduct_ProductSupplierLevel_Delete(delete_product_supplier_level=f'Failedsave: {str(e)}')
        







################################################## Supplier Matrix update ########################

############################################## E4K_TblproductProductStockingtypeMatrix update

class E4k_Tblproduct_ProductSupplierMatrix_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        productid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        suppliermatrix = graphene.List(required = True,of_type=graphene.JSONString)

    success = graphene.String()
    @staticmethod
    def mutate(root, info, companyid, productid, supplierid,suppliermatrix):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company,productid=productid)
            supplier = Tblsupplier.objects.get(companyid=company, businessid = supplierid)
            with transaction.atomic():
                try:
                    product_suppliermatrix_matrix_instance = TblproductProductSuppliersMatrix.objects.get(
                        companyid=company,
                        productid=product,
                        supplierid = supplier
                    )
                    exclude_keys = ["LeadTime", "IsBulkOrder",'WarehouseID','SupplierCode','SupplierXRate','Select']
                    suppliermatrix_data = product_suppliermatrix_matrix_instance.suppliermatrix
                    supplier_matix_update =[]
                    for j in range(len(suppliermatrix)):
                        update_data_dict_keys = {key: value for key, value in suppliermatrix[j].items() if key not in exclude_keys}
                        for i in range(len(suppliermatrix_data)):
                            filtered_dict = {key: value for key, value in suppliermatrix_data[i].items() if key not in exclude_keys}
                            if set(update_data_dict_keys.values()) == set(filtered_dict.values()):
                                suppliermatrix_data[i]['SupplierCode']=str(suppliermatrix[j]['SupplierCode'])
                                suppliermatrix_data[i]['LeadTime']=int(suppliermatrix[j]['LeadTime'])
                                suppliermatrix_data[i]['WarehouseID']=str(suppliermatrix[j]['WarehouseID'])
                                suppliermatrix_data[i]['SupplierXRate']=float(suppliermatrix[j]['SupplierXRate'])
                                suppliermatrix_data[i]['IsBulkOrder']=str(suppliermatrix[j]['IsBulkOrder'])
                                suppliermatrix_data[i]['Select']=suppliermatrix[j]['Select']
                                supplier_matix_update.append(suppliermatrix_data[i])
                    product_suppliermatrix_matrix_instance.suppliermatrix = supplier_matix_update
                    product_suppliermatrix_matrix_instance.save()
                    return E4k_Tblproduct_ProductSupplierMatrix_Update(success = "Success")
                except TblproductProductStockingtypeMatrix.DoesNotExist:
                    return E4k_Tblproduct_ProductSupplierMatrix_Update(success = "Product Stocking type Not found")
        except Tblcompany.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierMatrix_Update(success='Failed: Company does not exist')
        except Tblsupplier.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierMatrix_Update(success='Failed: Supplier does not exist')
        except TblproductProducts.DoesNotExist:
            return E4k_Tblproduct_ProductSupplierMatrix_Update(success='Failed: Product does not exist')
        except Exception as e:
            return E4k_Tblproduct_ProductSupplierMatrix_Update(success='Failed: '+str(e))
                




###################### All Product Supplier Matrix Create Functions
################ Obsolete matrix table create 
class AllE4k_Tblproduct_ProductSupplierColMatrix_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)

    success = graphene.String()

    @staticmethod
    def mutate(root, info, companyid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            supplier = TblproductProductSupplierLevel.objects.filter(companyid=company)
            with transaction.atomic():
                i=1
                for supplier_level_data in supplier:
                    #print('###### Product = %s' % supplier_level_data.productid)
                    try:
                        
                        supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                                productid=supplier_level_data.productid,
                                                                                                 supplierid=supplier_level_data.supplierid,
                                                                                                 )
                        
                    
                        for field in supplier_level_data._meta.fields:
                            
                            column_name = field.attname

                            if column_name not in ['id','companyid_id', 'productid_id','supplierid_id']:
                                column_value = getattr(supplier_level_data, column_name)
                                supplier_level_col.Update_Product_Supplier_Level_ColMatrix(
                                    supplier_level=column_value,
                                    column_name=column_name,
                                    productid=supplier_level_data.productid,
                                    companyid = company
                                )
                        supplier_matrix_update = TblproductProductSuppliersMatrix.objects.get(companyid = company,
                                                                                                productid=supplier_level_data.productid,
                                                                                                supplierid=supplier_level_data.supplierid,)
                        supplier_matrix_update.Update_Product_Supplier_Matrix(company = company,
                                                                                                productid=supplier_level_data.productid,
                                                                                                supplierid=supplier_level_data.supplierid,)
                        print('Count = ',i)
                        i+=1
                    except TblproductProductSupplierLevelColmatrix.DoesNotExist:
                        supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.create(companyid = company,
                                                                                                productid=supplier_level_data.productid,
                                                                                                 supplierid=supplier_level_data.supplierid,
                                                                                                 suppliercolmatrix = {"value":0}
                                                                                                 )
                        
                        supplier_level_col.save()
                        supplier_level_col = TblproductProductSupplierLevelColmatrix.objects.get(companyid = company,
                                                                                                productid=supplier_level_data.productid,
                                                                                                 supplierid=supplier_level_data.supplierid,
                                                                                                 )
                        
                    
                        for field in supplier_level_data._meta.fields:
                            
                            column_name = field.attname

                            if column_name not in ['id','companyid_id', 'productid_id','supplierid_id']:
                                column_value = getattr(supplier_level_data, column_name)
                                supplier_level_col.Update_Product_Supplier_Level_ColMatrix(
                                    supplier_level=column_value,
                                    column_name=column_name,
                                    productid=supplier_level_data.productid,
                                    companyid = company
                                )

                    except TblproductProductSuppliersMatrix.DoesNotExist:
                        print(supplier_level_data,'################################',supplier_level_data.productid,'#$$$$$$$$$$$$$$$$$$',supplier_level_data.supplierid)   
                        
                return AllE4k_Tblproduct_ProductSupplierColMatrix_Create(success = "Success")
        except Tblcompany.DoesNotExist:
            return AllE4k_Tblproduct_ProductSupplierColMatrix_Create(success='Failed: Company does not exist')
        except TblproductProductSupplierLevel.DoesNotExist:
            return AllE4k_Tblproduct_ProductSupplierColMatrix_Create(success='Failed: Product does not exist')
        except Exception as e:
            return AllE4k_Tblproduct_ProductSupplierColMatrix_Create(success='Failed: '+str(e))
        
class AllE4k_TblSuppliermatixupdateCheck(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        supplierid = graphene.String(required=True)
        productid = graphene.String(required=True)

    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, supplierid, productid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            product = TblproductProducts.objects.get(companyid=company, productid=productid)
            supplier = Tblsupplier.objects.get(companyid=company, businessid=supplierid)
            supplier_query = TblproductProductSuppliersMatrix.objects.get(companyid=company, supplierid=supplier, productid=product)
            
            if supplier_query:
                supplier_query.Update_Product_Supplier_Matrix(company=company,
                                                        supplierid=supplier,
                                                         productid=product)
                return AllE4k_TblSuppliermatixupdateCheck(success='True')
            else:
                return AllE4k_TblSuppliermatixupdateCheck(success='False')
        except Tblcompany.DoesNotExist:
            return AllE4k_TblSuppliermatixupdateCheck(success='Failed: Company does not exist')
        except TblproductProductSuppliersMatrix.DoesNotExist:
            return AllE4k_TblSuppliermatixupdateCheck(success='Failed: Product does not exist')
        except Exception as e:
            return AllE4k_TblSuppliermatixupdateCheck(success='Failed: '+str(e))


########################################################## Copy Product from Exiting Product
class E4k_TblProduct_Copy_Existing_Product(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        source_productid = graphene.String(required=True)
        target_productid = graphene.String(required=True)

    success = graphene.String()
    
    @staticmethod
    def mutate(root, info, companyid, source_productid, target_productid):
        try:
            with transaction.atomic():
                company = Tblcompany.objects.get(companyid=companyid)
                try:
                    existing_product = TblproductProducts.objects.get(companyid=company,productid=source_productid)
                    try :
                        product_target = TblproductProducts.objects.get(companyid=company, productid=target_productid)

                        return E4k_TblProduct_Copy_Existing_Product(success='Target Product id already exists')
                    except TblproductProducts.DoesNotExist:
                        # Copy product details
                        new_product = TblproductProducts(
                            companyid = company,
                            productid = target_productid,
                            description = existing_product.description,
                            category1id = existing_product.category1id,
                            category2id = existing_product.category2id,
                            category3id = existing_product.category3id,
                            weight = existing_product.weight,
                            supplimentaryunits = existing_product.supplimentaryunits,
                            nominal_code = existing_product.nominal_code,
                            commodity_code = existing_product.commodity_code,
                            notes = existing_product.notes,
                            classid = existing_product.classid,
                            obsolete_class = existing_product.obsolete_class,
                            live = True if existing_product.live == b'\x01' else False,
                            styleimage = existing_product.styleimage,
                            batchcontrol = True if existing_product.batchcontrol == b'\x01' else False,
                            stockinguom = existing_product.stockinguom,
                            issueuom = existing_product.issueuom,
                            stockingtype = existing_product.stockingtype,
                            countryid = existing_product.countryid,
                        )
                        new_product.save()


                        # Copy properties and their values
                        for property in existing_product.tblproductproductproperties_set.all():
                            property_copy = TblproductProductProperties(
                                companyid=property.companyid,
                                productid=new_product,
                                propertyid=property.propertyid,
                                seqno=property.seqno
                            )
                            property_copy.save()

                            for value in property.tblproductproductpropertyvalues_set.all():
                                value_copy = TblproductProductPropertyValues(
                                    companyid=value.companyid,
                                    product_propid=property_copy,
                                    product_prop_value=value.product_prop_value
                                )
                                value_copy.save()

                        # Copy product property level if it exists
                        if hasattr(existing_product, 'tblproductproductpropertylevel'):
                            existing_level = existing_product.tblproductproductpropertylevel
                            level_copy = TblproductProductPropertyLevel(
                                companyid=existing_level.companyid,
                                productid=new_product,  # This must be a new product instance
                                stockmatrix=existing_level.stockmatrix,
                                pricematrix=existing_level.pricematrix,
                                stklvlmatrix=existing_level.stklvlmatrix,
                                stklocmatrix=existing_level.stklocmatrix,
                                stktypematrix=existing_level.stktypematrix,
                                obslmatrix=existing_level.obslmatrix
                            )
                            level_copy.save()
                        
                        # Copy product property level Col matrix if it exists
                        if hasattr(existing_product, 'tblproductproductpropertylevelcolmatrix'):
                            existing_level = existing_product.tblproductproductpropertylevelcolmatrix
                            level_copy_col = TblproductProductPropertyLevelColmatrix(
                                companyid=existing_level.companyid,
                                productid=new_product,  
                                stockcolmatrix=existing_level.stockcolmatrix,
                                pricecolmatrix=existing_level.pricecolmatrix,
                                stklvlcolmatrix=existing_level.stklvlcolmatrix,
                                stkloccolmatrix=existing_level.stkloccolmatrix,
                                stktypecolmatrix=existing_level.stktypecolmatrix,
                                obslcolmatrix=existing_level.obslcolmatrix
                            )
                            level_copy_col.save()

                        
                        ## Copy property matrix properties
                        for property in existing_product.tblproductproductpropertymatrix_set.all():
                            property_copy = TblproductProductPropertyMatrix(
                                companyid=property.companyid,
                                productid=new_product,
                                propertymatix=property.propertymatix,
                                propertycolmatrix=property.propertycolmatrix
                            )
                            property_copy.save()
                        
                        ### copy stocking level matrix properties
                        for property in existing_product.tblproductproductstockinglevelmatrix_set.all():
                            property_copy = TblproductProductStockinglevelMatrix(
                                companyid=property.companyid,
                                productid=new_product,
                                stocklevelmatix=property.stocklevelmatix,
                            )
                            property_copy.save()
                        
                        ### copy stocking Type matrix properties
                        for property in existing_product.tblproductproductstockingtypematrix_set.all():
                            property_copy = TblproductProductStockingtypeMatrix(
                                companyid=property.companyid,
                                productid=new_product,
                                stocktypematix=property.stocktypematix,
                                
                            )
                            property_copy.save()

                        ### Copy Vatcode matrix properties
                        for property in existing_product.tblproductproductvatcodematrix_set.all():
                            property_copy = TblproductProductVatcodeMatrix(
                                companyid=property.companyid,
                                productid=new_product,
                                vatcodematix=property.vatcodematix,
                                
                            )
                            property_copy.save()

                        #### Copy Standard Cost Matrix 
                        for property in existing_product.tblproductproductcoststandardmatrix_set.all():
                            property_copy = TblproductProductCostStandardMatrix(
                                companyid=property.companyid,
                                productid=new_product,
                                stdcostmatix=property.stdcostmatix,
                                
                            )
                            property_copy.save()

                        ##### Copy Supplier Cost Matrix
                        # for property in existing_product.tblproductproductcostsuppliermatrix_set.all():
                        #     property_copy = TblproductProductCostSupplierMatrix(
                        #         companyid=property.companyid,
                        #         productid=new_product,
                        #         businessid = property.businessid,
                        #         supcostmatix=property.supcostmatix,
                                
                        #     )
                        #     property_copy.save()

                        ##### Copy Standard Price matrix
                        for property in existing_product.tblproductproductpricestandardmatrix_set.all():
                            property_copy = TblproductProductPriceStandardMatrix(
                                companyid=property.companyid,
                                productid=new_product,
                                stdpricematix=property.stdpricematix,
                                
                            )
                            property_copy.save()

                        
                        #### Copy Customer Price Matrix
                        # for property in existing_product.tblproductproductpricecustomermatrix_set.all():
                        #     property_copy = TblproductProductPriceCustomerMatrix(
                        #         companyid=property.companyid,
                        #         productid=new_product,
                        #         businessid = property.businessid,
                        #         cuspricematix=property.cuspricematix,
                                
                        #     )
                        #     property_copy.save()

                        
                        ### Copy Obsolete Matrix 
                        # for property in existing_product.tblproductproductobsoletematrix_set.all():
                        #     property_copy = TblproductProductObsoleteMatrix(
                        #         companyid=property.companyid,
                        #         productid=new_product,
                        #         obslmatix=property.obslmatix,
                                
                        #     )
                        #     property_copy.save()

                        #### Copy product Reps
                        for rep in existing_product.tblproductproductreps_set.all():
                            rep_copy = TblproductProductReps(
                                companyid=rep.companyid,
                                productid=new_product,
                                repid=rep.repid,
                                seqno=rep.seqno
                            )
                            rep_copy.save()


                        try:
                            product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.get(
                                companyid=company,
                                productid=new_product
                            )
                        except TblproductProductObsoleteMatrix.DoesNotExist:
                            product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.create(
                                companyid=company,
                                productid=new_product,
                                obslmatix = [{"value":0}]
                            )
                            product_obsoletetype_matrix_instance.save()
                            product_obsoletetype_matrix_instance = TblproductProductObsoleteMatrix.objects.get(
                                companyid=company,
                                productid=new_product
                            )
                            product_obsoletetype_matrix_instance.Update_Product_ObsoleteType_Matrix(company=company,
                                                                                                    productid=new_product
                                                                                                    )
                            
                        


                        ### Copy Product Paramerter settings with parameter  set values
                        # for setting in existing_product.tblproductparametertssetvalues_set.all():
                        #     setting_copy = TblproductParametertsSetvalues(
                        #         companyid=setting.companyid,
                        #         settingid=setting.settingid,
                        #         productid=new_product,
                        #         value=setting.value
                        #     )
                        #     setting_copy.save()


                        

                        return E4k_TblProduct_Copy_Existing_Product(success='Success')
                except TblproductProducts.DoesNotExist:
                    return E4k_TblProduct_Copy_Existing_Product(success='Failed: Source Product does not exist')
        except Tblcompany.DoesNotExist:
            return E4k_TblProduct_Copy_Existing_Product(success='Failed: Company does not exist')
        




class Mutation(graphene.ObjectType):
    ############category1 mutation

    E4K_TblProduct_ProductCategory1_Create = E4K_TblProduct_ProductCategory1_Create.Field()
    E4K_TblProduct_ProductCategory1_Update = E4K_TblProduct_ProductCategory1_Update.Field()
    E4K_TblProduct_ProductCategory1_Delete = E4K_TblProduct_ProductCategory1_Delete.Field()

    ############category2 mutation
    E4K_TblProduct_ProductCategory2_Create = E4K_TblProduct_ProductCategory2_Create.Field()
    E4K_TblProduct_ProductCategory2_Update = E4K_TblProduct_ProductCategory2_Update.Field()
    E4k_TblProduct_ProductCategory2_Delete = E4k_TblProduct_ProductCategory2_Delete.Field()

    ############category3 mutation
    E4k_TblProduct_ProductCategory3_Create = E4k_TblProduct_ProductCategory3_Create.Field()
    E4k_TblProduct_ProductCategory3_Update = E4k_TblProduct_ProductCategory3_Update.Field()
    E4k_TblProduct_ProductCategory3_Delete = E4k_TblProduct_ProductCategory3_Delete.Field()

    ############product class mutation
    E4k_TblProduct_ProductClass_Create = E4k_TblProduct_ProductClass_Create.Field()
    E4k_TblProduct_ProductClass_Update = E4k_TblProduct_ProductClass_Update.Field()
    E4k_TblProduct_ProductClass_Delete = E4k_TblProduct_ProductClass_Delete.Field()

    #############Product COlour class mutation
    E4k_TblProduct_ProductColours_Create = E4k_TblProduct_ProductColours_Create.Field()
    E4k_TblProduct_ProductColours_Update = E4k_TblProduct_ProductColours_Update.Field()
    E4k_TblProduct_ProductColours_Delete = E4k_TblProduct_ProductColours_Delete.Field()

    #############Product Fits class mutation
    E4k_TblProduct_ProductFits_Create = E4k_TblProduct_ProductFits_Create.Field()
    E4k_TblProduct_ProductFits_Update = E4k_TblProduct_ProductFits_Update.Field()
    E4k_TblProduct_ProductFits_Delete = E4k_TblProduct_ProductFits_Delete.Field()

    #############Product obsolete Types mutation
    E4k_TblProduct_ProductObsoleteTypes_Create = E4k_TblProduct_ProductObsoleteTypes_Create.Field()
    E4k_TblProduct_ProductObsoleteTypes_Update = E4k_TblProduct_ProductObsoleteTypes_Update.Field()
    E4k_TblProduct_ProductObsoleteTypes_Delete = E4k_TblProduct_ProductObsoleteTypes_Delete.Field()

    #############Product Parameters Settings mutation
    E4k_TblProduct_ProductParameterSettings_Create = E4k_TblProduct_ProductParameterSettings_Create.Field()
    E4k_TblProduct_ProductParameterSettings_Update = E4k_TblProduct_ProductParameterSettings_Update.Field()
    E4k_TblProduct_ProductParameterSettings_Delete = E4k_TblProduct_ProductParameterSettings_Delete.Field()

    ############## product parameters settings mutation
    E4k_TblProduct_ProductPriceTypes_Create = E4k_TblProduct_ProductPriceTypes_Create.Field()
    E4k_TblProduct_ProductPriceTypes_Update = E4k_TblProduct_ProductPriceTypes_Update.Field()
    E4k_TblProduct_ProductPriceTypes_Delete = E4k_TblProduct_ProductPriceTypes_Delete.Field()

    ###################### Tbl_FSK_ProductPropertyTypes_Create
    E4k_TblProduct_ProductPropertyTypes_Create = E4k_TblProduct_ProductPropertyTypes_Create.Field()
    E4k_TblProduct_ProductPropertyTypes_Update = E4k_TblProduct_ProductPropertyTypes_Update.Field()
    E4k_TblProduct_ProductPropertyTypes_Delete = E4k_TblProduct_ProductPropertyTypes_Delete.Field()


    ######################### E4k_Tblproduct_ProductPropertyType_Values_Create
    E4k_Tblproduct_ProductPropertyType_Values_Create = E4k_Tblproduct_ProductPropertyType_Values_Create.Field()
    E4k_Tblproduct_ProductPropertyType_Values_Update = E4k_Tblproduct_ProductPropertyType_Values_Update.Field()
    E4k_TblProduct_ProductPropertyType_Values_Delete = E4k_TblProduct_ProductPropertyType_Values_Delete.Field()

    ############### Tbl_FSK_Product_StockingTypes_ Mutation
    E4k_TblProduct_ProductStockingTypes_Create = E4k_TblProduct_ProductStockingTypes_Create.Field()
    E4k_TblProduct_ProductStockingTypes_Update = E4k_TblProduct_ProductStockingTypes_Update.Field()
    E4k_TblProduct_ProductStockingTypes_Delete = E4k_TblProduct_ProductStockingTypes_Delete.Field()

    ####################### Tbl_Fsk_product_typeof_issue_type Mutation
    E4k_TblProduct_ProductTypeofissue_Create = E4k_TblProduct_ProductTypeofissue_Create.Field()
    E4k_TblProduct_ProductTypeofissue_Update = E4k_TblProduct_ProductTypeofissue_Update.Field()
    E4k_TblProduct_ProductTypeofissue_Delete = E4k_TblProduct_ProductTypeofissue_Delete.Field()

    ########################### Tbl_FSK_Product_Unitofissue Mutations
    E4k_TblProduct_ProductUnitofissue_Create = E4k_TblProduct_ProductUnitofissue_Create.Field()
    E4k_TblProduct_ProductUnitofissue_Update = E4k_TblProduct_ProductUnitofissue_Update.Field()
    E4k_TblProduct_ProductUnitofissue_Delete = E4k_TblProduct_ProductUnitofissue_Delete.Field()

    ############################ E4k_TblProduct_ProductSizeRanges Mutation
    E4k_TblProduct_ProductSizeRanges_Create = E4k_TblProduct_ProductSizeRanges_Create.Field()
    E4k_TblProduct_ProductSizeRanges_Update = E4k_TblProduct_ProductSizeRanges_Update.Field()
    E4k_TblProduct_ProductSizeRanges_Delete = E4k_TblProduct_ProductSizeRanges_Delete.Field()

    ################################# E4k_TblProduct_ProductSizeRanges_Create1 for one by one create
    E4k_TblProduct_ProductSizeRangesValues_Create = E4k_TblProduct_ProductSizeRangeValues_Create.Field()
    E4k_TblProduct_ProductSizeRangesValues_Update = E4k_TblProduct_ProductSizeRangeValues_Update.Field()
    E4k_TblProduct_ProductSizeRangesValues_Delete = E4k_TblProduct_ProductSizeRangeValues_Delete.Field()
    E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update = E4k_TblProduct_ProductSizeRangeValuesSizeValue_Update.Field()

    ################################## Product size ranges value  bulk create
    E4k_TblProduct_ProductSizeRangesValues_Bulk_Create = E4k_TblProduct_ProductSizeRangesValues_Bulk_Create.Field()
    E4k_TblProduct_ProductSizeRangesValues_Bulk_Update = E4k_TblProduct_ProductSizeRangesValues_Bulk_Update.Field()
    E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete = E4k_TblProduct_ProductSizeRangesValues_Bulk_Delete.Field()


    ############################ E4k_TblProduct_CommodityCodes Mutation
    E4k_TblProduct_CommodityCodes_Create = E4k_TblProduct_CommodityCodes_Create.Field()
    E4k_TblProduct_CommodityCodes_Update = E4k_TblProduct_CommodityCodes_Update.Field()
    E4k_TblProduct_CommodityCodes_Delete = E4k_TblProduct_CommodityCodes_Delete.Field()

    ############################# E4k_TblProduct_Product Mutation
    E4k_TblProduct_Product_Create = E4k_TblProduct_Product_Create.Field()
    E4k_TblProduct_Product_Update = E4k_TblProduct_Product_Update.Field()
    E4k_TblProduct_Product_Delete = E4k_TblProduct_Product_Delete.Field()

    ################################ E4k_TblProduct_Parameterssetvalues Mutation
    E4k_TblProduct_Parameterssetvalues_Create = E4k_Tblproduct_ParametertsSetvalues_Create.Field()
    E4k_TblProduct_Parameterssetvalues_Update = E4k_Tblproduct_ParametertsSetvalues_Update.Field()
    E4k_TblProduct_Parameterssetvalues_Delete = E4k_Tblproduct_ParametertsSetvalues_Delete.Field()


    ######################################## E4k_Tblproduct_ParametertsCustomersSetvalues_Update
    E4k_Tblproduct_ParametertsCustomersSetvalues_Update = E4k_Tblproduct_ParametertsCustomersSetvalues_Update.Field()
    
    ######################################## E4k_Tblproduct_ProductGallery Mutation
    E4k_Tblproduct_ProductGallery_Create = E4k_Tblproduct_ProductGallery_Create.Field()
    E4k_Tblproduct_ProductGallery_Update = E4k_Tblproduct_ProductGallery_Update.Field()
    E4k_Tblproduct_ProductGallery_Delete = E4k_Tblproduct_ProductGallery_Delete.Field()

    ######################################## E4k_Tblproduct_ProductProperties  Mutation
    E4k_Tblproduct_ProductProperties_Create = E4k_Tblproduct_ProductProperties_Create.Field()
    E4k_Tblproduct_ProductProperties_Update = E4k_Tblproduct_ProductProperties_Update.Field()
    E4k_Tblproduct_ProductProperties_Delete = E4k_Tblproduct_ProductProperties_Delete.Field()

    ######################################## E4k_Tblproduct_ProductProperties_Values Mutation
    E4k_Tblproduct_ProductProperties_Values_Create = E4k_Tblproduct_ProductProperties_Values_Create.Field()
    E4k_Tblproduct_ProductProperties_Values_Update = E4k_Tblproduct_ProductProperties_Values_Update.Field()
    E4k_Tblproduct_ProductProperties_Values_Delete = E4k_Tblproduct_ProductProperties_Values_Delete.Field()

    ########################################## E4k_TblproductProductReps Mutation
    E4k_Tblproduct_ProductReps_Create = E4k_Tblproduct_ProductReps_Create.Field()
    E4k_Tblproduct_ProductReps_Update = E4k_Tblproduct_ProductReps_Update.Field()
    E4k_Tblproduct_ProductReps_Delete = E4k_Tblproduct_ProductReps_Delete.Field()

    ########################################## E4k_TblproductProductPropertyLevel Mutation
    E4k_Tblproduct_ProductPropertyLevel_Create = E4k_Tblproduct_ProductPropertyLevel_Create.Field()
    E4k_Tblproduct_ProductPropertyLevel_Update = E4k_Tblproduct_ProductPropertyLevel_Update.Field()
    E4k_Tblproduct_ProductPropertyLevel_Delete = E4k_Tblproduct_ProductPropertyLevel_Delete.Field()

    ########################################## E4k_Tblproduct_ProductSuppliers Mutation
    E4k_Tblproduct_ProductSuppliers_Create = E4k_Tblproduct_ProductSuppliers_Create.Field()


    ########################################## E4k_Tblproduct_ProductStockinglevelMatrix Mutation
    E4k_Tblproduct_ProductStockinglevelMatrix_Create = E4k_Tblproduct_ProductStockinglevelMatrix_Create.Field()
    E4k_Tblproduct_ProductStockinglevelMatrix_Update = E4k_Tblproduct_ProductStockinglevelMatrix_Update.Field()

    ########################################## E4k_Tblproduct_ProductStockingtypeMatrix Mutation
    E4k_Tblproduct_ProductStockingtypeMatrix_Create = E4k_Tblproduct_ProductStockingtypeMatrix_Create.Field()
    E4k_Tblproduct_ProductStockingtypeMatrix_Update = E4k_Tblproduct_ProductStockingtypeMatrix_Update.Field()

    ########################################## E4k_Tblproduct_ProductObsoletetypeMatrix Mutation
    E4k_Tblproduct_ProductObsoletetypeMatrix_Create = E4k_Tblproduct_ProductObsoletetypeMatrix_Create.Field()
    E4k_Tblproduct_ProductObsoletetypeMatrix_Update = E4k_Tblproduct_ProductObsoletetypeMatrix_Update.Field()

    ########################################## E4k_Tblproduct_ProductCostStandardMatrix Mutation
    E4k_Tblproduct_ProductCostStandardMatrix_Create = E4k_Tblproduct_ProductCostStandardMatrix_Create.Field()
    E4k_Tblproduct_ProductCostStandardMatrix_Update = E4k_Tblproduct_ProductCostStandardMatrix_Update.Field()

    ########################################## E4k_Tblproduct_ProductCostSupplierMatrix Mutation
    E4k_Tblproduct_ProductCostSupplierMatrix_Create = E4k_Tblproduct_ProductCostSupplierMatrix_Create.Field()
    E4k_Tblproduct_ProductCostSupplierMatrix_Update = E4k_Tblproduct_ProductCostSupplierMatrix_Update.Field()

    ############################################# E4k_Tblproduct_ProductPriceCustomerMatrix Mutation
    E4k_Tblproduct_ProductPriceCustomerMatrix_Create = E4k_Tblproduct_ProductPriceCustomerMatrix_Create.Field()
    E4k_Tblproduct_ProductPriceCustomerMatrix_Update = E4k_Tblproduct_ProductPriceCustomerMatrix_Update.Field()

    ############################################## E4k_Tblproduct_ProductPriceStandardMatrix Mutation
    E4k_Tblproduct_ProductPriceStandardMatrix_Create = E4k_Tblproduct_ProductPriceStandardMatrix_Create.Field()
    E4k_Tblproduct_ProductPriceStandardMatrix_Update = E4k_Tblproduct_ProductPriceStandardMatrix_Update.Field()
    
    ############################################## E4k_Tblproduct_ProductPriceStandardDateMatrix_Create
    E4k_Tblproduct_ProductPriceStandardDateMatrix_Create = E4k_Tblproduct_ProductPriceStandardDateMatrix_Create.Field()
    E4k_Tblproduct_ProductPriceStandardDateMatrix_Update = E4k_Tblproduct_ProductPriceStandardDateMatrix_Update.Field()
    E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete = E4k_Tblproduct_ProductPriceStandarDateMatrix_Delete.Field()


    #################################################### E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create
    E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create = E4k_Tblproduct_ProductPriceStandarQtyMatrix_Create.Field()
    E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update = E4k_Tblproduct_ProductPriceStandardQtyMatrix_Update.Field()
    E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete = E4k_Tblproduct_ProductPriceStandarQtyMatrix_Delete.Field()

    ############################################## E4k_Tblproduct_ProductVatcodeMatrix Mutation
    E4k_Tblproduct_ProductVatcodeMatrix_Create = E4k_Tblproduct_ProductVatcodeMatrix_Create.Field()
    E4k_Tblproduct_ProductVatcodeMatrix_Update = E4k_Tblproduct_ProductVatcodeMatrix_Update.Field()

    ############################################### E4k_Tblproduct_ProductSuppliersWeekdays Mutation
    E4k_Tblproduct_ProductSuppliersWeekdays_Create = E4k_Tblproduct_ProductSuppliersWeekdays_Create.Field()
    E4k_Tblproduct_ProductSuppliersWeekdays_Update = E4k_Tblproduct_ProductSuppliersWeekdays_Update.Field()
    E4k_Tblproduct_ProductSuppliersWeekdays_Delete = E4k_Tblproduct_ProductSuppliersWeekdays_Delete.Field()

    #################################################### E4k SUpplier Level and Matrix relate Mutation
    E4k_Tblproduct_ProductSupplierLevel_Create = E4k_Tblproduct_ProductSupplierLevel_Create.Field()
    E4k_Tblproduct_ProductSupplierLevel_Update = E4k_Tblproduct_ProductSupplierLevel_Update.Field()
    E4k_Tblproduct_ProductSupplierLevel_Delete = E4k_Tblproduct_ProductSupplierLevel_Delete.Field()

    ########################################## E4k_Tblproduct_ProductSupplierMatrix_Update
    E4k_Tblproduct_ProductSupplierMatrix_Update = E4k_Tblproduct_ProductSupplierMatrix_Update.Field()




    FSKAll_Product_Property_Matrix = TblFSK_All_Product_Property_Matrix.Field()
    FSKAll_Product_Property_Level_Matrix = Tbl_FSK_ProductPropertyLevel.Field()
    E4k_TblProduct_Product_image_update = E4k_TblProduct_Products_image_update_code.Field()
    All_Tblproduct_ProductObsoletetypeMatrix_Create =AllE4k_Tblproduct_ProductObsoletetypeMatrix_Create.Field()

    ###### AllE4k_Tblproduct_ProductSupplierColMatrix_Create 
    AllE4k_Tblproduct_ProductSupplierColMatrix_Create =AllE4k_Tblproduct_ProductSupplierColMatrix_Create.Field()
    AllE4k_TblSuppliermatixupdateCheck = AllE4k_TblSuppliermatixupdateCheck.Field()



    ####### Duplicate the Product 
    E4k_TblProduct_Copy_Existing_Product = E4k_TblProduct_Copy_Existing_Product.Field()