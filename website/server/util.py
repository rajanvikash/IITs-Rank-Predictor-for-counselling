import json
import pickle

import numpy as np

__data_columns = None
__model = None
__pool = None
__degree_name = None
__category = None
__program_duration = None
__instituteName = None
__department_name = None


def get_predictedCrank(year , pool , program_duration ,degree ,category ,institute_name, department_name ):
    try:
        loc_index_pool = __data_columns.index(pool.lower())
    except:
        loc_index_pool = -1

    try:
        loc_index_program_duration = __data_columns.index(program_duration.lower())
    except:
        loc_index_program_duration = -1

    try:
        loc_index_degree = __data_columns.index(degree.lower())
    except:
        loc_index_degree =-1


    try:
        loc_index_category = __data_columns.index(category.lower())
    except:
        loc_index_category = -1


    try:
        loc_index_institute_name = __data_columns.index(institute_name.lower())
    except:
        loc_index_institute_name = -1

    try:
        loc_index_department_name = __data_columns.index(department_name.lower())
    except:
        loc_index_department_name = -1




    x = np.zeros(len(__data_columns))
    x[0] = year

    if loc_index_pool >= 0:
        x[loc_index_pool] = 1

    if loc_index_program_duration >= 0:
        x[loc_index_program_duration] = 1

    if loc_index_degree >= 0:
        x[loc_index_degree] = 1

    if loc_index_category >= 0:
        x[loc_index_category] = 1

    if loc_index_institute_name >= 0:
        x[loc_index_institute_name] = 1

    if loc_index_department_name >= 0:
        x[loc_index_department_name] = 1


    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __model
    global __pool
    global __degree_name
    global __category
    global __program_duration
    global __instituteName
    global __department_name

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __pool = __data_columns[1:3]
        __program_duration = __data_columns[3:5]
        __degree_name = __data_columns[5:7]
        __category = __data_columns[7:16]
        __instituteName = __data_columns[16:26]
        __department_name = __data_columns[26:]
    if __model == None:
        with open("./artifacts/iit_closingrank_predictor", 'rb') as f:
            __model = pickle.load(f)


    print('loading of saved artifacts...done')


def get_pool():
    return __pool

def get_program_duration():
    return __program_duration

def get_degree_name():
    return __degree_name


def get_category():
    return __category

def get_instituteName():
    return __instituteName


def get_department_name():
    return __department_name

def get_data_columns():
    return __data_columns


load_saved_artifacts()


if __name__ == '__main__':

    # load_saved_artifacts()
    print((__data_columns))
    # print(get_predictedCrank(2018 , 'Gender-Neutral' , '4 Years', 'B.Tech', 'GEN' , 'IIT-Kanpur' ,'Aerospace Engineering' ))
    print(get_pool())
    # print(get_program_duration())
    # print(get_degree_name())
    # print(get_category())
    # print(get_instituteName())
    # print(get_department_name())
