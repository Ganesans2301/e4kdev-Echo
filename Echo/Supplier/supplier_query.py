import graphene
from Customer.models import (Tblcompany,TblbusContactRef)
from .models import (Tblsupplier,TblbusContactRef,TblsupplierAccount,
                     TblsupplierMemo, TblsupplierBalance, TblsupplierTurnover,TblwhoWarehouses,
                       TblsupplierAddress,TblwhoWarehousesTypes,TblsupplierNotes,TblsupplierCategory1,
                       TblsupplierCategory2,TblsupplierCategory3,TblsupplierClass,
                       TblsupplierContact,TblsupplierSettings,
                       TblsupplierSetvalues)
from .supplier_schema import (TblsupplierCategory1Type,Tblsuppliercategory2Type,TblsupplierCategory3Type,
                              TblsupplierClassType,TblsupplierContactType,TblsupplierType,
                              TblsupplierMemoType, TblsupplierBalanceType, TblsupplierTurnoverType, 
                              TblsupplierAddressType, TblsupplierNotesType, TblsupplierContactType, 
                              TblsupplierTurnoverType,TblwhoWarehousesTypesType,TblwhoWarehousesType,
                                TblsupplierAccountType,TblbusContactRefType)
from django.db import connection

from graphql import GraphQLError
from decimal import Decimal

class Supplier:
    @staticmethod
    def resolve_E4k_TblSupplierList(companyid):
        try:
            with connection.cursor() as cursor:
                
                query = """
                 SELECT 
                    c.CompanyID, 
                    c.BusinessID, 
                    c.Name AS CustomerName, 
                    c.CountryID, 
                    c.IsLive, 
                    cat1.Category1Name AS Category1Name, 
                    cat2.Category2Name AS Category2Name, 
                    cat3.Category3Name AS Category3Name, 
                    cl.Class_Name AS ClassName, 
                    N.NomDescription AS NominalDescription,
                    c.IsExtract, 
                    c.IsStop,
                    country.Country,
                    csv.Value
                    
                FROM 
                    tblsupplier c
                LEFT JOIN 
                    tblsupplier_category1 cat1 ON c.Category1ID = cat1.Category1ID
                LEFT JOIN 
                    tblsupplier_category2 cat2 ON c.Category2ID = cat2.Category2ID
                LEFT JOIN 
                    tblsupplier_category3 cat3 ON c.Category3ID = cat3.Category3ID
                LEFT JOIN 
                    tblsupplier_class cl ON c.ClassID = cl.ClassID
                LEFT JOIN 
                    tblbus_countries country ON c.CountryID = country.CountryID
               
                LEFT JOIN 
                    tblacc_nominal N ON c.Default_Nominal = N.NomCode
                LEFT JOIN 
                    tblsupplier_setvalues csv ON c.BusinessID = csv.BusinessID AND csv.SettingID = 'LOGO'
    
                WHERE 
                    c.CompanyID = %s
                """
                cursor.execute(query, [companyid])
                result = cursor.fetchall()

                # Extract column names
                columns = [col[0] for col in cursor.description]

                # Convert the result to a list of dictionaries
                result_dicts = [dict(zip(columns, row)) for row in result]
                
                for row in result_dicts:
                    row['IsStop'] = True if row['IsStop'] == 1 else False
                    row['IsExtract'] = True if row['IsExtract'] == 1 else False
                    row['IsLive'] = True if row['IsLive'] == 1 else False
                   
                return result_dicts  
                 
              
               
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
class TotalAccount:
    @staticmethod
    def get_address_counts(businessid, companyid):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        t3.`CompanyID`,
                        t3.`AddressTypeID`, 
                        IF(ISNULL(t1.AddressCount), 0, t1.AddressCount) AS AddressCount,
                        t3.`Description`,
                        IF(ISNULL(t1.CtCount), 0, t1.CtCount) AS CtCount
                    FROM 
                        `tblbus_addresstypes` t3
                    LEFT JOIN (
                        SELECT 
                            q1.CompanyID,
                            q1.AddressTypeID,
                            COUNT(DISTINCT q1.AddressID) AS AddressCount,
                            IF(ISNULL(SUM(t2.ct)), 0, SUM(t2.ct)) AS CtCount
                        FROM 
                            `tblsupplier_address` q1
                        LEFT JOIN (
                            SELECT 
                                CompanyID, 
                                AddressID, 
                                COUNT(`AddressID`) AS ct
                            FROM 
                                `tblsupplier_contact`
                            GROUP BY 
                                CompanyID, 
                                AddressID
                        ) t2 
                        ON 
                            q1.CompanyID = t2.CompanyID 
                            AND q1.AddressID = t2.AddressID
                        WHERE 
                            q1.`BusinessID` = %s
                        GROUP BY 
                            q1.CompanyID, 
                            q1.AddressTypeID
                    ) t1 
                    ON 
                        t3.`CompanyID` = t1.`CompanyID` 
                        AND t3.`AddressTypeID` = t1.`AddressTypeID`
                    WHERE 
                        t3.`CompanyID` = %s
                        AND t3.IsSupplier='1'
                    GROUP BY 
                        t3.`CompanyID`, 
                        t3.`AddressTypeID`,
                        t3.`Description`
                    ORDER BY 
                        t3.`AddressTypeID`;
                """, [businessid, companyid])
                
                rows = cursor.fetchall()
                print("AddressCount data:", rows)
                
                # Processing the result rows into a list of dictionaries
                results = []
                for row in rows:
                    result = {
                        "companyId": row[0],
                        "addressTypeId": row[1],
                        "addressCount": int(row[2]),  # Ensure integer conversion
                        "description": row[3],
                        "ctCount": float(row[4]) if isinstance(row[4], Decimal) else row[4]  # Convert Decimal to float if necessary
                    }
                    results.append(result)
                
                return results

        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
class SupplierContact:
    @staticmethod
    def get_contact_details(businessid, addresstypeid,companyid):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                 SELECT 
                    cc.CompanyID,
                    t1.Name,
                    cc.Value,
                    cc.ID,
                    cc.ContactType_ID,
                    cc.AddressID,
                    addr.Description,
                    addr.Address1,
                    addr.Address2,
                    addr.Address3,
                    addr.City,
                    addr.County,
                    countries.Country,
                    addr.Postcode,
                    addr.AddressTypeID,
                    addr.BusinessID
                FROM 
                    tblsupplier_contact cc
                JOIN 
                    tblbus_contact_ref t1 
                    ON cc.CompanyID = t1.CompanyID 
                    AND cc.ContactType_ID = t1.ContactType_ID
                JOIN 
                    tblsupplier_address addr 
                    ON cc.CompanyID = addr.CompanyID 
                    AND cc.AddressID = addr.AddressID
                JOIN
                    tblbus_countries countries 
                    ON addr.CountryCode = countries.CountryID 
                WHERE 
                    addr.BusinessID = %s
                    AND addr.AddressTypeID = %s
                    AND addr.CompanyID = %s;


                """, [businessid, addresstypeid , companyid])
                
                rows = cursor.fetchall()
                print("Contact details data:", rows)
                
                results = []
                for row in rows:
                    result = {
                        "companyId": row[0],
                        "name": row[1],
                        "value": row[2],
                        "ID": row[3],
                        "contactTypeId": row[4],
                        "addressId": row[5],
                        "description": row[6],
                        "address1": row[7],
                        "address2": row[8],
                        "address3": row[9],
                        "city": row[10],
                        "county": row[11],
                        "country": row[12],
                        "postcode": row[13],
                        "addressTypeId": row[14],
                        "BusinessID" : row[15],
                        
                    }
                    results.append(result)
                
                return results

        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
class SupplierTurnover:
    def resolve_E4k_Get_SupplierTurnOver(self, info, businessid):
        query = """
        SELECT SUM(`Turnover`)
        FROM tblcustomer_turnover
        WHERE `CompanyID` = '001' AND `BusinessID` = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [businessid])
            result = cursor.fetchone()

        return result[0] if result and result[0] is not None else 0

        


class SupplierQuery(graphene.ObjectType):

    # E4k_TblsupplierCategory1list = graphene.List(TblsupplierCategory1Type)
    E4k_TblsupplierCategory1 = graphene.List(TblsupplierCategory1Type, companyid=graphene.String())

    # E4k_TblsupplierCategory2list = graphene.List(Tblsuppliercategory2Type)
    E4k_TblsupplierCategory2 = graphene.List(Tblsuppliercategory2Type, companyid=graphene.String())

    # E4k_TblsupplierCategory3list = graphene.List(TblsupplierCategory3Type)
    E4k_TblsupplierCategory3 = graphene.List(TblsupplierCategory3Type, companyid=graphene.String())

    # E4k_TblsupplierClasslist = graphene.List(TblsupplierClassType)
    E4k_TblsupplierClass = graphene.List(TblsupplierClassType, companyid=graphene.String())

    E4k_SupplierContact = graphene.List(TblsupplierContactType, companyid = graphene.String(), addressid = graphene.String())
    E4k_TblsupplierContact = graphene.List(TblsupplierContactType, companyid=graphene.String())

    E4k_Tblsupplierlist = graphene.List(TblsupplierType)
    E4k_Tblsupplier = graphene.List(TblsupplierType,companyid =graphene.String(),  businessid=graphene.String())

    E4k_TblsupplierNoteslist = graphene.List(TblsupplierNotesType)
    E4k_TblsupplierNotes = graphene.List(TblsupplierNotesType, companyid=graphene.String(), businessid=graphene.String())

    E4k_TblsupplierAddresslist = graphene.List(TblsupplierAddressType)
    E4k_TblsupplierAddress = graphene.List(TblsupplierAddressType, businessid = graphene.String() , companyid= graphene.String() , addresstypeid= graphene.String(),addressid = graphene.String())


    E4k_TblwhoWarehousesTypeslist = graphene.List(TblwhoWarehousesTypesType)
    E4k_TblwhoWarehousesTypes= graphene.Field(TblwhoWarehousesTypesType,whtypeid= graphene.Int())

    E4k_TblsupplierMemolist = graphene.List(TblsupplierMemoType)    
    E4k_TblsupplierMemo = graphene.Field(TblsupplierMemoType, businessid = graphene.Int())

    E4k_TblsupplierTurnoverlist = graphene.List(TblsupplierTurnoverType)
    E4k_TblsupplierTurnover = graphene.Field(TblsupplierTurnoverType, businessid = graphene.Int())

    E4k_TblwhoWarehouseslist = graphene.List(TblwhoWarehousesType)
    E4k_TblwhoWarehouses = graphene.Field(TblwhoWarehousesType, warehouseid = graphene.String())

    E4k_TblsupplierBalancelist = graphene.List(TblsupplierBalanceType)
    E4k_TblsupplierBalance = graphene.Field(TblsupplierBalanceType,businessid = graphene.String())  

    # E4k_TblsupplierAccountlist = graphene.List(TblsupplierAccountType)
    E4k_TblsupplierAccount = graphene.List(TblsupplierAccountType, companyid = graphene.String(),businessid = graphene.String()) 

    E4k_TblSuppliertList = graphene.List(of_type=graphene.JSONString, companyid=graphene.String(required=True))

    E4k_supplieraddresscounts = graphene.List(of_type=graphene.JSONString ,companyid= graphene.String(required =True), businessid=graphene.String(required=True))
    E4k_TblbusContactRef = graphene.List(TblbusContactRefType, companyid = graphene.String())

    E4k_GetSupplierContactList =graphene.List(of_type = graphene.JSONString, addresstypeid = graphene.String(), companyid = graphene.String(), businessid = graphene.String())
    E4k_TblSuppliersettings = graphene.List(of_type=graphene.JSONString,businessid=graphene.String(),companyid = graphene.String(),settingid=graphene.String())


    E4k_SearchSupplierBusinessid = graphene.String(companyid =  graphene.String() , businessid =  graphene.String())
    E4k_totalturnoverSupplier = graphene.Float(companyid = graphene.String(), businessid = graphene.String())









 ################################## Supplier List get function ################
  
  
    def resolve_E4k_TblSuppliertList(self, info, companyid):
        return Supplier.resolve_E4k_TblSupplierList(companyid=companyid)



    # def resolve_E4k_TblsupplierCategory1list(self,info,*kwargs):
    
    #     return TblsupplierCategory1.objects.all()
    
    def resolve_E4k_TblsupplierCategory1(self, info, companyid=None, *kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblsupplierCategory1.objects.filter(companyid=company)
            else:
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            # if companyid:
            #     if not Tblsupplier.objects.filter(companyid=companyid).exists():
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            #     return TblsupplierCategory1.objects.filter(companyid=companyid)
            # else:
            #     return TblsupplierCategory1.objects.all()
        except TblsupplierCategory1.DoesNotExist:
            raise GraphQLError(f"Supplier Category for Company ID '{companyid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")

        
                 
                


    
    def resolve_E4k_TblsupplierCategory2(self,info,companyid,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblsupplierCategory2.objects.filter(companyid=company)
            else:
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            # if companyid:
            #     if not Tblsupplier.objects.filter(companyid=companyid).exists():
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            #     return TblsupplierCategory2.objects.filter(companyid=companyid)
            # else:
            #     return TblsupplierCategory2.objects.all()
        except TblsupplierCategory2.DoesNotExist:
            raise  GraphQLError(f"Supplier Category for Company ID '{companyid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")
        
                
     
    def resolve_E4k_TblsupplierCategory3(self,info,companyid,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblsupplierCategory3.objects.filter(companyid=company)
            else:
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
            # if companyid:
            #     if not Tblsupplier.objects.filter(companyid=companyid).exists():
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            #     return TblsupplierCategory3.objects.filter(companyid=companyid)
            # else :
            #     return TblsupplierCategory3.objects.all()
        except TblsupplierCategory3.DoesNotExist:
            raise GraphQLError(f"Supplier Category for Company ID '{companyid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")
      
    
    def resolve_E4k_TblsupplierClass(self,info,companyid,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblsupplierClass.objects.filter(companyid=company)
            else:
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
            # if companyid :
            #     if not Tblsupplier.objects.filter(companyid=companyid).exists():
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            #     return TblsupplierClass.objects.filter(companyid=companyid)
            # else:
            #     return TblsupplierClass.objects.all()
        except TblsupplierClass.DoesNotExist:
            raise GraphQLError(f"Supplier Class for Company ID '{companyid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")
        
      
    def resolve_E4k_TblsupplierContact(self,info,companyid,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblsupplierContact.objects.filter(companyid=company)
            else:
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
            # if companyid:
            #     if Tblsupplier.objects.filter(companyid=companyid).exists():
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            #     else:
            #         return TblsupplierContact.objects.filter(companyid=companyid)
            # else:
            #     return TblsupplierContact.objects.all()
        except TblsupplierContact.DoesNotExist:
            raise GraphQLError(f"Supplier Contact for Company ID '{companyid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")
        
        
    def resolve_E4k_SupplierContact(self,info,companyid,addressid,*kwargs):
        try:
          
            
            if companyid and addressid:
                if not Tblsupplier.objects.filter(companyid=companyid).exists():
                    raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                return TblsupplierContact.objects.filter(companyid=companyid, addressid=addressid)
            else:
                return TblsupplierContact.objects.all()
        except TblsupplierContact.DoesNotExist:
            raise GraphQLError(f"Supplier Contact with Company ID '{companyid}' and Address ID '{addressid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")
        
    
    
    # def resolve_E4k_Tblsupplierlist(self,info,*kwargs):
    #     return Tblsupplier.objects.all()
    def resolve_E4k_Tblsupplier(self,info,businessid,companyid,*kwargs):
        try:
            return Tblsupplier.objects.filter(businessid =businessid , companyid = companyid)
        except Tblsupplier.DoesNotExist:
            return None

    
   
    def resolve_E4k_TblsupplierNotes(self,info,companyid,businessid,*kwargs):
        try:
            companyid = Tblcompany.objects.get(companyid = companyid)
            if businessid !='':
                return TblsupplierNotes.objects.filter(companyid = companyid , businessid = businessid)
            else:
                return TblsupplierNotes.objects.filter(companyid = companyid)
        except Tblsupplier.DoesNotExist:
            raise GraphQLError("supplier does not exist")
        except Tblcompany.DoesNotExist:
            raise GraphQLError("Company does not exist")
        except Exception as e:
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")
        
                
        #     return TblsupplierNotes.objects.get(pk =noteid)
        # except TblsupplierNotes.DoesNotExist:
        #     return None
 
    def  resolve_E4k_TblsupplierAddresslist(self,info,*kwargs):
        return TblsupplierAddress.objects.all()
            
    def resolve_E4k_TblsupplierAddress(self, info, addressid, businessid, addresstypeid, companyid, *kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if addressid:
                return TblsupplierAddress.objects.filter(companyid=company, addressid=addressid, businessid=businessid)
            else:
                return TblsupplierAddress.objects.filter(companyid=company, businessid=businessid, addresstypeid=addresstypeid)
        except TblsupplierAddress.DoesNotExist:
            return None

                

        #     return TblsupplierAddress.objects.get(pk =addressid)
        # except TblsupplierAddress.DoesNotExist:
        #     return None


    def resolve_E4k_TblwhoWarehousesTypeslist(self,info,*kwargs):
        return TblwhoWarehousesTypes.objects.all()
    def resolve_E4k_TblwhoWarehousesTypes(self,info,whtypeid,*kwargs):
        try:
            return TblwhoWarehousesTypes.objects.get(pk =whtypeid)
        except TblwhoWarehousesTypes.DoesNotExist:
            return None
        
    

    def resolve_E4k_TblsupplierMemo(self,info,*kwargs):
        return TblsupplierMemo.objects.all()
    def resolve_E4k_TblsupplierMemo(self,info,businessid,*kwargs):
        try:
            return TblsupplierMemo.objects.get(pk = businessid)
        except TblsupplierMemo.DoesNotExist:
            return None
    

    def resolve_E4k_TblsupplierTurnoverlist(self,info,*kwargs):
        return TblsupplierTurnover.objects.all()
    def resolve_E4k_TblsupplierTurnover(self,info,businessid,*kwargs):
        try:
            return TblsupplierTurnover.objects.get(pk = businessid)
        except TblsupplierTurnover.DoesNotExist:
            return None


    def resolve_E4k_TblwhoWarehouseslist(self,info,*kwargs):
        return TblwhoWarehouses.objects.all()       
    
    def resolve_E4k_TblwhoWarehouses(self,info,warehouseid,*kwargs):
        try:
            return TblwhoWarehouses.objects.get(pk =warehouseid)
        except TblwhoWarehouses.DoesNotExist:
            return None


    def resolve_E4k_TblsupplierBalancelist(self,info,*kwargs):
        return TblsupplierBalance.objects.all()
    def resolve_E4k_TblsupplierBalance(self,info,businessid,*kwargs):
        try:
            return TblsupplierBalance.objects.get(pk =businessid)
        except TblsupplierBalance.DoesNotExist:
            return None


    # def resolve_E4k_TblsupplierAccountlist(self,info,*kwargs):
    #     return TblsupplierAccount.objects.all()
    

    def resolve_E4k_TblsupplierAccount(self,info,businessid,companyid,*kwargs):
        try:
            companyid = Tblcompany.objects.get(companyid=companyid)
            if businessid !='':
                return TblsupplierAccount.objects.filter(companyid = companyid , businessid = businessid)
            # else :
            #     return TblsupplierAccount.objects.filter(companyid = companyid)
            

        except TblsupplierAccount.DoesNotExist:
            return 'Tblaccount does not exist'
        except Tblcompany.DoesNotExist:
            return 'Company does not exist'
        
        
        
        #     return TblsupplierAccount.objects.get(pk =businessid)
        # except TblsupplierAccount.DoesNotExist:
        #     return None
    def resolve_E4k_supplieraddresscounts(self, info, companyid,businessid):
        return TotalAccount.get_address_counts(companyid=companyid,businessid=businessid)
    
    #################################### bustable ######################################################
    
    def resolve_E4k_TblbusContactRef(self,info,companyid,*kwargs):
        try:
            if companyid :
                try:
                    Tblcompany.objects.get(companyid=companyid)
                except Tblcompany.DoesNotExist:
                    raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                
                return TblbusContactRef.objects.filter(companyid=companyid)
            else :
                return TblbusContactRef.objects.all()
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        
    
    def resolve_E4k_GetSupplierContactList (self, info,businessid , addresstypeid,companyid, *kwargs):
        return SupplierContact.get_contact_details(businessid= businessid , addresstypeid= addresstypeid, companyid=companyid)
            
        
    @staticmethod
    def resolve_E4k_TblSuppliersettings(self, info, companyid, businessid, settingid):
        try:
            companyid = Tblcompany.objects.get(companyid=companyid)
            Lookup = [] 
            if businessid != '':
             
                try: 
                    businessid  = Tblsupplier.objects.get(companyid=companyid , businessid=businessid )
                    if settingid != '':
                        try: 
                            return TblsupplierSettings.objects.get(settingid=settingid, companyid=companyid)
                        except TblsupplierSettings.DoesNotExist:
                            return "CustomerSettings Not Found" 
                    else :
                        Lookup_table = TblsupplierSettings.objects.filter(companyid=companyid).order_by('category' ,'seqno')
                       
                        
                        for table in Lookup_table:
                          
                            if table.settingid:
                                settings = TblsupplierSettings.objects.get(settingid=table.settingid , companyid=companyid)
                                Lookup_query =settings.lookup_table  
                                
                                try:
                                    customersetvalues = TblsupplierSetvalues.objects.get(settingid=settings, companyid=companyid ,businessid=businessid ) 
                                    
                                    if not Lookup_query:
                                        if not customersetvalues:
                                            Lookup.append({
                                                   'settingid': table.settingid,
                                                    'SettingName': table.settingname1,
                                                    'Type': table.type,
                                                    'lookup_text': None,
                                                    'Lookup_Table': Lookup_query,
                                                    'category' : table.category,
                                                    'Default': table.default,
                                                    'system_default': table.default,
                                                    'seqno': table.seqno
                                            })
                                        else :
                                            table.lookup_text= customersetvalues.value
                                            Lookup.append({
                                                    'settingid': table.settingid,
                                                    'SettingName': table.settingname1,
                                                    'Type': table.type,
                                                    'lookup_text': None,
                                                    'Lookup_Table': Lookup_query,
                                                    'Default': customersetvalues.value,
                                                    'system_default': table.default,
                                                    'category' : table.category,
                                                    'seqno': table.seqno
                                                })
                                    else :
                                       
                                        if Lookup_query:
                                            with connection.cursor() as cursor:
                                                cursor.execute(Lookup_query)
                                                rows = cursor.fetchall()
                                                print("reer" , rows)
                                            result = [row[0] for row in rows]   
                                            table.lookup_text = result
                                            print("Lookup", result)
                                            
                                            if not customersetvalues.value:     
                                                Lookup.append({
                                                    'settingid': table.settingid,
                                                    'SettingName': table.settingname1,
                                                    'Type': table.type,
                                                    'lookup_text': result,
                                                    'Lookup_Table': Lookup_query,
                                                    'Default': table.default,
                                                    'system_default': table.default,
                                                    'category' : table.category,
                                                    'seqno': table.seqno
        
                                                })
                                                
                                            else :
                                                table.lookup_text= customersetvalues.value
                                                Lookup.append({
                                                    'settingid': table.settingid,
                                                    'SettingName': table.settingname1,
                                                    'Type': table.type,
                                                    'lookup_text': result,
                                                    'Lookup_Table': Lookup_query,
                                                    'Default': customersetvalues.value,
                                                    'system_default': table.default,
                                                    'category' : table.category,
                                                    'seqno': table.seqno
                                                })
                                        else:
                                            
                                             Lookup.append({
                                                    'settingid': table.settingid,
                                                    'SettingName': table.settingname1,
                                                    'Type': table.type,
                                                    'lookup_text': result,
                                                    'Lookup_Table': Lookup_query,
                                                    'Default':customersetvalues.value,
                                                    'system_default': table.default,
                                                    'category' : table.category,
                                                    'seqno': table.seqno
        
                                                })
                                                
                                            
                                    
                                             
                                except TblsupplierSetvalues.DoesNotExist:
                                    if not Lookup_query:
                                        table.lookup_text = None
                                        Lookup.append({
                                                 'settingid': table.settingid,
                                                  'SettingName': table.settingname1,
                                                  'Type': table.type,
                                                  'lookup_text': table.lookup_text,
                                                  'Lookup_Table': Lookup_query,
                                                  'Default': table.default,
                                                  'system_default': table.default,
                                                  'category' : table.category,
                                                  'seqno': table.seqno
                                        })
                                        
                                    else:
                                        
                                        # if "tble4KStrValues" in Lookup_query:
                                            with connection.cursor() as cursor:
                                                cursor.execute(Lookup_query)
                                                rows = cursor.fetchall()
                                            
                                            result = [row[0] for row in rows]
                                            table.lookup_text = result
                                            Lookup.append({
                                                    'settingid': table.settingid,
                                                    'SettingName': table.settingname1,
                                                    'Type': table.type,
                                                    'lookup_text': result,
                                                    'Lookup_Table': Lookup_query,
                                                    'Default': table.default,
                                                    'system_default': table.default,
                                                    'category' : table.category,
                                                    'seqno': table.seqno
                                                })
                except Tblsupplier.DoesNotExist:
                    return "Business Not Found"   
                
            else:
                if settingid !='':
                    try:
                        TblsupplierSettings.objects.get(companyid = companyid , settingid =settingid)
                    
                    except TblsupplierSettings.DoesNotExist:
                        return "CustomerSettings Not Found"
                else:
                    Lookup_table = TblsupplierSettings.objects.filter(companyid=companyid).order_by('category' , 'seqno')
                    for table in Lookup_table:
                        if table.settingid :
                            settings = TblsupplierSettings.objects.get(settingid=table.settingid , companyid=companyid)
                            Lookup_query = settings.lookup_table
                            
                            if not Lookup_query:
                                table.lookup_text = None
                                Lookup.append({
                                              'settingid': table.settingid,
                                               'SettingName': table.settingname1,
                                               'Type': table.type,
                                               'lookup_text': table.lookup_text,
                                               'Lookup_Table': Lookup_query,
                                               'Default': table.default,
                                               'system_default': table.default,
                                               'category' : table.category,
                                               'seqno': table.seqno
                                     })
                            else:
                                with connection.cursor() as cursor:
                                     cursor.execute(Lookup_query)
                                     rows = cursor.fetchall()
                                     result = [row[0] for row in rows]
                                     table.lookup_text = result
                                     Lookup.append({
                                              'settingid': table.settingid,
                                               'SettingName': table.settingname1,
                                               'Type': table.type,
                                               'lookup_text': result,
                                               'Lookup_Table': Lookup_query,
                                               'Default': table.default,
                                               'system_default': table.default,
                                               'category' : table.category,
                                               'seqno': table.seqno
                                              })
                                                                   
            return Lookup                
        except Tblcompany.DoesNotExist:
            return (f"Company id '{companyid}' not found.")

    @staticmethod
    def resolve_E4k_SearchSupplierBusinessid( self, info , companyid , businessid):
        try :
            companyid = Tblcompany.objects.get(companyid = companyid)
            businessid = Tblsupplier.objects.filter(businessid=businessid , companyid = companyid)
            
            if len(businessid) == 0 :
                return "Sucess"
            else : 
                return "Failed"
        except Tblcompany.DoesNotExist:
            return (f"Company id '{companyid}' not found.")
        
    @staticmethod   
    def resolve_E4k_totalturnoverSupplier(self, info, companyid, businessid):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT SUM(Turnover) AS TotalTurnover
                FROM tblsupplier_turnover
                WHERE BusinessID = %s AND CompanyID = %s
            """, [businessid, companyid])
            row = cursor.fetchone()
         
        return row[0] if row else None