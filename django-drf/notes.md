## API - Application programming interface 

- two way communication between frontend and backend.

CLIENT <-> API <->  BACKEND

## REST API - representational stateful API 

- doesn't store any info about the client 

## Endpoints - 
1. API endpoint : users can use to return some data to frontend. 

2. Web application endpoint : users can directly sccess from web browser.

# Serialization - translation of data one format to another

- model data to JSON or XML or any other type 

### Function based Views 
### Class based views 

### Mixins - 
- reusable code , classes that provide specific functionalities.
- ListModelMixin : return list of objects 
- CreateModelMixin : 
- DestroyModelMixin : 
- UpdateModelMixin :
- RetriveModelMixin : 

### Generics - 


### ViewSets - 
- viewsets.ViewSet
- viewsets.ModelViewSet

## Nested serializers 

### Pagination - 
- break down a long list of data into chunks and display /send that

- PageNumberPagination : takes a page size 
- LimitOffsetPagination : how many items 

