def strip_jsonp_to_json(jsonp):
    if isinstance(jsonp, str):
        l_index = jsonp.index('(') + 1
        r_index = jsonp.rindex(')')
        return jsonp[l_index:r_index]
    return jsonp  # Return as is if it's already a JSON string