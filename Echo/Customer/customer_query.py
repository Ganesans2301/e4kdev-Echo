
from django.db import connection,transaction
from datetime import date, datetime,timedelta
import graphene
from django.core.paginator import Paginator
from graphene_django.types import DjangoObjectType
from .models import (Tblcompany,TblcustomerTurnover,TblcustomerSettings,TblcustomerSetvalues,
                     TblcustomerAccount,TblaccCashbook,TblcustomerBalance,TblbusCountries,
                     TblcustomerMemo,TblbusCountryMembers,TblbusCurrencies,
                     TblcustomerCategory1,TblcustomerCategory2,TblcustomerAddress,
                     TblcustomerCategory3,TblcustomerClass,TblbusGroups,TblgenAutonumbers,
                     TblaccNominal,TblaccVatcodes,TblbusServicePeople,TblbusSalesPeople,
                     TblbusPaymenttermsRef,TblbusPaymentterms,TblaccNominalTran,Tblcustomer,
                     TblbusAddresstypeRef,TblbusAddresstypes,TblbusContactRef,TblcustomerContact,
                     Tblcustomer,TblcustomerServicePeple,TblcustomerSalesTrans,TblcustomerNotes,
                     TblgenUsers)
from .customer_schema import (TblcompanyType,TblbusCountriesType,TblbusCountryMembersType,
                              TblbusCurrenciesType,TblcustomerCategory1Type,Tblbuscustomercategory2Type,
                              TblcustomerCategory3Type, TblcustomerClassType, TblbusGroupsType, 
                              TblgenAutonumbersType, TblaccNominalType, TblaccVatcodesType, 
                              TblbusServicePeopleType, TblbusSalesPeopleType, 
                              TblbusPaymenttermsRefType, TblbusPaymenttermsType, 
                              TblaccNominalTranType, TblcustomerType,TblbusAddresstypeRefType,
                              TblbusAddresstypesType,TblbusContactRefType,TblcustomerContactType,
                              TblcustomerServicePepleType,TblcustomerSalesTransType,TblcustomerNotesType,
                              TblgenUsersType,TblcustomerAddressType,TblcustomerMemoType,
                              TblcustomerAccountType,TblcustomerBalanceType,TblaccCashbookType,
                              TblcustomerTurnoverType)
from  Product.product_query import bytes_to_boolean


from decimal import Decimal
import random
import string
import socket
import graphene


from graphql import GraphQLError


class NextNo:
    def get_next_no(self, table_name, field_name, companyid):
        # Assuming TblgenAutonumbers is the model you're querying and 'autonumber' is the field holding the current value
        auto_numbers = TblgenAutonumbers.objects.filter(table_name=table_name, field_name=field_name, companyid=companyid)
        
        if not auto_numbers.exists():
            raise ValueError("No auto numbers found for the given parameters.")
        
        # Get the first record from the filtered results
        auto_number = auto_numbers.first()
        
        # Ensure 'autonumber' is the correct field that holds the current value
        next_no = auto_number.autonumber + 1
        # Update the auto number record
        auto_number.autonumber = next_no
        auto_number.save()
        
        return next_no

class companyNotFound(Exception):
    pass


class DataNotFound(Exception):
    pass

class CustomerList:
    @staticmethod
    def resolve_E4k_TblCustomerList(companyid):
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
                    G.GroupName,
                    N.NomDescription AS NominalDescription,
                    c.IsExtract, 
                    c.IsStop,
                    country.Country, 
                    csv.Value
                FROM 
                    tblcustomer c
                LEFT JOIN 
                    tblcustomer_category1 cat1 ON c.Category1ID = cat1.Category1ID
                LEFT JOIN 
                    tblcustomer_category2 cat2 ON c.Category2ID = cat2.Category2ID
                LEFT JOIN 
                    tblcustomer_category3 cat3 ON c.Category3ID = cat3.Category3ID
                LEFT JOIN 
                    tblcustomer_class cl ON c.ClassID = cl.ClassID
                LEFT JOIN 
                    tblbus_countries country ON c.CountryID = country.CountryID
                LEFT JOIN 
                    tblbus_groups G ON c.GroupID = G.GroupID
                LEFT JOIN 
                    tblacc_nominal N ON c.Default_Nominal = N.NomCode
                LEFT JOIN 
                    tblcustomer_setvalues csv ON c.BusinessID = csv.BusinessID AND csv.SettingID = 'LOGO'
                WHERE 
                    c.CompanyID = %s
                   
                """
                cursor.execute(query, [companyid])
                result = cursor.fetchall()

                # Extract column names
                columns = [col[0] for col in cursor.description]

                # Convert the result to a list of dictionaries
                result_dicts = [dict(zip(columns, row)) for row in result]
                print((result_dicts[0]))
                
                for row in result_dicts:
                    row['IsStop'] = True if row['IsStop'] == 1 else False
                    
                    row['IsExtract'] = True if row['IsExtract'] == 1 else False
                    row['IsLive'] = True if row['IsLive'] == 1 else False
                   
                return result_dicts   
        except Exception as e:
            print(f"An error occurred: {e}")
            return []


        

class CustomerTurnover:
    def resolve_E4k_Get_CustomerTurnOver(self, info, businessid):
        query = """
        SELECT SUM(`Turnover`)
        FROM tblcustomer_turnover
        WHERE `CompanyID` = '001' AND `BusinessID` = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [businessid])
            result = cursor.fetchone()

        return result[0] if result and result[0] is not None else 0


class TotalAccount:
    @staticmethod
    def get_address_counts(businessid,companyid):
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
                            `tblcustomer_address` q1
                        LEFT JOIN (
                            SELECT 
                                CompanyID, 
                                AddressID, 
                                COUNT(`AddressID`) AS ct
                            FROM 
                                `tblcustomer_contact`
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
                        AND t3.`IsCustomer` = 1 
                    GROUP BY 
                        t3.`CompanyID`, 
                        t3.`AddressTypeID`,
                        t3.`Description`
                    ORDER BY 
                        t3.`AddressTypeID`;


                """, [businessid,companyid])
                
                rows = cursor.fetchall()
                
                results = []
                for row in rows:
                    result = {
                        "companyId": row[0],
                        "addressTypeId": row[1],
                        "addressCount": int(row[2]),  
                        "description": row[3],
                        "ctCount": float(row[4]) if isinstance(row[4], Decimal) else row[4]  
                    }
                    results.append(result)
                
                return results

        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
        
class ContactList:
    @staticmethod
    def get_contact_details(businessid, addresstypeid):
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
                            tblcustomer_contact cc
                        JOIN 
                            tblbus_contact_ref t1 
                            ON cc.CompanyID = t1.CompanyID 
                            AND cc.ContactType_ID = t1.ContactType_ID
                        JOIN 
                            tblcustomer_address addr 
                            ON cc.CompanyID = addr.CompanyID 
                            AND cc.AddressID = addr.AddressID
                        JOIN
                            tblbus_countries countries 
                            ON addr.CountryCode = countries.CountryID 
                        WHERE 
                            addr.BusinessID = %s
                            AND addr.AddressTypeID = %s;

                """, [businessid, addresstypeid])
                
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
        





class CustomerQuery(graphene.ObjectType):
  
    E4k_company = graphene.List(TblcompanyType, companyid=graphene.String(required=True))

    E4k_country = graphene.List(TblbusCountriesType, companyid=graphene.String(required=True))

    E4k_country_member = graphene.List(TblbusCountryMembersType,  companyid=graphene.String())

    E4k_currency = graphene.List(TblbusCurrenciesType, companyid = graphene.String())

    E4k_Tblcustomercategory1 = graphene.List(TblcustomerCategory1Type ,companyid=graphene.String())

    E4k_Tblcustomercategory2 = graphene.List(Tblbuscustomercategory2Type, companyid = graphene.String())
    
    E4K_Tblcustomercategory3 = graphene.List(TblcustomerCategory3Type , companyid = graphene.String())

    E4k_customerclass= graphene.List(TblcustomerClassType, companyid=graphene.String())

    E4k_Group = graphene.List(TblbusGroupsType, companyid=graphene.String())

    E4k_Tblnominallist = graphene.List(TblaccNominalType, companyid = graphene.String())


    E4k_TblaccVatcodes = graphene.List(TblaccVatcodesType, companyid=graphene.String())

    E4k_TblgenAutonumberslist=graphene.List(TblgenAutonumbersType)

    E4k_TblbusServicePeople =graphene.List(TblbusServicePeopleType, companyid= graphene.String())

    E4k_TblbusSalesPeople =graphene.List(TblbusSalesPeopleType, companyid= graphene.String())

    E4k_TblbusPaymenttermsRef = graphene.List(TblbusPaymenttermsRefType, companyid= graphene.String())

    E4k_TblbusPaymenttermslist = graphene.List(TblbusPaymenttermsType , companyid = graphene.String())

    E4k_TblaccNominalTranlist = graphene.List(TblaccNominalTranType, companyid= graphene.String())


    E4k_TblbusAddresstypeRef = graphene.List(TblbusAddresstypeRefType, companyid= graphene.String())

    E4k_TblbusAddresstypes = graphene.List(TblbusAddresstypesType,companyid= graphene.String())
    
    E4k_TblbusContactRef = graphene.List(TblbusContactRefType, companyid = graphene.String())

    E4k_TblcustomerContactlist = graphene.List(TblcustomerContactType)
    E4k_TblcustomerContact = graphene.List(TblcustomerContactType , companyid = graphene.String() ,addressid= graphene.Int())

    E4k_Tblcustomers = graphene.List(TblcustomerType, companyid= graphene.String(), businessid = graphene.String())
     
    E4k_Tblcustomer_ServicePeplelist= graphene.List(TblcustomerServicePepleType)
    E4k_Tblcustomer_ServicePeple = graphene.List(TblcustomerServicePepleType, companyid = graphene.String(), businessid=graphene.String())
    
    
    E4k_TblcustomerSalesTranslist = graphene.List(TblcustomerSalesTransType)
    E4k_TblcustomerSalesTrans = graphene.List(TblcustomerSalesTransType, businessid = graphene.String(), companyid = graphene.String())

    E4k_TblcustomerNoteslist = graphene.List(TblcustomerNotesType , companyid = graphene.String())
    E4k_TblcustomerNotes = graphene.Field(TblcustomerNotesType, companyid = graphene.String() ,businessid= graphene.String())    

    E4k_TblgenUserslist = graphene.List(TblgenUsersType, companyid = graphene.String())
    E4k_TblgenUsers = graphene.List(TblgenUsersType,companyid = graphene.String())

    E4k_TblcustomerAddresslist = graphene.List(TblcustomerAddressType)
    E4k_TblcustomerAddress = graphene.List(TblcustomerAddressType,companyid = graphene.String(), businessid =graphene.String(),addressid = graphene.String(),addresstypeid= graphene.String())

    E4k_Tblcustomermemolist = graphene.List(TblcustomerMemoType, companyid = graphene.String())
    E4k_TblcustomerMemo = graphene.List(TblcustomerMemoType, companyid = graphene.String(), businessid = graphene.String())  

    E4k_TblcustomerAccountlist = graphene.List(TblcustomerAccountType, companyid = graphene.String())
    E4k_TblcustomerAccount = graphene.List(TblcustomerAccountType,  businessid = graphene.String()) 

    E4k_TblcustomerBalancelist = graphene.List(TblcustomerBalanceType , companyid = graphene.String())
    E4k_TblcustomerBalance = graphene.List(TblcustomerBalanceType,companyid = graphene.String(), businessid = graphene.String())

    E4k_TblaccCashbooklist = graphene.List(TblaccCashbookType, companyid = graphene.String())
    E4k_TblaccCashbook = graphene.List(TblaccCashbookType, companyid = graphene.String(), businessid = graphene.String()) 

    E4k_TblcustomerTurnoverlist = graphene.List(TblcustomerTurnoverType, companyid = graphene.String())
    E4k_TblcustomerTurnover = graphene.List(TblcustomerTurnoverType, companyid = graphene.String(), businessid = graphene.String())   
    
    
    ######################################## Raw Query using Get Function ########################################################################

    E4k_totalturnover = graphene.Float(companyid=graphene.String(), businessid=graphene.String())
    
    E4k_GetContactList  = graphene.List(of_type = graphene.JSONString,businessid = graphene.String(), addresstypeid = graphene.String())

    E4k_TblCustomerList = graphene.List(of_type=graphene.JSONString, companyid=graphene.String(required=True))

    
    E4k_addresscounts = graphene.List(of_type=graphene.JSONString ,companyid =graphene.String(required=True) ,businessid=graphene.String(required=True))
    
    
    GetCustomerAddress = graphene.List(TblcustomerAddressType, businessid=graphene.String(),addresstypeid= graphene.String(required=True))
    
    E4k_ContactList = graphene.List(of_type=graphene.JSONString,businessid=graphene.String(),addresstypeid = graphene.String(required=True))
   
    
    E4k_TblCustomersettings = graphene.List(of_type=graphene.JSONString,businessid=graphene.String(),companyid = graphene.String(),settingid=graphene.String())
    E4k_Businessid_search = graphene.String(companyid = graphene.String(),businessid = graphene.String())


    






    

# all company query function 


# Get contact list based on addresstypeid 

    def resolve_E4k_GetContactList (self, info,businessid , addresstypeid, *kwargs):
        return ContactList.get_contact_details(businessid= businessid , addresstypeid= addresstypeid)
        


  
    def resolve_E4k_company(self, info, companyid, *kwargs): 
        try:
            
            if companyid :
                try:
                    Tblcompany.objects.get(companyid=companyid)
                except Tblcompany.DoesNotExist:
                    raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                return Tblcompany.objects.filter(companyid=companyid)
            else :
                return Tblcompany.objects.all()
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        

    def resolve_E4k_TblCustomerList(self, info, companyid):
            return CustomerList.resolve_E4k_TblCustomerList(companyid=companyid)

    
    
    

    # Countries query function 
   
    
    
    def resolve_E4k_country(self, info, companyid=None, *kwargs):
        try:
            
            company= Tblcompany.objects.get(companyid=companyid)
            if companyid :
                return TblbusCountries.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
         
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        


        

   # countiresMembers tbl query function 
    def resolve_E4k_country_members(self, info, *kwargs):
        return TblbusCountryMembers.objects.all()

    def resolve_E4k_country_member(self, info, companyid ,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblbusCountryMembers.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")

        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
  

    def resolve_E4k_currency(self, info,companyid, *kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblbusCurrencies.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
       

    def resolve_E4k_Tblcustomercategory1(self, info, companyid):
        try :
        
            company= Tblcompany.objects.get(companyid= companyid)
            if companyid:
                return TblcustomerCategory1.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
       
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        
        
        
        
    def resolve_E4k_Tblcustomercategory2 (self, info,companyid):
        try: 
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblcustomerCategory2.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
      



    def resolve_E4K_Tblcustomercategory3(self, info, companyid):
        try:
           company = Tblcompany.objects.get(companyid=companyid)
           if companyid:
                return TblcustomerCategory3.objects.filter(companyid=company)
           else:
               raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        
   

   # CustomerClass function for query   


    
    def resolve_E4k_customerclass(self,info,companyid, *kwargs ):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblcustomerClass.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
            
 
   
# customerGroups Functin for Query


    
    def resolve_E4k_Group(self,info,companyid,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblbusGroups.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
   

# AccountNominal Function for Query

    def resolve_E4k_Tblnominallist(self,info,companyid ,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return  TblaccNominal.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
    
        

#  Filter Function by using vatcode     
    def resolve_E4k_TblaccVatcodes(self,info,companyid,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblaccVatcodes.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:  
            raise GraphQLError(f"An error occurred: {str(e)}")
        
            
    
    def resolve_E4k_TblgenAutonumberslist(self,info,*kwargs):
        return TblgenAutonumbers.objects.all()
    def resolve_E4k_TblgenAutonumbers(self,info,companyid,businessid,*kwargs):
        try:
            companyid = Tblcompany.objects.filter(companyid = companyid)
            if businessid != '':
                return TblgenAutonumbers.objects.filter(companyid = companyid , businessid = businessid)
            else :
                return TblgenAutonumbers.objects.filter(companyid = companyid)
        except Tblcompany.DoesNotExist:
           return companyNotFound(f"Company id '{companyid}' not found.")
        except TblgenAutonumbers.DoesNotExist:
            return "GenUser Not "
        
       
        
   
    
    def resolve_E4k_TblbusServicePeople(self,info,companyid, *kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblbusServicePeople.objects.filter(companyid = company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
            
        
  
    
    def resolve_E4k_TblbusSalesPeople(self,info,companyid, *kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblbusSalesPeople.objects.filter(companyid = company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
      

    def resolve_E4k_TblbusPaymenttermsRef(self,info ,companyid, *kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblbusPaymenttermsRef.objects.filter(companyid = company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        
        
    def resolve_E4k_TblbusPaymenttermslist(self,info,companyid,*kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if companyid:
                return TblbusPaymentterms.objects.filter(companyid = company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
       
       
       
       
       
    def resolve_E4k_TblaccNominalTranlist(self,info,companyid,*kwargs):
        try:
            if companyid :
                try:
                    Tblcompany.objects.get(companyid=companyid)
                except Tblcompany.DoesNotExist:
                    raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                return TblaccNominalTran.objects.filter(companyid = companyid)
            else :
                return TblaccNominalTran.objects.all()
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        
     
     
     
    
    def resolve_E4k_TblbusAddresstypeRef(self,info,companyid ,*kwargs):
        try:
            company= Tblcompany.objects.get(companyid=company)
            if companyid:
                return TblbusAddresstypeRef.objects.filter(companyid = companyid)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            # if companyid :
            #     try:
            #         Tblcompany.objects.get(companyid=companyid)
            #     except Tblcompany.DoesNotExist:
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                
            #     return TblbusAddresstypeRef.objects.filter(companyid = companyid)
            # else :
            #     return TblbusAddresstypeRef.objects.all()
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        
       
       

    def resolve_E4k_TblbusAddresstypes(self,info,companyid,*kwargs):
        try:
            
            company= Tblcompany.objects.get(companyid =companyid)
            if companyid:
                return TblbusAddresstypes.objects.filter(companyid=company)
            else :
                raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
            
            # if companyid :
            #     try:
            #         Tblcompany.objects.get(companyid=companyid)
            #     except Tblcompany.DoesNotExist:
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                
            #     return TblbusAddresstypes.objects.filter(companyid=companyid)
            # else :
            #     return TblbusAddresstypes.objects.all()
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
        
      
    
    def resolve_E4k_TblbusContactRef(self,info,companyid,*kwargs):
        try:
             company = Tblcompany.objects.get(companyid=companyid)
             if companyid:
                 return TblbusContactRef.objects.filter(companyid = companyid)
             else :
                 raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
             
            # if companyid :
            #     try:
            #         Tblcompany.objects.get(companyid=companyid)
            #     except Tblcompany.DoesNotExist:
            #         raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                
            #     return TblbusContactRef.objects.filter(companyid=companyid)
            # else :
            #     return TblbusContactRef.objects.all()
        except Exception as e:
            raise GraphQLError(f"An error occurred: {str(e)}")
      
      
      
    def resolve_E4k_TblcustomerContactlist(self,info,*kwargs):
        return TblcustomerContact.objects.all() 
    
    def resolve_E4k_TblcustomerContact(self,info,addressid,companyid,*kwargs):
        try: 
            if addressid !='':
                try: 
                    company = Tblcompany.objects.get(companyid = companyid)
                except Tblcompany.DoesNotExist:
                    raise GraphQLError(f"Company with ID '{companyid}' does not exist.")
                return TblcustomerContact.objects.filter( companyid = company, addressid=addressid) 
            else:
                return TblcustomerContact.objects.all() 

        except TblcustomerContact.DoesNotExist:
            return None
        

                
        
    def resolve_E4k_TblCustomerlist( self,info,*kwargs):
        return Tblcustomer.objects.all()
        
    
    def resolve_E4k_Tblcustomers(self, info, businessid, companyid, *kwargs):
        try:
            # Check if company exists
            company = Tblcompany.objects.get(companyid=companyid)
            
            # Filter by businessid if provided, otherwise filter by companyid only
            if businessid:
                result = Tblcustomer.objects.filter(companyid=company, businessid=businessid)
            else:
                result = Tblcustomer.objects.filter(companyid=company)
            
            # If result is an empty list, return None
            if not result.exists():
                return None
            
            return result
        
        except Tblcompany.DoesNotExist:
            # Return custom error message when company is not found
            return companyNotFound(f"Company id '{companyid}' not found.")
        
        except Tblcustomer.DoesNotExist:
            # Handle case where no customers are found (though it's unlikely to raise this exception)
            return None
        
        
    
    @staticmethod
    def resolve_E4k_Businessid_search(self,info,companyid,businessid):
        try:
            company = Tblcompany.objects.get(companyid = companyid)
            business = Tblcustomer.objects.filter(companyid=company, businessid=businessid)
            if len(business) == 0:
                return "Success"
            else:
                return "Failed"
        except Tblcompany.DoesNotExist:
            return "Companyid not found"

  
  
  
    def resolve_E4k_Tblcustomer_ServicePeple(self,info,businessid,companyid ,*kwargs):
        try:
            
            companyid = Tblcompany.objects.get(companyid = companyid)
            if businessid !='' :
                return TblcustomerServicePeple.objects.filter(companyid = companyid , businessid = businessid)
            else :
                return TblcustomerServicePeple.objects.filter(companyid = companyid)
        except Tblcompany.DoesNotExist: 
           return companyNotFound(f"Company id '{companyid}' not found.")
        except TblcustomerServicePeple.DoesNotExist:
            return ["customerServicePeple Not Found"]
        


  
    
    def resolve_E4k_TblcustomerSalesTrans(self,info,companyid ,businessid,*kwargs):
        try:
            companyid = Tblcompany.objects.get(companyid =companyid)
            if businessid !='' :
                return TblcustomerSalesTrans.objects.filter(companyid = companyid , businessid = businessid)
            else :
                return TblcustomerSalesTrans.objects.filter(companyid = companyid)
        except Tblcompany.DoesNotExist:
            return companyNotFound(f"Company id '{companyid}' not found.")
        except TblcustomerSalesTrans.DoesNotExist:
            return "customerSalesTrans Not Found"
      
    
   
    
    def resolve_E4k_TblcustomerNotes(self,info,companyid ,businessid,*kwargs): 
        try:
            companyid = Tblcompany.objects.get(companyid=companyid)
            if businessid!= '':
                return TblcustomerNotes.objects.filter(companyid = companyid , businessid = businessid)
            else :
                return TblcustomerNotes.objects.filter(companyid = companyid)
        except Tblcompany.DoesNotExist:
           return companyNotFound(f"Company id '{companyid}' not found.")
        except TblcustomerNotes.DoesNotExist:
            return "CustomerNote Not Found"
          
    
    def resolve_E4k_TblcustomerNotes(self, info, businessid,companyid, *kwargs):
        notes = TblcustomerNotes.objects.filter(businessid=businessid, companyid = companyid)
        if notes.exists():
            return notes.first()
        else:
            return None  
    
    def resolve_E4k_TblgenUserslist(self,info,companyid, *kwargs):
        return TblgenUsers.objects.filter(companyid = companyid)    
    def resolve_E4k_TblgenUsers(self,info,companyid, *kwargs):
        try:
            return TblgenUsers.objects.filter(companyid = companyid)
        except TblgenUsers.DoesNotExist:
            return None
        
    def resolve_E4k_TblcustomerAddresslist(self,info,*kwargs):
        return TblcustomerAddress.objects.all()
    
    def resolve_E4k_TblcustomerAddress(self, info, addressid, businessid, addresstypeid, companyid, *kwargs):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            if addressid:
                return TblcustomerAddress.objects.filter(companyid=company, addressid=addressid, businessid=businessid)
            else:
                return TblcustomerAddress.objects.filter(companyid=company, businessid=businessid, addresstypeid=addresstypeid)
        except TblcustomerAddress.DoesNotExist:
            return None

        
    def resolve_GetCustomerAddress(self, info, businessid, addresstypeid, **kwargs):
        return TblcustomerAddress.objects.filter(businessid=businessid, addresstypeid=addresstypeid)
        
    
 

    def resolve_E4k_TblcustomerMemo(self,info,companyid ,businessid , *kwargs):
        try :
            company = Tblcompany.objects.get(companyid = companyid )
            if businessid !='':
                Memo = TblcustomerMemo.objects.filter(companyid = company, businessid = businessid)
                return Memo
            else :
                return TblcustomerMemo.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            return companyNotFound(f"Company id '{companyid}' not found.")
        except TblcustomerMemo.DoesNotExist:
            return "Customer Memo Not Found"
            



    def resolve_E4k_TblcustomerAccountlist(self,info,companyid, *kwargs):
        return TblcustomerAccount.objects.filter(companyid = companyid)
    
    def resolve_E4k_TblcustomerAccount(self,info,businessid, *kwargs):
        try:
            return TblcustomerAccount.objects.filter(businessid=businessid)
        except TblcustomerAccount.DoesNotExist:
            return None


    

    def resolve_E4k_TblcustomerBalance(self,info,businessid,companyid,*kwargs):
        try:
            companyid = Tblcompany.objects.get(companyid = companyid)
            if businessid !='' :
                return TblcustomerBalance.objects.filter(businessid=businessid, companyid = companyid)
            else :
                return TblcustomerBalance.objects.filter(companyid = companyid)
        except Tblcompany.DoesNotExist:
           return companyNotFound(f"Company id '{companyid}' not found.")
        except TblcustomerBalance.DoesNotExist:
            return "Customer Balance Not Found"
         

    
    def resolve_E4k_TblaccCashbooklist(self,info,companyid , businessid,*kwargs):
        return TblaccCashbook.objects.filter(companyid = companyid)
    
    def resolve_E4k_TblaccCashbook(self,info,companyid, businessid ):
        try:
                company= Tblcompany.objects.get(companyid=companyid)
                if  businessid != '':
                    accountcashback = TblaccCashbook.objects.filter(companyid=company , businessid=businessid)
                    return accountcashback
                else :
                    return TblaccCashbook.objects.filter(companyid=company)
            
        except Tblcompany.DoesNotExist:
           return companyNotFound(f"Company id '{companyid}' not found.")
        except TblaccCashbook.DoesNotExist:
            return "Account Cashbook Not Found"
        
    
   
    
    def resolve_E4k_TblcustomerTurnover(self,info,companyid ,businessid , ):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            
            if businessid !='':
                data = TblcustomerTurnover.objects.filter(companyid=company, businessid=businessid)
                return data
            else:
                
                return TblcustomerTurnover.objects.filter(companyid = company)
        except Tblcompany.DoesNotExist:
            raise companyNotFound(f"Company id '{companyid}' not found.")
        except TblcustomerTurnover.DoesNotExist:
            return None;
    
    def resolve_E4k_addresscounts(self, info, businessid,companyid):
        return TotalAccount.get_address_counts(businessid=businessid, companyid=companyid)
    
    def resolve_E4k_ContactList(selef,info, businessid, addresstypeid, *kwargs):
        return ContactList.get_contact_details(businessid=businessid, addresstypeid=addresstypeid)
       


    def resolve_E4k_totalturnover(self, info, companyid, businessid):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT SUM(Turnover) AS TotalTurnover
                FROM tblcustomer_turnover
                WHERE BusinessID = %s AND CompanyID = %s
            """, [businessid, companyid])
            row = cursor.fetchone()
            # print("dwd", row)
        return row[0] if row else None
    
    
    @staticmethod
    # def resolve_E4k_TblCustomersettings(self, info, companyid, businessid, settingid):
    #     try:
    #         companyid = Tblcompany.objects.get(companyid=companyid)
    #         Lookup = [] 
    #         if businessid != '':
    #             try: 
    #                 businessid  = Tblcustomer.objects.get(companyid=companyid , businessid=businessid )
    #                 if settingid != '':
    #                     try: 
    #                         return TblcustomerSettings.objects.get(settingid=settingid, companyid=companyid)
    #                     except TblcustomerSettings.DoesNotExist:
    #                         return "CustomerSettings Not Found" 
    #                 else :
    #                     Lookup_table = TblcustomerSettings.objects.filter(companyid=companyid).order_by('category' ,'seqno')
                       
    #                     for table in Lookup_table:
                          
    #                         if table.settingid:
    #                             settings = TblcustomerSettings.objects.get(settingid=table.settingid , companyid=companyid)
    #                             Lookup_query =settings.lookup_table 
                                
                               
                    
                                
    #                             try:
    #                                 customersetvalues = TblcustomerSetvalues.objects.get(settingid=settings, companyid=companyid ,businessid=businessid ) 
                                    
    #                                 if not Lookup_query:
    #                                     if not customersetvalues:
    #                                         Lookup.append({
    #                                                'settingid': table.settingid,
    #                                                 'SettingName': table.settingname1,
    #                                                 'Type': table.type,
    #                                                 'lookup_text': None,
    #                                                 'Lookup_Table': Lookup_query,
    #                                                 'category' : table.category,
    #                                                 'Default': table.default,
    #                                                 'seqno': table.seqno
    #                                         })
    #                                     else :
    #                                         table.lookup_text= customersetvalues.value
    #                                         Lookup.append({
    #                                                 'settingid': table.settingid,
    #                                                 'SettingName': table.settingname1,
    #                                                 'Type': table.type,
    #                                                 'lookup_text': None,
    #                                                 'Lookup_Table': Lookup_query,
    #                                                 'Default': customersetvalues.value,
    #                                                 'category' : table.category,
    #                                                 'seqno': table.seqno
    #                                             })
    #                                 else :
                                       
    #                                     if "tble4KStrValues" in Lookup_query:
    #                                         with connection.cursor() as cursor:
    #                                             cursor.execute(Lookup_query)
    #                                             rows = cursor.fetchall()
    #                                         result = [row[0] for row in rows]
    #                                         table.lookup_text = result
                                            
                                                    
                                      
                                           
                                            
    #                                         if not customersetvalues.value:     
    #                                             Lookup.append({
    #                                                 'settingid': table.settingid,
    #                                                 'SettingName': table.settingname1,
    #                                                 'Type': table.type,
    #                                                 'lookup_text': result,
    #                                                 'Lookup_Table': Lookup_query,
    #                                                 'Default': table.default,
    #                                                 'category' : table.category,
    #                                                 'seqno': table.seqno
        
    #                                             })
                                                
    #                                         else :
    #                                             table.lookup_text= customersetvalues.value
    #                                             Lookup.append({
    #                                                 'settingid': table.settingid,
    #                                                 'SettingName': table.settingname1,
    #                                                 'Type': table.type,
    #                                                 'lookup_text': result,
    #                                                 'Lookup_Table': Lookup_query,
    #                                                 'Default': customersetvalues.value,
    #                                                 'category' : table.category,
    #                                                 'seqno': table.seqno
    #                                             })
    #                                     else:
                                            
    #                                          Lookup.append({
    #                                                 'settingid': table.settingid,
    #                                                 'SettingName': table.settingname1,
    #                                                 'Type': table.type,
    #                                                 'lookup_text': result,
    #                                                 'Lookup_Table': Lookup_query,
    #                                                 'Default':customersetvalues.value,
    #                                                 'category' : table.category,
    #                                                 'seqno': table.seqno
        
    #                                             })
                                             
                                 
                                                 
                                             
                                             
                                            
                                             
              
    #                             except TblcustomerSetvalues.DoesNotExist:
    #                                 if not Lookup_query:
    #                                     table.lookup_text = None
    #                                     Lookup.append({
    #                                              'settingid': table.settingid,
    #                                               'SettingName': table.settingname1,
    #                                               'Type': table.type,
    #                                               'lookup_text': table.lookup_text,
    #                                               'Lookup_Table': Lookup_query,
    #                                               'Default': table.default,
    #                                               'category' : table.category,
    #                                               'seqno': table.seqno
    #                                     })
                                        
    #                                 else:
                                        
    #                                     if "tble4KStrValues" in Lookup_query:
    #                                         with connection.cursor() as cursor:
    #                                             cursor.execute(Lookup_query)
    #                                             rows = cursor.fetchall()
                                            
    #                                         result = [row[0] for row in rows]
    #                                         table.lookup_text = result
    #                                         Lookup.append({
    #                                                 'settingid': table.settingid,
    #                                                 'SettingName': table.settingname1,
    #                                                 'Type': table.type,
    #                                                 'lookup_text': result,
    #                                                 'Lookup_Table': Lookup_query,
    #                                                 'Default': table.default,
    #                                                 'category' : table.category,
    #                                                 'seqno': table.seqno
    #                                             })
    #             except Tblcustomer.DoesNotExist:
    #                 return "Business Not Found"   
                
    #         else:
    #             if settingid !='':
    #                 try:
    #                     TblcustomerSettings.objects.get(companyid = companyid , settingid =settingid)
                    
    #                 except TblcustomerSettings.DoesNotExist:
    #                     return "CustomerSettings Not Found"
    #             else:
    #                 Lookup_table = TblcustomerSettings.objects.filter(companyid=companyid).order_by('category' , 'seqno')
    #                 for table in Lookup_table:
    #                     if table.settingid :
    #                         settings = TblcustomerSettings.objects.get(settingid=table.settingid , companyid=companyid)
    #                         Lookup_query = settings.lookup_table
                            
    #                         if not Lookup_query:
    #                             table.lookup_text = None
    #                             Lookup.append({
    #                                           'settingid': table.settingid,
    #                                            'SettingName': table.settingname1,
    #                                            'Type': table.type,
    #                                            'lookup_text': table.lookup_text,
    #                                            'Lookup_Table': Lookup_query,
    #                                            'Default': table.default,
    #                                            'category' : table.category,
    #                                            'seqno': table.seqno
    #                                  })
    #                         else:
    #                             with connection.cursor() as cursor:
    #                                  cursor.execute(Lookup_query)
    #                                  rows = cursor.fetchall()
    #                                  result = [row[0] for row in rows]
    #                                  table.lookup_text = result
    #                                  Lookup.append({
    #                                           'settingid': table.settingid,
    #                                            'SettingName': table.settingname1,
    #                                            'Type': table.type,
    #                                            'lookup_text': result,
    #                                            'Lookup_Table': Lookup_query,
    #                                            'Default': table.default,
    #                                            'category' : table.category,
    #                                            'seqno': table.seqno
    #                                           })
                                                                   
    #         return Lookup                
    #     except Tblcompany.DoesNotExist:
    #         return companyNotFound(f"Company id '{companyid}' not found.")
    
    
    # @staticmethod
    # def resolve_E4k_TblCustomersettings(self, info, companyid, businessid, settingid):
    #     try:
    #         companyid = Tblcompany.objects.get(companyid=companyid)
    #         Lookup = [] 
    #         if businessid != '':
    #             try: 
    #                 businessid = Tblcustomer.objects.get(companyid=companyid, businessid=businessid)
    #                 if settingid != '':
    #                     try: 
    #                         return TblcustomerSettings.objects.get(settingid=settingid, companyid=companyid)
    #                     except TblcustomerSettings.DoesNotExist:
    #                         return "CustomerSettings Not Found" 
    #                 else:
    #                     Lookup_table = TblcustomerSettings.objects.filter(companyid=companyid).order_by('category', 'seqno')
    #                     for table in Lookup_table:
    #                         if table.settingid:
    #                             settings = TblcustomerSettings.objects.get(settingid=table.settingid, companyid=companyid)
    #                             Lookup_query = settings.lookup_table  

    #                             try:
    #                                 customersetvalues = TblcustomerSetvalues.objects.get(settingid=settings, companyid=companyid, businessid=businessid)
                                    
    #                                 if not Lookup_query:
    #                                     if not customersetvalues:
    #                                         Lookup.append({
    #                                             'settingid': table.settingid,
    #                                             'SettingName': table.settingname1,
    #                                             'Type': table.type,
    #                                             'lookup_text': None,
    #                                             'Lookup_Table': Lookup_query,
    #                                             'category': table.category,
    #                                             'Default': table.default,
    #                                             'seqno': table.seqno
    #                                         })
    #                                     else:
    #                                         Lookup.append({
    #                                             'settingid': table.settingid,
    #                                             'SettingName': table.settingname1,
    #                                             'Type': table.type,
    #                                             'lookup_text': None,
    #                                             'Lookup_Table': Lookup_query,
    #                                             'Default': customersetvalues.value,
    #                                             'category': table.category,
    #                                             'seqno': table.seqno
    #                                         })
    #                                 else:
    #                                     with connection.cursor() as cursor:
    #                                         cursor.execute(Lookup_query)
    #                                         rows = cursor.fetchall()
    #                                     result = [row[0] for row in rows]
    #                                     table.lookup_text = result

    #                                     if not customersetvalues.value:
    #                                         Lookup.append({
    #                                             'settingid': table.settingid,
    #                                             'SettingName': table.settingname1,
    #                                             'Type': table.type,
    #                                             'lookup_text': result,
    #                                             'Lookup_Table': Lookup_query,
    #                                             'Default': table.default,
    #                                             'category': table.category,
    #                                             'seqno': table.seqno
    #                                         })
    #                                     else:
    #                                         Lookup.append({
    #                                             'settingid': table.settingid,
    #                                             'SettingName': table.settingname1,
    #                                             'Type': table.type,
    #                                             'lookup_text': result,
    #                                             'Lookup_Table': Lookup_query,
    #                                             'Default': customersetvalues.value,
    #                                             'category': table.category,
    #                                             'seqno': table.seqno
    #                                         })

    #                             except TblcustomerSetvalues.DoesNotExist:
    #                                 if not Lookup_query:
    #                                     table.lookup_text = None
    #                                     Lookup.append({
    #                                         'settingid': table.settingid,
    #                                         'SettingName': table.settingname1,
    #                                         'Type': table.type,
    #                                         'lookup_text': table.lookup_text,
    #                                         'Lookup_Table': Lookup_query,
    #                                         'Default': table.default,
    #                                         'category': table.category,
    #                                         'seqno': table.seqno
    #                                     })
    #                                 else:
    #                                     with connection.cursor() as cursor:
    #                                         cursor.execute(Lookup_query)
    #                                         rows = cursor.fetchall()
                                        
    #                                     result = [row[0] for row in rows]
    #                                     table.lookup_text = result
    #                                     Lookup.append({
    #                                         'settingid': table.settingid,
    #                                         'SettingName': table.settingname1,
    #                                         'Type': table.type,
    #                                         'lookup_text': result,
    #                                         'Lookup_Table': Lookup_query,
    #                                         'Default': table.default,
    #                                         'category': table.category,
    #                                         'seqno': table.seqno
    #                                     })

    #             except Tblcustomer.DoesNotExist:
    #                 return "Business Not Found"   

    #         else:
    #             if settingid != '':
    #                 try:
    #                     TblcustomerSettings.objects.get(companyid=companyid, settingid=settingid)
    #                 except TblcustomerSettings.DoesNotExist:
    #                     return "CustomerSettings Not Found"
    #             else:
    #                 Lookup_table = TblcustomerSettings.objects.filter(companyid=companyid).order_by('category', 'seqno')
    #                 for table in Lookup_table:
    #                     if table.settingid:
    #                         settings = TblcustomerSettings.objects.get(settingid=table.settingid, companyid=companyid)
    #                         Lookup_query = settings.lookup_table

    #                         if not Lookup_query:
    #                             table.lookup_text = None
    #                             Lookup.append({
    #                                 'settingid': table.settingid,
    #                                 'SettingName': table.settingname1,
    #                                 'Type': table.type,
    #                                 'lookup_text': table.lookup_text,
    #                                 'Lookup_Table': Lookup_query,
    #                                 'Default': table.default,
    #                                 'category': table.category,
    #                                 'seqno': table.seqno
    #                             })
    #                         else:
    #                             with connection.cursor() as cursor:
    #                                 cursor.execute(Lookup_query)
    #                                 rows = cursor.fetchall()
    #                                 result = [row[0] for row in rows]
    #                                 table.lookup_text = result
    #                                 Lookup.append({
    #                                     'settingid': table.settingid,
    #                                     'SettingName': table.settingname1,
    #                                     'Type': table.type,
    #                                     'lookup_text': result,
    #                                     'Lookup_Table': Lookup_query,
    #                                     'Default': table.default,
    #                                     'category': table.category,
    #                                     'seqno': table.seqno
    #                                 })

    #         return Lookup                
    #     except Tblcompany.DoesNotExist:
    #         return companyNotFound(f"Company id '{companyid}' not found.")
    

    @staticmethod
    def resolve_E4k_TblCustomersettings(self, info, companyid, businessid, settingid):
        try:
            company = Tblcompany.objects.get(companyid=companyid)
            Lookup = []
            
            if businessid:
                try:
                    business = Tblcustomer.objects.get(companyid=company, businessid=businessid)

                    if settingid:
                        try:
                            return TblcustomerSettings.objects.get(settingid=settingid, companyid=company)
                        except TblcustomerSettings.DoesNotExist:
                            return "CustomerSettings Not Found"
                    else:
                        Lookup_table = TblcustomerSettings.objects.filter(companyid=company).order_by('category', 'seqno')

                        for table in Lookup_table:
                            if table.settingid:
                                settings = TblcustomerSettings.objects.get(settingid=table.settingid, companyid=company)
                                Lookup_query = settings.lookup_table
                            

                                # Condition to handle empty, null, or invalid Lookup_query
                                if not Lookup_query or not Lookup_query.strip():
                                    try:
                                        customersetvalues = TblcustomerSetvalues.objects.get(settingid=settings, companyid=company, businessid=business)
                                    except TblcustomerSetvalues.DoesNotExist:
                                        customersetvalues = None
                                    Lookup.append({
                                        'settingid': table.settingid,
                                        'SettingName': table.settingname1,
                                        'Type': table.type,
                                        'lookup_text': "",
                                        'Lookup_Table': Lookup_query,
                                        'Default':customersetvalues.value if customersetvalues else table.default,
                                        'system_default': table.default,
                                        'category': table.category,
                                        'seqno': table.seqno
                                    })
                                    continue

                                try:
                                    customersetvalues = TblcustomerSetvalues.objects.get(settingid=settings, companyid=company, businessid=business)

                                    result = None
                                    if '{e4KCompany}' in Lookup_query:
                                        Lookup_query = Lookup_query.replace('{e4KCompany}', str(companyid))

                                    # Check for each table separately
                                    if "tble4KStrValues" in Lookup_query:
                                        with connection.cursor() as cursor:
                                            cursor.execute(Lookup_query)
                                            rows = cursor.fetchall()
                                            result = [row[0] for row in rows]

                                    elif "tblproduct_price_types" in Lookup_query:
                                        with connection.cursor() as cursor:
                                            cursor.execute(Lookup_query)
                                            rows = cursor.fetchall()
                                            result = [row[0] for row in rows]

                                    elif "tblwho_warehouses" in Lookup_query:
                                        with connection.cursor() as cursor:
                                            cursor.execute(Lookup_query)
                                            rows = cursor.fetchall()
                                            result = [row[0] for row in rows]

                                    Lookup.append({
                                        'settingid': table.settingid,
                                        'SettingName': table.settingname1,
                                        'Type': table.type,
                                        'lookup_text': result,
                                        'Lookup_Table': Lookup_query,
                                        'Default': customersetvalues.value if customersetvalues else table.default,
                                        'system_default': table.default,
                                        'category': table.category,
                                        'seqno': table.seqno
                                    })
                                except TblcustomerSetvalues.DoesNotExist:
                                    result = None
                                    if '{e4KCompany}' in Lookup_query:
                                        Lookup_query = Lookup_query.replace('{e4KCompany}', str(companyid))

                                    # Check for each table separately
                                    if "tble4KStrValues" in Lookup_query:
                                        with connection.cursor() as cursor:
                                            cursor.execute(Lookup_query)
                                            rows = cursor.fetchall()
                                            result = [row[0] for row in rows]

                                    elif "tblproduct_price_types" in Lookup_query:
                                        with connection.cursor() as cursor:
                                            cursor.execute(Lookup_query)
                                            rows = cursor.fetchall()
                                            result = [row[0] for row in rows]

                                    elif "tblwho_warehouses" in Lookup_query:
                                        with connection.cursor() as cursor:
                                            cursor.execute(Lookup_query)
                                            rows = cursor.fetchall()
                                            result = [row[0] for row in rows]

                                    Lookup.append({
                                        'settingid': table.settingid,
                                        'SettingName': table.settingname1,
                                        'Type': table.type,
                                        'lookup_text': result if result else "",
                                        'Lookup_Table': Lookup_query,
                                        'Default': table.default,
                                        'system_default': table.default,
                                        'category': table.category,
                                        'seqno': table.seqno
                                    })

                except Tblcustomer.DoesNotExist:
                    return "Business Not Found"
            else:
                if settingid:
                    try:
                        TblcustomerSettings.objects.get(companyid=company, settingid=settingid)
                    except TblcustomerSettings.DoesNotExist:
                        return "CustomerSettings Not Found"
                else:
                    Lookup_table = TblcustomerSettings.objects.filter(companyid=company).order_by('category', 'seqno')
                    for table in Lookup_table:
                        if table.settingid:
                            settings = TblcustomerSettings.objects.get(settingid=table.settingid, companyid=company)
                            Lookup_query = settings.lookup_table

                            # Condition to handle empty, null, or invalid Lookup_query
                            if not Lookup_query or not Lookup_query.strip():
                                Lookup.append({
                                    'settingid': table.settingid,
                                    'SettingName': table.settingname1,
                                    'Type': table.type,
                                    'lookup_text': "",
                                    'Lookup_Table': Lookup_query,
                                    'Default': table.default,
                                    'system_default': table.default,
                                    'category': table.category,
                                    'seqno': table.seqno
                                })
                                continue

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
                                    'category': table.category,
                                    'seqno': table.seqno
                                })

            return Lookup
        except Tblcompany.DoesNotExist:
            return f"Company id '{companyid}' not found."


    # @staticmethod
    # def resolve_E4k_TblCustomersettings(self, info, companyid, businessid, settingid):
    #     try:
    #         # Retrieve the company object
    #         company = Tblcompany.objects.get(companyid=companyid)
    #         Lookup = [] 

    #         if businessid:
    #             try:
                 
    #                 business = Tblcustomer.objects.get(companyid=company, businessid=businessid)

    #                 if settingid:
    #                     try: 
    #                         return TblcustomerSettings.objects.get(settingid=settingid, companyid=company)
    #                     except TblcustomerSettings.DoesNotExist:
    #                         return "CustomerSettings Not Found"
    #                 else:
    #                     Lookup_table = TblcustomerSettings.objects.filter(companyid=company).order_by('category', 'seqno')

    #                     for table in Lookup_table:
    #                         if table.settingid:
    #                             settings = TblcustomerSettings.objects.get(settingid=table.settingid, companyid=company)
    #                             Lookup_query = settings.lookup_table

    #                             try:
    #                                 customersetvalues = TblcustomerSetvalues.objects.get(settingid=settings, companyid=company, businessid=business)
    #                                 system_default = customersetvalues.value if customersetvalues else table.default
    #                                 # default_value = customersetvalues.value if customersetvalues else table.default

    #                                 if not Lookup_query:
    #                                     Lookup.append({
    #                                         'settingid': table.settingid,
    #                                         'SettingName': table.settingname1,
    #                                         'Type': table.type,
    #                                         'lookup_text': None,
    #                                         'Lookup_Table': Lookup_query,
    #                                         'category': table.category,
    #                                         'Default': table.default, 
    #                                         'system_default': system_default,  
    #                                         'seqno': table.seqno
    #                                     })
    #                                 else:
    #                                     result = None
    #                                     if '{e4KCompany}' in Lookup_query:
    #                                         Lookup_query = Lookup_query.replace('{e4KCompany}', str(companyid))

    #                                     if "tble4KStrValues" in Lookup_query:
    #                                         with connection.cursor() as cursor:
    #                                             cursor.execute(Lookup_query)
    #                                             rows = cursor.fetchall()
    #                                             result = [row[0] for row in rows]

    #                                     Lookup.append({
    #                                         'settingid': table.settingid,
    #                                         'SettingName': table.settingname1,
    #                                         'Type': table.type,
    #                                         'lookup_text': result,
    #                                         'Lookup_Table': Lookup_query,
    #                                         'Default': table.default,  
    #                                         'system_default': system_default,  
    #                                         'category': table.category,
    #                                         'seqno': table.seqno
    #                                     })
    #                             except TblcustomerSetvalues.DoesNotExist:
    #                                 system_default = None 
    #                                 default_value = table.default  
    #                                 if not Lookup_query:
    #                                     table.lookup_text = None
    #                                 else:
    #                                     result = None
    #                                     if '{e4KCompany}' in Lookup_query:
    #                                         Lookup_query = Lookup_query.replace('{e4KCompany}', str(companyid))

    #                                     if "tble4KStrValues" in Lookup_query:
    #                                         with connection.cursor() as cursor:
    #                                             cursor.execute(Lookup_query)
    #                                             rows = cursor.fetchall()
    #                                             result = [row[0] for row in rows]

    #                                 Lookup.append({
    #                                     'settingid': table.settingid,
    #                                     'SettingName': table.settingname1,
    #                                     'Type': table.type,
    #                                     'lookup_text': result if result else table.lookup_text,
    #                                     'Lookup_Table': Lookup_query,
    #                                     'Default':table.default, 
    #                                     'system_default': system_default, 
    #                                     'category': table.category,
    #                                     'seqno': table.seqno
    #                                 })

    #             except Tblcustomer.DoesNotExist:
    #                 return "Business Not Found"   
    #         else:
    #             if settingid:
    #                 try:
    #                     TblcustomerSettings.objects.get(companyid=company, settingid=settingid)
    #                 except TblcustomerSettings.DoesNotExist:
    #                     return "CustomerSettings Not Found"
    #             else:
    #                 Lookup_table = TblcustomerSettings.objects.filter(companyid=company).order_by('category', 'seqno')
    #                 for table in Lookup_table:
    #                     if table.settingid:
    #                         settings = TblcustomerSettings.objects.get(settingid=table.settingid, companyid=company)
    #                         Lookup_query = settings.lookup_table

    #                         try:
    #                             customersetvalues = TblcustomerSetvalues.objects.get(settingid=settings, companyid=company)
    #                             system_default = customersetvalues.value if customersetvalues else None
    #                             default_value = customersetvalues.value if customersetvalues else table.default

    #                             if not Lookup_query:
    #                                 table.lookup_text = None
    #                                 Lookup.append({
    #                                     'settingid': table.settingid,
    #                                     'SettingName': table.settingname1,
    #                                     'Type': table.type,
    #                                     'lookup_text': table.lookup_text,
    #                                     'Lookup_Table': Lookup_query,
    #                                     'Default': table.default,
    #                                     'system_default': system_default, 
    #                                     'category': table.category,
    #                                     'seqno': table.seqno
    #                                 })
    #                             else:
    #                                 with connection.cursor() as cursor:
    #                                     cursor.execute(Lookup_query)
    #                                     rows = cursor.fetchall()
    #                                     result = [row[0] for row in rows]
    #                                     table.lookup_text = result
    #                                     Lookup.append({
    #                                         'settingid': table.settingid,
    #                                         'SettingName': table.settingname1,
    #                                         'Type': table.type,
    #                                         'lookup_text': result,
    #                                         'Lookup_Table': Lookup_query,
    #                                         'Default': table.default, 
    #                                         'system_default': system_default, 
    #                                         'category': table.category,
    #                                         'seqno': table.seqno
    #                                     })

    #                         except TblcustomerSetvalues.DoesNotExist:
                                
    #                             system_default = None  
    #                             default_value = table.default  

    #                             if not Lookup_query:
    #                                 table.lookup_text = None
    #                                 Lookup.append({
    #                                     'settingid': table.settingid,
    #                                     'SettingName': table.settingname1,
    #                                     'Type': table.type,
    #                                     'lookup_text': table.lookup_text,
    #                                     'Lookup_Table': Lookup_query,
    #                                     'Default': table.default, 
    #                                     'system_default': system_default, 
    #                                     'category': table.category,
    #                                     'seqno': table.seqno
    #                                 })
    #                             else:
    #                                 with connection.cursor() as cursor:
    #                                     cursor.execute(Lookup_query)
    #                                     rows = cursor.fetchall()
    #                                     result = [row[0] for row in rows]
    #                                     table.lookup_text = result
    #                                     Lookup.append({
    #                                         'settingid': table.settingid,
    #                                         'SettingName': table.settingname1,
    #                                         'Type': table.type,
    #                                         'lookup_text': result,
    #                                         'Lookup_Table': Lookup_query,
    #                                         'Default':table.default, 
    #                                         'system_default': system_default,  
    #                                         'category': table.category,
    #                                         'seqno': table.seqno
    #                                     })

    #         return Lookup                

    #     except Tblcompany.DoesNotExist:
    #         return f"Company id '{companyid}' not found."
