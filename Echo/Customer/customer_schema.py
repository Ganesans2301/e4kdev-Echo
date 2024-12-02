import re
from datetime import date, datetime,timedelta
from decimal import Decimal, InvalidOperation
import random
import string
import socket
import base64
import graphene
from graphene_django import DjangoObjectType
from django.db import transaction
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

from graphene_file_upload.scalars import Upload
from django.conf import settings
import os
from  Product.utils import parse_date





class NextNo:
    def get_next_no(self, table_name, field_name, companyid):

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


#Company Tbl query
class TblcompanyType(DjangoObjectType):
    class Meta:
        model = Tblcompany
        fields = '__all__'
# Country Tbl query 
class TblbusCountriesType(DjangoObjectType):
    class Meta:
        model = TblbusCountries
        fields = '__all__'
#countryMembers Tbl
class TblbusCountryMembersType(DjangoObjectType):
    class Meta:
        model = TblbusCountryMembers
        fields = '__all__'
#Courrency Tbl
class TblbusCurrenciesType(DjangoObjectType):
    class Meta:
        model = TblbusCurrencies
        fields = '__all__'
# Customercategory1 tbl query 

class TblcustomerCategory1Type(DjangoObjectType):
    class Meta:
        model = TblcustomerCategory1
        fields = '__all__'
 # Customercategory2 tbl query
class Tblbuscustomercategory2Type(DjangoObjectType):
    class Meta:
        model = TblcustomerCategory2
        fields = '__all__'

# customercategory3 tbl query class define
class TblcustomerCategory3Type(DjangoObjectType):
    class Meta:
        model = TblcustomerCategory3
        fields = '__all__'
#customer class tbl query class define
class TblcustomerClassType(DjangoObjectType):
    class Meta:
        model = TblcustomerClass
        feilds = '__all__'
# Groups Class define
class TblbusGroupsType(DjangoObjectType):
    class Meta:
        model= TblbusGroups
        fields ='__all__'
# AutoGenNumber class define
class TblgenAutonumbersType(DjangoObjectType):
    class Meta:
        model= TblgenAutonumbers
        fields = '__all__'


#Nominal Tbl Query class define

class TblaccNominalType(DjangoObjectType):
    class Meta:
        model = TblaccNominal
        fields = '__all__'
    
class TblaccountNominalType(DjangoObjectType):
    class Meta:
        model = TblaccNominal
        fields = '__all__'


class TblaccVatcodesType(DjangoObjectType):
    class Meta:
        model =TblaccVatcodes
        fields = '__all__'

class TblbusServicePeopleType(DjangoObjectType):
    class Meta:
        model = TblbusServicePeople
        fields ='__all__'


class TblbusSalesPeopleType(DjangoObjectType):
    class Meta:
        model = TblbusSalesPeople
        fields ='__all__'


class TblbusPaymenttermsRefType(DjangoObjectType):
    class Meta:
        model = TblbusPaymenttermsRef
        fields = '__all__'

class TblbusPaymenttermsType(DjangoObjectType):
    class Meta:
        model = TblbusPaymentterms
        feilds ='__all__'

class TblaccNominalTranType(DjangoObjectType):
    class Meta:
        model = TblaccNominalTran
        feilds = '__all__'

class TblcustomerType(DjangoObjectType):
    class Meta:
        model = Tblcustomer
        fields = '__all__'


class TblbusAddresstypeRefType(DjangoObjectType):
    class Meta:
        model = TblbusAddresstypeRef
        fields = '__all__'


class TblbusAddresstypesType(DjangoObjectType):
    class Meta:
        model = TblbusAddresstypes
        feilds = '__all__'

class TblbusContactRefType(DjangoObjectType):
    class Meta:
        model = TblbusContactRef
        feilds = '__all__'


class TblcustomerContactType(DjangoObjectType):
    class Meta:
        model = TblcustomerContact
        feilds = '__all__'


class TblcustomerServicePepleType(DjangoObjectType):
    class Meta:
        model = TblcustomerServicePeple
        feilds = '__all__'

class TblcustomerSalesTransType(DjangoObjectType):
    class Meta:
        model = TblcustomerSalesTrans
        feilds = '__all__'

class TblgenUsersType(DjangoObjectType):
    class Meta: 
        model = TblgenUsers
        feilds = '__all__'

class TblcustomerNotesType(DjangoObjectType):
    class Meta: 
        model = TblcustomerNotes  
        feilds = '__all__'


class TblcustomerAddressType(DjangoObjectType):
    class Meta: 
        model = TblcustomerAddress
        feilds = '__all__'

class TblcustomerMemoType(DjangoObjectType):
    class Meta:
        model = TblcustomerMemo
        feilds = '__all__'

class TblcustomerAccountType(DjangoObjectType):
    class Meta:
        model = TblcustomerAccount
        feilds = '__all__'


class TblcustomerBalanceType(DjangoObjectType):
    class Meta:
        model = TblcustomerBalance
        feilds = '__all__'


class TblaccCashbookType(DjangoObjectType):
    class Meta:
        model = TblaccCashbook
        feilds = '__all__'


class TblcustomerTurnoverType(DjangoObjectType):
    class Meta:
        model = TblcustomerTurnover
        feilds = '__all__'

class TblcustomerSetvaluesType(DjangoObjectType):
    class Meta:
        model = TblcustomerSetvalues
        feilds = '__all__'


class E4k_Company_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        name = graphene.String(required=True)
        address1 = graphene.String(required=True)
        address2 = graphene.String(required=True)
        address3 = graphene.String(required=True)
        address4 = graphene.String(required=True)
        postcode = graphene.String(required=True)
        phone = graphene.String(required=True)
        fax = graphene.String(required=True)
        email = graphene.String(required=True)
        vatno = graphene.String(required=True)
        holdingcompany = graphene.String(required=True)
        countryid = graphene.Int(required=True)
        currency_code = graphene.Int(required=True)

    company = graphene.Field(TblcompanyType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, name, address1, address2, address3, address4, postcode, phone, fax, email, vatno, holdingcompany, countryid, currency_code):
        errors = []

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format.")
        
        # Check if companyid already exists
        if Tblcompany.objects.filter(companyid=companyid).exists():
            errors.append("CompanyID already exists.")
        
        # Check if email already exists
        if Tblcompany.objects.filter(email=email).exists():
            errors.append("Email already exists.")
        
        # Check phone and fax formats (basic check for numeric values)
        if not phone.isdigit():
            errors.append("Phone number should contain only digits.")
        if not fax.isdigit():
            errors.append("Fax number should contain only digits.")
        
        # Validate that required fields are not empty
        required_fields = [name,  postcode, phone, fax, email, vatno, holdingcompany]
        for field in required_fields:
            if not field:
                errors.append(f"{field} is required.")

        # Validate foreign key existence
        try:
            TblbusCountries.objects.get(countryid=countryid)
        except TblbusCountries.DoesNotExist:
            errors.append("CountryID does not exist.")

        try:
            TblbusCurrencies.objects.get(currency_code=currency_code)
        except TblbusCurrencies.DoesNotExist:
            errors.append("Currency code does not exist.")
        
        # If there are errors, return the errors
        if errors:
            return E4k_Company_Create(success=False, error=", ".join(errors))
        
        # Create the company
        try:
            company = Tblcompany(
                companyid=companyid,
                name=name,
                address1=address1,
                address2=address2,
                address3=address3,
                address4=address4,
                postcode=postcode,
                phone=phone,
                fax=fax,
                email=email,
                vatno=vatno,
                holdingcompany=holdingcompany,
                countryid_id=countryid,
                currency_code_id=currency_code,
            )
            company.save()
            return E4k_Company_Create(company=company, success=True)
        except Exception as e:
            return E4k_Company_Create(success=False, error=str(e))



# update company 
class E4k_Company_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        name = graphene.String()
        address1 = graphene.String()
        address2 = graphene.String()
        address3 = graphene.String()
        address4 = graphene.String()
        postcode = graphene.String()
        phone = graphene.String()
        fax = graphene.String()
        email = graphene.String()
        vatno = graphene.String()
        holdingcompany = graphene.String()
        countryid = graphene.Int()
        currency_code = graphene.Int()

    company = graphene.Field(TblcompanyType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, name=None, address1=None, address2=None, address3=None, address4=None, postcode=None, phone=None, fax=None, email=None, vatno=None, holdingcompany=None, countryid=None, currency_code=None):
        try:
            # Fetch the company instance
            company = Tblcompany.objects.get(pk=companyid)
            errors = []

            # Validate fields and update them if provided
            if name is not None:
                company.name = name

            if address1 is not None:
                company.address1 = address1

            if address2 is not None:
                company.address2 = address2

            if address3 is not None:
                company.address3 = address3

            if address4 is not None:
                company.address4 = address4

            if postcode is not None:
                company.postcode = postcode

            if phone is not None:
                if not phone.isdigit():
                    errors.append("Phone number should contain only digits.")
                else:
                    company.phone = phone

            if fax is not None:
                if not fax.isdigit():
                    errors.append("Fax number should contain only digits.")
                else:
                    company.fax = fax

            if email is not None:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    errors.append("Invalid email format.")
                elif Tblcompany.objects.filter(email=email).exclude(pk=companyid).exists():
                    errors.append("Email already exists.")
                else:
                    company.email = email

            if vatno is not None:
                company.vatno = vatno

            if holdingcompany is not None:
                company.holdingcompany = holdingcompany

            if countryid is not None:
                try:
                    country_instance = TblbusCountries.objects.get(countryid=countryid)
                    company.countryid = country_instance
                except TblbusCountries.DoesNotExist:
                    errors.append("CountryID does not exist.")
            
            if currency_code is not None:
                try:
                    currency_instance = TblbusCurrencies.objects.get(currency_code=currency_code)
                    company.currency_code = currency_instance
                except TblbusCurrencies.DoesNotExist:
                    errors.append("Currency code does not exist.")

            # If there are errors, return the errors
            if errors:
                return E4k_Company_Update(success=False, error=", ".join(errors))

            # Save the updated company instance
            company.save()
            return E4k_Company_Update(company=company, success=True)
        except Tblcompany.DoesNotExist:
            return E4k_Company_Update(success=False, error="CompanyID does not exist.")
        except Exception as e:
            return E4k_Company_Update(success=False, error=str(e))



# Delete opertation in company tbl recorde by using companyid
class E4k_Company_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
#  if  delete sucess 
    success = graphene.Boolean()

    def mutate(self, info, companyid):
        try:
            company = Tblcompany.objects.get(pk=companyid)
            company.delete()
            return E4k_Company_Delete(success=True)
        except Tblcompany.DoesNotExist:
            return E4k_Company_Delete(success=False)
        


# Country tbl Mutation
class E4k_Country_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        country = graphene.String()
        member = graphene.Int()

    country = graphene.Field(TblbusCountriesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, country=None, member=None):
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblbus_countries', field_name='CountryID', companyid=companyid)

        # Validate if the CountryID already exists
        if TblbusCountries.objects.filter(countryid=next_no).exists():
            return E4k_Country_Create(success=False, error="CountryID already exists.")

        # Validate if the company exists
        try:
            company = Tblcompany.objects.get(companyid=companyid)
        except Tblcompany.DoesNotExist:
            return E4k_Country_Create(success=False, error="CompanyID does not exist.")
            
        try:
            member = TblbusCountryMembers.objects.get(companyid=companyid,groupid=member)
        except TblbusCountryMembers.DoesNotExist:
            return E4k_Country_Create(success=False, error="MemberID does not exist.")
        if TblbusCountries.objects.filter(companyid = member.companyid, country= country).exists():
            return E4k_Country_Create(success=False, error="Country already exists in this company.")
       
        # Create the country instance
        country_instance = TblbusCountries(
            companyid=company,
            countryid=next_no,
            country=country,
            member=member
        )
        country_instance.save()

        return E4k_Country_Create(country=country_instance, success=True)


# Update Country Mutation
class E4K_Country_Update(graphene.Mutation):
    class Arguments:
        countryid = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        country = graphene.String(required=True)
        member = graphene.Int(required=True)

    country = graphene.Field(TblbusCountriesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, countryid, companyid=None, country=None, member=None):
        errors = []

        try:
            # Fetch the country instance to update
            country_instance = TblbusCountries.objects.get(companyid= companyid, countryid=countryid)

            # Validate companyid
            if country is not None:
                TblbusCountries.objects.filter(companyid= country_instance.companyid , country = country)
                return E4K_Country_Update(success=False, error="Country already exists in this company.")
            if companyid is not None:
                try:
                    company_instance = Tblcompany.objects.get(companyid=companyid)
                    country_instance.companyid = company_instance
                except Tblcompany.DoesNotExist:
                    errors.append("CompanyID does not exist.")
            
            # Validate country
            if country is not None:
                if len(country.strip()) == 0:
                    errors.append("Country name cannot be empty.")
                else:
                    country_instance.country = country
            
            # Validate member_id
            if member is not None:
                try:
                    member_instance = TblbusCountryMembers.objects.get(groupid = member)
                    country_instance.member = member_instance
                except TblbusCountryMembers.DoesNotExist:
                    errors.append("MemberID does not exist.")

            # If there are errors, return the errors
            if errors:
                return E4K_Country_Update(success=False, error=", ".join(errors))

            # Save the updated country instance
            country_instance.save()
            return E4K_Country_Update(country=country_instance, success=True)
        except TblbusCountries.DoesNotExist:
            return E4K_Country_Update(success=False, error="CountryID does not exist.")
        except Exception as e:
            return E4K_Country_Update(success=False, error=str(e))


# Delete Country by using countryid
class E4k_Country_Delete(graphene.Mutation):
    class Arguments:
        countryid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, countryid):
        try:
            country_instance = TblbusCountries.objects.get(countryid=countryid, companyid= companyid)
            country_instance.delete()
           
            return E4k_Country_Delete(success=True)
        except TblbusCountries.DoesNotExist:
            return E4k_Country_Delete(success=False)

# Create, Update, and Delete Mutations for TblbusCountryMembers
class E4k_CountryMember_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        group_name = graphene.String(required=True)

    country_member = graphene.Field(TblbusCountryMembersType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, group_name):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(pk=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
        
        # Validate group name
        if not group_name or group_name.strip() == "":
            errors.append("Group name is required.")
        
        # Check if the group name already exists for the company
        if TblbusCountryMembers.objects.filter(companyid=company, group_name=group_name).exists():
            errors.append("Group name already exists within the company.")

        if errors:
            return E4k_CountryMember_Create(success=False, error=", ".join(errors))
        
        # Generate the next GroupID
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblbus_country_members', field_name='GroupID', companyid=companyid)
        
        # Create the country member instance
        try:
            country_member_instance = TblbusCountryMembers(
                companyid=company,
                groupid=next_no,
                group_name=group_name
            )
            country_member_instance.save()
            return E4k_CountryMember_Create(country_member=country_member_instance, success=True)
        except Exception as e:
            return E4k_CountryMember_Create(success=False, error=str(e))
############################################# 

class E4k_CountryMember_Update(graphene.Mutation):
    class Arguments:
        groupid = graphene.Int(required=True)
        companyid = graphene.String()
        group_name = graphene.String()

    country_member = graphene.Field(TblbusCountryMembersType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, groupid, companyid=None, group_name=None):
        errors = []

        try:
            country_member_instance = TblbusCountryMembers.objects.get(pk=groupid)
        except TblbusCountryMembers.DoesNotExist:
            return E4k_CountryMember_Update(success=False, error="Country member not found.")
        
        # Validate and update company ID
        if companyid:
            try:
                company_instance = Tblcompany.objects.get(pk=companyid)
                country_member_instance.companyid = company_instance
            except Tblcompany.DoesNotExist:
                errors.append("CompanyID does not exist.")

        # Validate group name
        if group_name:
            if group_name.strip() == "":
                errors.append("Group name cannot be empty.")
            elif TblbusCountryMembers.objects.filter(companyid=country_member_instance.companyid, group_name=group_name).exists():
                errors.append("Group name already exists within the company.")
            else:
                country_member_instance.group_name = group_name
        
        if errors:
            return E4k_CountryMember_Update(success=False, error=", ".join(errors))

        # Save the updated country member instance
        try:
            country_member_instance.save()
            return E4k_CountryMember_Update(country_member=country_member_instance, success=True)
        except Exception as e:
            return E4k_CountryMember_Update(success=False, error=str(e))

#########################Delete ##########################
class E4k_CountryMember_Delete(graphene.Mutation):
    class Arguments:
        groupid = graphene.Int(required=True)
        companyid   = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid,groupid):
        try:
            country_member_instance = TblbusCountryMembers.objects.get(groupid=groupid,companyid = companyid)
            country_member_instance.delete()
            
            return E4k_CountryMember_Delete(success=True)
        except TblbusCountryMembers.DoesNotExist:
            return E4k_CountryMember_Delete(success=False)

# Currency Mutation for Create , Update , Delete 
class E4k_Currency_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        currency_name = graphene.String(required=True)
        currency_symbol = graphene.String(required=True)
        currency_exchange_rate = graphene.Decimal(required=True)
        isocode = graphene.String(required=True)

    currency = graphene.Field(TblbusCurrenciesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, currency_name, currency_symbol, currency_exchange_rate, isocode):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(companyid=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
        
        # Validate required fields
        if not currency_name or currency_name.strip() == "":
            errors.append("Currency name is required.")
            return E4k_Currency_Create(success =False, error ="Currency name is required.")
        if TblbusCurrencies.objects.filter(companyid= companyid,currency_name=currency_name).exists():
            errors.append("Currency name already exists within the company.")
            return E4k_Currency_Create(success=False, error="Currency name already exists") 
        if not currency_symbol or currency_symbol.strip() == "":
            errors.append("Currency symbol is required.")
            return E4k_Currency_Create(success =False, error ="Currency symbol is required.")
        if currency_exchange_rate is None:
            errors.append("Currency exchange rate is required.")
            return E4k_Currency_Create(success =False, error ="Currency exchange rate is required.")
        if not isocode or isocode.strip() == "":
            errors.append("ISO code is required.")
            return E4k_Currency_Create(success =False, error ="ISO code is required.")
        
        # Check if the ISO code already exists
        if TblbusCurrencies.objects.filter(isocode=isocode).exists():
            errors.append("ISO code already exists.")
            return E4k_Currency_Create(success=False, error=", ".join(errors))

        if errors:
            return E4k_Currency_Create(success=False, error=", ".join(errors))
        
        # Generate the next Currency_Code
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblbus_currencies', field_name='Currency_Code', companyid=companyid)
        
        # Create the currency instance
        try:
            currency_instance = TblbusCurrencies(
                companyid=company,
                currency_code=next_no,
                currency_name=currency_name,
                currency_symbol=currency_symbol,
                currency_exchange_rate=currency_exchange_rate,
                isocode=isocode
            )
            currency_instance.save()
            return E4k_Currency_Create(currency=currency_instance, success=True)
        except Exception as e:
            return E4k_Currency_Create(success=False, error=str(e))

# update operation in  currency tbl
class E4k_Currency_Update(graphene.Mutation):
    class Arguments:
        currency_code = graphene.Int(required=True)
        companyid = graphene.String()
        currency_name = graphene.String()
        currency_symbol = graphene.String()
        currency_exchange_rate = graphene.Decimal()
        isocode = graphene.String()

    currency = graphene.Field(TblbusCurrenciesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, currency_code, companyid=None, currency_name=None, currency_symbol=None, currency_exchange_rate=None, isocode=None):
        errors = []

        try:
            currency_instance = TblbusCurrencies.objects.get(companyid = companyid ,currency_code=currency_code)
        except TblbusCurrencies.DoesNotExist:
            return E4k_Currency_Update(success=False, error="Currency not found.")
        
        # Validate and update company ID
        if companyid:
            try:
                company_instance = Tblcompany.objects.get(companyid=companyid)
                currency_instance.companyid = company_instance
            except Tblcompany.DoesNotExist:
                errors.append("CompanyID does not exist.")

        # Validate and update currency name
        if currency_name:
            if TblbusCurrencies.objects.filter(companyid = companyid ,currency_name=currency_name ).exists():
                return E4k_Currency_Update(success=False, error="Currency name already exists.")

            if currency_name.strip() == "":
                errors.append("Currency name cannot be empty.")
                return E4k_Currency_Update(success=False, error = "Currency name cannot be empty.")
            else:
                currency_instance.currency_name = currency_name
        
        # Validate and update currency symbol
        if currency_symbol:
            if currency_symbol.strip() == "":
                errors.append("Currency symbol cannot be empty.")
                return E4k_Currency_Update(success = False , error = "Currency symbol cannot be empty.")
            else:
                currency_instance.currency_symbol = currency_symbol

        # Validate and update currency exchange rate
        if currency_exchange_rate is not None:
            currency_instance.currency_exchange_rate = currency_exchange_rate

        # Validate and update ISO code
        if isocode:
            if isocode.strip() == "":
                errors.append("ISO code cannot be empty.")
                return E4k_Currency_Update (success=False, error ="ISO code cannot be empty")
            elif TblbusCurrencies.objects.filter(isocode=isocode).exists() and TblbusCurrencies.objects.get(isocode=isocode).currency_code != currency_code:
                errors.append("ISO code already exists.")
                return E4k_Currency_Update(success=False, error="ISO code already exists.")
            else:
                currency_instance.isocode = isocode

        if errors:
            return E4k_Currency_Update(success=False, error=", ".join(errors))

        # Save the updated currency instance
        try:
            currency_instance.save()
            return E4k_Currency_Update(currency=currency_instance, success=True)
        except Exception as e:
            return E4k_Currency_Update(success=False, error=str(e))

# Delete opertation in currency tbl
class E4k_Currency_Delete(graphene.Mutation):
    class Arguments:
        currency_code = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        

    success = graphene.Boolean()

    def mutate(self, info, companyid,currency_code):
        try:
            currency_instance = TblbusCurrencies.objects.get(companyid=companyid,currency_code=currency_code)
            currency_instance.delete()
          
            return E4k_Currency_Delete(success=True) 
            
        
        except TblbusCurrencies.DoesNotExist:
            return E4k_Currency_Delete(success=False)
        
#customercategory1 update,create, delete function

class E4k_CustomerCategory1_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category1name = graphene.String(required=True)

    customer_category1 = graphene.Field(TblcustomerCategory1Type)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, category1name):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(companyid=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
            return E4k_CustomerCategory1_Create(success=False, error="CompanyID does not exist.")

        # Check if category1name already exists for the given companyid
        if TblcustomerCategory1.objects.filter(companyid=company, category1name=category1name).exists():
            return E4k_CustomerCategory1_Create(success=False, error="Category1Name already exists for this company.")

        # Generate the next Category1ID
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblcustomer_category1', field_name='Category1ID', companyid=companyid)
        
        if next_no is None:
            return E4k_CustomerCategory1_Create(success=False, error="Failed to generate next Category1ID")

        # Create the customer category1 instance
        try:
            customer_category1 = TblcustomerCategory1(
                companyid=company,
                category1id=int(next_no),  # Ensure next_no is an integer
                category1name=category1name
            )
            customer_category1.save()
            return E4k_CustomerCategory1_Create(customer_category1=customer_category1, success=True)
        except Exception as e:
            return E4k_CustomerCategory1_Create(success=False, error=str(e))



class E4k_CustomerCategory1_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category1id = graphene.Int(required=True)
        category1name = graphene.String()

    customer_category1 = graphene.Field(TblcustomerCategory1Type)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, category1id, companyid, category1name=None):
        try:
            customer_category1 = TblcustomerCategory1.objects.get(companyid = companyid ,category1id=category1id)
        except TblcustomerCategory1.DoesNotExist:
            return E4k_CustomerCategory1_Update(success=False, error="Category1ID does not exist.")

        if category1name:
            # # Check if the new category1name already exists for the same company
            if TblcustomerCategory1.objects.filter(companyid=customer_category1.companyid, category1name=category1name).exists():
                return E4k_CustomerCategory1_Update(success=False, error="Category1 name already exists for this company.")

            customer_category1.category1name = category1name
            try:
                customer_category1.save()
                return E4k_CustomerCategory1_Update(customer_category1=customer_category1, success=True)
            except Exception as e:
                return E4k_CustomerCategory1_Update(success=False, error=str(e))
        else:
            return E4k_CustomerCategory1_Update(success=False, error="No updates provided.")


class E4k_CustomerCategory1_Delete(graphene.Mutation):
    class Arguments:
        category1id = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, category1id):
        try:
            customer_category1 = TblcustomerCategory1.objects.get(category1id=category1id,companyid=companyid)
            customer_category1.delete()
           
            return E4k_CustomerCategory1_Delete(success=True)
        except TblcustomerCategory1.DoesNotExist:
            return E4k_CustomerCategory1_Delete(success=False)  
        

# Customercategory2 mutation for create,update,delete

class E4k_CustomerCategory2_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category2name = graphene.String(required=True)

    customer_category2 = graphene.Field(Tblbuscustomercategory2Type)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, category2name):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(companyid=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
        

        if TblcustomerCategory2.objects.filter(companyid=company, category2name=category2name).exists():
            errors.append("Category2 name already exists for this company.")

        if errors:
            return E4k_CustomerCategory2_Create(success=False, error=", ".join(errors))

        # Generate the next Category2ID
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblcustomer_category2', field_name='Category2ID', companyid=companyid)
        
        if next_no is None:
            return E4k_CustomerCategory2_Create(success=False, error="Failed to generate next Category2ID")

        
        try:
            customer_category2 = TblcustomerCategory2(
                companyid=company,
                category2id=int(next_no),  # Ensure next_no is an integer
                category2name=category2name
            )
            customer_category2.save()
            return E4k_CustomerCategory2_Create(customer_category2=customer_category2, success=True)
        except Exception as e:
            return E4k_CustomerCategory2_Create(success=False, error=str(e))


class E4k_CustomerCategory2_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category2id = graphene.Int(required=True)
        category2name = graphene.String()

    customer_category2 = graphene.Field(Tblbuscustomercategory2Type)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, category2id,companyid, category2name=None):
        try:
            customer_category2 = TblcustomerCategory2.objects.get(companyid = companyid , category2id=category2id)
        except TblcustomerCategory2.DoesNotExist:
            return E4k_CustomerCategory2_Update(success=False, error="Category2ID does not exist.")

        if category2name:
            # Check if the new category2name already exists for the same company
            if TblcustomerCategory2.objects.filter(companyid=customer_category2.companyid, category2name=category2name).exists():
                return E4k_CustomerCategory2_Update(success=False, error="Category2 name already exists for this company.")

            customer_category2.category2name = category2name
            try:
                customer_category2.save()
                return E4k_CustomerCategory2_Update(customer_category2=customer_category2, success=True)
            except Exception as e:
                return E4k_CustomerCategory2_Update(success=False, error=str(e))
        else:
            return E4k_CustomerCategory2_Update(success=False, error="No updates provided.")


class E4k_CustomerCategory2_Delete(graphene.Mutation):
    class Arguments:
        category2id = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, category2id):
        try:
            customer_category2 = TblcustomerCategory2.objects.get(category2id=category2id,companyid =companyid)
            customer_category2.delete()
           
            return E4k_CustomerCategory2_Delete(success=True)
        except TblcustomerCategory1.DoesNotExist:
            return E4k_CustomerCategory2_Delete(success=False) 
    


# Customercategory3 Mutation Decleration


class E4k_CustomerCategory3_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category3name = graphene.String(required=True)

    customer_category3 = graphene.Field(TblcustomerCategory3Type)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, category3name):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(companyid=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
        
        # Check if category3name already exists for the given company
        if TblcustomerCategory3.objects.filter(companyid=company, category3name=category3name).exists():
            errors.append("Category3 name already exists for this company.")

        if errors:
            return E4k_CustomerCategory3_Create(success=False, error=", ".join(errors))

        # Generate the next Category3ID
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblcustomer_category3', field_name='Category3ID', companyid=companyid)
        
        if next_no is None:
            return E4k_CustomerCategory3_Create(success=False, error="Failed to generate next Category3ID")

        # Create the customer category3 instance
        try:
            customer_category3 = TblcustomerCategory3(
                companyid=company,
                category3id=int(next_no),  # Ensure next_no is an integer
                category3name=category3name
            )
            customer_category3.save()
            return E4k_CustomerCategory3_Create(customer_category3=customer_category3, success=True)
        except Exception as e:
            return E4k_CustomerCategory3_Create(success=False, error=str(e))


class E4k_CustomerCategory3_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        category3id = graphene.Int(required=True)
        category3name = graphene.String()

    customer_category3 = graphene.Field(TblcustomerCategory3Type)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, category3id, companyid ,category3name=None):
        try:
            customer_category3 = TblcustomerCategory3.objects.get(companyid=companyid ,category3id=category3id)
        except TblcustomerCategory3.DoesNotExist:
            return E4k_CustomerCategory3_Update(success=False, error="Category3ID does not exist.")

        if category3name:
            # Check if the new category3name already exists for the same company
            if TblcustomerCategory3.objects.filter(companyid=customer_category3.companyid, category3name=category3name).exists():
                return E4k_CustomerCategory3_Update(success=False, error="Category3 name already exists for this company.")

            customer_category3.category3name = category3name
            try:
                customer_category3.save()
                return E4k_CustomerCategory3_Update(customer_category3=customer_category3, success=True)
            except Exception as e:
                return E4k_CustomerCategory3_Update(success=False, error=str(e))
        else:
            return E4k_CustomerCategory3_Update(success=False, error="No updates provided.")

# customercategory 3 Delete operations
class E4k_CustomerCategory3_Delete(graphene.Mutation):
    class Arguments:
        category3id = graphene.Int(required=True)
        companyid = graphene.String(required=True)


    success = graphene.Boolean()

    def mutate(self, info,companyid, category3id):
        try:
            customer_category3 = TblcustomerCategory3.objects.get(category3id=category3id,companyid=companyid)
            customer_category3.delete()
           
            return E4k_CustomerCategory3_Delete(success=True)
        except TblcustomerCategory3.DoesNotExist:
            return E4k_CustomerCategory3_Delete(success=False)
        

# CustomerClass Mutation for create , Update, Delete
class E4k_CustomerClass_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        class_name = graphene.String(required=True)

    customer_class = graphene.Field(TblcustomerClassType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, class_name):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(companyid=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
        
        # Check if class_name already exists for the given company
        if TblcustomerClass.objects.filter(companyid=company, class_name=class_name).exists():
            errors.append("Class name already exists for this company.")

        if errors:
            return E4k_CustomerClass_Create(success=False, error=", ".join(errors))

        # Generate the next ClassID
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblcustomer_class', field_name='ClassID', companyid=companyid)
        
        if next_no is None:
            return E4k_CustomerClass_Create(success=False, error="Failed to generate next ClassID")

        # Create the customer class instance
        try:
            customer_class = TblcustomerClass(
                companyid=company,
                classid=int(next_no),  # Ensure next_no is an integer
                class_name=class_name
            )
            customer_class.save()
            return E4k_CustomerClass_Create(customer_class=customer_class, success=True)
        except Exception as e:
            return E4k_CustomerClass_Create(success=False, error=str(e))


class E4k_CustomerClass_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        classid = graphene.Int(required=True)
        class_name = graphene.String()

    customer_class = graphene.Field(TblcustomerClassType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, classid,companyid, class_name=None):
        try:
            customer_class = TblcustomerClass.objects.get(companyid=companyid,classid=classid)
        except TblcustomerClass.DoesNotExist:
            return E4k_CustomerClass_Update(success=False, error="ClassID does not exist.")

        if class_name:
            # Check if the new class_name already exists for the same company
            if TblcustomerClass.objects.filter(companyid=customer_class.companyid, class_name=class_name).exists():
                return E4k_CustomerClass_Update(success=False, error="Class name already exists for this company.")

            customer_class.class_name = class_name
            try:
                customer_class.save()
                return E4k_CustomerClass_Update(customer_class=customer_class, success=True)
            except Exception as e:
                return E4k_CustomerClass_Update(success=False, error=str(e))
        else:
            return E4k_CustomerClass_Update(success=False, error="No updates provided.")


class E4k_CustomerClass_Delete(graphene.Mutation):
    class Arguments:
        classid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, classid):
        try:
            customer_class = TblcustomerClass.objects.get(companyid =companyid ,classid=classid)
            customer_class.delete()
           
            return E4k_CustomerClass_Delete(success=True)

        except TblcustomerClass.DoesNotExist:
            return E4k_CustomerClass_Delete(success=False)

  # Group Tbl Mutation for Create,update,delete

class E4K_TblbusGroup_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        groupname = graphene.String(required=True)

    group = graphene.Field(TblbusGroupsType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, groupname):
        errors = []

        # Validate company ID
        try:
            company = Tblcompany.objects.get(companyid=companyid)
        except Tblcompany.DoesNotExist:
            errors.append("CompanyID does not exist.")
        
        # Check if groupname already exists for the given company
        if TblbusGroups.objects.filter(companyid=company, groupname=groupname).exists():
            errors.append("Group name already exists for this company.")

        if errors:
            return E4K_TblbusGroup_Create(success=False, error=", ".join(errors))

        # Generate the next GroupID
        autonumber = NextNo()
        next_no = autonumber.get_next_no(table_name='tblbus_groups', field_name='GroupID', companyid=companyid)
        
        if next_no is None:
            return E4K_TblbusGroup_Create(success=False, error="Failed to generate next GroupID")

        # Create the group instance
        try:
            group = TblbusGroups(
                companyid=company,
                groupid=next_no,
                groupname=groupname
            )
            group.save()
            return E4K_TblbusGroup_Create(group=group, success=True)
        except Exception as e:
            return E4K_TblbusGroup_Create(success=False, error=str(e))


class E4k_TblbusGroup_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        groupid = graphene.Int(required=True)
        groupname = graphene.String()

    group = graphene.Field(TblbusGroupsType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, groupid,companyid, groupname=None):
        try:
            group = TblbusGroups.objects.get(groupid=groupid, companyid=companyid)
        except TblbusGroups.DoesNotExist:
            return E4k_TblbusGroup_Update(success=False, error="GroupID does not exist.")

        if groupname:
            # Check if the new groupname already exists for the same company
            if TblbusGroups.objects.filter(companyid=group.companyid, groupname=groupname).exists():
                return E4k_TblbusGroup_Update(success=False, error="Group name already exists for this company.")

            group.groupname = groupname
            try:
                group.save()
                return E4k_TblbusGroup_Update(group=group, success=True)
            except Exception as e:
                return E4k_TblbusGroup_Update(success=False, error=str(e))
        else:
            return E4k_TblbusGroup_Update(success=False, error="No updates provided.")

class E4k_TblbusGroup_Delete(graphene.Mutation):
    class Arguments:
        groupid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, groupid):
        try:
            group = TblbusGroups.objects.get(groupid=groupid, companyid=companyid)
            group.delete()
          
            return E4k_TblbusGroup_Delete(success=True)
        except TblbusGroups.DoesNotExist:
            return E4k_TblbusGroup_Delete(success=False)

# class CreateTblaccNominal(graphene.Mutation):
class E4k_TblaccNominal_create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        nomcode = graphene.String(required=True)
        nomdescription = graphene.String()
        nomdc = graphene.String()
        nompl = graphene.Int()
        nombs = graphene.Int()
        live = graphene.Boolean()

    nominal = graphene.Field(TblaccNominalType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(
        self, 
        info, 
        companyid, 
        nomcode=None, 
        nomdescription=None, 
        nomdc=None, 
        nompl=None, 
        nombs=None, 
        live=True
    ):  
        # Check for duplicate `nomcode`
        if TblaccNominal.objects.filter(companyid=companyid, nomcode=nomcode).exists():
            return E4k_TblaccNominal_create(success=False, error="Nominal code already exists!")

        # Check for duplicate `nomdescription`
        if nomdescription and TblaccNominal.objects.filter(companyid=companyid, nomdescription=nomdescription).exists():
            return E4k_TblaccNominal_create(success=False, error="Nominal description already exists!")

        try:
            # Create and save new nominal record
            nominal = TblaccNominal(
                companyid_id=companyid,
                nomcode=nomcode,
                nomdescription=nomdescription,
                nomdc=nomdc,
                nompl=nompl,
                nombs=nombs,
                live=live
            )
            nominal.save()
            return E4k_TblaccNominal_create(nominal=nominal, success=True)

        except Exception as e:
            return E4k_TblaccNominal_create(success=False, error=str(e))




class E4k_TblaccNominal_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        nomcode = graphene.String(required=True)
        nomdescription = graphene.String()
        nomdc = graphene.String()
        nompl = graphene.Int()
        nombs = graphene.Int()
        live = graphene.Boolean()

    nominal = graphene.Field(TblaccNominalType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nomcode,companyid, nomdescription=None, nomdc=None, nompl=None, nombs=None, live=None):
        try:
            nominal = TblaccNominal.objects.get(companyid =companyid ,nomcode=nomcode)
        except TblaccNominal.DoesNotExist:
            return E4k_TblaccNominal_Update(success=False, error="Nominal code does not exist!")
        
            
          
        if nomdescription is not None:
            if TblaccNominal.objects.filter(companyid= companyid ,nomdescription=nomdescription).exists():
                return E4k_TblaccNominal_Update(success=False, error="Nominal description already exists!")
            
            nominal.nomdescription = nomdescription
        if nomdc is not None:
            nominal.nomdc = nomdc
        if nompl is not None:
            nominal.nompl = nompl
        if nombs is not None:
            nominal.nombs = nombs
        if live is not None:
            nominal.live = live

        try:
            nominal.save()
            return E4k_TblaccNominal_Update(nominal=nominal, success=True)
        except Exception as e:
            return E4k_TblaccNominal_Update(success=False, error=str(e))

class E4k_TblaccNominal_Delete(graphene.Mutation):
    class Arguments:
        nomcode = graphene.String(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, nomcode):
        try:
            nominal = TblaccNominal.objects.get(nomcode=nomcode,companyid=companyid)
            nominal.delete()
           
            return E4k_TblaccNominal_Delete(success=True)
        except TblaccNominal.DoesNotExist:
            return E4k_TblaccNominal_Delete(success=False)
        
# TblaccVATCode Mutation for cerate update delete

class E4k_TblaccVatcodes_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        description = graphene.String()
        vatpercent = graphene.Decimal()
        sagecode = graphene.String()

    vatcode = graphene.Field(TblaccVatcodesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, description=None, vatpercent=None, sagecode=None):
        errors = []

        try:
            # Check if a record with the same companyid and description already exists
            if description:
                existing_record = TblaccVatcodes.objects.filter(companyid=companyid, description=description)
                if existing_record.exists():
                    errors.append("A record with the same description already exists.")
                    return E4k_TblaccVatcodes_Create( success =False, error ="A record with the same description already exists.")
            
            # Generate the next VAT code
            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblacc_vatcodes', field_name='VATCode', companyid=companyid)
            
            if next_no is None:
                errors.append("Failed to generate next VAT code.")
            
            # Validate vatpercent
            if vatpercent is not None:
                if vatpercent < 0 or vatpercent > 100:
                    errors.append("vatpercent must be between 0 and 100.")

            if errors:
                return E4k_TblaccVatcodes_Create(success=False, error=", ".join(errors))

            # Create VAT code instance
            vatcode_obj = TblaccVatcodes(
                companyid_id=companyid,
                vatcode=next_no,
                description=description,
                vatpercent=vatpercent,
                sagecode=sagecode
            )
            vatcode_obj.save()
            return E4k_TblaccVatcodes_Create(vatcode=vatcode_obj, success=True)

        except Exception as e:
            return E4k_TblaccVatcodes_Create(success=False, error=str(e))


class E4k_TblaccVatcodes_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        vatcode = graphene.Int(required=True)
        description = graphene.String()
        vatpercent = graphene.Float()
        sagecode = graphene.String()

    vatcode = graphene.Field(TblaccVatcodesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, vatcode, companyid,description=None, vatpercent=None, sagecode=None):
        errors = []

        try:
            vatcode_obj = TblaccVatcodes.objects.get(companyid = companyid ,vatcode=vatcode)

            # Validate vatpercent
            if vatpercent is not None:
                if vatpercent < 0 or vatpercent > 100:
                    errors.append("vatpercent must be between 0 and 100.")

            # Check for duplicate companyid and description
            if description:
                # Assuming TblaccVatcodes has a companyid field
                existing_record = TblaccVatcodes.objects.filter(companyid=vatcode_obj.companyid, description=description).exclude(vatcode=vatcode)
                if existing_record.exists():
                    errors.append("A record with the same companyid and description already exists.")
                    return E4k_TblaccVatcodes_Update( success = False,  error="A record with the same  description already exists.")

            # If errors exist, return them
            if errors:
                return E4k_TblaccVatcodes_Update(success=False, error=", ".join(errors))

            # Proceed with the update if no validation errors
            if description is not None:
                vatcode_obj.description = description
            if vatpercent is not None:
                vatcode_obj.vatpercent = vatpercent
            if sagecode is not None:
                vatcode_obj.sagecode = sagecode
            
            vatcode_obj.save()
            return E4k_TblaccVatcodes_Update(vatcode=vatcode_obj, success=True)

        except TblaccVatcodes.DoesNotExist:
            return E4k_TblaccVatcodes_Update(success=False, error="VAT code does not exist.")
        except Exception as e:
            return E4k_TblaccVatcodes_Update(success=False, error=str(e))

class E4k_TblaccVatcodes_Delete(graphene.Mutation):
    class Arguments:
        vatcode = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, vatcode):
        try:
            vatcode_obj = TblaccVatcodes.objects.get(vatcode=vatcode,companyid=companyid)
            vatcode_obj.delete()
           
            return E4k_TblaccVatcodes_Delete(success=True)
        except TblaccVatcodes.DoesNotExist:
            return E4k_TblaccVatcodes_Delete(success=False)

################# Create #############################

class E4k_TblbusServicePeople_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        csname = graphene.String()

    service_person = graphene.Field(TblbusServicePeopleType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, csname=None):
        try:
            # Check if companyid exists
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblbusServicePeople_Create(success=False, error="Company with provided ID does not exist.")

            autonumer = NextNo()
            next_no = autonumer.get_next_no(table_name='tblbus_service_people', field_name='CSGroupID', companyid=companyid)
            
            # validate next_no if needed

            if next_no is None:
                return E4k_TblbusServicePeople_Create(success=False, error="Failed to generate next CSGroupID.")
            
            service_person = TblbusServicePeople(
                companyid_id=companyid,
                csgroupid=next_no,
                csname=csname
            )
            service_person.save()
            return E4k_TblbusServicePeople_Create(service_person=service_person, success=True)
        except Exception as e:
            return E4k_TblbusServicePeople_Create(success=False, error=str(e))


# Ensure that TblbusServicePeopleType is correctly defined as follows:



class E4k_TblbusServicePeople_Update(graphene.Mutation):
    class Arguments:
        csgroupid = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        csname = graphene.String()

    service_person = graphene.Field(TblbusServicePeopleType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, csgroupid, companyid, csname=None):
        try:
            # Check if the service person exists based on csgroupid and companyid
            try:
                service_person = TblbusServicePeople.objects.get(csgroupid=csgroupid, companyid=companyid)
            except TblbusServicePeople.DoesNotExist:
                return E4k_TblbusServicePeople_Update(success=False, error="Service person with provided IDs does not exist.")

            # Validate csname if provided
            if csname:
                # Add your csname validation logic here, e.g., length, format, etc.
                if len(csname) > 50:  # Example validation for maximum length
                    return E4k_TblbusServicePeople_Update(success=False, error="csname must be maximum 50 characters long.")

                service_person.csname = csname

            service_person.save()
            return E4k_TblbusServicePeople_Update(service_person=service_person, success=True)
        except Exception as e:
            return E4k_TblbusServicePeople_Update(success=False, error=str(e))


############## Delete #################
class E4k_TblbusServicePeople_Delete(graphene.Mutation):
    class Arguments:
        csgroupid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, csgroupid):
        service_person = TblbusServicePeople.objects.get(csgroupid=csgroupid,companyid=companyid)
        service_person.delete()
       
        return E4k_TblbusServicePeople_Delete(success=True)
    

# TblbusSalesPeople Create, Update, Delete 
    
class E4k_TblbusSalesPeople_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        repkey = graphene.String()
        forename = graphene.String()
        surname = graphene.String()
        live = graphene.Boolean()

    success = graphene.Boolean()
    error = graphene.String()
    sales_person = graphene.Field(TblbusSalesPeopleType)

    def mutate(self, info, companyid, repkey, forename, surname, live=True):
        try:
            # Check if a person with the same forename and surname already exists for the given companyid
            existing_salesperson = TblbusSalesPeople.objects.filter(companyid=companyid, forename=forename, surname=surname)
            if existing_salesperson.exists():
                return E4k_TblbusSalesPeople_Create(success=False, error="A sales person with the same forename and surname already exists.")

            # Validate repkey length
            # if len(repkey) > 20:
            #     raise ValueError("Repkey must be a maximum of 20 characters long.")

            # Generate the next RepID using autonumber
            autonumer = NextNo()
            next_no = autonumer.get_next_no(table_name='tblbus_sales_people', field_name='RepID', companyid=companyid)

            # Create the new sales person record
            sales_person = TblbusSalesPeople(
                companyid_id=companyid,
                repid=next_no,
                repkey=repkey,
                forename=forename,
                surname=surname,
                live=live
            )
            sales_person.save()

            return E4k_TblbusSalesPeople_Create(success=True, error=None, sales_person=sales_person)

        except ValueError as e:
            return E4k_TblbusSalesPeople_Create(success=False, error=str(e))
        except Exception as e:
            return E4k_TblbusSalesPeople_Create(success=False, error="An unexpected error occurred.")



class E4k_TblbusSalesPeople_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        repid = graphene.Int(required=True)
        repkey = graphene.String()
        forename = graphene.String()
        surname = graphene.String()
        live = graphene.Boolean()

    success = graphene.Boolean()
    error = graphene.String()
    sales_person = graphene.Field(TblbusSalesPeopleType)

    def mutate(self, info, companyid, repid, repkey=None, forename=None, surname=None, live=None):
        try:
            sales_person = TblbusSalesPeople.objects.get(companyid=companyid, repid=repid)
            
            if  TblbusSalesPeople.objects.filter(companyid=sales_person.companyid,forename=forename, surname=surname ).exists():
                return E4k_TblbusSalesPeople_Update(success=False, error="A sales person with the same forename and surname already exists.")

            if repkey is not None:
                if len(repkey) > 20:
                    raise ValueError("Repkey must be a maximum of 20 characters long.")
                sales_person.repkey = repkey

            if forename is not None:
                sales_person.forename = forename

            if surname is not None:
                sales_person.surname = surname

            if live is not None:
                sales_person.live = live

            sales_person.save()
            return E4k_TblbusSalesPeople_Update(success=True, error=None, sales_person=sales_person)

        except TblbusSalesPeople.DoesNotExist:
            return E4k_TblbusSalesPeople_Update(success=False, error="Sales person not found.")
        except ValueError as e:
            return E4k_TblbusSalesPeople_Update(success=False, error=str(e))
        except Exception as e:
            return E4k_TblbusSalesPeople_Update(success=False, error="An unexpected error occurred.")



class E4k_TblbusSalesPeople_Delete(graphene.Mutation):
    class Arguments:
        repid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info,companyid, repid):
        sales_person = TblbusSalesPeople.objects.get(repid=repid,companyid = companyid)
        sales_person.delete()
        
        return E4k_TblbusSalesPeople_Delete(success=True)

 #  TblbusPaymenttermsRef Tbl Mutation for Create,Update,delete

class E4K_TblbusPaymenttermsRef_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        term_type_name = graphene.String(required=True)
        term_type_formula = graphene.String(required=True)

    Payment_Ref = graphene.Field(TblbusPaymenttermsRefType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, term_type_name, term_type_formula):
        try:
            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblbus_paymentterms_ref', field_name='Term_TypeID', companyid=companyid)
            if not next_no:
                return E4K_TblbusPaymenttermsRef_Create(success=False, error="No auto numbers found for Term_TypeID.")
            
            # Validate companyid
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4K_TblbusPaymenttermsRef_Create(success=False, error="CompanyID does not exist.")
            
            # Validate term_type_name
            if not term_type_name:
                return E4K_TblbusPaymenttermsRef_Create(success=False, error="Term type name is required.")
            
            # Validate term_type_formula
            if not term_type_formula:
                return E4K_TblbusPaymenttermsRef_Create(success=False, error="Term type formula is required.")
            
            if TblbusPaymenttermsRef.objects.filter(term_typeid=next_no).exists():
                return E4K_TblbusPaymenttermsRef_Create(success=False, error="Term Type ID already exists.")

            Payment_Ref = TblbusPaymenttermsRef(
                companyid_id=companyid,
                term_typeid=next_no,
                term_type_name=term_type_name,
                term_type_formula=term_type_formula
            )
            Payment_Ref.save()
            return E4K_TblbusPaymenttermsRef_Create(Payment_Ref=Payment_Ref, success=True)
        except Exception as e:
            return E4K_TblbusPaymenttermsRef_Create(success=False, error=str(e))

   ###############Update############################# 
class E4k_TblbusPaymenttermsRef_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        term_typeid = graphene.Int(required=True)
        term_type_name = graphene.String()
        term_type_formula = graphene.String()

    paymenttermsref = graphene.Field(TblbusPaymenttermsRefType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, term_typeid, term_type_name=None, term_type_formula=None):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblbusPaymenttermsRef_Update(success=False, error="CompanyID does not exist.")
            
            paymenttermsref = TblbusPaymenttermsRef.objects.get(companyid=companyid, term_typeid=term_typeid)

            if term_type_name is not None:
                if not term_type_name:
                    return E4k_TblbusPaymenttermsRef_Update(success=False, error="Term type name cannot be empty.")
                paymenttermsref.term_type_name = term_type_name
            
            if term_type_formula is not None:
                if not term_type_formula:
                    return E4k_TblbusPaymenttermsRef_Update(success=False, error="Term type formula cannot be empty.")
                paymenttermsref.term_type_formula = term_type_formula

            paymenttermsref.save()
            return E4k_TblbusPaymenttermsRef_Update(paymenttermsref=paymenttermsref, success=True)
        except TblbusPaymenttermsRef.DoesNotExist:
            return E4k_TblbusPaymenttermsRef_Update(success=False, error='Payment terms reference not found')
        except Exception as e:
            return E4k_TblbusPaymenttermsRef_Update(success=False, error=str(e))

  ################## Delete ######################################      
class E4k_TblbusPaymenttermsRef_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        term_typeid = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid, term_typeid):
        try:
            paymenttermsref = TblbusPaymenttermsRef.objects.get(companyid=companyid, term_typeid=term_typeid)
            paymenttermsref.delete()
        
            return E4k_TblbusPaymenttermsRef_Delete(success=True)
        except TblbusPaymenttermsRef.DoesNotExist:
            raise Exception('Payment terms reference not found')






#   Paymetterms Tbl Mutation for delete update create
class E4k_TblbusPaymentterms_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        typeid = graphene.Int(required=True)
        description = graphene.String()
        days = graphene.Int()

    paymentterms = graphene.Field(TblbusPaymenttermsType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, typeid, description=None, days=None):
        try:
            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblbus_paymentterms', field_name='PaymentTermsID', companyid=companyid)
            if not next_no:
                return E4k_TblbusPaymentterms_Create(success=False, error="No auto numbers found for PaymentTermsID.")
            
            # Validate companyid
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblbusPaymentterms_Create(success=False, error="CompanyID does not exist.")
            
            # Validate typeid
            if not TblbusPaymenttermsRef.objects.filter(term_typeid=typeid).exists():
                return E4k_TblbusPaymentterms_Create(success=False, error="TypeID does not exist.")
            if TblbusPaymentterms.objects.filter(companyid =companyid, description =description).exists():
                return E4k_TblbusPaymentterms_Create(success=False, error="Description already exists.")

            # Validate days
            if days is not None and days < 0:
                return E4k_TblbusPaymentterms_Create(success=False, error="Days must be a positive integer.")
            # if days is not None and days > 30:
            #     return E4k_TblbusPaymentterms_Create(success=False, error="Days must be less than or equal to 30.")
            

            paymentterms = TblbusPaymentterms(
                companyid_id=companyid,
                paymenttermsid=next_no,
                typeid_id=typeid,
                description=description,
                days=days
            )
            paymentterms.save()
            return E4k_TblbusPaymentterms_Create(paymentterms=paymentterms, success=True)
        except Exception as e:
            return E4k_TblbusPaymentterms_Create(success=False, error=str(e))



###########################Update#############################


class E4k_TblbusPaymentterms_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        paymenttermsid = graphene.Int(required=True)
        typeid = graphene.Int()
        description = graphene.String()
        days = graphene.Int()

    paymentterms = graphene.Field(TblbusPaymenttermsType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, paymenttermsid, typeid=None, description=None, days=None):
        try:
            # Validate companyid
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblbusPaymentterms_Update(success=False, error="CompanyID does not exist.")
            
            paymentterms = TblbusPaymentterms.objects.get(companyid=companyid, paymenttermsid=paymenttermsid)
            
            if typeid is not None:
                if not TblbusPaymenttermsRef.objects.filter(term_typeid=typeid).exists():
                    return E4k_TblbusPaymentterms_Update(success=False, error="TypeID does not exist.")
                paymentterms.typeid_id = typeid
            
            if description is not None:
                if TblbusPaymentterms.objects.filter(companyid = companyid , description=description).exists():
                    return E4k_TblbusPaymentterms_Update(success=False, error="Description already exists.")
                paymentterms.description = description
            
            if days is not None:
                if days < 0:
                    return E4k_TblbusPaymentterms_Update(success=False, error="Days must be a positive integer.")
                paymentterms.days = days
            
            paymentterms.save()
            return E4k_TblbusPaymentterms_Update(paymentterms=paymentterms, success=True)
        except TblbusPaymentterms.DoesNotExist:
            return E4k_TblbusPaymentterms_Update(success=False, error='Payment terms not found')
        except Exception as e:
            return E4k_TblbusPaymentterms_Update(success=False, error=str(e))






#######################Delete############################################################## #       
class E4k_TblbusPaymentterms_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        paymenttermsid = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid, paymenttermsid):
        try:
            paymentterms = TblbusPaymentterms.objects.get(companyid=companyid, paymenttermsid=paymenttermsid)
            paymentterms.delete()
            
            return E4k_TblbusPaymentterms_Delete(success=True)
        except TblbusPaymentterms.DoesNotExist:
            raise Exception('Payment terms not found')


# TblaccNominalTran Tbl Create, Update , Delete
class E4k_TblaccNominalTran_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        nomcode = graphene.String()
        year = graphene.Int()
        period = graphene.Int()
        trantype = graphene.String()
        businessid = graphene.String()
        tranreference = graphene.String()
        source = graphene.Int()
        # debitcredit = graphene.String()
        amount = graphene.Decimal()
        nomledger = graphene.String()
        batchno = graphene.Int()
        narrative = graphene.String()

    nominaltran = graphene.Field(TblaccNominalTranType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, nomcode=None, year=None, period=None, trantype=None, businessid=None, tranreference=None, source=None, debitcredit=None, amount=None, nomledger=None, batchno=None, narrative=None):
        try:
            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblacc_nominal_tran', field_name='TransactionNo', companyid=companyid)
            if not next_no:
                return E4k_TblaccNominalTran_Create(success=False, error="No auto numbers found for TransactionNo.")

            batch_no = autonumber.get_next_no(table_name='tblacc_nominal_tran', field_name='BatchNo', companyid=companyid)
            if not batch_no:
                return E4k_TblaccNominalTran_Create(success=False, error="No auto numbers found for BatchNo.")
            
            if trantype not in ["INV", "CRN"]:
                return E4k_TblaccNominalTran_Create(success=False, error="Invalid transaction type. Only 'INV' and 'CRN' are allowed.")
            # if debitcredit not in ["D", "C"]:
            #     return E4k_TblaccNominalTran_Create(success=False, error="Invalid debitcredit. Only 'D' and 'C' are allowed.")
            if nomledger not in ["SP"]:
                return E4k_TblaccNominalTran_Create(success=False, error="Invalid nomledger. Only 'SP' is allowed.")
            trandate = datetime.now()

            # Validate foreign keys
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblaccNominalTran_Create(success=False, error="CompanyID does not exist.")
            if businessid and not Tblcustomer.objects.filter(businessid=businessid).exists():
                return E4k_TblaccNominalTran_Create(success=False, error="BusinessID does not exist.")
            if nomcode and not TblaccNominal.objects.filter(nomcode=nomcode).exists():
                return E4k_TblaccNominalTran_Create(success=False, error="Nomcode does not exist.")

            # Get debitcredit from TblaccNominal based on nomcode
            if nomcode:
                try:
                    nominal = TblaccNominal.objects.get(nomcode=nomcode)
                    debitcredit = nominal.nomdc
                except TblaccNominal.DoesNotExist:
                    return E4k_TblaccNominalTran_Create(success=False, error="Nomcode does not exist.")
                
            nominaltran = TblaccNominalTran(
                companyid_id=companyid,
                transactionno=next_no,
                nomcode_id=nomcode,
                year=year,
                period=period,
                trandate=trandate,
                trantype=trantype,
                businessid_id=businessid,
                tranreference=tranreference,
                source=source,
                debitcredit=debitcredit,
                amount=amount,
                nomledger=nomledger,
                batchno=batch_no,
                narrative=narrative
            )
            nominaltran.save()
            return E4k_TblaccNominalTran_Create(nominaltran=nominaltran, success=True)

        except Exception as e:
            return E4k_TblaccNominalTran_Create(success=False, error=str(e))

########################Delete #############################################################
class E4k_TblaccNominalTran_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        transactionno = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid, transactionno):
        try:
            nominaltran = TblaccNominalTran.objects.get(companyid=companyid, transactionno=transactionno)
            nominaltran.delete()
            return E4k_TblaccNominalTran_Delete(success=True)
        except TblaccNominalTran.DoesNotExist:
            raise Exception('Nominal transaction entry not found')

# AddressTypeRef Tbl Mutation for Delete,Update,Create

class E4k_TblbusAddresstypeRef_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        name = graphene.String()

    addresstype = graphene.Field(TblbusAddresstypeRefType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, name=None):
        try:
            # Validate companyid
            try:
                company = Tblcompany.objects.get(companyid=companyid)
            except Tblcompany.DoesNotExist:
                return E4k_TblbusAddresstypeRef_Create(success=False, error=f"Company with id {companyid} does not exist")
            
            # Validate name
            if name is None or name.strip() == "":
                return E4k_TblbusAddresstypeRef_Create(success=False, error="Name cannot be empty")

            # Generate next number
            autonumer = NextNo()
            next_no = autonumer.get_next_no(table_name='tblbus_addresstype_ref', field_name='Actual_TypeID', companyid=companyid)
            if not next_no:
                return E4k_TblbusAddresstypeRef_Create(success=False, error="Failed to generate next Actual_TypeID")
            
            # Check if name already exists for the company
            if TblbusAddresstypeRef.objects.filter(companyid=company, name=name).exists():
                return E4k_TblbusAddresstypeRef_Create(success=False, error="Address type name already exists for this company")

            addresstype = TblbusAddresstypeRef.objects.create(
                companyid=company,
                actual_typeid=next_no,
                name=name
            )
            return E4k_TblbusAddresstypeRef_Create(addresstype=addresstype, success=True)
        except Exception as e:
            return E4k_TblbusAddresstypeRef_Create(success=False, error=str(e))


########################Update ############################################################
class E4k_TblbusAddresstypeRef_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        actual_typeid = graphene.Int(required=True)
        name = graphene.String()

    addresstype = graphene.Field(TblbusAddresstypeRefType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, actual_typeid, name=None):
        try:
            # Validate companyid
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblbusAddresstypeRef_Update(success=False, error="CompanyID does not exist")
            
            # Fetch the address type entry
            try:
                addresstype = TblbusAddresstypeRef.objects.get(companyid=companyid, actual_typeid=actual_typeid)
            except TblbusAddresstypeRef.DoesNotExist:
                return E4k_TblbusAddresstypeRef_Update(success=False, error='Address type entry not found')

            # Validate and update name
            if name is not None:
                if name.strip() == "":
                    return E4k_TblbusAddresstypeRef_Update(success=False, error="Name cannot be empty")
                
                # Check if the new name already exists for the company
                if TblbusAddresstypeRef.objects.filter(companyid=companyid, name=name).exclude(actual_typeid=actual_typeid).exists():
                    return E4k_TblbusAddresstypeRef_Update(success=False, error="Address type name already exists for this company")

                addresstype.name = name

            addresstype.save()
            return E4k_TblbusAddresstypeRef_Update(addresstype=addresstype, success=True)
        except Exception as e:
            return E4k_TblbusAddresstypeRef_Update(success=False, error=str(e))



############### Delete #######################################################
class E4k_TblbusAddresstypeRef_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        actual_typeid = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid, actual_typeid):
        try:
            addresstype = TblbusAddresstypeRef.objects.get(companyid=companyid, actual_typeid=actual_typeid)
            addresstype.delete()
            
            return E4k_TblbusAddresstypeRef_Delete(success=True)
        except TblbusAddresstypeRef.DoesNotExist:
            raise Exception('Address type entry not found')



##########################Create ############################

class E4k_TblbusAddressType_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        description = graphene.String()
        actual_typeid = graphene.Int()

    addresstypes = graphene.Field(TblbusAddresstypesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, description=None, actual_typeid=None):
        try:
            # Validate companyid
            try:
                company = Tblcompany.objects.get(companyid=companyid)
            except Tblcompany.DoesNotExist:
                return E4k_TblbusAddressType_Create(success=False, error=f"Company with id {companyid} does not exist")
            
            # Generate the next address type ID
            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblbus_addresstypes', field_name='AddressTypeID', companyid=companyid)
            if not next_no:
                return E4k_TblbusAddressType_Create(success=False, error="Failed to generate next AddressTypeID")
            
            # Validate actual_typeid
            actual_type_ref = None
            if actual_typeid is not None:
                try:
                    actual_type_ref = TblbusAddresstypeRef.objects.get(pk=actual_typeid)
                except TblbusAddresstypeRef.DoesNotExist:
                    return E4k_TblbusAddressType_Create(success=False, error=f"Actual type reference with id {actual_typeid} does not exist")

            # Validate description
            if description is None or description.strip() == "":
                return E4k_TblbusAddressType_Create(success=False, error="Description cannot be empty")
            
            # Create the address type
            addresstypes = TblbusAddresstypes.objects.create(
                companyid_id=companyid,
                addresstypeid=next_no,
                actual_typeid=actual_type_ref,
                description=description,
            )
            addresstypes.save()

            return E4k_TblbusAddressType_Create(addresstypes=addresstypes, success=True)
        except Exception as e:
            return E4k_TblbusAddressType_Create(success=False, error=str(e))

###################Update ################################################################


class E4k_TblbusAddresstypes_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        addresstypeid = graphene.Int(required=True)
        description = graphene.String()
        actual_typeid = graphene.Int()

    addresstype = graphene.Field(TblbusAddresstypesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, addresstypeid, description=None, actual_typeid=None):
        try:
            # Validate companyid
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblbusAddresstypes_Update(success=False, error="CompanyID does not exist")
            
            # Fetch the address type entry
            try:
                addresstype = TblbusAddresstypes.objects.get(companyid=companyid, addresstypeid=addresstypeid)
            except TblbusAddresstypes.DoesNotExist:
                return E4k_TblbusAddresstypes_Update(success=False, error='Address type entry not found')

            # Validate and update description
            if description is not None:
                if description.strip() == "":
                    return E4k_TblbusAddresstypes_Update(success=False, error="Description cannot be empty")
                addresstype.description = description

            # Validate and update actual_typeid
            if actual_typeid is not None:
                try:
                    actual_type_ref = TblbusAddresstypeRef.objects.get(pk=actual_typeid)
                    addresstype.actual_typeid = actual_type_ref
                except TblbusAddresstypeRef.DoesNotExist:
                    return E4k_TblbusAddresstypes_Update(success=False, error=f"Actual type reference with id {actual_typeid} does not exist")

            addresstype.save()
            return E4k_TblbusAddresstypes_Update(addresstype=addresstype, success=True)
        except Exception as e:
            return E4k_TblbusAddresstypes_Update(success=False, error=str(e))


    
#################################Delete ######################################################
class E4k_TblbusAddresstypes_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        # actual_typeid= graphene.Int()
        addresstypeid = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid,addresstypeid):
        addresstype = TblbusAddresstypes.objects.get(companyid=companyid,addresstypeid=addresstypeid)
        addresstype.delete()
    
        return E4k_TblbusAddresstypes_Delete(success=True)
    
############################### Create ###############################################################



class E4k_TblbusContactRef_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        name = graphene.String()

    contactref = graphene.Field(TblbusContactRefType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, name=None):
        try:
            # Validate companyid
            try:
                companyid = Tblcompany.objects.get(companyid=companyid)
            except Tblcompany.DoesNotExist:
                return E4k_TblbusContactRef_Create(success=False, error=f"Company with id {companyid} does not exist")
            
            # Validate name
            if name is None or name.strip() == "":
                return E4k_TblbusContactRef_Create(success=False, error="Name cannot be empty")
           
                
            
            # Generate the next contact type ID
            autonumber = NextNo()
            next_no = autonumber.get_next_no(table_name='tblbus_contact_ref', field_name='ContactType_ID', companyid=companyid)
            if not next_no:
                return E4k_TblbusContactRef_Create(success=False, error="Failed to generate next ContactType_ID")

            # Create the contact reference
            contactref = TblbusContactRef.objects.create(
                companyid_id=companyid,
                contacttype_id=next_no,
                name=name
            )
            contactref.save()

            return E4k_TblbusContactRef_Create(contactref=contactref, success=True)
        except Exception as e:
            return E4k_TblbusContactRef_Create(success=False, error=str(e))

##################################Update ######################################################################
   
class E4k_TblbusContactRef_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        contacttype_id = graphene.Int(required=True)
        name = graphene.String()

    contactref = graphene.Field(TblbusContactRefType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, contacttype_id, name=None):
        try:
            # Validate companyid
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblbusContactRef_Update(success=False, error="CompanyID does not exist")
            
            # Fetch the contact reference
            try:
                contactref = TblbusContactRef.objects.get(companyid=companyid, contacttype_id=contacttype_id)
            except TblbusContactRef.DoesNotExist:
                return E4k_TblbusContactRef_Update(success=False, error='Contact reference not found')
            
            
          
                

            # Validate and update name
            
            
          
                
            if name is not None:
                if name.strip() == "":
                    return E4k_TblbusContactRef_Update(success=False, error="Name cannot be empty")
                contactref.name = name

            contactref.save()
            return E4k_TblbusContactRef_Update(contactref=contactref, success=True)
        except Exception as e:
            return E4k_TblbusContactRef_Update(success=False, error=str(e))

        
################################### Delete ##########################################

class E4k_TblbusContactRef_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        contacttype_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, companyid, contacttype_id, *kwargs):
        try:
            contactRef = TblbusContactRef.objects.get(companyid=companyid, contacttype_id=contacttype_id)
            contactRef.delete()
            
            return E4k_TblbusContactRef_Delete(success=True)
        except TblbusContactRef.DoesNotExist:
            raise Exception('Contact Ref not found')

        
         

################# Create ##############################


class E4k_TblcustomerContact_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        addressid = graphene.Int()
        contacttype_id = graphene.Int()
        value = graphene.String()

    contact = graphene.Field(TblcustomerContactType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, addressid=None, contacttype_id=None, value=None):
        try:
            # Validate company
            try:
                Tblcompany.objects.get(companyid=companyid)
            except Tblcompany.DoesNotExist:
                return E4k_TblcustomerContact_Create(success=False, error="Company not found")
            
            # Validate contact type
            try:
                contacttype = TblbusContactRef.objects.get(companyid=companyid, contacttype_id=contacttype_id)
            except TblbusContactRef.DoesNotExist:
                return E4k_TblcustomerContact_Create(success=False, error="Contact type not found")
            
            # Validate address
            try:
                address = TblcustomerAddress.objects.get(companyid=companyid, addressid=addressid)
            except TblcustomerAddress.DoesNotExist:
                return E4k_TblcustomerContact_Create(success=False, error="Address not found")
            
            # Validate value
            if contacttype_id == 1:
                if any(char.isalpha() for char in value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid phone number format: alphabets are not allowed.")
                
                if not re.match(r'^\+?[0-9]\d{0,10}[-.\s]?(\(?\d{0,100}?\)?[-.\s]?|\d{0,100}[-.\s]?)?\d{0,100}[-.\s]?\d{0,100}[-.\s]?\d{0,100}$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Telphone number format.")
                
            if contacttype_id == 3:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Email format.")
            if contacttype_id == 5:
                if any(char.isalpha() for char in value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid phone number format: alphabets are not allowed.")
                
                if not re.match(r'^\+?[0-9]\d{0,10}[-.\s]?(\(?\d{0,100}?\)?[-.\s]?|\d{0,100}[-.\s]?)?\d{0,100}[-.\s]?\d{0,100}[-.\s]?\d{0,100}$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Mobile number format.")
                
                
            if contacttype_id == 8:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Email format.")
                
            if contacttype_id == 9:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Email format.")
            
            if contacttype_id == 11:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Email format.")
                
            if contacttype_id == 31:
                if any(char.isalpha() for char in value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid phone number format: alphabets are not allowed.")
                
                if not re.match(r'^\+?[0-9]\d{0,10}[-.\s]?(\(?\d{0,100}?\)?[-.\s]?|\d{0,100}[-.\s]?)?\d{0,100}[-.\s]?\d{0,100}[-.\s]?\d{0,100}$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Telphone number format.")
            
            if contacttype_id == 25:
                if not re.match(r'^[YyNn]$',value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Yes/No format.")
            if contacttype_id == 27:
                if not re.match(r'^[YyNn]$', value):
                    return E4k_TblcustomerContact_Create(success=False, error="Invalid Yes/No format.")
                
        
            # if value is None or value.strip() == "":
            #     return E4k_TblcustomerContact_Create(success=False, error="Value is required")
            # if len(value) < 3:
            #     return E4k_TblcustomerContact_Create(success=False, error="Value is too short")
            # if len(value) > 100:
            #     return E4k_TblcustomerContact_Create(success=False, error="Value is too long")
            
            # Create contact
            contact = TblcustomerContact.objects.create(
                companyid_id=companyid,
                addressid_id=addressid,
                contacttype_id=contacttype_id,
                value=value
            )
            contact.save()
            return E4k_TblcustomerContact_Create(contact=contact, success=True)
        except Exception as e:
            return E4k_TblcustomerContact_Create(success=False, error=str(e))

############################# Update ##################################
class E4k_TblcustomerContact_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String()
        addressid = graphene.Int()
        contacttype_id = graphene.Int()
        value = graphene.String()

    contact = graphene.Field(TblcustomerContactType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id, companyid=None, addressid=None, contacttype_id=None, value=None):
        try:
            # Fetch the contact entry
            contact = TblcustomerContact.objects.get(id=id,companyid=companyid)
            
            # Validate company
            if companyid is not None:
                try:
                    Tblcompany.objects.get(companyid=companyid)
                except Tblcompany.DoesNotExist:
                    return E4k_TblcustomerContact_Update(success=False, error="Company not found")
                contact.companyid_id = companyid
            
            # Validate address
            if addressid is not None:
                try:
                    TblcustomerAddress.objects.get(companyid=companyid, addressid=addressid)
                except TblcustomerAddress.DoesNotExist:
                    return E4k_TblcustomerContact_Update(success=False, error="Address not found")
                contact.addressid_id = addressid
            
            # Validate contact type
            if contacttype_id ==1:
                if any(char.isalpha() for char in value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid phone number format: alphabets are not allowed.")
                
                if not re.match(r'^\+?[0-9]\d{0,10}[-.\s]?(\(?\d{0,100}?\)?[-.\s]?|\d{0,100}[-.\s]?)?\d{0,100}[-.\s]?\d{0,100}[-.\s]?\d{0,100}$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Telephone number format.")


            if contacttype_id == 3:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Email format.")
            if contacttype_id == 5:
                if any(char.isalpha() for char in value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid phone number format: alphabets are not allowed.")
                
                if not re.match(r'^\+?[0-9]\d{0,10}[-.\s]?(\(?\d{0,100}?\)?[-.\s]?|\d{0,100}[-.\s]?)?\d{0,100}[-.\s]?\d{0,100}[-.\s]?\d{0,100}$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Mobile number format.")
                
                
            if contacttype_id == 8:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Email format.")
                
            if contacttype_id == 9:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Email format.")
            
            if contacttype_id == 11:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Email format.")
                
            if contacttype_id == 31:
                if any(char.isalpha() for char in value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid phone number format: alphabets are not allowed.")
                
                if not re.match(r'^\+?[0-9]\d{0,10}[-.\s]?(\(?\d{0,100}?\)?[-.\s]?|\d{0,100}[-.\s]?)?\d{0,100}[-.\s]?\d{0,100}[-.\s]?\d{0,100}$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Telphone number format.")
            
            if contacttype_id == 25:
                if not re.match(r'^[YyNn]$',value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Yes/No format.")
            if contacttype_id == 27:
                if not re.match(r'^[YyNn]$', value):
                    return E4k_TblcustomerContact_Update(success=False, error="Invalid Yes/No format.")
                   
            if contacttype_id is not None:
                try:
                    TblbusContactRef.objects.get(companyid=companyid, contacttype_id=contacttype_id)
                except TblbusContactRef.DoesNotExist:
                    return E4k_TblcustomerContact_Update(success=False, error="Contact type not found")
                contact.contacttype_id = contacttype_id
            
            # # Validate value
            # if value is not None:
            #     if value.strip() == "":
            #         return E4k_TblcustomerContact_Update(success=False, error="Value is required")
            #     if len(value) < 3:
            #         return E4k_TblcustomerContact_Update(success=False, error="Value is too short")
            #     if len(value) > 100:
            #         return E4k_TblcustomerContact_Update(success=False, error="Value is too long")
            #     contact.value = value
            
            contact.save()
            return E4k_TblcustomerContact_Update(contact=contact, success=True)
        except TblcustomerContact.DoesNotExist:
            return E4k_TblcustomerContact_Update(success=False, error="Contact not found")
        except Exception as e:
            return E4k_TblcustomerContact_Update(success=False, error=str(e))




####################### Delete ##########################################
class E4k_TblcustomerContact_Delete(graphene.Mutation):
    class Arguments:
        addressid = graphene.Int()
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, addressid=None):
        try:
            if addressid is not None:
                contacts = TblcustomerContact.objects.filter(addressid=addressid, companyid=companyid)
            
            if contacts.exists():
                contacts.delete()
                return E4k_TblcustomerContact_Delete(success=True)
            else:
                return E4k_TblcustomerContact_Delete(success=False, error="Contact not found.")
        except Exception as e:
            return E4k_TblcustomerContact_Delete(success=False, error=str(e))
        
        

class E4k_CustomerContact_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        id = graphene.Int(required=True)
    
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self,info, companyid,id ) :
        try:
            contact = TblcustomerContact.objects.get(companyid=companyid , id=id )
            contact.delete()
            return E4k_CustomerContact_Delete(success=True)
        except TblcustomerContact.DoesNotExist:
            return E4k_CustomerContact_Delete(success=False, error="Contact not found.")
        except Exception as e:
            return E4k_CustomerContact_Delete(success=False, error=str(e))
        

        
        
        

    
        
        
        

        
        



############################## Create #############################################################


class E4k_Tblcustomer_Create(graphene.Mutation):
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
        groupid = graphene.Int()
        default_nominal = graphene.Int()
        isextract = graphene.Boolean()
        isstop = graphene.Boolean()
        

    customer = graphene.Field(TblcustomerType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, name=None, countryid=None, islive=True, category1id=None, category2id=None, category3id=None, classid=None, groupid=None, default_nominal=None, isextract=False, isstop=None):
        errors = []

        # Check if companyid exists
        if not Tblcompany.objects.filter(companyid=companyid).exists():
            errors.append("CompanyID does not exist.")

        # Check if countryid exists
        if countryid is not None and not TblbusCountries.objects.filter(countryid =countryid).exists():
            errors.append("CountryID does not exist.")

        if Tblcustomer.objects.filter(businessid=businessid).exists():
            errors.append("businessID already exists.")
        
        if Tblcustomer.objects.filter(name=name).exists():
            errors.append("Name already exists.")

        # Check if category1id exists
        if category1id is not None and not TblcustomerCategory1.objects.filter(category1id =category1id).exists():
            errors.append("Category1ID does not exist.")
        
        # Check if category2id exists
        if category2id is not None and not TblcustomerCategory2.objects.filter(category2id =category2id).exists():
            errors.append("Category2ID does not exist.")
        
        # Check if category3id exists
        if category3id is not None and not TblcustomerCategory3.objects.filter(category3id=category3id).exists():
            errors.append("Category3ID does not exist.")
        
        # Check if classid exists
        if classid is not None and not TblcustomerClass.objects.filter(classid=classid).exists():
            errors.append("ClassID does not exist.")
        
        # Check if groupid exists
        if groupid is not None and not TblbusGroups.objects.filter( groupid=groupid).exists():
            errors.append("GroupID does not exist.")
        
        # Check if default_nominal exists
        if default_nominal is not None and not TblaccNominal.objects.filter( nomcode=default_nominal).exists():
            errors.append("Default_Nominal does not exist.")
        
        # If there are errors, return the errors
        # if errors:
        #     return E4k_Tblcustomer_Create(success=False, error=", ".join(errors))

        # Create the customer
        try:
            customer = Tblcustomer(
                companyid_id=companyid,
                businessid=businessid,
                name=name , 
                countryid_id=countryid,
                islive=islive,
                category1id_id=category1id,
                category2id_id=category2id,
                category3id_id=category3id,
                classid_id=classid,
                groupid_id=groupid,
                default_nominal_id=default_nominal,
                isextract=isextract,
                isstop=isstop
            )
            customer.save()
            return E4k_Tblcustomer_Create(customer=customer, success=True)
        except Exception as e:
            return E4k_Tblcustomer_Create(success=False, error=str(e))



##############################################################

# class E4k_Tblcustomer_Update(graphene.Mutation):
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
#         groupid = graphene.Int()
#         default_nominal = graphene.Int()
#         isextract = graphene.Boolean()
#         isstop = graphene.Boolean()

#     customer = graphene.Field(TblcustomerType)
#     success = graphene.Boolean()
#     error = graphene.String()

#     def mutate(self, info, businessid, companyid=None, name=None , countryid=None, islive=None, category1id=None, category2id=None, category3id=None, classid=None, groupid=None, default_nominal=None, isextract=None, isstop=None):
#         try:
#             # Fetch the customer entry
#             customer = Tblcustomer.objects.get(businessid=businessid)

#             # Validate and update companyid
#             if companyid is not None:
#                 try:
#                     Tblcompany.objects.get(companyid=companyid)
#                 except Tblcompany.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Company not found")
#                 customer.companyid_id = companyid

#             # Validate name
#             if name is not None:
#                 customer.name = name

#             # Validate and update countryid
#             if countryid is not None:
#                 try:
#                     TblbusCountries.objects.get(countryid=countryid)
#                 except TblbusCountries.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Country not found")
#                 customer.countryid_id = countryid
           
#             # Validate and update category1id
#             if category1id is not None:
#                 try:
#                     TblcustomerCategory1.objects.get(category1id=category1id)
#                 except TblcustomerCategory1.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Category 1 not found")
#                 customer.category1id_id = category1id

#             # Validate and update category2id
#             if category2id is not None:
#                 try:
#                     TblcustomerCategory2.objects.get(category2id=category2id)
#                 except TblcustomerCategory2.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Category 2 not found")
#                 customer.category2id_id = category2id

#             # Validate and update category3id
#             if category3id is not None:
#                 try:
#                     TblcustomerCategory3.objects.get(category3id=category3id)
#                 except TblcustomerCategory3.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Category 3 not found")
#                 customer.category3id_id = category3id

#             # Validate and update classid
#             if classid is not None:
#                 try:
#                     TblcustomerClass.objects.get(classid=classid)
#                 except TblcustomerClass.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Class not found")
#                 customer.classid_id = classid

#             # Validate and update groupid
#             if groupid is not None:
#                 try:
#                     TblbusGroups.objects.get(groupid=groupid)
#                 except TblbusGroups.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Group not found")
#                 customer.groupid_id = groupid

#             # Validate and update default_nominal
#             if default_nominal is not None:
#                 try:
#                     TblaccNominal.objects.get(nomcode=default_nominal)
#                 except TblaccNominal.DoesNotExist:
#                     return E4k_Tblcustomer_Update(success=False, error="Default nominal not found")
#                 customer.default_nominal_id = default_nominal

#             # Update boolean fields
#             if islive is not None:
#                 customer.islive = islive
#             if isextract is not None:
#                 customer.isextract = isextract
#             if isstop is not None:
#                 customer.isstop = isstop

#             # Save the customer entry
#             customer.save()
#             return E4k_Tblcustomer_Update(customer=customer, success=True)

#         except Tblcustomer.DoesNotExist:
#             return E4k_Tblcustomer_Update(success=False, error="Customer not found.")
#         except Exception as e:
#             return E4k_Tblcustomer_Update(success=False, error=str(e))


class E4k_Tblcustomer_Update(graphene.Mutation):
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
        groupid = graphene.Int()
        default_nominal = graphene.Int()
        isextract = graphene.Boolean()
        isstop = graphene.Boolean()

    customer = graphene.Field(TblcustomerType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, businessid, companyid=None, name=None, countryid=None, islive=None, category1id=None, category2id=None, category3id=None, classid=None, groupid=None, default_nominal=None, isextract=None, isstop=None):
        try:
            # Fetch the customer entry
            customer = Tblcustomer.objects.get(businessid=businessid)

            # Validate and update companyid
            if companyid is not None:
                try:
                    Tblcompany.objects.get(companyid=companyid)
                except Tblcompany.DoesNotExist:
                    return E4k_Tblcustomer_Update(success=False, error="Company not found")
                customer.companyid_id = companyid

            # Validate name
            if name is not None:
                customer.name = name

            # Validate and update countryid (Set default if not provided)
            if countryid is None:
                countryid = 0  # Default value (change based on your needs)
            try:
                TblbusCountries.objects.get(countryid=countryid)
            except TblbusCountries.DoesNotExist:
                return E4k_Tblcustomer_Update(success=False, error="Country not found")
            customer.countryid_id = countryid

            # Validate and update category1id (Set default if not provided)
            if category1id is None:
                category1id = 0  # Default value (change as necessary)
            try:
                TblcustomerCategory1.objects.get(category1id=category1id)
            except TblcustomerCategory1.DoesNotExist:
                return E4k_Tblcustomer_Update(success=False, error="Category 1 not found")
            customer.category1id_id = category1id

            # Validate and update category2id (Set default if not provided)
            if category2id is None:
                category2id = 0  # Default value (change as necessary)
            try:
                TblcustomerCategory2.objects.get(category2id=category2id)
            except TblcustomerCategory2.DoesNotExist:
                return E4k_Tblcustomer_Update(success=False, error="Category 2 not found")
            customer.category2id_id = category2id

            # Validate and update category3id (Set default if not provided)
            if category3id is None:
                category3id = 0  # Default value (change as necessary)
            try:
                TblcustomerCategory3.objects.get(category3id=category3id)
            except TblcustomerCategory3.DoesNotExist:
                return E4k_Tblcustomer_Update(success=False, error="Category 3 not found")
            customer.category3id_id = category3id

            # Validate and update classid (Set default if not provided)
            if classid is None:
                classid = 0  # Default value (change as necessary)
            try:
                TblcustomerClass.objects.get(classid=classid)
            except TblcustomerClass.DoesNotExist:
                return E4k_Tblcustomer_Update(success=False, error="Class not found")
            customer.classid_id = classid

            # Validate and update groupid (Set default if not provided)
            if groupid is None:
                groupid = 0  # Default value (change as necessary)
            try:
                TblbusGroups.objects.get(groupid=groupid)
            except TblbusGroups.DoesNotExist:
                return E4k_Tblcustomer_Update(success=False, error="Group not found")
            customer.groupid_id = groupid

            # Validate and update default_nominal (Set default if not provided)
            if default_nominal is None:
                default_nominal = 0  # Default value (change as necessary)
            try:
                TblaccNominal.objects.get(nomcode=default_nominal)
            except TblaccNominal.DoesNotExist:
                return E4k_Tblcustomer_Update(success=False, error="Default nominal not found")
            customer.default_nominal_id = default_nominal

            # Update boolean fields
            if islive is not None:
                customer.islive = islive
            if isextract is not None:
                customer.isextract = isextract
            if isstop is not None:
                customer.isstop = isstop

            # Save the customer entry
            customer.save()
            return E4k_Tblcustomer_Update(customer=customer, success=True)

        except Tblcustomer.DoesNotExist:
            return E4k_Tblcustomer_Update(success=False, error="Customer not found.")
        except Exception as e:
            return E4k_Tblcustomer_Update(success=False, error=str(e))



####################################### Delete ################################################################################################
# class E4k_Tblcustomer_Delete(graphene.Mutation):
#     class Arguments:
#         businessid = graphene.String(required=True)
#         companyid  = graphene.String(required=True)
#     success = graphene.Boolean()
#     error = graphene.String()

#     def mutate(self, info, businessid,companyid):
#         try:
#             customer = Tblcustomer.objects.get(businessid=businessid,companyid=companyid)


#             customer.delete()
#             return E4k_Tblcustomer_Delete(success=True)
#         except Tblcustomer.DoesNotExist:
#             return E4k_Tblcustomer_Delete(success=False, error="Customer not found.")
#         except Exception as e:
#             return E4k_Tblcustomer_Delete(success=False, error=str(e))

class E4k_Tblcustomer_Delete(graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, businessid, companyid):
        try:
            customer = Tblcustomer.objects.get(businessid=businessid, companyid=companyid)
            
            # Update fields to deactivate the customer
            customer.isextract = customer.isextract == b'\x01'  # Set to True if you want to mark as extracted
            customer.isstop = customer.isstop == b'\x01'    # Mark as stopped
            customer.islive = customer.islive  == b'\x01'      # Deactivate customer
            
            customer.save()  # Save the updated customer object

            return E4k_Tblcustomer_Delete(success=True)
        except Tblcustomer.DoesNotExist:
            return E4k_Tblcustomer_Delete(success=False, error="Customer not found.")
        except Exception as e:
            return E4k_Tblcustomer_Delete(success=False, error=str(e))
   
############################# Create ##################################################


class E4k_TblcustomerServicePeple_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        csgroupid = graphene.Int(required=True)

    customer_service_peple = graphene.Field(TblcustomerServicePepleType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, csgroupid):
        try:
            # Validate companyid
            try:
                company = Tblcompany.objects.get(companyid=companyid)
            except Tblcompany.DoesNotExist:
                return E4k_TblcustomerServicePeple_Create(success=False, error="Company not found")

            # Validate businessid
            try:
                business = Tblcustomer.objects.get(businessid=businessid)
            except Tblcustomer.DoesNotExist:
                return E4k_TblcustomerServicePeple_Create(success=False, error="Business not found")

            # Validate csgroupid
            try:
                csgroupid = TblbusServicePeople.objects.get(csgroupid=csgroupid)  # Adjusted the field name from csgroupid to groupid
            except TblbusGroups.DoesNotExist:
                return E4k_TblcustomerServicePeple_Create(success=False, error="Customer Service Group not found")

            customer_service_peple = TblcustomerServicePeple(
                companyid=company,
                businessid=business,
                csgroupid=csgroupid  # Assuming csgroupid is a foreign key to TblbusGroups
            )
            customer_service_peple.save()
            return E4k_TblcustomerServicePeple_Create(customer_service_peple=customer_service_peple, success=True)
        except Exception as e:
            return E4k_TblcustomerServicePeple_Create(success=False, error=str(e))

 #######################################  Update  ##################################################


class E4k_TblcustomerServicePeple_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String()
        businessid = graphene.String()
        csgroupid = graphene.Int()

    customer_service_peple = graphene.Field(TblcustomerServicePepleType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id, companyid=None, businessid=None, csgroupid=None):
        try:
            customer_service_peple = TblcustomerServicePeple.objects.get(id=id)

            # Validate and update companyid
            if companyid is not None:
                try:
                    Tblcompany.objects.get(companyid=companyid)
                except Tblcompany.DoesNotExist:
                    return E4k_TblcustomerServicePeple_Update(success=False, error="Company not found")
                customer_service_peple.companyid_id = companyid

            # Validate and update businessid
            if businessid is not None:
                try:
                    Tblcustomer.objects.get(businessid=businessid)
                except Tblcustomer.DoesNotExist:
                    return E4k_TblcustomerServicePeple_Update(success=False, error="Business not found")
                customer_service_peple.businessid_id = businessid

            # Validate and update csgroupid
            if csgroupid is not None:
                try:
                    TblbusGroups.objects.get(csgroupid=csgroupid)
                except TblbusGroups.DoesNotExist:
                    return E4k_TblcustomerServicePeple_Update(success=False, error="Customer Service Group not found")
                customer_service_peple.csgroupid_id = csgroupid

            customer_service_peple.save()
            return E4k_TblcustomerServicePeple_Update(customer_service_peple=customer_service_peple, success=True)
        except TblcustomerServicePeple.DoesNotExist:
            return E4k_TblcustomerServicePeple_Update(success=False, error="Customer Service Peple not found.")
        except Exception as e:
            return E4k_TblcustomerServicePeple_Update(success=False, error=str(e))




################################ Delete ####################################################

class E4k_TblcustomerServicePeple_Delete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info,companyid , id):
        try:
            customer_service_peple = TblcustomerServicePeple.objects.get(id=id,companyid = companyid)
            customer_service_peple.delete()
            return E4k_TblcustomerServicePeple_Delete(success=True)
        except TblcustomerServicePeple.DoesNotExist:
            return E4k_TblcustomerServicePeple_Delete(success=False, error="Customer Service Peple not found.")
        except Exception as e:
            return E4k_TblcustomerServicePeple_Delete(success=False, error=str(e))
        
######################################## Create #############################################################################





class E4k_TblcustomerSalesTrans_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        unit_price = graphene.Decimal(required=True)
        quantity = graphene.Int(required=True)
        discount_percentage = graphene.Decimal(required=True)
        # trantype = graphene.String()
        custref = graphene.String()
        query = graphene.Boolean()
        qnote = graphene.String()

    customer_sales_trans = graphene.Field(TblcustomerSalesTransType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(
        self,
        info,
        companyid,
        businessid,
        unit_price,
        quantity,
        discount_percentage,
        trantype=None,
        custref=None,
        query=None,
        qnote=None,
    ):
        try:
            # Validate input arguments
            if None in [unit_price, quantity, discount_percentage]:
                raise ValueError("Unit price, quantity, and discount percentage must have valid values.")

          

            # Calculate goodscash
            goodscash = unit_price * quantity

            # Calculate VAT discount
            vatdiscount = goodscash * (discount_percentage / Decimal(100))

            # Fetch related data if needed
            company = Tblcompany.objects.get(companyid=companyid)
            business = Tblcustomer.objects.get(businessid=businessid)

            # Generate unique transaction number and batch number
            autonumber = NextNo()
            next_no = autonumber.get_next_no(
                table_name="tblcustomer_sales_trans",
                field_name="TransactionNo",
                companyid=companyid,
            )
            batch_no = autonumber.get_next_no(
                table_name="tblcustomer_sales_trans",
                field_name="Batchno",
                companyid=companyid,
            )

            # Generate random tranreference
            tranreference = ''.join(random.choices(string.digits, k=7))

            # Default values for financial fields
            osbal = Decimal('0.00')
            discount = Decimal('0.00')
            discountdays = 0
            rate = Decimal('1.00')
            paymenttermsid = 1  # Assuming a default payment term

            # Calculate Total Amount
            currtotal = goodscash + vatdiscount - discount

            # Calculate Outstanding Balance
            outstanding_balance = currtotal - osbal

            # Calculate Discount Amount
            discount_amount = currtotal * (discount / Decimal(100))

            # Calculate Due Date
            trandate = datetime.now()
            duedate = trandate + timedelta(days=discountdays)

            customer_sales_trans = TblcustomerSalesTrans(
                companyid=company,
                transactionno=next_no,
                businessid=business,
                tranreference=tranreference,
                trantype=trantype or "default_type",
                custref=custref or "default_ref",
                trandate=trandate,
                goodscash=goodscash,
                vatdiscount=vatdiscount,
                osbal=outstanding_balance,
                discount=discount_amount,
                discountdays=discountdays,
                batchno=batch_no,
                rate=rate,
                currtotal=currtotal,
                paymenttermsid=TblbusPaymentterms.objects.get(pk=paymenttermsid),
                duedate=duedate,
                query=query or False,
                qnote=qnote or "",
            )
            customer_sales_trans.save()
            return E4k_TblcustomerSalesTrans_Create(
                customer_sales_trans=customer_sales_trans, success=True
            )
        except Tblcompany.DoesNotExist:
            return E4k_TblcustomerSalesTrans_Create(success=False, error="Company ID does not exist.")
        except Tblcustomer.DoesNotExist:
            return E4k_TblcustomerSalesTrans_Create(success=False, error="Business ID does not exist.")
        except TblbusPaymentterms.DoesNotExist:
            return E4k_TblcustomerSalesTrans_Create(success=False, error="Payment Terms ID does not exist.")
        except Exception as e:
            return E4k_TblcustomerSalesTrans_Create(success=False, error=str(e))




class E4k_TblcustomerSalesTrans_Update(graphene.Mutation):
    class Arguments:
        transactionno = graphene.Int(required=True)
        companyid = graphene.String()
        businessid = graphene.String()
        tranreference = graphene.String()
        trantype = graphene.String()
        custref = graphene.String()
        trandate = graphene.String()  # Accepting string for conversion
        goodscash = graphene.Decimal()
        vatdiscount = graphene.Decimal()
        osbal = graphene.Decimal()
        discount = graphene.Decimal()
        discountdays = graphene.Int()
        batchno = graphene.Int()
        rate = graphene.Decimal()
        currtotal = graphene.Decimal()
        paymenttermsid = graphene.Int()
        duedate = graphene.String()  # Accepting string for conversion
        query = graphene.Boolean()
        qnote = graphene.String()

    customer_sales_trans = graphene.Field(TblcustomerSalesTransType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, transactionno, companyid=None, businessid=None, tranreference=None, trantype=None, custref=None, trandate=None, goodscash=None, vatdiscount=None, osbal=None, discount=None, discountdays=None, batchno=None, rate=None, currtotal=None, paymenttermsid=None, duedate=None, query=None, qnote=None):
        trandate = datetime.now()
        duedate = datetime.now()
    


        try:
            customer_sales_trans = TblcustomerSalesTrans.objects.get(transactionno=transactionno)
            if companyid is not None:
                customer_sales_trans.companyid_id = companyid
            if businessid is not None:
                customer_sales_trans.businessid_id = businessid
            if tranreference is not None:
                customer_sales_trans.tranreference = tranreference
            if trantype is not None:
                customer_sales_trans.trantype = trantype
            if custref is not None:
                customer_sales_trans.custref = custref
            if trandate is not None:
                customer_sales_trans.trandate =trandate
            if goodscash is not None:
                customer_sales_trans.goodscash = goodscash
            if vatdiscount is not None:
                customer_sales_trans.vatdiscount = vatdiscount
            if osbal is not None:
                customer_sales_trans.osbal = osbal
            if discount is not None:
                customer_sales_trans.discount = discount
            if discountdays is not None:
                customer_sales_trans.discountdays = discountdays
            if batchno is not None:
                customer_sales_trans.batchno = batchno
            if rate is not None:
                customer_sales_trans.rate = rate
            if currtotal is not None:
                customer_sales_trans.currtotal = currtotal
            if paymenttermsid is not None:
                customer_sales_trans.paymenttermsid_id = paymenttermsid
            if duedate is not None:
                customer_sales_trans.duedate = duedate
            if query is not None:
                customer_sales_trans.query = query
            if qnote is not None:
                customer_sales_trans.qnote = qnote
            customer_sales_trans.save()
            return E4k_TblcustomerSalesTrans_Update(customer_sales_trans=customer_sales_trans, success=True)
        except TblcustomerSalesTrans.DoesNotExist:
            return E4k_TblcustomerSalesTrans_Update(success=False, error="Customer Sales Transaction not found.")
        except Exception as e:
            return E4k_TblcustomerSalesTrans_Update(success=False, error=str(e))


############################# Delete #########################################


class E4k_TblcustomerSalesTrans_Delete(graphene.Mutation):
    class Arguments:
        transactionno = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid,transactionno):
        try:
            customer_sales_trans = TblcustomerSalesTrans.objects.get(transactionno=transactionno,companyid = companyid)
            customer_sales_trans.delete()
            return E4k_TblcustomerSalesTrans_Delete(success=True)
        except TblcustomerSalesTrans.DoesNotExist:
            return E4k_TblcustomerSalesTrans_Delete(success=False, error="Customer Sales Transaction not found.")
        except Exception as e:
            return E4k_TblcustomerSalesTrans_Delete(success=False, error=str(e))

####################### Create #################################################################################################


class E4k_TblgenUsers_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        userid = graphene.String(required=True)
        password = graphene.String()
        accessid = graphene.Int()
        forename = graphene.String()
        surname = graphene.String()
        description = graphene.String()
        telephone1 = graphene.String()
        telephone2 = graphene.String()
        loggedon = graphene.Boolean()
        locked = graphene.Boolean()
        canbechanged = graphene.Boolean()
        canbedeleted = graphene.Boolean()
        # ip_address = graphene.String()
        passwordpayment = graphene.String()
        warehouseid = graphene.String()
        emailid = graphene.String()

    user = graphene.Field(TblgenUsersType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, userid, password=None, accessid=None, forename=None, surname=None, description=None, telephone1=None, telephone2=None, loggedon=None, locked=None, canbechanged=None, canbedeleted=None, passwordpayment=None, warehouseid=None, emailid=None):
        try:
            last_logon = datetime.now()
            ip_address = socket.gethostbyname(socket.gethostname())  # Get the host's IP address

            if TblgenUsers.objects.filter(userid=userid).exists():
                return E4k_TblgenUsers_Create(success=False, error="User ID already exists.")
            if  TblgenUsers.objects.filter(password=password).exists():
                return E4k_TblgenUsers_Create(success=False, error="password alredy exists.")
            # if TblgenUsers.objects.filter(accessid=accessid).exists():
            #     return E4k_TblgenUsers_Create(success=False, error="Access ID already exists.")
            if TblgenUsers.objects.filter(forename=forename).exists():
                return E4k_TblgenUsers_Create(success=False, error="Forename already exists.")
            if TblgenUsers.objects.filter(surname=surname).exists():
                return E4k_TblgenUsers_Create(success=False, error="Surname already exists.")
            if TblgenUsers.objects.filter(passwordpayment=passwordpayment).exists():    
                return E4k_TblgenUsers_Create(success=False, error="passwordpayment already exists.")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", emailid ):
                return E4k_TblgenUsers_Create(success=False, error="Invalid email format.")
            if emailid is not None:
                if TblgenUsers.objects.filter(emailid=emailid).exists():
                    return E4k_TblgenUsers_Create(success=False, error="Email ID already exists.")
            
            



            user = TblgenUsers(
                companyid_id=companyid,
                userid=userid,
                password=password,
                accessid=accessid,
                forename=forename,
                surname=surname,
                description=description,
                telephone1=telephone1,
                telephone2=telephone2,
                last_logon=last_logon,
                loggedon=loggedon,
                locked=locked,
                canbechanged=canbechanged,
                canbedeleted=canbedeleted,
                ip_address=ip_address,
                passwordpayment=passwordpayment,
                warehouseid=warehouseid,
                emailid=emailid
            )
            user.save()
            return E4k_TblgenUsers_Create(user=user, success=True)
        except Exception as e:
            return E4k_TblgenUsers_Create(success=False, error=str(e))

        
#########################################################


class E4k_TblgenUsers_Update(graphene.Mutation):
    class Arguments:
        userid = graphene.String(required=True)
        companyid = graphene.String()
        password = graphene.String()
        accessid = graphene.Int()
        forename = graphene.String()
        surname = graphene.String()
        description = graphene.String()
        telephone1 = graphene.String()
        telephone2 = graphene.String()
        loggedon = graphene.Boolean()
        locked = graphene.Boolean()
        canbechanged = graphene.Boolean()
        canbedeleted = graphene.Boolean()
        passwordpayment = graphene.String()
        warehouseid = graphene.String()
        emailid = graphene.String()

    user = graphene.Field(TblgenUsersType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, userid, companyid=None, password=None, accessid=None, forename=None, surname=None, description=None, telephone1=None, telephone2=None, loggedon=None, locked=None, canbechanged=None, canbedeleted=None, passwordpayment=None, warehouseid=None, emailid=None):
        try:
            user = TblgenUsers.objects.get(userid=userid)
        except TblgenUsers.DoesNotExist:
            return E4k_TblgenUsers_Update(success=False, error="User not found.")

        # Perform field validations
        if password is not None and len(password) < 8:
            return E4k_TblgenUsers_Update(success=False, error="Password must be at least 8 characters long.")
        # Add more validations for other fields as needed

        # Update user fields
        if companyid is not None:
            user.companyid_id = companyid
        if password is not None:
            user.password = password
        if accessid is not None:
            user.accessid = accessid
        if forename is not None:
            user.forename = forename
        if surname is not None:
            user.surname = surname
        if description is not None:
            user.description = description
        if telephone1 is not None:
            user.telephone1 = telephone1
        if telephone2 is not None:
            user.telephone2 = telephone2
        if loggedon is not None:
            user.loggedon = loggedon
        if locked is not None:
            user.locked = locked
        if canbechanged is not None:
            user.canbechanged = canbechanged
        if canbedeleted is not None:
            user.canbedeleted = canbedeleted
        if passwordpayment is not None:
            user.passwordpayment = passwordpayment
        if warehouseid is not None:
            user.warehouseid = warehouseid
        if emailid is not None:
            user.emailid = emailid

        user.save()
        return E4k_TblgenUsers_Update(user=user, success=True)

        


######################### Delete #########################################################################################

class E4k_TblgenUsers_Delete(graphene.Mutation):
    class Arguments:
        userid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, userid):
        try:
            user = TblgenUsers.objects.get(userid=userid)
            user.delete()
            return E4k_TblgenUsers_Delete(success=True)
        except TblgenUsers.DoesNotExist:
            return E4k_TblgenUsers_Delete(success=False, error="User not found.")
        except Exception as e:
            return E4k_TblgenUsers_Delete(success=False, error=str(e))

##############################################################################################################################




class E4k_CustomerNote_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        note = graphene.String()
        userid = graphene.String()

    customer_note = graphene.Field(TblcustomerNotesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, note=None, userid=None):
        try:
            # Validation for foreign keys

            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_CustomerNote_Create(success=False, error="CompanyID does not exist.")
            if not Tblcustomer.objects.filter(businessid=businessid).exists():
                return E4k_CustomerNote_Create(success=False, error="BusinessID does not exist.")
            if userid and not TblgenUsers.objects.filter(userid=userid).exists():
                return E4k_CustomerNote_Create(success=False, error="UserID does not exist.")

            # Set the current date and time if note_date is not provided
            note_date = datetime.now()


            customer_note = TblcustomerNotes(
                companyid_id=companyid,
                businessid_id=businessid,
                note=note,
                userid_id=userid,
                note_date=note_date
            )
            customer_note.save()
            return E4k_CustomerNote_Create(customer_note=customer_note, success=True)
        except Exception as e:
            return E4k_CustomerNote_Create(success=False, error=str(e))


#################################################################################################################################################

class E4k_CustomerNote_Update(graphene.Mutation):
    class Arguments:
        # noteid = graphene.Int()
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        note = graphene.String()
        userid = graphene.String()

    customer_note = graphene.Field(TblcustomerNotesType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info,  companyid=None, businessid=None, note=None, userid=None):
        try:
            customer_note = TblcustomerNotes.objects.get(companyid = companyid, businessid= businessid)
            
            if companyid is not None:
                if not Tblcompany.objects.filter(companyid=companyid).exists():
                    return E4k_CustomerNote_Update(success=False, error="CompanyID does not exist.")
                customer_note.companyid_id = companyid

            if businessid is not None:
                if not Tblcustomer.objects.filter(businessid=businessid).exists():
                    return E4k_CustomerNote_Update(success=False, error="BusinessID does not exist.")
                customer_note.businessid_id = businessid

            if userid is not None:
                if not TblgenUsers.objects.filter(userid=userid).exists():
                    return E4k_CustomerNote_Update(success=False, error="UserID does not exist.")
                customer_note.userid_id = userid

            if note is not None:
                customer_note.note = note

            # Update the note_date to the current date and time
            customer_note.note_date = datetime.now()

            customer_note.save()
            return E4k_CustomerNote_Update(customer_note=customer_note, success=True)
        except TblcustomerNotes.DoesNotExist:
            return E4k_CustomerNote_Update(success=False, error="Customer Note not found.")
        except Exception as e:
            return E4k_CustomerNote_Update(success=False, error=str(e))
        


##############################################################################################
class E4k_CustomerNote_Delete(graphene.Mutation):
    class Arguments:
        noteid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info,companyid, noteid):
        
        try:
            customer_note = TblcustomerNotes.objects.get(noteid=noteid,companyid=companyid)
            customer_note.delete()
            return E4k_CustomerNote_Delete(success=True)
        except TblcustomerNotes.DoesNotExist:
            return E4k_CustomerNote_Delete(success=False, error="Customer Note not found.")
        except Exception as e:
            return E4k_CustomerNote_Delete(success=False, error=str(e))


###############################################################################################################################################################################################################

class E4k_CustomerAddress_Create(graphene.Mutation):
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
        

    customer_address = graphene.Field(TblcustomerAddressType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid,businessid,addressid =None,  description=None, address1=None, address2=None, address3=None, city=None, county=None, postcode=None, countrycode=None, addresstypeid=None):
        try:
            autonumber  = NextNo()
            next_no = autonumber.get_next_no(table_name='tblcustomer_address',field_name='AddressID',companyid=companyid)
            print(next_no)
            
            company = Tblcompany.objects.get(companyid = companyid);
            # Validation for foreign keys
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_CustomerAddress_Create(success=False, error="CompanyID does not exist.")
            if not Tblcustomer.objects.filter(companyid= company ,businessid=businessid).exists():
                return E4k_CustomerAddress_Create(success=False, error="BusinessID does not exist.")
            if countrycode and not TblbusCountries.objects.filter(companyid= company ,countryid=countrycode).exists():
                return E4k_CustomerAddress_Create(success=False, error="CountryCode does not exist.")
            if addresstypeid and not TblbusAddresstypes.objects.filter(companyid = company , addresstypeid=addresstypeid).exists():
                return E4k_CustomerAddress_Create(success=False, error="AddressTypeID does not exist.")

            # Create new address
            customer_address = TblcustomerAddress(
                companyid_id=companyid,
                businessid_id=businessid,
                description=description,
                address1=address1,
                address2=address2,
                address3=address3,
                addressid = next_no, 
                city=city,
                county=county,
                postcode=postcode,
                countrycode_id=countrycode,  
                addresstypeid_id=addresstypeid
            )
            
            customer_address.save()
            
            return E4k_CustomerAddress_Create(customer_address=customer_address, success=True)
        except Exception as e:
            return E4k_CustomerAddress_Create(success=False, error=str(e))

# Update customer address


class E4k_CustomerAddress_Update(graphene.Mutation):
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
        countrycode = graphene.Int()  # Refers to countryid in TblbusCountries
        addresstypeid = graphene.Int()

    customer_address = graphene.Field(TblcustomerAddressType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, addressid, companyid=None, businessid=None, description=None, address1=None, address2=None, address3=None, city=None, county=None, postcode=None, countrycode=None, addresstypeid=None):
        try:
        # Retrieve the customer address record
            customer_address = TblcustomerAddress.objects.get(addressid=addressid)

            if companyid is not None:
                # Fetch the company instance
                company = Tblcompany.objects.filter(companyid=companyid).first()
                if not company:
                    return E4k_CustomerAddress_Update(success=False, error="CompanyID does not exist.")
                customer_address.companyid = company  # Assign the instance

            if businessid is not None:
                business = Tblcustomer.objects.filter(businessid=businessid).first()
                if not business:
                    return E4k_CustomerAddress_Update(success=False, error="BusinessID does not exist.")
                customer_address.businessid = business  # Assuming there's a field for business in TblcustomerAddress

            # Handling countrycode: Set the related country object
            if countrycode is not None:
                country = TblbusCountries.objects.filter(countryid=countrycode).first()
                if country:
                    customer_address.countrycode = country  
                else:
                    return E4k_CustomerAddress_Update(success=False, error="CountryCode does not exist.")

            if addresstypeid is not None:
                address_type = TblbusAddresstypes.objects.filter(addresstypeid=addresstypeid).first()
                if not address_type:
                    return E4k_CustomerAddress_Update(success=False, error="AddressTypeID does not exist.")
                customer_address.addresstypeid = address_type  # Assign the instance

            # Update fields if they are provided
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

            # Save the updated customer address record
            customer_address.save()

            return E4k_CustomerAddress_Update(customer_address=customer_address, success=True)
        except TblcustomerAddress.DoesNotExist:
            return E4k_CustomerAddress_Update(success=False, error="Customer Address not found.")
        except Exception as e:
            return E4k_CustomerAddress_Update(success=False, error=str(e))



        
        

class E4k_CustomerAddress_Delete(graphene.Mutation):
    class Arguments:
        addressid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, addressid, companyid):
        try:
            customer_address = TblcustomerAddress.objects.get(addressid=addressid)
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_CustomerAddress_Delete(success=False, error="CompanyID does not exist.")
            customer_address.delete()
            return E4k_CustomerAddress_Delete(success=True)
        except TblcustomerAddress.DoesNotExist:
            return E4k_CustomerAddress_Delete(success=False, error="Customer Address not found.")
        except Exception as e:
            return E4k_CustomerAddress_Delete(success=False, error=str(e))
        
####################################################

class E4k_Tblcustomermemo_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        userid = graphene.String(required=True)
        memotext = graphene.String(required=True)
        # lastupdate_date = graphene.DateTime(required=True)

    customer_memo = graphene.Field(TblcustomerMemoType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, businessid, userid, memotext):
        try:
            # Validation for foreign keys
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_Tblcustomermemo_Create(success=False, error="CompanyID does not exist.")
            if not Tblcustomer.objects.filter(businessid=businessid).exists():
                return E4k_Tblcustomermemo_Create(success=False, error="BusinessID does not exist.")
            if not TblgenUsers.objects.filter(userid=userid).exists():
                return E4k_Tblcustomermemo_Create(success=False, error="UserID does not exist.")

            # Automatically set current date and time for lastupdate_date
            lastupdatedate = datetime.now()

            # Create new memo
            customer_memo = TblcustomerMemo(
                companyid_id=companyid,
                businessid_id=businessid,
                userid_id=userid,
                memotext=memotext,
                lastupdatedate=lastupdatedate
            )
            customer_memo.save()
            return E4k_Tblcustomermemo_Create(customer_memo=customer_memo, success=True)
        
        except Exception as e:
            return E4k_Tblcustomermemo_Create(success=False, error=str(e))



class E4k_Tblcustomermemo_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        userid = graphene.String(required=True)
        memotext = graphene.String(required=True)
        # lastupdate_date = graphene.DateTime() 
    
    customer_memo = graphene.Field(TblcustomerMemoType)
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, id, companyid, businessid, userid, memotext):
        try:
            # Validation for foreign keys
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_Tblcustomermemo_Update(success=False, error="CompanyID does not exist.")
            if not Tblcustomer.objects.filter(businessid=businessid).exists():
                return E4k_Tblcustomermemo_Update(success=False, error="BusinessID does not exist.")
            if not TblgenUsers.objects.filter(userid=userid).exists():
                return E4k_Tblcustomermemo_Update(success=False, error="UserID does not exist.")
        
            lastupdatedate = datetime.now()
        
            
            # Update memo       
            customer_memo = TblcustomerMemo.objects.get(id=id)
            customer_memo.companyid_id = companyid
            customer_memo.businessid_id = businessid
            customer_memo.userid_id = userid
            customer_memo.memotext = memotext
            customer_memo.lastupdate_date = lastupdatedate
            customer_memo.save()
            return E4k_Tblcustomermemo_Update(customer_memo=customer_memo, success=True)
        except TblcustomerMemo.DoesNotExist:    
            return E4k_Tblcustomermemo_Update(success=False, error="Customer Memo not found.")
        except Exception as e:
            return E4k_Tblcustomermemo_Update(success=False, error=str(e))
  # Delete Memo from Customer      
class E4k_Tblcustomermemo_Delete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid = graphene.String(required=True)
       
    
    success = graphene.Boolean()
    error = graphene.String()
    
    def mutate(self, info, id, companyid,*kwargs ):
        try:
                 
            customer_memo = TblcustomerMemo.objects.get(id=id,companyid= companyid)
            customer_memo.delete()
            
            return E4k_Tblcustomermemo_Delete(success=True)
        except TblcustomerMemo.DoesNotExist:
            return E4k_Tblcustomermemo_Delete(success=False, error="Customer Memo not found.")
        except Exception as e:
            return E4k_Tblcustomermemo_Delete(success=False, error=str(e))

################################################### 




class E4k_CustomerAccount_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        currency_code = graphene.Int()
        vatcode = graphene.Int()
        vatflag = graphene.String()
        vatno = graphene.String()
        nomcode = graphene.String()
        repid = graphene.Int()
        rep_comission = graphene.Decimal()
        paymenttermsid = graphene.Int()
        monthly_forecast = graphene.Decimal()
        discount = graphene.Decimal()
        credit_limit = graphene.Decimal()

    customer_account = graphene.Field(TblcustomerAccountType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(
        self, 
        info, 
        companyid, 
        businessid, 
        currency_code=None, 
        vatcode=None, 
        vatflag=None, 
        vatno=None, 
        nomcode=None, 
        repid=None, 
        rep_comission=None, 
        paymenttermsid=None, 
        monthly_forecast=None, 
        discount=None, 
        credit_limit=None
    ):
        try:
            # Validation for foreign keys
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_CustomerAccount_Create(success=False, error="CompanyID does not exist.")
            if not Tblcustomer.objects.filter(businessid=businessid).exists():
                return E4k_CustomerAccount_Create(success=False, error="BusinessID does not exist.")
            if currency_code is not None and not TblbusCurrencies.objects.filter(currency_code=currency_code).exists():
                return E4k_CustomerAccount_Create(success=False, error="CurrencyCode does not exist.")
            if vatcode is not None and not TblaccVatcodes.objects.filter(vatcode=vatcode).exists():
                return E4k_CustomerAccount_Create(success=False, error="VATCode does not exist.")
            if nomcode is not None and not TblaccNominal.objects.filter(nomcode=nomcode).exists():
                return E4k_CustomerAccount_Create(success=False, error="NominalCode does not exist.")
            if repid is not None and not TblbusSalesPeople.objects.filter(repid=repid).exists():
                return E4k_CustomerAccount_Create(success=False, error="RepID does not exist.")
            if paymenttermsid is not None and not TblbusPaymentterms.objects.filter(paymenttermsid=paymenttermsid).exists():
                return E4k_CustomerAccount_Create(success=False, error="PaymentTermsID does not exist.")
            
            if discount >100 :
                return E4k_CustomerAccount_Create(success=False, error="Discount should not exceed beyond 100.")
            if rep_comission >100 :
                return E4k_CustomerAccount_Create(success=False, error="Rep Commisinon should not exceed beyond 100.")
            

            # Set the current date and time
            date_used = datetime.now()
            date_opened = datetime.now()

            # Convert empty strings to 0 for decimal fields
            def convert_decimal(value):
                if value in (None, ""):
                    return Decimal('0')
                try:
                    return Decimal(value)
                except (InvalidOperation, ValueError):
                    raise ValueError(f"Invalid decimal value: {value}")

            customer_account = TblcustomerAccount(
                companyid_id=companyid,
                businessid_id=businessid,
                discount=convert_decimal(discount),
                credit_limit=convert_decimal(credit_limit),
                currency_code_id=currency_code if currency_code is not None else None,
                vatcode_id=vatcode if vatcode is not None else None,
                vatflag=vatflag if vatflag is not None else None,
                vatno=vatno if vatno is not None else None,
                date_used=date_used,
                date_opened=date_opened,
                nominal_code_id=nomcode if nomcode is not None else None,
                repid_id=repid if repid is not None else None,
                rep_comission=convert_decimal(rep_comission),
                paymenttermsid_id=paymenttermsid if paymenttermsid is not None else None,
                monthly_forecast=convert_decimal(monthly_forecast)
            )
            customer_account.save()
            return E4k_CustomerAccount_Create(customer_account=customer_account, success=True)
        except Exception as e:
            return E4k_CustomerAccount_Create(success=False, error=str(e))

#####################################

#############################################################################


class E4k_CustomerAccount_Update(graphene.Mutation):
    class Arguments:
        businessid = graphene.String()
        companyid = graphene.String()
        discount = graphene.Decimal()
        credit_limit = graphene.Decimal()
        currency_code = graphene.Int()
        vatcode = graphene.Int()
        vatflag = graphene.String()
        vatno = graphene.String()
        nomcode = graphene.String()
        repid = graphene.Int()
        rep_comission = graphene.Decimal()
        paymenttermsid = graphene.Int()
        monthly_forecast = graphene.Decimal()
        date_opened = graphene.String()  # Change to String for date parsing
        date_used = graphene.String() 
        # nominal_code= graphene.String()# Change to String for date parsing

    customer_account = graphene.Field(TblcustomerAccountType)
    success = graphene.Boolean()
    error = graphene.String()

   
    def mutate(self, info, businessid, companyid=None, discount=None, credit_limit=None, currency_code=None,
               vatcode=None, vatflag=None, vatno=None, nomcode=None, repid=None, rep_comission=None,
               paymenttermsid=None, monthly_forecast=None, date_opened=None, date_used=None):
        try:
            customer_account = TblcustomerAccount.objects.get(businessid=businessid)
            
           

            if companyid:
                if not Tblcompany.objects.filter(companyid=companyid).exists():
                    return E4k_CustomerAccount_Update(success=False, error="CompanyID does not exist.")
                customer_account.companyid_id = companyid

            if discount is not None:
                if discount >100 :
                    return E4k_CustomerAccount_Update(success=False, error="Discount should not exceed beyond 100.")
                customer_account.discount = discount

            if credit_limit is not None:
                customer_account.credit_limit = credit_limit

            if currency_code:
                if not TblbusCurrencies.objects.filter(currency_code=currency_code).exists():
                    return E4k_CustomerAccount_Update(success=False, error="CurrencyCode does not exist.")
                customer_account.currency_code_id = currency_code

            if vatcode:
                if not TblaccVatcodes.objects.filter(vatcode=vatcode).exists():
                    return E4k_CustomerAccount_Update(success=False, error="VATCode does not exist.")
                customer_account.vatcode_id = vatcode

            if vatflag is not None:
                customer_account.vatflag = vatflag

            if vatno is not None:
                customer_account.vatno = vatno

            if nomcode:
                if not TblaccNominal.objects.filter(nomcode=nomcode).exists():
                    return E4k_CustomerAccount_Update(success=False, error="NominalCode does not exist.")
                customer_account.nominal_code_id = nomcode

            if repid:
                if not TblbusSalesPeople.objects.filter(repid=repid).exists():
                    return E4k_CustomerAccount_Update(success=False, error="RepID does not exist.")
                customer_account.repid_id = repid

            if rep_comission is not None:
                if rep_comission >100 :
                    return E4k_CustomerAccount_Update(success=False, error="Rep Commisinon should not exceed beyond 100.")
            
                customer_account.rep_comission = rep_comission

            if paymenttermsid:
                if not TblbusPaymentterms.objects.filter(paymenttermsid=paymenttermsid).exists():
                    return E4k_CustomerAccount_Update(success=False, error="PaymentTermsID does not exist.")
                customer_account.paymenttermsid_id = paymenttermsid

            if monthly_forecast is not None:
                customer_account.monthly_forecast = monthly_forecast

            # Set dates using the static method
            if date_opened:
                customer_account.date_opened = parse_date(date_opened)
            else:
                customer_account.date_opened = datetime.date.today()

            if date_used:
                customer_account.date_used = parse_date(date_used)
            else:
                customer_account.date_used = datetime.date.today()

            # Save the updated account
            customer_account.save()

            return E4k_CustomerAccount_Update(customer_account=customer_account, success=True)
        except TblcustomerAccount.DoesNotExist:
            return E4k_CustomerAccount_Update(success=False, error="Customer Account not found.")
        except ValueError as ve:
            return E4k_CustomerAccount_Update(success=False, error=str(ve))
        except Exception as e:
            return E4k_CustomerAccount_Update(success=False, error=str(e))



################################################################
class E4k_CustomerAccount_Delete(graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        # nomcode = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    customer_account = graphene.Field(TblcustomerAccountType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, businessid,companyid,*kwargs):
        try:
            customer_account = TblcustomerAccount.objects.get(businessid=businessid,companyid=companyid)
            customer_account.delete()
            return E4k_CustomerAccount_Delete(success=True)
        except TblcustomerAccount.DoesNotExist:
            return E4k_CustomerAccount_Delete(success=False, error="Customer Account not found.")
        except Exception as e:
            return E4k_CustomerAccount_Delete(success=False, error=str(e))

##################################

class E4k_TblcustomerBalance_Create(graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        companyid = graphene.String(required=True)
        balance = graphene.Decimal()
        # date_used = graphene.DateTime()
        foreignbalance = graphene.Decimal()

    customer_balance = graphene.Field(TblcustomerBalanceType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, businessid, companyid, balance,foreignbalance):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblcustomerBalance_Create(success=False, error="CompanyID does not exist.")
            if not TblcustomerAccount.objects.filter(businessid=businessid).exists():
                return E4k_TblcustomerBalance_Create(success=False, error="BusinessID does not exist.")
        
            # Set the current date and time`
            date_used = datetime.now()
            # Create new account
            customer_balance = TblcustomerBalance(
                companyid_id=companyid,
                businessid_id=businessid,
                balance=balance,
                date_used=date_used,
                foreignbalance=foreignbalance
            )
            customer_balance.save()
            return E4k_TblcustomerBalance_Create(customer_balance=customer_balance, success=True)
        except Exception as e:
            return E4k_TblcustomerBalance_Create(success=False, error=str(e))

########################################

class E4k_TblcustomerBalance_Update(graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        companyid = graphene.String(required=True)
        balance = graphene.Decimal()
        foreignbalance = graphene.Decimal()

    customer_balance = graphene.Field(TblcustomerBalanceType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, businessid, companyid, balance,foreignbalance):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblcustomerBalance_Update(success=False, error="CompanyID does not exist.")
            if not TblcustomerAccount.objects.filter(businessid=businessid).exists():
                return E4k_TblcustomerBalance_Update(success=False, error="BusinessID does not exist.")
            customer_balance = TblcustomerBalance.objects.get(businessid=businessid,companyid=companyid)
            customer_balance.balance = balance
            customer_balance.foreignbalance = foreignbalance
            customer_balance.save()
            return E4k_TblcustomerBalance_Update(customer_balance=customer_balance, success=True)
        except TblcustomerBalance.DoesNotExist:
            return E4k_TblcustomerBalance_Update(success=False, error="Customer Balance not found.")
        except Exception as e:
            return E4k_TblcustomerBalance_Update(success=False, error=str(e))

############################### Delete ########################################################

class E4k_TblcustomerBalance_Delete(graphene.Mutation):
    class Arguments:
        businessid = graphene.String(required=True)
        companyid = graphene.String(required=True)
    
    customer_balance = graphene.Field(TblcustomerBalanceType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, businessid, companyid):
        try:
            customer_balance = TblcustomerBalance.objects.get(businessid=businessid,companyid=companyid)
            customer_balance.delete()
            return E4k_TblcustomerBalance_Delete(success=True)
        except TblcustomerBalance.DoesNotExist:
            return E4k_TblcustomerBalance_Delete(success=False, error="Customer Balance not found.")
        except Exception as e:
            return E4k_TblcustomerBalance_Delete(success=False, error=str(e))
        
  ######################  

class E4k_TblaccCashbook_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)  
        transactionno  = graphene.Int(required=True)
        nomcode =   graphene.Int()
        businessid = graphene.String()
        period = graphene.Int()
        trantype  = graphene.String()
        custref = graphene.String()
        tranreference = graphene.String()
        source = graphene.String()
        debitcredit = graphene.Decimal()
        amount = graphene.Decimal()
        nomledger = graphene.String()
        batchno = graphene.String()
        reconciled = graphene.Boolean()
        cbno = graphene.Int()
        bankcode  = graphene.String()
    cashbook = graphene.Field(TblaccCashbookType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, companyid, transactionno, nomcode,businessid,  period, trantype, custref, tranreference, source, debitcredit, amount, nomledger, batchno, reconciled, cbno, bankcode):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblaccCashbook_Create(success=False, error="CompanyID does not exist.")
            if TblaccCashbook.objects.filter(transactionno=transactionno).exists():
                return E4k_TblaccCashbook_Create(success=False, error="TransactionNo already exists.")
            if not TblaccNominal.objects.filter(nomcode=nomcode).exists():
                return E4k_TblaccCashbook_Create(success=False, error="NominalCode does not exist.")
            if not TblcustomerAccount.objects.filter(businessid=businessid).exists():
                return E4k_TblaccCashbook_Create(success=False, error="BusinessID does not exist.")
        
            # Set the current date and time`
            trandate = datetime.now()
            # Create new account
            cashbook = TblaccCashbook(
                companyid_id=companyid,
                transactionno=transactionno,
                nomcode_id=nomcode,
                businessid_id=businessid,
                period=period,
                trandate = trandate,
                trantype=trantype,
                custref=custref,
                tranreference=tranreference,
                source=source,
                debitcredit=debitcredit,
                amount=amount,
                nomledger=nomledger,
                batchno=batchno,
                reconciled=reconciled,
                cbno=cbno,
                bankcode=bankcode
            )
            cashbook.save()
            return E4k_TblaccCashbook_Create(cashbook=cashbook, success=True)
        except Exception as e:
            return E4k_TblaccCashbook_Create(success=False, error=str(e))

class E4k_TblaccCashbook_Update(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        transactionno  = graphene.Int(required=True)
        nomcode =   graphene.Int()
        businessid = graphene.String()
        period = graphene.Int()
        trantype  = graphene.String()
        custref = graphene.String()
        tranreference = graphene.String()
        source = graphene.String()
        debitcredit = graphene.Decimal()
        amount = graphene.Decimal()
        nomledger = graphene.String()
        batchno = graphene.String()
        reconciled = graphene.Boolean()
        cbno = graphene.Int()
        bankcode  = graphene.String()
    cashbook = graphene.Field(TblaccCashbookType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, companyid, transactionno, nomcode,businessid,  period, trantype, custref, tranreference, source, debitcredit, amount, nomledger, batchno, reconciled, cbno, bankcode):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblaccCashbook_Update(success=False, error="CompanyID does not exist.")
            if not TblaccNominal.objects.filter(nomcode=nomcode).exists():
                return E4k_TblaccCashbook_Update(success=False, error="NominalCode does not exist.")
            if not TblcustomerAccount.objects.filter(businessid=businessid).exists():
                return E4k_TblaccCashbook_Update(success=False, error="BusinessID does not exist.")
            cashbook = TblaccCashbook.objects.get(companyid=companyid,transactionno=transactionno)
            cashbook.nomcode_id = nomcode
            cashbook.businessid_id= businessid
            cashbook.period = period
            cashbook.trantype=trantype
            cashbook.custref=custref
            cashbook.tranreference=tranreference
            cashbook.source=source
            cashbook.debitcredit=debitcredit
            cashbook.amount=amount
            cashbook.nomledger=nomledger
            cashbook.batchno=batchno
            cashbook.reconciled=reconciled
            cashbook.cbno=cbno
            cashbook.bankcode=bankcode
            cashbook.save()
        
            return E4k_TblaccCashbook_Update(cashbook=cashbook, success=True)
        except TblaccCashbook.DoesNotExist:
            return E4k_TblaccCashbook_Update(success=False, error="Cashbook not found.")
        except Exception as e:
            return E4k_TblaccCashbook_Update(success=False, error=str(e))

######################

class E4k_TblaccCashbook_Delete(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        transactionno  = graphene.Int(required=True)
    
    cashbook = graphene.Field(TblaccCashbookType)
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, companyid, transactionno):
        try:
            cashbook = TblaccCashbook.objects.get(companyid_id=companyid,transactionno=transactionno)
            cashbook.delete()
            return E4k_TblaccCashbook_Delete(success=True)
        except TblaccCashbook.DoesNotExist:
            return E4k_TblaccCashbook_Delete(success=False, error="Cashbook not found.")
        except Exception as e:
            return E4k_TblaccCashbook_Delete(success=False, error=str(e))

###########################

class E4k_TblcustomerTurnover_Create(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True) 
        companyid  = graphene.String(required=True)
        businessid = graphene.String(required=True)
        period = graphene.Int()
        turnover = graphene.Decimal()
        year = graphene.Int()
    customer_turnover = graphene.Field(TblcustomerTurnoverType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info,companyid, businessid, period, turnover, id, year):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblcustomerTurnover_Create(success=False, error="CompanyID does not exist.")
            if not TblcustomerAccount.objects.filter(businessid=businessid).exists():
                return E4k_TblcustomerTurnover_Create(success=False, error="BusinessID does not exist.")
            
            
            
            # Create new account
            customer_turnover = TblcustomerTurnover(
                id=id,
                companyid_id=companyid,
                businessid_id=businessid,
                period=period,
                turnover=turnover,
                year=year
            )
            customer_turnover.save()
            return E4k_TblcustomerTurnover_Create(customer_turnover=customer_turnover, success=True)
        except Exception as e:
            return E4k_TblcustomerTurnover_Create(success=False, error=str(e))
        
class E4k_TblcustomerTurnover_Update(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid  = graphene.String(required=True)
        businessid = graphene.String(required=True)
        period = graphene.Int()
        turnover = graphene.Decimal()
        year = graphene.Int()
    customer_turnover = graphene.Field(TblcustomerTurnoverType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info,companyid, businessid, period, turnover, id, year):
        try:
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_TblcustomerTurnover_Update(success=False, error="CompanyID does not exist.")
            if not TblcustomerAccount.objects.filter(businessid=businessid).exists():
                return E4k_TblcustomerTurnover_Update(success=False, error="BusinessID does not exist.")
            customer_turnover = TblcustomerTurnover.objects.get(id=id)
            customer_turnover.companyid_id=companyid
            customer_turnover.businessid_id=businessid
            customer_turnover.period=period
            customer_turnover.turnover=turnover
            customer_turnover.year=year
            customer_turnover.save()
            return E4k_TblcustomerTurnover_Update(customer_turnover=customer_turnover, success=True)
        except TblcustomerTurnover.DoesNotExist:
            return E4k_TblcustomerTurnover_Update(success=False, error="CustomerTurnover not found.")
        except Exception as e:
            return E4k_TblcustomerTurnover_Update(success=False, error=str(e))

class E4k_TblcustomerTurnover_Delete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        companyid  = graphene.String(required=True)
    
    customer_turnover = graphene.Field(TblcustomerTurnoverType)
    success = graphene.Boolean()
    error = graphene.String()
    def mutate(self, info, companyid, id):
        try:
            customer_turnover = TblcustomerTurnover.objects.get(id=id, companyid=companyid)
            customer_turnover.delete()
            return E4k_TblcustomerTurnover_Delete(success=True)
        except TblcustomerTurnover.DoesNotExist:
            return E4k_TblcustomerTurnover_Delete(success=False, error="CustomerTurnover not found.")
        except Exception as e:
            return E4k_TblcustomerTurnover_Delete(success=False, error=str(e))
                  

###################################### both address and contact delete ##########################################
class E4k_DeleteAddressAndContacts(graphene.Mutation):
    class Arguments:
        addressid = graphene.Int(required=True)
        companyid = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, addressid, companyid):
        try:
            # Check if the company exists
            if not Tblcompany.objects.filter(companyid=companyid).exists():
                return E4k_DeleteAddressAndContacts(success=False, error="CompanyID does not exist.")

            # Find the customer address
            try:
                customer_address = TblcustomerAddress.objects.get(addressid=addressid)
            except TblcustomerAddress.DoesNotExist:
                return E4k_DeleteAddressAndContacts(success=False, error="Customer Address not found.")

            # Delete associated contacts first
            contacts = TblcustomerContact.objects.filter(addressid=addressid, companyid=companyid)
            if contacts.exists():
                contacts.delete()

            # Delete the customer address
            customer_address.delete()

            # Optionally, reduce the ID numbers (if needed)
           

            return E4k_DeleteAddressAndContacts(success=True)

        except Exception as e:
            return E4k_DeleteAddressAndContacts(success=False, error=str(e))
        
        
        
################################################################################################

class E4k_TblCustomer_SetValueUpdate(graphene.Mutation):
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
                businessid = Tblcustomer.objects.get(businessid = businessid)
                customer_settingid = TblcustomerSettings.objects.get(settingid = settingid , companyid = compan)
                try:
                    if customer_settingid.default == value:
                        if customer_settingid.default !=''  and  value != '' :
                            try:
                                setvalues = TblcustomerSetvalues.objects.get(settingid =settingid, companyid = compan , businessid = businessid)
                                setvalues.delete()
                            except TblcustomerSetvalues.DoesNotExist:
                                pass
                        elif customer_settingid.default == '' and value == '':
                            try:
                                setvalues1 = TblcustomerSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                setvalues1.delete()
                                
                            except TblcustomerSetvalues.DoesNotExist:
                                pass
                            
                        elif customer_settingid.default !='' and value =='':
                            try :
                                setvalues2 = TblcustomerSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                setvalues2.delete()
                            except TblcustomerSetvalues.DoesNotExist:
                                pass
                    
                    else :
                        if customer_settingid.default != value:
                            if customer_settingid.default == None and value != '':
                                try:
                                    setvalues  = TblcustomerSetvalues.objects.create(companyid = compan , businessid = businessid , settingid = customer_settingid, value = value)
                                    setvalues.save()
                                except TblcustomerSetvalues.DoesNotExist:
                                    pass
                            elif  value =='' and customer_settingid.default is not None:
                                try:
                                    setvalues1 = TblcustomerSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                    setvalues1.delete()
                                except TblcustomerSetvalues.DoesNotExist:
                                    pass
                            elif value!= '' and customer_settingid.default!= value:
                                try:
                                    setvalues2 = TblcustomerSetvalues.objects.get(companyid = compan , businessid = businessid , settingid = customer_settingid)
                                    setvalues2.value = value 
                                    setvalues2.save()
                                except TblcustomerSetvalues.DoesNotExist:
                                    setvalues3 = TblcustomerSetvalues.objects.create(companyid = compan , businessid = businessid , settingid = customer_settingid , value = value) 
                                    
                                    setvalues3.save()
                
                    return  E4k_TblCustomer_SetValueUpdate(customersetvalues ='Success')  
                except TblcustomerSetvalues.DoesNotExist:
                    return  E4k_TblCustomer_SetValueUpdate(customersetvalues ='SettingID does not exist')
        except Tblcompany.DoesNotExist:
            return  E4k_TblCustomer_SetValueUpdate(customersetvalues ='CompanyID does not exist')
        except Tblcustomer.DoesNotExist:
            return  E4k_TblCustomer_SetValueUpdate(customersetvalues ='BusinessID does not exist')
        except Exception as e:
            return  E4k_TblCustomer_SetValueUpdate(customersetvalues = str(e))
        


class E4k_TblCustomerLogo_Create(graphene.Mutation):
    class Arguments:
        companyid = graphene.String(required=True)
        businessid = graphene.String(required=True)
        settingid = graphene.String(required=True)
        value = graphene.String(required=True)  # This will hold the base64-encoded image string

    logo = graphene.String()  # This will return the file path after the mutation
    message = graphene.String()
    success = graphene.Boolean()  # Field to indicate success or error
    error = graphene.String()  # Field to provide error details

    @staticmethod
    def mutate(root, info, companyid, businessid, settingid, value):
        try:
            # Fetch company, business, and setting objects
            company = Tblcompany.objects.get(companyid=companyid)
            business = Tblcustomer.objects.get(businessid=businessid)
            setting = TblcustomerSettings.objects.get(settingid=settingid)

            # Check if the provided value is a valid base64 string
            if value:
                # Decode the base64 image string
                image_data = base64.b64decode(value)
                
                # Define the external directory to save the uploaded image
                file_dir = settings.EXTERNAL_MEDIA_ROOT
                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)
                
                # Define the file name (e.g., companyid_businessid.png)
                file_name = f"{companyid}_{businessid}.png"  # You can change the extension based on the image format
                file_path = os.path.join(file_dir, file_name)

                # Save the decoded image to the file path
                with open(file_path, 'wb') as image_file:
                    image_file.write(image_data)

                # Store the file path in the value field of TblcustomerSetvalues
                Logo, created = TblcustomerSetvalues.objects.update_or_create(
                    companyid=company,
                    businessid=business,
                    settingid=setting,
                    defaults={'value': file_path}  # Save the external file path
                )

                return E4k_TblCustomerLogo_Create(
                    logo=file_path,
                    message="Logo uploaded and saved successfully.",
                    success=True,  # Indicate success
                    error=None  # No error
                )
            else:
                return E4k_TblCustomerLogo_Create(
                    logo=None,
                    message="No logo provided.",
                    success=False,  # Indicate failure
                    error="No logo data was provided."  # Error detail
                )

        except Tblcompany.DoesNotExist:
            return E4k_TblCustomerLogo_Create(
                logo=None,
                message=f"Company with ID {companyid} does not exist.",
                success=False,  # Indicate failure
                error=f"Company with ID {companyid} does not exist."  # Error detail
            )
        except Tblcustomer.DoesNotExist:
            return E4k_TblCustomerLogo_Create(
                logo=None,
                message=f"Business with ID {businessid} does not exist.",
                success=False,  # Indicate failure
                error=f"Business with ID {businessid} does not exist."  # Error detail
            )
        except TblcustomerSettings.DoesNotExist:
            return E4k_TblCustomerLogo_Create(
                logo=None,
                message=f"Setting with ID {settingid} does not exist.",
                success=False,  # Indicate failure
                error=f"Setting with ID {settingid} does not exist."  # Error detail
            )
        except Exception as e:
            return E4k_TblCustomerLogo_Create(
                logo=None,
                message="An unexpected error occurred.",
                success=False,  # Indicate failure
                error=str(e)  # Provide the error message
            )




# class E4k_CustomerAndAccount_Create(graphene.Mutation):
#     class Arguments:
#         companyid = graphene.String(required=True)
#         businessid = graphene.String(required=True)
#         name = graphene.String()
#         countryid = graphene.Int()
#         islive = graphene.Boolean()
#         category1id = graphene.Int()
#         category2id = graphene.Int()
#         category3id = graphene.Int()
#         classid = graphene.Int()
#         groupid = graphene.Int()
#         default_nominal = graphene.Int()
#         isextract = graphene.Boolean()
#         isstop = graphene.Boolean()
#         currency_code = graphene.Int()
#         vatcode = graphene.Int()
#         vatflag = graphene.String()
#         vatno = graphene.String()
#         nomcode = graphene.String()
#         repid = graphene.Int()
#         rep_comission = graphene.Decimal()
#         paymenttermsid = graphene.Int()
#         monthly_forecast = graphene.Decimal()
#         discount = graphene.Decimal()
#         credit_limit = graphene.Decimal()
#         note = graphene.String()
#         userid = graphene.String()


#     success = graphene.Boolean()
#     error = graphene.String()

#     def mutate(self, info, **kwargs):
#         errors = []

#         companyid = kwargs.get('companyid')
#         businessid = kwargs.get('businessid')

#         # Start a transaction to ensure consistency
#         with transaction.atomic():
#             try:
#                 # Check if the customer exists, if not, create it
#                 customer, created = Tblcustomer.objects.get_or_create(
#                     companyid_id=companyid,
#                     businessid=businessid,
#                     defaults={
#                         'name': kwargs.get('name'),
#                         'countryid_id': kwargs.get('countryid'),
#                         'islive': kwargs.get('islive', True),
#                         'category1id_id': kwargs.get('category1id'),
#                         'category2id_id': kwargs.get('category2id'),
#                         'category3id_id': kwargs.get('category3id'),
#                         'classid_id': kwargs.get('classid'),
#                         'groupid_id': kwargs.get('groupid'),
#                         'default_nominal_id': kwargs.get('default_nominal'),
#                         'isextract': kwargs.get('isextract', False),
#                         'isstop': kwargs.get('isstop', False)
#                     }
#                 )

#                 if not created:
#                     return E4k_CustomerAndAccount_Create(success=False, error="Customer with this BusinessID already exists.")

#             except Exception as e:
#                 return E4k_CustomerAndAccount_Create(success=False, error=f"Customer creation failed: {str(e)}")

#             try:
#                 # Helper function to convert values to Decimal or set as 0 if missing
#                 def convert_decimal(value):
#                     if value in (None, ""):
#                         return Decimal('0')
#                     try:
#                         return Decimal(value)
#                     except (InvalidOperation, ValueError):
#                         raise ValueError(f"Invalid decimal value: {value}")

#                 # Check if customer account exists, if not, create it
#                 customer_account, account_created = TblcustomerAccount.objects.get_or_create(
#                     companyid_id=companyid,
#                     businessid_id=businessid,
#                     defaults={
#                         'currency_code_id': kwargs.get('currency_code', None),
#                         'vatcode_id': kwargs.get('vatcode', None),
#                         'vatflag': kwargs.get('vatflag', None),
#                         'vatno': kwargs.get('vatno', None),
#                         'nominal_code_id': kwargs.get('nomcode', None),
#                         'repid_id': kwargs.get('repid', None),
#                         'rep_comission': convert_decimal(kwargs.get('rep_comission')),
#                         'paymenttermsid_id': kwargs.get('paymenttermsid', None),
#                         'monthly_forecast': convert_decimal(kwargs.get('monthly_forecast')),
#                         'discount': convert_decimal(kwargs.get('discount')),
#                         'credit_limit': convert_decimal(kwargs.get('credit_limit')),
#                         'date_used': datetime.now(),
#                         'date_opened': datetime.now()
#                     }
#                 )
                
           

#                 if not account_created:
#                     # If the customer account already exists, you can return a message.
#                     return E4k_CustomerAndAccount_Create(success=False, error="Customer Account already exists for this BusinessID.")

#                 return E4k_CustomerAndAccount_Create(success=True)

#             except Exception as e:
#                 # Rollback transaction if any error occurs
#                 transaction.set_rollback(True)
#                 return E4k_CustomerAndAccount_Create(success=False, error=f"Account creation failed: {str(e)}")
            
            






class E4k_CustomerAndAccount_Create(graphene.Mutation):
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
        groupid = graphene.Int()
        default_nominal = graphene.Int()
        isextract = graphene.Boolean()
        isstop = graphene.Boolean()
        currency_code = graphene.Int()
        vatcode = graphene.Int()
        vatflag = graphene.String()
        vatno = graphene.String()
        nomcode = graphene.String()
        repid = graphene.Int()
        rep_comission = graphene.Decimal()
        paymenttermsid = graphene.Int()
        monthly_forecast = graphene.Decimal()
        discount = graphene.Decimal()
        credit_limit = graphene.Decimal()
        note = graphene.String()
        userid = graphene.String()

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, **kwargs):
        companyid = kwargs.get('companyid')
        businessid = kwargs.get('businessid')

        # Start a transaction to ensure consistency
        with transaction.atomic():
            try:
                # Check if the customer exists, if not, create it
                customer, created = Tblcustomer.objects.get_or_create(
                    companyid_id=companyid,
                    businessid=businessid,
                    defaults={
                        'name': kwargs.get('name'),
                        'countryid_id': kwargs.get('countryid'),
                        'islive': kwargs.get('islive', True),
                        'category1id_id': kwargs.get('category1id'),
                        'category2id_id': kwargs.get('category2id'),
                        'category3id_id': kwargs.get('category3id'),
                        'classid_id': kwargs.get('classid'),
                        'groupid_id': kwargs.get('groupid'),
                        'default_nominal_id': kwargs.get('default_nominal'),
                        'isextract': kwargs.get('isextract', False),
                        'isstop': kwargs.get('isstop', False)
                    }
                )

                if not created:
                    return E4k_CustomerAndAccount_Create(success=False, error="Customer with this BusinessID already exists.")

            except Exception as e:
                transaction.set_rollback(True)  # Ensure transaction is rolled back on failure
                return E4k_CustomerAndAccount_Create(success=False, error=f"Customer creation failed: {str(e)}")

            try:
                # Helper function to convert values to Decimal or set as 0 if missing
                def convert_decimal(value):
                    if value in (None, ""):
                        return Decimal('0')
                    try:
                        return Decimal(value)
                    except (InvalidOperation, ValueError):
                        raise ValueError(f"Invalid decimal value: {value}")

                # Check if customer account exists, if not, create it
                customer_account, account_created = TblcustomerAccount.objects.get_or_create(
                    companyid_id=companyid,
                    businessid_id=businessid,
                    defaults={
                        'currency_code_id': kwargs.get('currency_code', None),
                        'vatcode_id': kwargs.get('vatcode', None),
                        'vatflag': kwargs.get('vatflag', None),
                        'vatno': kwargs.get('vatno', None),
                        'nominal_code_id': kwargs.get('nomcode', None),
                        'repid_id': kwargs.get('repid', None),
                        'rep_comission': convert_decimal(kwargs.get('rep_comission')),
                        'paymenttermsid_id': kwargs.get('paymenttermsid', None),
                        'monthly_forecast': convert_decimal(kwargs.get('monthly_forecast')),
                        'discount': convert_decimal(kwargs.get('discount')),
                        'credit_limit': convert_decimal(kwargs.get('credit_limit')),
                        'date_used': datetime.now(),
                        'date_opened': datetime.now()
                    }
                )

                if not account_created:
                    return E4k_CustomerAndAccount_Create(success=False, error="Customer Account already exists for this BusinessID.")

            except Exception as e:
                transaction.set_rollback(True)
                return E4k_CustomerAndAccount_Create(success=False, error=f"Account creation failed: {str(e)}")

            try:
                # Create or retrieve the customer note
                customer_note, note_created = TblcustomerNotes.objects.get_or_create(
                    companyid_id=companyid,
                    businessid_id=businessid,
                    defaults={
                        'note': kwargs.get('note', ""),
                        'userid_id': kwargs.get('userid', None)
                    }
                )
                if not note_created:
                    return E4k_CustomerAndAccount_Create(success=False, error="Customer Note already exists for this BusinessID.")

            except Exception as e:
                transaction.set_rollback(True)
                return E4k_CustomerAndAccount_Create(success=False, error=f"Customer Note creation failed: {str(e)}")

            # If all operations were successful, return success
            return E4k_CustomerAndAccount_Create(success=True)


            

                




            

class CustomerMutation(graphene.ObjectType):
# 1 Company Mutaion Decleration
    E4k_CompanyCreate = E4k_Company_Create.Field()
    E4k_CompanyUpdate = E4k_Company_Update.Field()
    E4k_CompanyDelete = E4k_Company_Delete.Field()
# 2 country Mutation  Decleration  
    E4k_CountryCreate = E4k_Country_Create.Field()
    E4k_CountryUpdate = E4K_Country_Update.Field()
    E4k_CountryDelete = E4k_Country_Delete.Field()
# 3 countryMember Mutation Declareation
    E4k_CountryMemberCreate = E4k_CountryMember_Create.Field()
    E4k_CountryMemberUpdate =  E4k_CountryMember_Update.Field()
    E4k_CountryMemberDelete = E4k_CountryMember_Delete.Field()
# 4 Currency tbl Mutation Declaretion
    E4k_CurrencyCreate = E4k_Currency_Create.Field()
    E4k_CurrencyUpdate = E4k_Currency_Update.Field()
    E4K_CurrencyDelete = E4k_Currency_Delete.Field()
# 5 CustomerCategory1 tbl Mutation Declareation 
    E4k_CustomerCategory1Create= E4k_CustomerCategory1_Create.Field()
    E4k_CustomerCategory1Update= E4k_CustomerCategory1_Update.Field()
    E4k_CustomerCategory1Delete= E4k_CustomerCategory1_Delete.Field()
# 6 CustomerCategory2 tbl Mutation Declaretion
    E4k_CustomerCategory2Create= E4k_CustomerCategory2_Create.Field()
    E4k_CustomerCategory2Update= E4k_CustomerCategory2_Update.Field()
    E4k_CustomerCategory2Delete= E4k_CustomerCategory2_Delete.Field()
# 7 CustomerCategory3 tbl Mutation Decleration
    E4k_CustomerCategory3Create= E4k_CustomerCategory3_Create.Field()
    E4k_CustomerCategory3Update= E4k_CustomerCategory3_Update.Field()
    E4k_CustomerCategory3Delete= E4k_CustomerCategory3_Delete.Field()
# 8 CustomerClass tbl Mutation Decleration
    E4k_CustomerClassCreate = E4k_CustomerClass_Create.Field()
    E4k_CustomerClassUpdate = E4k_CustomerClass_Update.Field()
    E4K_CustomerClassDelete = E4k_CustomerClass_Delete.Field()
# 9 Group tbl Mutation Decleration   
    E4k_TblbusGroupCreate = E4K_TblbusGroup_Create.Field()
    E4k_TblbusGroupUpdate = E4k_TblbusGroup_Update.Field()
    E4k_TblbusGroupDelete = E4k_TblbusGroup_Delete.Field()
# 10 TblAcc Mutation Decleration
    E4k_TblacctNominalcreate = E4k_TblaccNominal_create.Field()
    E4k_TblaccNominalUpdate  = E4k_TblaccNominal_Update.Field()
    E4k_TblaccNominalDelete = E4k_TblaccNominal_Delete.Field()
# 11 TblaccVATCode Mutation Decleration
    E4k_TblaccVATCodesCreate = E4k_TblaccVatcodes_Create.Field()
    E4k_TblaccVatcodesUpdate = E4k_TblaccVatcodes_Update.Field()
    E4k_TblaccVatcodesDelete =E4k_TblaccVatcodes_Delete.Field()
# 12 TblbusServicepeople                                                                                                                
    E4k_TblbusServicePeopleCreate =E4k_TblbusServicePeople_Create.Field()
    E4k_TblbusServicePeopleUpdate = E4k_TblbusServicePeople_Update.Field()
    E4k_TblbusServicePeopleDelete = E4k_TblbusServicePeople_Delete.Field()

# 13  TblbusSalesPeople Mutation Decleration
    E4k_TblbusSalesPeopleCreate = E4k_TblbusSalesPeople_Create.Field() 
    E4k_TblbusSalesPeoplDelete = E4k_TblbusSalesPeople_Delete.Field()
    E4k_TblbusSalesPeopleUpdate = E4k_TblbusSalesPeople_Update.Field()
# 14 TblbusPaymenttermsRefCreate
    E4K_TblbusPaymenttermsRefCreate = E4K_TblbusPaymenttermsRef_Create.Field()
    E4K_TblbusPaymenttermsRefUpdate = E4k_TblbusPaymenttermsRef_Update.Field()
    E4K_TblbusPaymenttermsRefDelete = E4k_TblbusPaymenttermsRef_Delete.Field()
# 15 TblbusPaymentterms Tbl 
    E4k_TblbusPaymenttermsCreate = E4k_TblbusPaymentterms_Create.Field()
    E4k_TblbusPaymentterms_Update = E4k_TblbusPaymentterms_Update.Field()
    E4k_TblbusPaymenttermsDelete = E4k_TblbusPaymentterms_Delete.Field()
# 16 tblaccNominalTrans Tbl Mutation Declerations   
    E4k_TblaccNominalTrancreate = E4k_TblaccNominalTran_Create.Field()
    E4k_TblaccNominalTranUpdate = E4k_TblaccNominal_Update.Field()
    E4k_TblaccNominalTranDelete = E4k_TblaccNominalTran_Delete.Field()
# 17 Tbladdress_Ref Tbl Mutation Decleration
    E4k_TblbusAddresstypeRefCreate = E4k_TblbusAddresstypeRef_Create.Field()
    E4k_TblbusAddresstypeRefUpdate = E4k_TblbusAddresstypeRef_Update.Field()
    E4k_TblbusAddresstypeRefDelete = E4k_TblbusAddresstypeRef_Delete.Field()
# 18 TblAddresstype Tbl Mutation Decleration
    E4k_TblbusAddresstypeCreate = E4k_TblbusAddressType_Create.Field() 
    E4k_TblbusAddresstypeUpdate = E4k_TblbusAddresstypes_Update.Field()  
    E4k_TblbusAddresstypeDelete = E4k_TblbusAddresstypes_Delete.Field()
# 19 TblbusContactRef Tbl Mutation Decleration
    E4k_TblbusContactRefCreate = E4k_TblbusContactRef_Create.Field()
    E4k_TblbusContactRefUpdate = E4k_TblbusContactRef_Update.Field()
    E4k_TblbusContactRefDelete = E4k_TblbusContactRef_Delete.Field()
# 20 TblCustomerContact Tbl Mutation Decleration    
    E4k_TblcustomerContactCreate = E4k_TblcustomerContact_Create.Field()
    E4k_TblcustomerContactUpdate = E4k_TblcustomerContact_Update.Field()
    E4k_TblcustomerContactDelete = E4k_TblcustomerContact_Delete.Field()
    E4k_CustomerContactDelete= E4k_CustomerContact_Delete.Field()
# 21 Tblcustomer Tbl Mutation Decleration
    E4k_TblcustomerCreate = E4k_Tblcustomer_Create.Field()    
    E4k_TblcustomerUpdate = E4k_Tblcustomer_Update.Field()
    E4k_TblcustomerDelete = E4k_Tblcustomer_Delete.Field()
# 22 Tblcustomer
    E4k_TblcustomerServicePepleCreate = E4k_TblcustomerServicePeple_Create.Field()
    E4k_TblcustomerServicePepleUpdate =  E4k_TblcustomerServicePeple_Update.Field()
    E4k_TblcustomerServicePeple_Delete = E4k_TblcustomerServicePeple_Delete. Field()
#  23 TblcustomerSales tbl  
    E4k_TblcustomerSalesTransCreate = E4k_TblcustomerSalesTrans_Create.Field()  
    E4k_TblcustomerSalesTransUpdate = E4k_TblcustomerSalesTrans_Update.Field()
    E4k_TblcustomerSalesTransDelete = E4k_TblcustomerSalesTrans_Delete.Field()
# 24 Tbcustomer Note Tbl
    E4k_CustomerNoteCreate = E4k_CustomerNote_Create.Field()
    E4k_CustomerNoteUpdate = E4k_CustomerNote_Update.Field()
    E4k_CustomerNoteDelete = E4k_CustomerNote_Delete.Field()

# 25  gen User Table Mutation Decleration       
    E4k_TblgenUsersCreate  = E4k_TblgenUsers_Create.Field()
    E4k_TblgenUsers_Update = E4k_TblgenUsers_Update.Field()    
    E4k_TblgenUsers_Delete = E4k_TblgenUsers_Delete.Field()
# 26 Addresss 
    E4k_TblustomerAddressCreate = E4k_CustomerAddress_Create.Field()
    E4k_CustomerAddressUpdate = E4k_CustomerAddress_Update.Field()
    E4k_TblcustomerAddressDelete = E4k_CustomerAddress_Delete.Field()     
# 27 Memo
    E4k_TblcustomermemoCreate = E4k_Tblcustomermemo_Create.Field()
    E4k_TblcustomermemoUpdate = E4k_Tblcustomermemo_Update.Field()  
    E4k_TblcustomermemoDelete = E4k_Tblcustomermemo_Delete.Field()
# 28 Account
    E4k_CustomerAccountCreate = E4k_CustomerAccount_Create.Field()  
    E4k_CustomerAccountUpdate = E4k_CustomerAccount_Update.Field()
    E4k_CustomerAccountDelete = E4k_CustomerAccount_Delete.Field()
# 29 Balance  
    E4k_TblcustomerBalanceCreate = E4k_TblcustomerBalance_Create.Field()
    E4k_TblcustomerBalanceUpdate = E4k_TblcustomerBalance_Update.Field()
    E4k_TblcustomerBalanceDelete = E4k_TblcustomerBalance_Delete.Field()
# 30 Cashbook 
    E4k_TblaccCashbookCreate = E4k_TblaccCashbook_Create.Field() 
    E4k_TblaccCashbookUpdate = E4k_TblaccCashbook_Update.Field()
    E4k_TblaccCashbookDelete = E4k_TblaccCashbook_Delete.Field()
# 31 Turnover
    E4k_TblcustomerTurnoverCreate = E4k_TblcustomerTurnover_Create.Field()
    E4k_TblcustomerTurnoverUpdate = E4k_TblcustomerTurnover_Update.Field()
    E4k_TblcustomerTurnoverDelete = E4k_TblcustomerTurnover_Delete.Field()

    # E4kTblcustomerSetvaluesCreate  = E4k_CreateTblcustomerSetvalues.Field()
    E4kDeleteAddressAndContacts = E4k_DeleteAddressAndContacts.Field()
    E4kTblCustomerSetValueUpdate = E4k_TblCustomer_SetValueUpdate.Field()
     

    create_customer_logo = E4k_TblCustomerLogo_Create.Field()
    E4k_CustomerAndAccount_Create = E4k_CustomerAndAccount_Create.Field()