import graphene
from Product import product_schema,product_query
from Customer import customer_schema,customer_query
from Supplier import supplier_schema,supplier_query


class Query(product_query.Query,customer_query.CustomerQuery,supplier_query.SupplierQuery, graphene.ObjectType):
    pass

class Mutation(product_schema.Mutation,customer_schema.CustomerMutation,supplier_schema.SupplierMutation, graphene.ObjectType):
    # Combine the mutations from different apps
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
product_schema = graphene.Schema(query=product_query.Query,mutation=product_schema.Mutation)
customer_schema = graphene.Schema(query=customer_query.CustomerQuery,mutation=customer_schema.CustomerMutation)
supplier_schema = graphene.Schema(query=supplier_query.SupplierQuery,mutation=supplier_schema.SupplierMutation)