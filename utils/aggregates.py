from django.db.models import Aggregate, When, Case


class Abs(Aggregate):
    '''
    ORM 聚合Aggregate 绝对值实现
    '''
    function = 'ABS'
    name = 'Abs'


class fnMonthNum(Aggregate):
    '''
    ORM 聚合Aggregate 绝对值实现
    '''
    function = 'dbo.fnMonthNum'
    name = 'dbo.fnMonthNum'
    template = '%(function)s(%(expressions)s,GETDATE())'

    def as_sql(self, compiler, connection, **extra_context):
        print('self.filter')
        if self.filter:
            if connection.features.supports_aggregate_filter_clause:
                filter_sql, filter_params = self.filter.as_sql(compiler, connection)
                template = self.filter_template % extra_context.get('template', self.template)
                sql, params = super().as_sql(compiler, connection, template=template, filter=filter_sql)
                return sql, params + filter_params
            else:
                print('self.filter')
                copy = self.copy()
                copy.filter = None
                source_expressions = copy.get_source_expressions()
                condition = When(self.filter, then=source_expressions[0])
                copy.set_source_expressions([Case(condition)] + source_expressions[1:])
                return super(Aggregate, copy).as_sql(compiler, connection, **extra_context)

        connection.ops.check_expression_support(self)
        sql_parts = []
        params = []
        for arg in self.source_expressions:
            arg_sql, arg_params = compiler.compile(arg)
            sql_parts.append(arg_sql)
            params.extend(arg_params)
        data = {**self.extra, **extra_context}
        # Use the first supplied value in this order: the parameter to this
        # method, a value supplied in __init__()'s **extra (the value in
        # `data`), or the value defined on the class.
        if self.function is not None:
            data['function'] = self.function
        else:
            data.setdefault('function', self.function)
        template = self.template or data.get('template', self.template)

        arg_joiner = self.arg_joiner or data.get('arg_joiner', self.arg_joiner)

        data['expressions'] = data['field'] = arg_joiner.join(sql_parts)
        print('template', template % data)
        return template % data, params

        # return super().as_sql(compiler, connection, **extra_context)

    # dbo.fnMonthNum(
    #     BirthDate,
    #     GETDATE()
    # )
