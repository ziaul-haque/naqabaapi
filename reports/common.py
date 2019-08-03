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
    cursor = db_con.cursor()
    result = cursor.execute(raw_sql)

    columns = [column[0] for column in cursor.description]

    response = []
    for row in result:
        response.append(dict(zip(columns, row)))

    cursor.close()
    return response


def args_to_string(args):
    param_str = "'%s'"
    param_number = "%s"
    param_null = "NULL"

    args = list(args)
    result_str = ""
    for idx, arg in enumerate(args):
        if arg is None:
            result_str += param_null
        elif isinstance(arg, (str, 'utf-8')):
            result_str += param_str % str(arg)
        else:
            result_str += param_number % str(arg)

        if idx + 1 != len(args):
            result_str += ", "
    return result_str


def made_database_stored_procedure_query(stored_procedure_name, args,
                                         fields=None):
    try:
        query = "CALL {sp_name}({sp_args})".format(
            sp_name=stored_procedure_name,
            sp_args=args_to_string(args)
        )
        result = made_raw_sql_query(query)
    except Exception as e:
        raise Exception("Error while calling stored procedure")

    # filter dict fields
    filtered_result = [filter_dict_fields(row, fields=fields) for row in
                       result]
    return filtered_result
