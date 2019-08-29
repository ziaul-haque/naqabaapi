

from Model import db_con

__all__ = [
    "made_raw_sql_query",
    "made_database_stored_procedure_query"
]


def filter_dict_fields(my_dict, fields=None, trim_fields=None):
    fields = list(fields or [])
    trim_fields = list(trim_fields or [])

    if not trim_fields and fields:
        trim_fields = list(set(my_dict.keys()).difference(set(fields)))

    for field in trim_fields:
        my_dict.pop(field)

    return my_dict


def made_raw_sql_query(raw_sql):
    response = []
    with db_con.cursor() as cursor:
        result = cursor.execute(raw_sql)
        columns = [column[0] for column in cursor.description]
        for row in result:
            response.append(dict(zip(columns, row)))

    return response


def convert_immutable_dict_to_dict(immutable_dict):
    mutable_dict = {}
    for key, value in immutable_dict.items():
        if value == "" or value == "None":
            mutable_dict[key] = None
        else:
            mutable_dict[key] = value
    return mutable_dict


def args_to_string(args):
    result_str = ""
    idx = 0
    if len(args) > 0:
        kwargs = convert_immutable_dict_to_dict(args)
        for key, value in kwargs.items():
            if key.find('id') < 1:
                result_str += str('@' + key + '=') + "'%s'" % value
            else:
                result_str += str('@' + key + '=') + value
            if idx + 1 != len(args):
                result_str += ", "
            idx = idx + 1
    return result_str


def made_database_stored_procedure_query(stored_procedure_name, args,
                                         fields=None):
    try:
        query = "EXEC {sp_name} {sp_args}".format(
            sp_name=stored_procedure_name,
            sp_args=args_to_string(args)
        )
        result = made_raw_sql_query(query)
    except Exception as e:
        raise Exception("Error while calling stored procedure, message: " + str(e))

    # filter dict fields
    filtered_result = [filter_dict_fields(row, fields=fields) for row in
                       result]
    return filtered_result
