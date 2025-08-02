#rnd #web 
[[proposal_rudra]]

# PROJECT PROPOSAL 

# project integration google map api. 

need to setup the django project. 
google map api key is acquired
need to use that api key for accessing the locations of the places that are stored  the database. the database have stored the details about NSW rest areas.
the areas that are listed there needs to be mapped or accessed using google map api. 

a simple UI django project that list out the rest areas from the  database and link them with the location thorugh google map api such that the areas can be 
easily localized by the users when clicked on the  rest area name.



### errors encountered

(.restareas_env) PS C:\Users\rudra\rudra_md\sydney_rest_areas> python .\manage.py migrate
System check identified some issues:

WARNINGS:
?: (staticfiles.W004) The directory 'C:\Users\rudra\rudra_md\sydney_rest_areas\static' in the STATICFILES_DIRS setting does not exist.
Traceback (most recent call last):
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\base\base.py", line 279, in ensure_connection
    self.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\base\base.py", line 256, in connect
    self.connection = self.get_new_connection(conn_params)
                      ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\postgresql\base.py", line 332, in get_new_connection
    connection = self.Database.connect(**conn_params)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\psycopg2\__init__.py", line 135, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "sydneyrestareas" does not exist


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\rudra\rudra_md\sydney_rest_areas\manage.py", line 22, in <module>
    main()
    ~~~~^^
  File "C:\Users\rudra\rudra_md\sydney_rest_areas\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line
    utility.execute()
    ~~~~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\management\__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\management\base.py", line 416, in run_from_argv
    self.execute(*args, **cmd_options)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\management\base.py", line 460, in execute
    output = self.handle(*args, **options)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\management\base.py", line 107, in wrapper
    res = handle_func(*args, **kwargs)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\management\commands\migrate.py", line 114, in handle
    executor = MigrationExecutor(connection, self.migration_progress_callback)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\migrations\executor.py", line 18, in __init__
    self.loader = MigrationLoader(self.connection)
                  ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\migrations\loader.py", line 58, in __init__
    self.build_graph()
    ~~~~~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\migrations\loader.py", line 235, in build_graph
    self.applied_migrations = recorder.applied_migrations()
                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\migrations\recorder.py", line 89, in applied_migrations
    if self.has_table():
       ~~~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\migrations\recorder.py", line 63, in has_table
    with self.connection.cursor() as cursor:
         ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\base\base.py", line 320, in cursor
    return self._cursor()
           ~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\base\base.py", line 296, in _cursor
    self.ensure_connection()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\base\base.py", line 278, in ensure_connection
    with self.wrap_database_errors:
         ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\base\base.py", line 279, in ensure_connection
    self.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\base\base.py", line 256, in connect
    self.connection = self.get_new_connection(conn_params)
                      ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\postgresql\base.py", line 332, in get_new_connection
    connection = self.Database.connect(**conn_params)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\psycopg2\__init__.py", line 135, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
django.db.utils.OperationalError: connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "sydneyrestareas" does not exist

(.restareas_env) PS C:\Users\rudra\rudra_md\sydney_rest_areas> python .\manage.py migrate
System check identified some issues:

WARNINGS:
?: (staticfiles.W004) The directory 'C:\Users\rudra\rudra_md\sydney_rest_areas\static' in the STATICFILES_DIRS setting does not exist.
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(.restareas_env) PS C:\Users\rudra\rudra_md\sydney_rest_areas> python .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified some issues:

WARNINGS:
?: (staticfiles.W004) The directory 'C:\Users\rudra\rudra_md\sydney_rest_areas\static' in the STATICFILES_DIRS setting does not exist.

System check identified 1 issue (0 silenced).
July 31, 2025 - 17:42:20
Django version 5.2.4, using settings 'sydney_rest_areas.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[31/Jul/2025 17:42:24] "GET / HTTP/1.1" 200 1402
Not Found: /favicon.ico
[31/Jul/2025 17:42:25] "GET /favicon.ico HTTP/1.1" 404 2994
C:\Users\rudra\rudra_md\sydney_rest_areas\rest_areas\views.py:31: UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'rest_areas.models.RestArea'> QuerySet.
  paginator = Paginator(rest_areas, 20)  # Show 20 rest areas per page
Internal Server Error: /list/
Traceback (most recent call last):
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
psycopg2.errors.UndefinedTable: relation "rest_areas" does not exist
LINE 1: SELECT COUNT(*) AS "__count" FROM "rest_areas"
                                          ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\rudra\rudra_md\sydney_rest_areas\rest_areas\views.py", line 33, in rest_areas_list
    page_obj = paginator.get_page(page_number)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\paginator.py", line 85, in get_page
    return self.page(number)
           ~~~~~~~~~^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\paginator.py", line 89, in page
    number = self.validate_number(number)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\paginator.py", line 70, in validate_number
    if number > self.num_pages:
                ^^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ~~~~~~~~~^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\paginator.py", line 116, in num_pages
    if self.count == 0 and not self.allow_empty_first_page:
       ^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ~~~~~~~~~^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\core\paginator.py", line 110, in count
    return c()
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\models\query.py", line 604, in count
    return self.query.get_count(using=self.db)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\models\sql\query.py", line 644, in get_count
    return obj.get_aggregation(using, {"__count": Count("*")})["__count"]
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\models\sql\query.py", line 626, in get_aggregation
    result = compiler.execute_sql(SINGLE)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\models\sql\compiler.py", line 1623, in execute_sql
    cursor.execute(sql, params)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\utils.py", line 122, in execute
    return super().execute(sql, params)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        sql, params, many=False, executor=self._execute
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\rudra\rudra_md\.restareas_env\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
django.db.utils.ProgrammingError: relation "rest_areas" does not exist
LINE 1: SELECT COUNT(*) AS "__count" FROM "rest_areas"
                                          ^
                                          

bibek101101
rUdra@999@9999