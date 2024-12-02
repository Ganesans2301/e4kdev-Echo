# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    reconciled = models.TextField(db_column='Reconciled')  # Field name made lowercase. This field type is a guess.
    cbno = models.IntegerField(db_column='CBNo', blank=True, null=True)  # Field name made lowercase.
    bankcode = models.CharField(db_column='BankCode', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblacc_cashbook'


class TblaccNominal(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    nomcode = models.CharField(db_column='NomCode', primary_key=True, max_length=12)  # Field name made lowercase.
    nomdescription = models.CharField(db_column='NomDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomdc = models.CharField(db_column='NomDC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nompl = models.IntegerField(db_column='NomPL', blank=True, null=True)  # Field name made lowercase.
    nombs = models.IntegerField(db_column='NomBS', blank=True, null=True)  # Field name made lowercase.
    live = models.IntegerField(db_column='Live')  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'tblacc_nominal_tran'


class TblaccVatcodes(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    vatcode = models.IntegerField(db_column='VATCode', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sagecode = models.CharField(db_column='SageCode', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblacc_vatcodes'


class TblbusAddresstypeRef(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    actual_typeid = models.IntegerField(db_column='Actual_TypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_addresstype_ref'


class TblbusAddresstypes(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    addresstypeid = models.IntegerField(db_column='AddressTypeID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actual_typeid = models.ForeignKey(TblbusAddresstypeRef, models.DO_NOTHING, db_column='Actual_TypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_addresstypes'


class TblbusContactRef(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    contacttype_id = models.IntegerField(db_column='ContactType_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_contact_ref'


class TblbusCountries(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', primary_key=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('TblbusCountryMembers', models.DO_NOTHING, db_column='Member', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_countries'


class TblbusCountryMembers(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_country_members'


class TblbusCurrencies(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    currency_code = models.IntegerField(db_column='Currency_Code', primary_key=True)  # Field name made lowercase.
    currency_name = models.CharField(db_column='Currency_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    currency_symbol = models.CharField(db_column='Currency_Symbol', max_length=4, blank=True, null=True)  # Field name made lowercase.
    currency_exchange_rate = models.DecimalField(db_column='Currency_Exchange_Rate', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isocode = models.CharField(db_column='ISOCode', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_currencies'


class TblbusGroups(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_groups'


class TblbusPaymentterms(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    paymenttermsid = models.IntegerField(db_column='PaymentTermsID', primary_key=True)  # Field name made lowercase.
    typeid = models.ForeignKey('TblbusPaymenttermsRef', models.DO_NOTHING, db_column='TypeID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    days = models.CharField(db_column='Days', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_paymentterms'


class TblbusPaymenttermsRef(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    term_typeid = models.IntegerField(db_column='Term_TypeID', primary_key=True)  # Field name made lowercase.
    term_type_name = models.CharField(db_column='Term_Type_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    term_type_formula = models.CharField(db_column='Term_Type_Formula', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_paymentterms_ref'


class TblbusSalesPeople(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    repid = models.IntegerField(db_column='RepID', primary_key=True)  # Field name made lowercase.
    repkey = models.CharField(db_column='RepKey', max_length=10, blank=True, null=True)  # Field name made lowercase.
    forename = models.CharField(db_column='Forename', max_length=50, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    live = models.IntegerField(db_column='Live')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_sales_people'


class TblbusServicePeople(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    csgroupid = models.IntegerField(db_column='CSGroupID', primary_key=True)  # Field name made lowercase.
    csname = models.CharField(db_column='CSName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbus_service_people'


class TblcmpDefaults(models.Model):
    companyid = models.ForeignKey('Tblcompany', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    paramid = models.CharField(db_column='ParamID', primary_key=True, max_length=20)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=150, blank=True, null=True)  # Field name made lowercase.
    paramgroup = models.CharField(db_column='ParamGroup', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'tblcompany'


class Tblcustomer(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.CharField(db_column='BusinessID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    islive = models.IntegerField(db_column='IsLive')  # Field name made lowercase.
    category1id = models.ForeignKey('TblcustomerCategory1', models.DO_NOTHING, db_column='Category1ID', blank=True, null=True)  # Field name made lowercase.
    category2id = models.ForeignKey('TblcustomerCategory2', models.DO_NOTHING, db_column='Category2ID', blank=True, null=True)  # Field name made lowercase.
    category3id = models.ForeignKey('TblcustomerCategory3', models.DO_NOTHING, db_column='Category3ID', blank=True, null=True)  # Field name made lowercase.
    classid = models.ForeignKey('TblcustomerClass', models.DO_NOTHING, db_column='ClassID', blank=True, null=True)  # Field name made lowercase.
    groupid = models.ForeignKey(TblbusGroups, models.DO_NOTHING, db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    default_nominal = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='Default_Nominal', blank=True, null=True)  # Field name made lowercase.
    isextract = models.IntegerField(db_column='IsExtract')  # Field name made lowercase.
    isstop = models.IntegerField(db_column='IsStop', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'tblcustomer_account'


class TblcustomerAddress(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.OneToOneField(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', primary_key=True)  # Field name made lowercase. The composite primary key (BusinessID, AddressID) found, that is not supported. The first column is selected.
    addressid = models.IntegerField(db_column='AddressID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=75, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=75, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=75, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=75, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=75, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryCode', blank=True, null=True)  # Field name made lowercase.
    addresstypeid = models.ForeignKey(TblbusAddresstypes, models.DO_NOTHING, db_column='AddressTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_address'
        unique_together = (('businessid', 'addressid'),)


class TblcustomerAddressMappings(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    invaddressid = models.ForeignKey(TblcustomerAddress, models.DO_NOTHING, db_column='InvAddressID', to_field='AddressID')  # Field name made lowercase.
    deladdressid = models.ForeignKey(TblcustomerAddress, models.DO_NOTHING, db_column='DelAddressID', to_field='AddressID', related_name='tblcustomeraddressmappings_deladdressid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_address_mappings'


class TblcustomerBalance(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.OneToOneField(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', primary_key=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    date_used = models.DateTimeField(db_column='Date_Used', blank=True, null=True)  # Field name made lowercase.
    foreignbalance = models.DecimalField(db_column='ForeignBalance', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_balance'


class TblcustomerCategory1(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category1id = models.IntegerField(db_column='Category1ID', primary_key=True)  # Field name made lowercase.
    category1name = models.CharField(db_column='Category1Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_category1'


class TblcustomerCategory2(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category2id = models.IntegerField(db_column='Category2ID', primary_key=True)  # Field name made lowercase.
    category2name = models.CharField(db_column='Category2Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_category2'


class TblcustomerCategory3(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category3id = models.IntegerField(db_column='Category3ID', primary_key=True)  # Field name made lowercase.
    category3name = models.CharField(db_column='Category3Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_category3'


class TblcustomerClass(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    class_name = models.CharField(db_column='Class_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_class'


class TblcustomerContact(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(TblcustomerAddress, models.DO_NOTHING, db_column='AddressID', to_field='AddressID', blank=True, null=True)  # Field name made lowercase.
    contacttype = models.ForeignKey(TblbusContactRef, models.DO_NOTHING, db_column='ContactType_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_contact'


class TblcustomerMemo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    userid = models.ForeignKey('TblgenUsers', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    memotext = models.TextField(db_column='MemoText', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_memo'


class TblcustomerNotes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    noteid = models.AutoField(db_column='NoteID', primary_key=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('TblgenUsers', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    note_date = models.DateTimeField(db_column='Note_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
    query = models.IntegerField(db_column='Query')  # Field name made lowercase.
    qnote = models.TextField(db_column='QNote', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_sales_trans'


class TblcustomerServicePeple(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    csgroupid = models.ForeignKey(TblbusServicePeople, models.DO_NOTHING, db_column='CSGroupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_service_peple'


class TblcustomerSettings(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.CharField(db_column='SettingID', primary_key=True, max_length=20)  # Field name made lowercase.
    settingname1 = models.CharField(db_column='SettingName1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey('TblgenCategories', models.DO_NOTHING, db_column='Category', to_field='CategoryID', blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lookup_text = models.CharField(db_column='Lookup_Text', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_settings'


class TblcustomerSetvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    settingid = models.ForeignKey(TblcustomerSettings, models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_setvalues'


class TblcustomerTurnover(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    turnover = models.DecimalField(db_column='Turnover', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer_turnover'


class Tble4Kstrvalues(models.Model):
    companyid = models.OneToOneField(Tblcompany, models.DO_NOTHING, db_column='CompanyID', primary_key=True)  # Field name made lowercase. The composite primary key (CompanyID, Module, Type, ValueIndex) found, that is not supported. The first column is selected.
    module = models.CharField(db_column='Module', max_length=3)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    valueindex = models.IntegerField(db_column='ValueIndex')  # Field name made lowercase.
    valuetext = models.CharField(db_column='ValueText', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tble4kstrvalues'
        unique_together = (('companyid', 'module', 'type', 'valueindex'),)


class TblgenAutonumbers(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=75)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=50)  # Field name made lowercase.
    autonumber = models.IntegerField(db_column='AutoNumber', blank=True, null=True)  # Field name made lowercase.
    locked = models.CharField(db_column='Locked', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datelocked = models.DateTimeField(db_column='DateLocked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgen_autonumbers'


class TblgenCategories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    moduleid = models.CharField(db_column='ModuleID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgen_categories'


class TblgenMaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    master_typeid = models.ForeignKey('TblgenMastertype', models.DO_NOTHING, db_column='Master_TypeID', blank=True, null=True)  # Field name made lowercase.
    master_description = models.CharField(db_column='Master_Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgen_master'


class TblgenMastertype(models.Model):
    typeid = models.IntegerField(db_column='TypeID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    typedescription = models.CharField(db_column='TypeDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgen_mastertype'


class TblgenParameters(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    paramid = models.CharField(db_column='ParamID', primary_key=True, max_length=20)  # Field name made lowercase.
    category = models.ForeignKey(TblgenCategories, models.DO_NOTHING, db_column='Category', to_field='CategoryID', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    input_mask = models.CharField(db_column='Input_Mask', max_length=15, blank=True, null=True)  # Field name made lowercase.
    moduleid = models.CharField(db_column='ModuleID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
    loggedon = models.IntegerField(db_column='LoggedOn')  # Field name made lowercase.
    locked = models.IntegerField(db_column='Locked')  # Field name made lowercase.
    canbechanged = models.IntegerField(db_column='CanBeChanged')  # Field name made lowercase.
    canbedeleted = models.IntegerField(db_column='CanBeDeleted')  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    passwordpayment = models.CharField(db_column='PasswordPayment', max_length=20, blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.CharField(db_column='WarehouseID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgen_users'


class TblproductCategory1(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category1id = models.IntegerField(db_column='Category1ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_category1'


class TblproductCategory2(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category2id = models.IntegerField(db_column='Category2ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_category2'


class TblproductCategory3(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category3id = models.IntegerField(db_column='Category3ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_category3'


class TblproductClass(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_class'


class TblproductColours(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    colourid = models.CharField(db_column='ColourID', primary_key=True, max_length=15)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colourcode = models.CharField(db_column='ColourCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_colours'


class TblproductCommoditycodes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    commodity_code = models.CharField(db_column='Commodity_Code', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_commoditycodes'


class TblproductCustomerClass(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    prodclassid = models.ForeignKey(TblproductClass, models.DO_NOTHING, db_column='ProdClassID')  # Field name made lowercase.
    cusclassid = models.ForeignKey(TblcustomerClass, models.DO_NOTHING, db_column='CusClassID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_customer_class'


class TblproductFits(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    fitid = models.CharField(db_column='FitID', primary_key=True, max_length=5)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_fits'


class TblproductGender(models.Model):
    companyid = models.CharField(db_column='CompanyID', max_length=3)  # Field name made lowercase.
    genid = models.CharField(db_column='GenID', primary_key=True, max_length=5)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_gender'


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
        managed = False
        db_table = 'tblproduct_intrastat'


class TblproductMemo(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('TblproductProducts', models.DO_NOTHING, db_column='ProductID', primary_key=True)  # Field name made lowercase.
    memotext = models.TextField(db_column='MemoText', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(TblgenUsers, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_memo'


class TblproductObsoleteTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    obsoleteid = models.IntegerField(db_column='ObsoleteID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isallow_sale = models.TextField(db_column='IsAllow_Sale')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblproduct_obsolete_types'


class TblproductParametersCustomerSetvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.ForeignKey('TblproductParametersSettings', models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_parameters_customer_setvalues'


class TblproductParametersSettings(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.CharField(db_column='SettingID', primary_key=True, max_length=20)  # Field name made lowercase.
    settingname = models.CharField(db_column='SettingName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(TblgenCategories, models.DO_NOTHING, db_column='Category', to_field='CategoryID', blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lookup_text = models.CharField(db_column='Lookup_Text', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iscustomer = models.IntegerField(db_column='IsCustomer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_parameters_settings'


class TblproductParametertsSetvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.ForeignKey('XtblproductParametersSettings', models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_parameterts_setvalues'


class TblproductPriceTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    priceid = models.IntegerField(db_column='PriceID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price_type = models.IntegerField(db_column='Price_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'tblproduct_product_bom'
        unique_together = (('companyid', 'styleid', 'colourid', 'styleid_bom', 'colourid_bom'),)


class TblproductProductCostStandardMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdcostmatix = models.JSONField(db_column='StdCostMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_cost_standard_matrix'


class TblproductProductCostSupplierMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.ForeignKey('Tblsupplier', models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    supcostmatix = models.JSONField(db_column='SupCostMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_cost_supplier_matrix'


class TblproductProductFreetext(models.Model):
    companyid = models.CharField(db_column='CompanyId', primary_key=True, max_length=50)  # Field name made lowercase. The composite primary key (CompanyId, WareHouseId, ProductID, FreeTextType) found, that is not supported. The first column is selected.
    warehouseid = models.CharField(db_column='WareHouseId', max_length=10)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=25)  # Field name made lowercase.
    freetexttype = models.CharField(db_column='FreeTextType', max_length=50)  # Field name made lowercase.
    freetext = models.TextField(db_column='FreeText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_freetext'
        unique_together = (('companyid', 'warehouseid', 'productid', 'freetexttype'),)


class TblproductProductGallery(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    productimage = models.CharField(db_column='ProductImage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is360 = models.IntegerField(db_column='Is360', blank=True, null=True)  # Field name made lowercase.
    noframes = models.IntegerField(db_column='NoFrames', blank=True, null=True)  # Field name made lowercase.
    nofootages = models.IntegerField(db_column='NoFootages', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_gallery'


class TblproductProductObsoleteMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    obslmatix = models.JSONField(db_column='ObslMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_obsolete_matrix'


class TblproductProductPriceCustomerMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    cuspricematix = models.JSONField(db_column='CusPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_price_customer_matrix'


class TblproductProductPriceStandardDateMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdpricematix = models.JSONField(db_column='StdPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_price_standard_date_matrix'


class TblproductProductPriceStandardMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdpricematix = models.JSONField(db_column='StdPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_price_standard_matrix'


class TblproductProductPriceStandardQtyMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stdpricematix = models.JSONField(db_column='StdPriceMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_price_standard_qty_matrix'


class TblproductProductProperties(models.Model):
    product_propid = models.AutoField(db_column='Product_PropId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    propertyid = models.ForeignKey('TblproductPropertyTypes', models.DO_NOTHING, db_column='PropertyId', blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_properties'


class TblproductProductPropertyLevel(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('TblproductProducts', models.DO_NOTHING, db_column='ProductID', primary_key=True)  # Field name made lowercase.
    stockmatrix = models.JSONField(db_column='StockMatrix', blank=True, null=True)  # Field name made lowercase.
    pricematrix = models.JSONField(db_column='PriceMatrix', blank=True, null=True)  # Field name made lowercase.
    stklvlmatrix = models.JSONField(db_column='StkLvlMatrix', blank=True, null=True)  # Field name made lowercase.
    stklocmatrix = models.JSONField(db_column='StkLocMatrix', blank=True, null=True)  # Field name made lowercase.
    stktypematrix = models.JSONField(db_column='StkTypeMatrix', blank=True, null=True)  # Field name made lowercase.
    obslmatrix = models.JSONField(db_column='ObslMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_property_level'


class TblproductProductPropertyLevelColmatrix(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('TblproductProducts', models.DO_NOTHING, db_column='ProductID', primary_key=True)  # Field name made lowercase.
    stockcolmatrix = models.JSONField(db_column='StockColMatrix', blank=True, null=True)  # Field name made lowercase.
    pricecolmatrix = models.JSONField(db_column='PriceColMatrix', blank=True, null=True)  # Field name made lowercase.
    stklvlcolmatrix = models.JSONField(db_column='StkLvlColMatrix', blank=True, null=True)  # Field name made lowercase.
    stkloccolmatrix = models.JSONField(db_column='StkLocColMatrix', blank=True, null=True)  # Field name made lowercase.
    stktypecolmatrix = models.JSONField(db_column='StkTypeColMatrix', blank=True, null=True)  # Field name made lowercase.
    obslcolmatrix = models.JSONField(db_column='ObslColMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_property_level_colmatrix'


class TblproductProductPropertyMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    propertymatix = models.JSONField(db_column='PropertyMatix', blank=True, null=True)  # Field name made lowercase.
    propertycolmatrix = models.JSONField(db_column='PropertyColMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_property_matrix'


class TblproductProductPropertyValues(models.Model):
    product_prop_value_id = models.AutoField(db_column='Product_Prop_Value_Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    product_propid = models.ForeignKey(TblproductProductProperties, models.DO_NOTHING, db_column='Product_PropId', blank=True, null=True)  # Field name made lowercase.
    product_prop_value = models.CharField(db_column='Product_Prop_Value', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_property_values'


class TblproductProductReps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    repid = models.ForeignKey(TblbusSalesPeople, models.DO_NOTHING, db_column='RepID')  # Field name made lowercase.
    seqno = models.SmallIntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_reps'


class TblproductProductStockinglevelMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stocklevelmatix = models.JSONField(db_column='StockLevelMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_stockinglevel_matrix'


class TblproductProductStockingtypeMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    stocktypematix = models.JSONField(db_column='StockTypeMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_stockingtype_matrix'


class TblproductProductSupplierLevel(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Tblsupplier', models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    suppliermatrix = models.JSONField(db_column='SupplierMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_supplier_level'


class TblproductProductSupplierLevelColmatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Tblsupplier', models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    suppliercolmatrix = models.JSONField(db_column='SupplierColMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_supplier_level_colmatrix'


class TblproductProductSuppliersMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Tblsupplier', models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    suppliermatrix = models.JSONField(db_column='SupplierMatrix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_suppliers_matrix'


class TblproductProductSuppliersWeekdays(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    supplierid = models.ForeignKey('Tblsupplier', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    weekday = models.IntegerField(db_column='WeekDay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_suppliers_weekdays'


class TblproductProductVatcodeMatrix(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('TblproductProducts', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    vatcodematix = models.JSONField(db_column='VatCodeMatix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_product_vatcode_matrix'


class TblproductProducts(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', primary_key=True, max_length=25)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category1id = models.ForeignKey(TblproductCategory1, models.DO_NOTHING, db_column='Category1ID', blank=True, null=True)  # Field name made lowercase.
    category2id = models.ForeignKey(TblproductCategory2, models.DO_NOTHING, db_column='Category2ID', blank=True, null=True)  # Field name made lowercase.
    category3id = models.ForeignKey(TblproductCategory3, models.DO_NOTHING, db_column='Category3ID', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    supplimentaryunits = models.CharField(db_column='SupplimentaryUnits', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nominal_code = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='Nominal_Code', blank=True, null=True)  # Field name made lowercase.
    commodity_code = models.ForeignKey(TblproductCommoditycodes, models.DO_NOTHING, db_column='Commodity_Code', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    classid = models.ForeignKey(TblproductClass, models.DO_NOTHING, db_column='ClassID', blank=True, null=True)  # Field name made lowercase.
    obsolete_class = models.ForeignKey(TblproductObsoleteTypes, models.DO_NOTHING, db_column='Obsolete_Class', blank=True, null=True)  # Field name made lowercase.
    live = models.TextField(db_column='Live')  # Field name made lowercase. This field type is a guess.
    styleimage = models.CharField(db_column='StyleImage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    batchcontrol = models.TextField(db_column='BatchControl')  # Field name made lowercase. This field type is a guess.
    stockinguom = models.ForeignKey('TblproductTypeofissue', models.DO_NOTHING, db_column='StockingUOM', blank=True, null=True)  # Field name made lowercase.
    issueuom = models.ForeignKey('TblproductUnitofissue', models.DO_NOTHING, db_column='IssueUOM', blank=True, null=True)  # Field name made lowercase.
    stockingtype = models.ForeignKey('TblproductStockingTypes', models.DO_NOTHING, db_column='StockingType', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_products'


class TblproductPropertyLevelTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    propertylvlid = models.IntegerField(db_column='PropertyLvlID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_property_level_types'


class TblproductPropertyTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    propertyid = models.IntegerField(db_column='PropertyID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isstatic = models.IntegerField(db_column='IsStatic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_property_types'


class TblproductPropertyTypesValues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    proptypeid = models.ForeignKey(TblproductPropertyTypes, models.DO_NOTHING, db_column='PropTypeID')  # Field name made lowercase.
    proptype_values = models.CharField(db_column='PropType_Values', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_property_types_values'


class TblproductSizeRangeValues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    rangeid = models.ForeignKey('TblproductSizeRanges', models.DO_NOTHING, db_column='RangeID')  # Field name made lowercase.
    size_number = models.IntegerField(db_column='Size_Number')  # Field name made lowercase.
    size_value = models.CharField(db_column='Size_Value', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_size_range_values'


class TblproductSizeRanges(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    rangeid = models.CharField(db_column='RangeID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_size_ranges'


class TblproductStockingTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    stockingtype = models.CharField(db_column='StockingType', primary_key=True, max_length=1)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_stocking_types'


class TblproductTypeofissue(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    issue_type = models.IntegerField(db_column='Issue_Type', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_typeofissue'


class TblproductUnitofissue(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    issue_units = models.IntegerField(db_column='Issue_Units', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_unitofissue'


class TblproductUnitofmeasure(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitID', primary_key=True)  # Field name made lowercase.
    unitshortcode = models.CharField(db_column='UnitShortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitdescription = models.CharField(db_column='UnitDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='Seqno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct_unitofmeasure'


class TblproductUnitofmeasureCustomer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblcustomer, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    unitid = models.ForeignKey(TblproductUnitofmeasure, models.DO_NOTHING, db_column='UnitID')  # Field name made lowercase.
    unitshortcode = models.CharField(db_column='UnitShortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'tblproduct_unitofmeasureconversion'


class Tblsupplier(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.CharField(db_column='BusinessID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    islive = models.IntegerField(db_column='IsLive')  # Field name made lowercase.
    category1id = models.ForeignKey('TblsupplierCategory1', models.DO_NOTHING, db_column='Category1ID', blank=True, null=True)  # Field name made lowercase.
    category2id = models.ForeignKey('TblsupplierCategory2', models.DO_NOTHING, db_column='Category2ID', blank=True, null=True)  # Field name made lowercase.
    category3id = models.ForeignKey('TblsupplierCategory3', models.DO_NOTHING, db_column='Category3ID', blank=True, null=True)  # Field name made lowercase.
    classid = models.ForeignKey('TblsupplierClass', models.DO_NOTHING, db_column='ClassID', blank=True, null=True)  # Field name made lowercase.
    default_nominal = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='Default_Nominal', blank=True, null=True)  # Field name made lowercase.
    isextract = models.IntegerField(db_column='IsExtract')  # Field name made lowercase.
    isstop = models.IntegerField(db_column='IsStop', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier'


class TblsupplierAccount(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.OneToOneField(Tblsupplier, models.DO_NOTHING, db_column='BusinessID', primary_key=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='Bank_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bank_account_name = models.CharField(db_column='Bank_Account_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bank_sort_code = models.CharField(db_column='Bank_Sort_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bank_account_num = models.CharField(db_column='Bank_Account_Num', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    credit_limit = models.DecimalField(db_column='Credit_Limit', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currency_code = models.ForeignKey(TblbusCurrencies, models.DO_NOTHING, db_column='Currency_Code', blank=True, null=True)  # Field name made lowercase.
    vatcode = models.ForeignKey(TblaccVatcodes, models.DO_NOTHING, db_column='VATCode', blank=True, null=True)  # Field name made lowercase.
    vatflag = models.CharField(db_column='VATFlag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vatno = models.CharField(db_column='VATNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_used = models.DateTimeField(db_column='Date_Used', blank=True, null=True)  # Field name made lowercase.
    date_opened = models.DateTimeField(db_column='Date_Opened', blank=True, null=True)  # Field name made lowercase.
    nominal_code = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='Nominal_Code', blank=True, null=True)  # Field name made lowercase.
    paymenttermsid = models.ForeignKey(TblbusPaymentterms, models.DO_NOTHING, db_column='PaymentTermsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_account'


class TblsupplierAddress(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    addressid = models.IntegerField(db_column='AddressID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=75, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=75, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=75, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=75, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=75, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryCode', blank=True, null=True)  # Field name made lowercase.
    addresstypeid = models.ForeignKey(TblbusAddresstypes, models.DO_NOTHING, db_column='AddressTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_address'


class TblsupplierBalance(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.OneToOneField(Tblsupplier, models.DO_NOTHING, db_column='BusinessID', primary_key=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    date_used = models.DateTimeField(db_column='Date_Used', blank=True, null=True)  # Field name made lowercase.
    foreignbalance = models.DecimalField(db_column='ForeignBalance', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_balance'


class TblsupplierCategory1(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category1id = models.IntegerField(db_column='Category1ID', primary_key=True)  # Field name made lowercase.
    category1name = models.CharField(db_column='Category1Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_category1'


class TblsupplierCategory2(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category2id = models.IntegerField(db_column='Category2ID', primary_key=True)  # Field name made lowercase.
    category2name = models.CharField(db_column='Category2Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_category2'


class TblsupplierCategory3(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category3id = models.IntegerField(db_column='Category3ID', primary_key=True)  # Field name made lowercase.
    category3name = models.CharField(db_column='Category3Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_category3'


class TblsupplierClass(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    class_name = models.CharField(db_column='Class_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_class'


class TblsupplierContact(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(TblsupplierAddress, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    contacttype = models.ForeignKey(TblbusContactRef, models.DO_NOTHING, db_column='ContactType_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_contact'


class TblsupplierMemo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    userid = models.ForeignKey(TblgenUsers, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    memotext = models.TextField(db_column='MemoText', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_memo'


class TblsupplierNotes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    noteid = models.AutoField(db_column='NoteID', primary_key=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(TblgenUsers, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    note_date = models.DateTimeField(db_column='Note_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_notes'


class TblsupplierSettings(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.CharField(db_column='SettingID', primary_key=True, max_length=20)  # Field name made lowercase.
    settingname1 = models.CharField(db_column='SettingName1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(TblgenCategories, models.DO_NOTHING, db_column='Category', to_field='CategoryID', blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lookup_text = models.CharField(db_column='Lookup_Text', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_settings'


class TblsupplierSetvalues(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    settingid = models.ForeignKey(TblsupplierSettings, models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_setvalues'


class TblsupplierTurnover(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    turnover = models.DecimalField(db_column='Turnover', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier_turnover'


class TblwhoWarehouses(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    warehouseid = models.CharField(db_column='WarehouseID', primary_key=True, max_length=10)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WarehouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationcontroled = models.IntegerField(db_column='LocationControled')  # Field name made lowercase.
    noofaisles = models.IntegerField(db_column='NoOfAisles', blank=True, null=True)  # Field name made lowercase.
    noofbays = models.IntegerField(db_column='NoOfBays', blank=True, null=True)  # Field name made lowercase.
    noofshelfs = models.IntegerField(db_column='NoOfShelfs', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    live = models.IntegerField(db_column='Live')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vatno = models.CharField(db_column='VATno', max_length=12, blank=True, null=True)  # Field name made lowercase.
    whtypeid = models.ForeignKey('TblwhoWarehousesTypes', models.DO_NOTHING, db_column='WHTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblwho_warehouses'


class TblwhoWarehousesTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    whtypeid = models.SmallIntegerField(db_column='WHTypeID', primary_key=True)  # Field name made lowercase.
    whtype = models.CharField(db_column='WHType', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblwho_warehouses_types'


class WebSecurityAppUsertoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_security_app_usertoken'


class XtblproductParametersSettings(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    settingid = models.CharField(db_column='SettingID', primary_key=True, max_length=20)  # Field name made lowercase.
    settingname = models.CharField(db_column='SettingName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    default = models.CharField(db_column='Default', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    lookup_table = models.CharField(db_column='Lookup_Table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lookup_text = models.CharField(db_column='Lookup_Text', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xtblproduct_parameters_settings'


class XxxxtblproductProductSuppliers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    warehouseid = models.ForeignKey(TblwhoWarehouses, models.DO_NOTHING, db_column='WarehouseID', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    productid = models.ForeignKey(TblproductProducts, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    supplierprod_code = models.CharField(db_column='SupplierProd_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_price = models.IntegerField(db_column='Supplier_price', blank=True, null=True)  # Field name made lowercase.
    supplierseq = models.SmallIntegerField(db_column='SupplierSeq', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=10)  # Field name made lowercase.
    leadtime = models.IntegerField(db_column='Leadtime', blank=True, null=True)  # Field name made lowercase.
    isbulkorder = models.IntegerField(db_column='IsBulkOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xxxxtblproduct_product_suppliers'


class XxxxtblproductProductSuppliersCopy(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyID', max_length=3)  # Field name made lowercase.
    warehouseid = models.CharField(db_column='WarehouseID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=25)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=25)  # Field name made lowercase.
    supplierprod_code = models.CharField(db_column='SupplierProd_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_price = models.IntegerField(db_column='Supplier_price', blank=True, null=True)  # Field name made lowercase.
    supplierseq = models.SmallIntegerField(db_column='SupplierSeq', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=10)  # Field name made lowercase.
    leadtime = models.IntegerField(db_column='Leadtime', blank=True, null=True)  # Field name made lowercase.
    isbulkorder = models.IntegerField(db_column='IsBulkOrder', blank=True, null=True)  # Field name made lowercase.
    dutycost = models.DecimalField(db_column='DutyCost', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xxxxtblproduct_product_suppliers_copy'
