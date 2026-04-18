from fastapi import FastAPI
api = FastAPI()
@api.get('/')
def index():
    return {'message':'aryan saxena can master any thing'}
@api.get('about')
def about():
    return {'message ':'you might be gay'}
@api.get('favourite')
def favoutite():
    return {'chamarnigga'}
