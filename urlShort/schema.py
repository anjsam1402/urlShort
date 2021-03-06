import graphene

import urlShortener.schema


class Query(urlShortener.schema.Query, graphene.ObjectType):
    pass


class Mutation(urlShortener.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)