from django.db import models
from Customer.models import (Tblcompany,TblbusCountries,TblaccNominal,TblbusCurrencies,TblaccVatcodes,
                               TblbusPaymentterms,TblbusAddresstypes,TblbusContactRef,TblgenUsers,TblgenAutonumbers,TblcustomerAddress
                               )



class Tblsupplier(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.CharField(db_column='BusinessID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TblbusCountries, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    islive = models.BooleanField(db_column='IsLive',default=True)  # Field name made lowercase. This field type is a guess.
    category1id = models.ForeignKey('TblsupplierCategory1', models.DO_NOTHING, db_column='Category1ID', blank=True, null=True)  # Field name made lowercase.
    category2id = models.ForeignKey('TblsupplierCategory2', models.DO_NOTHING, db_column='Category2ID', blank=True, null=True)  # Field name made lowercase.
    category3id = models.ForeignKey('TblsupplierCategory3', models.DO_NOTHING, db_column='Category3ID', blank=True, null=True)  # Field name made lowercase.
    classid = models.ForeignKey('TblsupplierClass', models.DO_NOTHING, db_column='ClassID', blank=True, null=True)  # Field name made lowercase.
    default_nominal = models.ForeignKey(TblaccNominal, models.DO_NOTHING, db_column='Default_Nominal', blank=True, null=True)  # Field name made lowercase.
    isextract = models.BooleanField(db_column='IsExtract',default=False)  # Field name made lowercase. This field type is a guess.
    isstop = models.BooleanField(db_column='IsStop', default=False,blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
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
        #managed = False
        db_table = 'tblsupplier_account'


class TblsupplierAddress(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    addressid = models.IntegerField(db_column='AddressID', primary_key=True)  # Field name made lowercase.
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
        #managed = False
        db_table = 'tblsupplier_category1'


class TblsupplierCategory2(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    category2id = models.IntegerField(db_column='Category2ID', primary_key=True)  # Field name made lowercase.
    category2name = models.CharField(db_column='Category2Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
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
        #managed = False
        db_table = 'tblsupplier_class'


class TblsupplierContact(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(TblsupplierAddress, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    contacttype = models.ForeignKey(TblbusContactRef, models.DO_NOTHING, db_column='ContactType_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblsupplier_contact'


class TblsupplierMemo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    userid = models.ForeignKey(TblgenUsers, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    memotext = models.TextField(db_column='MemoText', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblsupplier_memo'


class TblsupplierNotes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    noteid = models.AutoField(db_column='NoteID', primary_key=True)  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(TblgenUsers, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    note_date = models.DateTimeField(db_column='Note_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblsupplier_notes'


class TblsupplierSettings(models.Model):
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
        db_table = 'tblsupplier_settings'


class TblsupplierSetvalues(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    settingid = models.ForeignKey(TblsupplierSettings, models.DO_NOTHING, db_column='SettingID')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblsupplier_setvalues'


class TblsupplierTurnover(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    businessid = models.ForeignKey(Tblsupplier, models.DO_NOTHING, db_column='BusinessID')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    turnover = models.DecimalField(db_column='Turnover', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblsupplier_turnover'


class TblwhoWarehouses(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    warehouseid = models.CharField(db_column='WarehouseID', primary_key=True, max_length=10)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WarehouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationcontroled = models.BooleanField(db_column='LocationControled',default=False)  # Field name made lowercase. This field type is a guess.
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
    live = models.BooleanField(db_column='Live',default=False)  # Field name made lowercase. This field type is a guess.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vatno = models.CharField(db_column='VATno', max_length=12, blank=True, null=True)  # Field name made lowercase.
    whtypeid = models.ForeignKey('TblwhoWarehousesTypes', models.DO_NOTHING, db_column='WHTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblwho_warehouses'


class TblwhoWarehousesTypes(models.Model):
    companyid = models.ForeignKey(Tblcompany, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    whtypeid = models.SmallIntegerField(db_column='WHTypeID', primary_key=True)  # Field name made lowercase.
    whtype = models.CharField(db_column='WHType', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblwho_warehouses_types'



