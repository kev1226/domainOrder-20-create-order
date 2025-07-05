from ariadne import QueryType, MutationType, make_executable_schema
from app.graphql.resolver import resolve_create_order

type_defs = """
    type OrderResponse {
        id: ID!
        status: String!
        message: String!
    }

    type Mutation {
        createOrder: OrderResponse!
    }

    type Query {
        _: Boolean
    }
"""


query = QueryType()
mutation = MutationType()

mutation.set_field("createOrder", resolve_create_order)

schema = make_executable_schema(type_defs, [query, mutation])
