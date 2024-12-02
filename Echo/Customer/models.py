from django.db import models

# Customer Phase Models and Supplier Models 

class TblaccCashbook(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    transactionno = models.IntegerField(db_column='TransactionNo', primary_key=True)  # Field name made lowercase.
    nomcode = models.ForeignKey('TblaccNominal', models.DO_NOTHING, db_column='NomCode')  # Field name made lowercase.
    businessid = models.ForeignKey('Tblcustomer', models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trandate = models.DateTimeField(db_column='TranDate', blank=True, null=True)  # Field name made lowercase.
    custref = models.CharField(db_column='CustRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tranreference = models.CharField(db_column='TranReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.IntegerField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    debitcredit = models.CharField(db_column='DebitCredit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nomledger = models.CharField(db_column='NomLedger', max_length=50, blank=True, null=True)  # Field name made lowercase.
    batchno = models.IntegerField(db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    reconciled = models.BooleanField(db_column='Reconciled',default=False)  # Field name made lowercase. This field type is a guess.
    cbno = models.IntegerField(db_column='CBNo', blank=True, null=True)  # Field name made lowercase.
    bankcode = models.CharField(db_column='BankCode', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblacc_cashbook'


class TblaccNominal(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    nomcode = models.CharField(db_column='NomCode', primary_key=True, max_length=12)  # Field name made lowercase.
    nomdescription = models.CharField(db_column='NomDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomdc = models.CharField(db_column='NomDC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nompl = models.IntegerField(db_column='NomPL', blank=True, null=True)  # Field name made lowercase.
    nombs = models.IntegerField(db_column='NomBS', blank=True, null=True)  # Field name made lowercase.
    live = models.BooleanField(db_column='Live',default=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'tblacc_nominal'


class TblaccNominalTran(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    transactionno = models.IntegerField(db_column='TransactionNo', primary_key=True)  # Field name made lowercase.
    nomcode = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='NomCode', blank=True, null=True)  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.
    trandate = models.DateTimeField(db_column='TranDate', blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TranType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    businessid = models.ForeignKey('Tblcustomer', models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    tranreference = models.CharField(db_column='TranReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.IntegerField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    debitcredit = models.CharField(db_column='DebitCredit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nomledger = models.CharField(db_column='NomLedger', max_length=50, blank=True, null=True)  # Field name made lowercase.
    batchno = models.IntegerField(db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    narrative = models.CharField(db_column='Narrative', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblacc_nominal_tran'


class TblaccVatcodes(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    vatcode = models.IntegerField(db_column='VATCode', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sagecode = models.CharField(db_column='SageCode', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblacc_vatcodes'


class TblbusAddresstypeRef(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    actual_typeid = models.IntegerField(db_column='Actual_TypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_addresstype_ref'


class TblbusAddresstypes(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    addresstypeid = models.IntegerField(db_column='AddressTypeID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actual_typeid = models.ForeignKey(TblbusAddresstypeRef, models.DO_NOTHING, db_column='Actual_TypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_addresstypes'


class TblbusContactRef(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    contacttype_id = models.IntegerField(db_column='ContactType_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_contact_ref'


class TblbusCountries(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', primary_key=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('TblbusCountryMembers', models.DO_NOTHING, db_column='Member', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_countries'


class TblbusCountryMembers(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_country_members'


class TblbusCurrencies(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    currency_code = models.IntegerField(db_column='Currency_Code', primary_key=True)  # Field name made lowercase.
    currency_name = models.CharField(db_column='Currency_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    currency_symbol = models.CharField(db_column='Currency_Symbol', max_length=4, blank=True, null=True)  # Field name made lowercase.
    currency_exchange_rate = models.DecimalField(db_column='Currency_Exchange_Rate', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isocode = models.CharField(db_column='ISOCode', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_currencies'


class TblbusGroups(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_groups'


class TblbusPaymentterms(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    paymenttermsid = models.IntegerField(db_column='PaymentTermsID', primary_key=True)  # Field name made lowercase.
    typeid = models.ForeignKey('TblbusPaymenttermsRef', models.DO_NOTHING, db_column='TypeID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    days = models.CharField(db_column='Days', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_paymentterms'


class TblbusPaymenttermsRef(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    term_typeid = models.IntegerField(db_column='Term_TypeID', primary_key=True)  # Field name made lowercase.
    term_type_name = models.CharField(db_column='Term_Type_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    term_type_formula = models.CharField(db_column='Term_Type_Formula', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_paymentterms_ref'


class TblbusSalesPeople(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    repid = models.IntegerField(db_column='RepID', primary_key=True)  # Field name made lowercase.
    repkey = models.CharField(db_column='RepKey', max_length=10, blank=True, null=True)  # Field name made lowercase.
    forename = models.CharField(db_column='Forename', max_length=50, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    live = models.BooleanField(db_column='Live',default=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'tblbus_sales_people'


class TblbusServicePeople(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    csgroupid = models.IntegerField(db_column='CSGroupID', primary_key=True)  # Field name made lowercase.
    csname = models.CharField(db_column='CSName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblbus_service_people'


class TblcmpDefaults(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    paramid = models.CharField(db_column='ParamID', primary_key=True, max_length=20)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=150, blank=True, null=True)  # Field name made lowercase.
    paramgroup = models.CharField(db_column='ParamGroup', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcmp_defaults'


class Tblcompany(models.Model):
    companyid = models.CharField(db_column='CompanyID', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vatno = models.CharField(db_column='VATno', max_length=12, blank=True, null=True)  # Field name made lowercase.
    holdingcompany = models.CharField(db_column='HoldingCompany', max_length=3, blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    currency_code = models.ForeignKey(TblbusCurrencies, models.DO_NOTHING, db_column='Currency_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcompany'


class Tblcustomer(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.CharField(db_column='BusinessID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # countryid = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryID', null=True, blank=True)  # Allow NULL value
    islive = models.BooleanField(db_column='IsLive',default=True)  # Field name made lowercase. This field type is a guess.
    category1id = models.ForeignKey('TblcustomerCategory1', models.DO_NOTHING, db_column='Category1ID', blank=True, null=True)  # Field name made lowercase.
    category2id = models.ForeignKey('TblcustomerCategory2', models.DO_NOTHING, db_column='Category2ID', blank=True, null=True)  # Field name made lowercase.
    category3id = models.ForeignKey('TblcustomerCategory3', models.DO_NOTHING, db_column='Category3ID', blank=True, null=True)  # Field name made lowercase.
    classid = models.ForeignKey('TblcustomerClass', models.DO_NOTHING, db_column='ClassID', blank=True, null=True)  # Field name made lowercase.
    groupid = models.ForeignKey(TblbusGroups, models.DO_NOTHING, db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    default_nominal = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='Default_Nominal', blank=True, null=True)  # Field name made lowercase.
    isextract = models.BooleanField(db_column='IsExtract',default=False)  # Field name made lowercase. This field type is a guess.
    isstop = models.BooleanField(db_column='IsStop', default=False,blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'tblcustomer'


class TblcustomerAccount(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.OneToOneField(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', primary_key=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    credit_limit = models.DecimalField(db_column='Credit_Limit', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currency_code = models.ForeignKey(TblbusCurrencies, models.DO_NOTHING, db_column='Currency_Code', blank=True, null=True)  # Field name made lowercase.
    vatcode = models.ForeignKey(TblaccVatcodes, models.DO_NOTHING, db_column='VATCode', blank=True, null=True)  # Field name made lowercase.
    vatflag = models.CharField(db_column='VATFlag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vatno = models.CharField(db_column='VATNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_used = models.DateTimeField(db_column='Date_Used', blank=True, null=True)  # Field name made lowercase.
    date_opened = models.DateTimeField(db_column='Date_Opened', blank=True, null=True)  # Field name made lowercase.
    nominal_code = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='Nominal_Code', blank=True, null=True)  # Field name made lowercase.
    repid = models.ForeignKey(TblbusSalesPeople, models.DO_NOTHING, db_column='RepID', blank=True, null=True)  # Field name made lowercase.
    rep_comission = models.DecimalField(db_column='Rep_Comission', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    paymenttermsid = models.ForeignKey(TblbusPaymentterms, models.DO_NOTHING, db_column='PaymentTermsID', blank=True, null=True)  # Field name made lowercase.
    monthly_forecast = models.DecimalField(db_column='Monthly_Forecast', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_account'


class TblcustomerAddress(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase. The composite primary key (BusinessID, AddressID) found, that is not supported. The first column is selected.
    addressid = models.IntegerField(db_column='AddressID',primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=75, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=75, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=75, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=75, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(db_column='County', max_length=75, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryCode', blank=True, null=True)  # Field name made lowercase.
    addresstypeid = models.ForeignKey(TblbusAddresstypes, models.DO_NOTHING, db_column='AddressTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_address'
        


class TblcustomerAddressMappings(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    invaddressid = models.ForeignKey(TblcustomerAddress, models.DO_NOTHING, db_column='InvAddressID', to_field='addressid')  # Field name made lowercase.
    deladdressid = models.ForeignKey(TblcustomerAddress, models.DO_NOTHING, db_column='DelAddressID', to_field='addressid', related_name='tblcustomeraddressmappings_deladdressid_set')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_address_mappings'


class TblcustomerBalance(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.OneToOneField(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', primary_key=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    date_used = models.DateTimeField(db_column='Date_Used', blank=True, null=True)  # Field name made lowercase.
    foreignbalance = models.DecimalField(db_column='ForeignBalance', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_balance'


class TblcustomerCategory1(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category1id = models.IntegerField(db_column='Category1ID', primary_key=True)  # Field name made lowercase.
    category1name = models.CharField(db_column='Category1Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_category1'


class TblcustomerCategory2(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category2id = models.IntegerField(db_column='Category2ID', primary_key=True)  # Field name made lowercase.
    category2name = models.CharField(db_column='Category2Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_category2'


class TblcustomerCategory3(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category3id = models.IntegerField(db_column='Category3ID', primary_key=True)  # Field name made lowercase.
    category3name = models.CharField(db_column='Category3Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_category3'


class TblcustomerClass(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    class_name = models.CharField(db_column='Class_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_class'


class TblcustomerContact(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(TblcustomerAddress, models.DO_NOTHING, db_column='AddressID', to_field='addressid', blank=True, null=True)  # Field name made lowercase.
    contacttype = models.ForeignKey(TblbusContactRef, models.DO_NOTHING, db_column='ContactType_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_contact'


class TblcustomerMemo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    userid = models.ForeignKey('TblgenUsers', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    memotext = models.TextField(db_column='MemoText', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_memo'


class TblcustomerNotes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    noteid = models.AutoField(db_column='NoteID', primary_key=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('TblgenUsers', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    note_date = models.DateTimeField(db_column='Note_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_notes'


class TblcustomerSalesTrans(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    transactionno = models.IntegerField(db_column='TransactionNo', primary_key=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    tranreference = models.CharField(db_column='Tranreference', max_length=15, blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='Trantype', max_length=10, blank=True, null=True)  # Field name made lowercase.
    custref = models.CharField(db_column='CustRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trandate = models.DateTimeField(db_column='Trandate', blank=True, null=True)  # Field name made lowercase.
    goodscash = models.DecimalField(db_column='Goodscash', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatdiscount = models.DecimalField(db_column='Vatdiscount', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    osbal = models.DecimalField(db_column='Osbal', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountdays = models.IntegerField(db_column='Discountdays', blank=True, null=True)  # Field name made lowercase.
    batchno = models.IntegerField(db_column='Batchno', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currtotal = models.DecimalField(db_column='CurrTotal', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    paymenttermsid = models.ForeignKey(TblbusPaymentterms, models.DO_NOTHING, db_column='PaymentTermsID', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    query = models.BooleanField(db_column='Query',default=False)  # Field name made lowercase. This field type is a guess.
    qnote = models.TextField(db_column='QNote', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_sales_trans'


class TblcustomerServicePeple(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    csgroupid = models.ForeignKey(TblbusServicePeople, models.DO_NOTHING, db_column='CSGroupID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_service_peple'


class TblcustomerSettings(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.CharField(db_column='SettingID', primary_key=True, max_length=20)  # Field name made lowercase.
    settingname1 = models.CharField(db_column='SettingName1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=30, blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lookup_text = models.CharField(db_column='Lookup_Text', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_settings'


class TblcustomerSetvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    settingid = models.ForeignKey(TblcustomerSettings, models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_setvalues'


class TblcustomerTurnover(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    turnover = models.DecimalField(db_column='Turnover', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblcustomer_turnover'


class Tble4Kstrvalues(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    module = models.CharField(db_column='Module', primary_key=True, max_length=3)  # Field name made lowercase. The composite primary key (Module, Type, ValueIndex) found, that is not supported. The first column is selected.
    modulename = models.CharField(db_column='ModuleName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    valueindex = models.IntegerField(db_column='ValueIndex')  # Field name made lowercase.
    valuetext = models.CharField(db_column='ValueText', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tble4kstrvalues'
        unique_together = (('module', 'type', 'valueindex'),)


class TblgenAutonumbers(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    table_name = models.CharField(db_column='TableName', max_length=75)  # Field name made lowercase.
    field_name = models.CharField(db_column='FieldName', max_length=50)  # Field name made lowercase.
    autonumber = models.IntegerField(db_column='AutoNumber', blank=True, null=True)  # Field name made lowercase.
    locked = models.CharField(db_column='Locked', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datelocked = models.DateTimeField(db_column='DateLocked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblgen_autonumbers'


class TblgenParameters(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    paramid = models.CharField(db_column='ParamID', primary_key=True, max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    input_mask = models.CharField(db_column='Input_Mask', max_length=15, blank=True, null=True)  # Field name made lowercase.
    moduleid = models.CharField(db_column='ModuleID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblgen_parameters'


class TblgenUsers(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accessid = models.IntegerField(db_column='AccessID', blank=True, null=True)  # Field name made lowercase.
    forename = models.CharField(db_column='Forename', max_length=50, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telephone1 = models.CharField(db_column='Telephone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telephone2 = models.CharField(db_column='Telephone2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_logon = models.DateTimeField(db_column='Last_Logon', blank=True, null=True)  # Field name made lowercase.
    loggedon = models.BooleanField(db_column='LoggedOn',default=False)  # Field name made lowercase. This field type is a guess.
    locked = models.BooleanField(db_column='Locked',default=False)  # Field name made lowercase. This field type is a guess.
    canbechanged = models.BooleanField(db_column='CanBeChanged',default=False)  # Field name made lowercase. This field type is a guess.
    canbedeleted = models.BooleanField(db_column='CanBeDeleted',default=False)  # Field name made lowercase. This field type is a guess.
    ip_address = models.CharField(db_column='IP_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    passwordpayment = models.CharField(db_column='PasswordPayment', max_length=20, blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.CharField(db_column='WarehouseID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblgen_users'
        
        
class TblgenQrcodeFields(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblgen_qrcode_fields'