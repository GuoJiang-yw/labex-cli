class ParseSkills:
    def __init__(self) -> None:
        pass

    def __parse_python_skill(self, content):
        build_in_functions = [
            "abs(",
            "enumerate(",
            "float(",
            "input(",
            "int(",
            "len(",
            "map(",
            "max(",
            "min(",
            "next(",
            "open(",
            "print(",
            "round(",
            "sorted(",
            "str(",
            "sum(",
            "zip(",
            "type(",
            "super(",
            "id(",
            "filter(",
            "ord(",
            "reversed(",
            "bytes(",
            "assert(",
            "encode(",
            "isinstance(",
            "all(",
            "bin(",
            "any(",
            "hex(",
            "divmod(",
            "chr(",
            "slice(",
            "strip(",
        ]

        librarys = [
            "re",
            "os",
            "glob",
            "argparse",
            "math",
            "datetime",
            "sys",
            "multiprocessing",
            "unittest",
            "sqlite3",
            "logging",
            "copy",
            "collections",
            "itertools",
            "typing",
            "threading",
            "time",
            "webbrowser",
            "pygame",
            "random",
            "zlib",
            "textwrap",
            "calendar",
            "functools",
            "operator",
            "enum",
            "dateutil",
            "secrets",
            "io",
            "pathlib",
            "dask",
            "tkinter",
            "ctypes",
            "requests",
            "pytz",
            "tqdm",
            "bitstring",
            "numpy",
            "pandas",
            "matplotlib",
            "flask",
            "pyarrow",
            "scipy",
            "beautifulsoup",
            "seaborn",
            "sklearn",
            "basic_units",
            "pil",
        ]

        skills = []
        # python/if_else
        if "if " in content and "else" in content:
            skills.append("python/if_else")
        # python/python_interpreter
        if "python3" in content:
            skills.append("python/python_interpreter")
        # python/python_scripts
        if ".py" in content:
            skills.append("python/python_scripts")
        # python/math_operator
        if "+" in content or "-" in content or "*" in content or "/" in content:
            skills.append("python/math_operator")
        # python/assignment
        if " = " in content:
            skills.append("python/assignment")
        # python/variables
        if "int(" in content or "float(" in content or "str(" in content:
            skills.append("python/variables")
        # python/ipython
        if "ipython" in content:
            skills.append("python/ipython")
        # python/del
        if "del " in content:
            skills.append("python/del")
        # python/function_basic
        if "def " in content:
            skills.append("python/function_basic")
        # python/args_and_kwargs
        if "*args" in content or "**kwargs" in content:
            skills.append("python/args_and_kwargs")
        # python/lambda_function
        if "lambda " in content:
            skills.append("python/lambda_function")
        # python/local_and_global
        if "global " in content:
            skills.append("python/local_and_global")
        # python/yield_values
        if "yield " in content:
            skills.append("python/yield_values")
        # python/comparison
        if "==" in content or "!=" in content or "<" in content or ">" in content:
            skills.append("python/comparison")
        # python/boolean
        if "True" in content or "False" in content:
            skills.append("python/boolean")
        # python/switch_case
        if "switch " in content and "case " in content:
            skills.append("python/switch_case")
        # python/while_loop
        if "while " in content:
            skills.append("python/while_loop")
        # python/range
        if "range(" in content:
            skills.append("python/range")
        # python/walrus
        if ":=" in content:
            skills.append("python/walrus")
        # python/data_types
        if "list(" in content or "tuple(" in content or "dict(" in content:
            skills.append("python/data_types")
        # python/list
        if "append(" in content or "pop(" in content or "remove(" in content:
            skills.append("python/list")
        # python/tuple
        if "tuple(" in content:
            skills.append("python/tuple")
        # python/dict
        if "dict(" in content:
            skills.append("python/dict")
        # python/set
        if "set(" in content:
            skills.append("python/set")
        # python/virtual_environments
        if "virtualenv" in content:
            skills.append("python/virtual_environments")
        # python/pypi
        if "pip install " in content:
            skills.append("python/pypi")
        # python/conda
        if "conda install " in content:
            skills.append("python/conda")
        # python/try_except
        if "try:" in content and "except" in content:
            skills.append("python/try_except")
        # python/syntax_errors
        if "SyntaxError" in content:
            skills.append("python/syntax_errors")
        # python/raise_errors
        if "raise " in content:
            skills.append("python/raise_errors")
        # python/class
        if "class " in content:
            skills.append("python/class")
        # python/attributes
        if "self." in content:
            skills.append("python/attributes")
        # python/inheritance
        if "super(" in content:
            skills.append("python/inheritance")

        for function in build_in_functions:
            if function in content:
                skills.append(f"python/{function[:-1]}")
        for library in librarys:
            if f"import {library}" in content or f"from {library}" in content:
                skills.append(f"python/{library}")

        return list(set(skills))

    def __parse_tkinter_skill(self, content):
        build_in_functions = [
            "Button",
            "Checkbutton",
            "Combobox",
            "Entry",
            "Frame",
            "Label",
            "LabeledScale",
            "Labelframe",
            "Menubutton",
            "Notebook",
            "OptionMenu",
            "Panedwindow",
            "Progressbar",
            "Radiobutton",
            "Scale",
            "Scrollbar",
            "Separator",
            "Sizegrip",
            "Spinbox",
            "Treeview",
            "Canvas",
            "Listbox",
            "Menu",
            "Text",
            "Toplevel",
            "Variable",
            "BooleanVar",
            "DoubleVar",
            "IntVar",
            "StringVar",
            "BitmapImage",
            "PhotoImage",
            "Directory",
            "Open",
            "SaveAs",
            "Chooser",
            "Style",
            "Font",
        ]
        skills = []
        for function in build_in_functions:
            if f".{function}" in content:
                skills.append(f"tkinter/{function.lower()}")
        return list(set(skills))

    def __parse_sklearn_skill(self, content):
        sklearn_skills = """
        sklearn.base: Base Classes and Utility Functions
        sklearn.calibration: Probability Calibration
        sklearn.cluster: Clustering
        sklearn.compose: Composite Estimators
        sklearn.covariance: Covariance Estimators
        sklearn.cross_decomposition: Cross decomposition
        sklearn.datasets: Datasets
        sklearn.decomposition: Matrix Decomposition
        sklearn.discriminant_analysis: Discriminant Analysis
        sklearn.dummy: Dummy estimators
        sklearn.ensemble: Ensemble Methods
        sklearn.exceptions: Exceptions and Warnings
        sklearn.experimental: Experimental
        sklearn.feature_extraction: Feature Extraction
        sklearn.feature_selection: Feature Selection
        sklearn.gaussian_process: Gaussian Processes
        sklearn.impute: Impute
        sklearn.inspection: Inspection
        sklearn.isotonic: Isotonic Regression
        sklearn.kernel_approximation: Kernel Approximation
        sklearn.kernel_ridge: Kernel Ridge Regression
        sklearn.linear_model: Linear Models
        sklearn.manifold: Manifold Learning
        sklearn.metrics: Metrics
        sklearn.mixture: Gaussian Mixture Models
        sklearn.model_selection: Model Selection
        sklearn.multiclass: Multiclass Classification
        sklearn.multioutput: Multioutput Regression and Classification
        sklearn.naive_bayes: Naive Bayes
        sklearn.neighbors: Nearest Neighbors
        sklearn.neural_network: Neural Network Models
        sklearn.pipeline: Pipeline
        sklearn.preprocessing: Preprocessing and Normalization
        sklearn.random_projection: Random Projection
        sklearn.semi_supervised: Semi-Supervised Learning
        sklearn.svm: Support Vector Machines
        sklearn.tree: Decision Trees
        sklearn.utils: Utilities
        """

        clean_skills = []
        for line in sklearn_skills.split("\n"):
            if len(line) > 0:
                skill_id = line.split(": ")[0].strip()
                clean_skills.append(skill_id)

        add_skills = []
        for s in clean_skills:
            if f"{s}" in content:
                add_skills.append(s.replace(".", "/"))
        return list(set(add_skills))

    def __parse_shell_skill(self, content):
        skills = []
        # shell/if_else
        if "if" in content and "else" in content:
            skills.append("shell/if_else")
        # shell/case_esac
        if "case" in content and "esac" in content:
            skills.append("shell/case_esac")
        # shell/while_loop
        if "while" in content:
            skills.append("shell/while_loop")
        # shell/break
        if "break" in content:
            skills.append("shell/break")
        # shell/for_loop
        if "for" in content:
            skills.append("shell/for_loop")
        # shell/function_return_values
        if "return" in content:
            skills.append("shell/function_return_values")
        # shell/function_basic
        if "function" in content:
            skills.append("shell/function_basic")
        # shell/function_arguments
        if "$1" in content:
            skills.append("shell/function_arguments")
        # shell/variable_substitution
        if "${" in content:
            skills.append("shell/variable_substitution")
        # shell/string_operator
        if "==" in content or "!=" in content:
            skills.append("shell/string_operator")
        # shell/boolean_operator
        if "&&" in content or "||" in content:
            skills.append("shell/boolean_operator")
        # shell/file_test_operator
        if "-f" in content or "-d" in content:
            skills.append("shell/file_test_operator")
        # shell/relational_operator
        if "-eq" in content or "-ne" in content:
            skills.append("shell/relational_operator")
        # shell/arithmetic_operator
        if "$((" in content:
            skills.append("shell/arithmetic_operator")
        # shell/local_variables
        if "local" in content:
            skills.append("shell/local_variables")
        # shell/special_variables
        if "$#" in content:
            skills.append("shell/special_variables")
        # shell/input_redirection
        if " < " in content:
            skills.append("shell/input_redirection")
        # shell/output_redirection
        if " > " in content:
            skills.append("shell/output_redirection")

        return list(set(skills))

    def __parse_rust_skill(self, content):
        build_in_functions = [
            "never",
            "array",
            "bool",
            "char",
            "f32",
            "f64",
            "fn",
            "i8",
            "i16",
            "i32",
            "i64",
            "i128",
            "isize",
            "pointer",
            "reference",
            "slice",
            "tuple",
            "u8",
            "u16",
            "u32",
            "u64",
            "u128",
            "unit",
            "usize",
            "assert_matches",
            "async_iter",
            "intrinsics",
            "simd",
            "alloc",
            "any",
            "arch",
            "ascii",
            "backtrace",
            "borrow",
            "boxed",
            "cell",
            "clone",
            "cmp",
            "collections",
            "convert",
            "default",
            "env",
            "error",
            "ffi",
            "fmt",
            "fs",
            "future",
            "hash",
            "hint",
            "io",
            "iter",
            "marker",
            "mem",
            "net",
            "num",
            "ops",
            "option",
            "os",
            "panic",
            "path",
            "pin",
            "prelude",
            "primitive",
            "process",
            "ptr",
            "rc",
            "result",
            "string",
            "sync",
            "task",
            "thread",
            "time",
            "vec",
            "concat_bytes",
            "concat_idents",
            "const_format_args",
            "format_args_nl",
            "log_syntax",
            "trace_macros",
            "assert",
            "assert_eq",
            "assert_ne",
            "cfg",
            "column",
            "compile_error",
            "concat",
            "dbg",
            "debug_assert",
            "debug_assert_eq",
            "debug_assert_ne",
            "eprint",
            "eprintln",
            "format",
            "format_args",
            "include",
            "include_bytes",
            "include_str",
            "x86_64",
            "line",
            "matches",
            "module_path",
            "option_env",
            "print",
            "println",
            "stringify",
            "thread_local",
            "todo",
            "trydeprecated",
            "unimplemented",
            "unreachable",
            "write",
            "writeln",
            "selfty",
            "async",
            "await",
            "break",
            "const",
            "continue",
            "crate",
            "dyn",
            "else",
            "enum",
            "extern",
            "false",
            "for",
            "if",
            "impl",
            "let",
            "loop",
            "match",
            "mod",
            "move",
            "mut",
            "pub",
            "ref",
            "return",
            "self",
            "static",
            "struct",
            "super",
            "trait",
            "true",
            "type",
            "union",
            "unsafe",
            "use",
            "where",
            "while",
            "rustc",
            "rustup",
        ]
        skills = []
        for function in build_in_functions:
            if f".{function}" in content:
                skills.append(f"rust/{function.lower()}")
        return list(set(skills))

    def __parse_pygame_skill(self, content):
        build_in_functions = [
            "color",
            "display",
            "draw",
            "event",
            "font",
            "image",
            "key",
            "locals",
            "mixer",
            "mouse",
            "rect",
            "surface",
            "time",
            "music",
            "cursors",
            "joystick",
            "mask",
            "sprite",
            "transform",
            "bufferproxy",
            "freetype",
            "gfxdraw",
            "midi",
            "pixelarray",
            "pixelcopy",
            "sndarray",
            "surfarray",
            "math",
            "camera",
            "controller",
            "examples",
            "fastevent",
            "scrap",
            "tests",
            "touch",
            "version",
        ]

        skills = []
        for function in build_in_functions:
            if f"pygame.{function}." in content:
                skills.append(f"pygame/{function}")
        return list(set(skills))

    def __parse_django_skill(self, content):
        skills = []
        # django/applications
        if "django.apps" in content:
            skills.append("django/applications")
        # django/built_in_views
        if (
            "django.views.generic" in content
            or "django.views.View" in content
            or "django.views.TemplateView" in content
        ):
            skills.append("django/built_in_views")
        # django/clickjacking_protection
        if "django.middleware.clickjacking" in content:
            skills.append("django/clickjacking_protection")
        # django/contrib_packages
        if "django.contrib" in content:
            skills.append("django/contrib_packages")
        # django/databases
        if "django.db" in content:
            skills.append("django/databases")
        # django/django_admin
        if "django.contrib.admin" in content:
            skills.append("django/django_admin")
        # django/django_exceptions
        if "django.core.exceptions" in content:
            skills.append("django/django_exceptions")
        # django/file_handling
        if "django.core.files" in content:
            skills.append("django/file_handling")
        # django/forms
        if "django.forms" in content:
            skills.append("django/forms")
        # django/logging
        if "django.utils.log" in content:
            skills.append("django/logging")
        # django/middleware
        if "django.middleware" in content:
            skills.append("django/middleware")
        # django/migration_operations
        if "django.db.migrations" in content:
            skills.append("django/migration_operations")
        # django/models
        if "django.db.models" in content:
            skills.append("django/models")
        # django/paginator
        if "django.core.paginator" in content:
            skills.append("django/paginator")
        # django/request_and_response
        if "django.http" in content:
            skills.append("django/request_and_response")
        # django/schemaeditor
        if "django.db.models" in content:
            skills.append("django/schemaeditor")
        # django/settings
        if "django.conf.settings" in content:
            skills.append("django/settings")
        # django/signals
        if "django.dispatch" in content:
            skills.append("django/signals")
        # django/templates
        if "django.template" in content:
            skills.append("django/templates")
        # django/simpletemplateresponse
        if "django.template.response" in content:
            skills.append("django/simpletemplateresponse")
        # django/unicode_data
        if "django.utils.encoding" in content:
            skills.append("django/unicode_data")
        # django/django_urls
        if "django.urls" in content:
            skills.append("django/django_urls")
        # django/django_utils
        if "django.utils" in content:
            skills.append("django/django_utils")
        # django/validators
        if "django.core.validators" in content:
            skills.append("django/validators")
        return list(set(skills))

    def __parse_go_skill(self, content):
        skills = []
        # go/for
        if "for " in content:
            skills.append("go/for")
        # go/if_else
        if "if " in content and "else " in content:
            skills.append("go/if_else")
        # go/switch
        if "switch " in content and "case " in content:
            skills.append("go/switch")
        # go/slices
        if "[]" in content:
            skills.append("go/slices")
        # go/range
        if "range " in content:
            skills.append("go/range")
        # go/maps
        if "map " in content:
            skills.append("go/maps")
        # go/functions
        if "() {" in content and "func " in content:
            skills.append("go/functions")
        # go/variables
        if "var " in content:
            skills.append("go/variables")
        # go/constants
        if "const " in content:
            skills.append("go/constants")
        # go/closures
        if "func " in content and "return " in content:
            skills.append("go/closures")
        # go/pointers
        if "*" in content:
            skills.append("go/pointers")
        # go/strings
        if "string " in content:
            skills.append("go/strings")
        # go/structs
        if "struct " in content:
            skills.append("go/structs")
        # go/interfaces
        if "interface " in content:
            skills.append("go/interfaces")
        # go/struct_embedding
        if "type " in content:
            skills.append("go/struct_embedding")
        # go/generics
        if "<" in content and ">" in content:
            skills.append("go/generics")
        # go/errors
        if "error " in content:
            skills.append("go/errors")
        # go/channels
        if "chan " in content:
            skills.append("go/channels")
        # go/select
        if "select " in content:
            skills.append("go/select")
        # go/timeouts
        if "time.Sleep(" in content:
            skills.append("go/timeouts")
        # go/timers
        if "time.AfterFunc(" in content:
            skills.append("go/timers")
        # go/tickers
        if "time.Tick(" in content:
            skills.append("go/tickers")
        # go/waitgroups
        if "sync.WaitGroup " in content:
            skills.append("go/waitgroups")
        # go/rate_limiting
        if "time.Sleep(" in content:
            skills.append("go/rate_limiting")
        # go/atomic
        if "atomic.Value " in content:
            skills.append("go/atomic")
        # go/mutexes
        if "sync.Mutex " in content:
            skills.append("go/mutexes")
        # go/sorting
        if "sort.Slice " in content:
            skills.append("go/sorting")
        # go/panic
        if "panic(" in content:
            skills.append("go/panic")
        # go/defer
        if "defer " in content:
            skills.append("go/defer")
        # go/recover
        if "recover(" in content:
            skills.append("go/recover")
        # go/text_templates
        if "template " in content:
            skills.append("go/text_templates")
        # go/regular_expressions
        if "regexp " in content:
            skills.append("go/regular_expressions")
        # go/json
        if "json.Marshal " in content:
            skills.append("go/json")
        # go/xml
        if "xml.Marshal " in content:
            skills.append("go/xml")
        # go/time
        if "time.Now " in content:
            skills.append("go/time")
        # go/epoch
        if "time.Unix " in content:
            skills.append("go/epoch")
        # go/time_formatting_parsing
        if "time.Parse " in content:
            skills.append("go/time_formatting_parsing")
        # go/random_numbers
        if "rand.Intn " in content:
            skills.append("go/random_numbers")
        # go/number_parsing
        if "strconv.Atoi " in content:
            skills.append("go/number_parsing")
        # go/url_parsing
        if "url.Parse " in content:
            skills.append("go/url_parsing")
        # go/sha256_hashes
        if "crypto.SHA256 " in content:
            skills.append("go/sha256_hashes")
        # go/base64_encoding
        if "encoding.Base64 " in content:
            skills.append("go/base64_encoding")
        # go/reading_files
        if "os.Open " in content:
            skills.append("go/reading_files")
        # go/writing_files
        if "os.Create " in content:
            skills.append("go/writing_files")
        # go/line_filters
        if "bufio.NewScanner " in content:
            skills.append("go/line_filters")
        # go/file_paths
        if "filepath.Join " in content:
            skills.append("go/file_paths")
        # go/directories
        if "os.Mkdir " in content:
            skills.append("go/directories")
        # go/temporary_files_and_directories
        if "os.TempDir " in content:
            skills.append("go/temporary_files_and_directories")
        # go/embed_directive
        if "embed " in content:
            skills.append("go/embed_directive")
        # go/testing_and_benchmarking
        if "testing.T " in content:
            skills.append("go/testing_and_benchmarking")
        # go/command_line
        if "os.Args " in content:
            skills.append("go/command_line")
        # go/environment_variables
        if "os.Getenv " in content:
            skills.append("go/environment_variables")
        # go/http_client
        if "http.Get " in content:
            skills.append("go/http_client")
        # go/http_server
        if "http.HandleFunc " in content:
            skills.append("go/http_server")
        # go/context
        if "context.Background " in content:
            skills.append("go/context")
        # go/processes
        if "os.StartProcess " in content:
            skills.append("go/processes")
        # go/signals
        if "os.Signal " in content:
            skills.append("go/signals")
        # go/exit
        if "os.Exit " in content:
            skills.append("go/exit")
        # go/values
        if "reflect.ValueOf " in content:
            skills.append("go/values")

        return list(set(skills))

    def __parse_flask_skill(self, content):
        flask_skills = """
        Application Object
        Flask
        Flask.aborter
        Flask.aborter_class
        Flask.add_template_filter()
        Flask.add_template_global()
        Flask.add_template_test()
        Flask.add_url_rule()
        Flask.after_request()
        Flask.after_request_funcs
        Flask.app_context()
        Flask.app_ctx_globals_class
        Flask.async_to_sync()
        Flask.auto_find_instance_path()
        Flask.before_request()
        Flask.before_request_funcs
        Flask.blueprints
        Flask.cli
        Flask.config
        Flask.config_class
        Flask.context_processor()
        Flask.create_global_jinja_loader()
        Flask.create_jinja_environment()
        Flask.create_url_adapter()
        Flask.debug
        Flask.default_config
        Flask.delete()
        Flask.dispatch_request()
        Flask.do_teardown_appcontext()
        Flask.do_teardown_request()
        Flask.endpoint()
        Flask.ensure_sync()
        Flask.error_handler_spec
        Flask.errorhandler()
        Flask.extensions
        Flask.full_dispatch_request()
        Flask.get()
        Flask.get_send_file_max_age()
        Flask.got_first_request
        Flask.handle_exception()
        Flask.handle_http_exception()
        Flask.handle_url_build_error()
        Flask.handle_user_exception()
        Flask.has_static_folder
        Flask.import_name
        Flask.inject_url_defaults()
        Flask.instance_path
        Flask.iter_blueprints()
        Flask.jinja_env
        Flask.jinja_environment
        Flask.jinja_loader
        Flask.jinja_options
        Flask.json
        Flask.json_provider_class
        Flask.log_exception()
        Flask.logger
        Flask.make_aborter()
        Flask.make_config()
        Flask.make_default_options_response()
        Flask.make_response()
        Flask.make_shell_context()
        Flask.name
        Flask.open_instance_resource()
        Flask.open_resource()
        Flask.patch()
        Flask.permanent_session_lifetime
        Flask.post()
        Flask.preprocess_request()
        Flask.process_response()
        Flask.put()
        Flask.redirect()
        Flask.register_blueprint()
        Flask.register_error_handler()
        Flask.request_class
        Flask.request_context()
        Flask.response_class
        Flask.root_path
        Flask.route()
        Flask.run()
        Flask.secret_key
        Flask.select_jinja_autoescape()
        Flask.send_static_file()
        Flask.session_interface
        Flask.shell_context_processor()
        Flask.shell_context_processors
        Flask.should_ignore_error()
        Flask.static_folder
        Flask.static_url_path
        Flask.teardown_appcontext()
        Flask.teardown_appcontext_funcs
        Flask.teardown_request()
        Flask.teardown_request_funcs
        Flask.template_context_processors
        Flask.template_filter()
        Flask.template_folder
        Flask.template_global()
        Flask.template_test()
        Flask.test_cli_runner()
        Flask.test_cli_runner_class
        Flask.test_client()
        Flask.test_client_class
        Flask.test_request_context()
        Flask.testing
        Flask.trap_http_exception()
        Flask.update_template_context()
        Flask.url_build_error_handlers
        Flask.url_default_functions
        Flask.url_defaults()
        Flask.url_for()
        Flask.url_map
        Flask.url_map_class
        Flask.url_rule_class
        Flask.url_value_preprocessor()
        Flask.url_value_preprocessors
        Flask.view_functions
        Flask.wsgi_app()
        Blueprint Objects
        Blueprint
        Blueprint.add_app_template_filter()
        Blueprint.add_app_template_global()
        Blueprint.add_app_template_test()
        Blueprint.add_url_rule()
        Blueprint.after_app_request()
        Blueprint.after_request()
        Blueprint.after_request_funcs
        Blueprint.app_context_processor()
        Blueprint.app_errorhandler()
        Blueprint.app_template_filter()
        Blueprint.app_template_global()
        Blueprint.app_template_test()
        Blueprint.app_url_defaults()
        Blueprint.app_url_value_preprocessor()
        Blueprint.before_app_request()
        Blueprint.before_request()
        Blueprint.before_request_funcs
        Blueprint.cli
        Blueprint.context_processor()
        Blueprint.delete()
        Blueprint.endpoint()
        Blueprint.error_handler_spec
        Blueprint.errorhandler()
        Blueprint.get()
        Blueprint.get_send_file_max_age()
        Blueprint.has_static_folder
        Blueprint.import_name
        Blueprint.jinja_loader
        Blueprint.make_setup_state()
        Blueprint.open_resource()
        Blueprint.patch()
        Blueprint.post()
        Blueprint.put()
        Blueprint.record()
        Blueprint.record_once()
        Blueprint.register()
        Blueprint.register_blueprint()
        Blueprint.register_error_handler()
        Blueprint.root_path
        Blueprint.route()
        Blueprint.send_static_file()
        Blueprint.static_folder
        Blueprint.static_url_path
        Blueprint.teardown_app_request()
        Blueprint.teardown_request()
        Blueprint.teardown_request_funcs
        Blueprint.template_context_processors
        Blueprint.template_folder
        Blueprint.url_default_functions
        Blueprint.url_defaults()
        Blueprint.url_value_preprocessor()
        Blueprint.url_value_preprocessors
        Blueprint.view_functions
        Incoming Request Data
        Request
        Request.accept_charsets
        Request.accept_encodings
        Request.accept_languages
        Request.accept_mimetypes
        Request.access_control_request_headers
        Request.access_control_request_method
        Request.access_route
        Request.application()
        Request.args
        Request.authorization
        Request.base_url
        Request.blueprint
        Request.blueprints
        Request.cache_control
        Request.charset
        Request.close()
        Request.content_encoding
        Request.content_length
        Request.content_md5
        Request.content_type
        Request.cookies
        Request.data
        Request.date
        Request.dict_storage_class
        Request.encoding_errors
        Request.endpoint
        Request.environ
        Request.files
        Request.form
        Request.form_data_parser_class
        Request.from_values()
        Request.full_path
        Request.get_data()
        Request.get_json()
        Request.headers
        Request.host
        Request.host_url
        Request.if_match
        Request.if_modified_since
        Request.if_none_match
        Request.if_range
        Request.if_unmodified_since
        Request.input_stream
        Request.is_json
        Request.is_multiprocess
        Request.is_multithread
        Request.is_run_once
        Request.is_secure
        Request.json
        Request.list_storage_class
        Request.make_form_data_parser()
        Request.max_content_length
        Request.max_form_memory_size
        Request.max_form_parts
        Request.max_forwards
        Request.method
        Request.mimetype
        Request.mimetype_params
        Request.on_json_loading_failed()
        Request.origin
        Request.parameter_storage_class
        Request.path
        Request.pragma
        Request.query_string
        Request.range
        Request.referrer
        Request.remote_addr
        Request.remote_user
        Request.root_path
        Request.root_url
        Request.routing_exception
        Request.scheme
        Request.script_root
        Request.server
        Request.shallow
        Request.stream
        Request.trusted_hosts
        Request.url
        Request.url_charset
        Request.url_root
        Request.url_rule
        Request.user_agent
        Request.user_agent_class
        Request.values
        Request.view_args
        Request.want_form_data_parsed
        request
        Response Objects
        Response
        Response.accept_ranges
        Response.access_control_allow_credentials
        Response.access_control_allow_headers
        Response.access_control_allow_methods
        Response.access_control_allow_origin
        Response.access_control_expose_headers
        Response.access_control_max_age
        Response.add_etag()
        Response.age
        Response.allow
        Response.autocorrect_location_header
        Response.automatically_set_content_length
        Response.cache_control
        Response.calculate_content_length()
        Response.call_on_close()
        Response.charset
        Response.close()
        Response.content_encoding
        Response.content_language
        Response.content_length
        Response.content_location
        Response.content_md5
        Response.content_range
        Response.content_security_policy
        Response.content_security_policy_report_only
        Response.content_type
        Response.cross_origin_embedder_policy
        Response.cross_origin_opener_policy
        Response.data
        Response.date
        Response.default_mimetype
        Response.default_status
        Response.delete_cookie()
        Response.direct_passthrough
        Response.expires
        Response.force_type()
        Response.freeze()
        Response.from_app()
        Response.get_app_iter()
        Response.get_data()
        Response.get_etag()
        Response.get_json()
        Response.get_wsgi_headers()
        Response.get_wsgi_response()
        Response.implicit_sequence_conversion
        Response.is_json
        Response.is_sequence
        Response.is_streamed
        Response.iter_encoded()
        Response.json
        Response.last_modified
        Response.location
        Response.make_conditional()
        Response.make_sequence()
        Response.max_cookie_size
        Response.mimetype
        Response.mimetype_params
        Response.response
        Response.retry_after
        Response.set_cookie()
        Response.set_data()
        Response.set_etag()
        Response.status
        Response.status_code
        Response.stream
        Response.vary
        Response.www_authenticate
        Sessions
        session
        session.new
        session.modified
        session.permanent
        Session Interface
        SessionInterface
        SessionInterface.get_cookie_domain()
        SessionInterface.get_cookie_httponly()
        SessionInterface.get_cookie_name()
        SessionInterface.get_cookie_path()
        SessionInterface.get_cookie_samesite()
        SessionInterface.get_cookie_secure()
        SessionInterface.get_expiration_time()
        SessionInterface.is_null_session()
        SessionInterface.make_null_session()
        SessionInterface.null_session_class
        SessionInterface.open_session()
        SessionInterface.pickle_based
        SessionInterface.save_session()
        SessionInterface.should_set_cookie()
        SecureCookieSessionInterface
        SecureCookieSessionInterface.digest_method()
        SecureCookieSessionInterface.key_derivation
        SecureCookieSessionInterface.open_session()
        SecureCookieSessionInterface.salt
        SecureCookieSessionInterface.save_session()
        SecureCookieSessionInterface.serializer
        SecureCookieSessionInterface.session_class
        SecureCookieSession
        SecureCookieSession.accessed
        SecureCookieSession.get()
        SecureCookieSession.modified
        SecureCookieSession.setdefault()
        NullSession
        NullSession.clear()
        NullSession.pop()
        NullSession.popitem()
        NullSession.setdefault()
        NullSession.update()
        SessionMixin
        SessionMixin.accessed
        SessionMixin.modified
        SessionMixin.permanent
        Test Client
        FlaskClient
        FlaskClient.open()
        FlaskClient.session_transaction()
        Test CLI Runner
        FlaskCliRunner
        FlaskCliRunner.invoke()
        Application Globals
        g
        _AppCtxGlobals
        _AppCtxGlobals.get()
        _AppCtxGlobals.pop()
        _AppCtxGlobals.setdefault()
        Useful Functions and Classes
        current_app
        has_request_context()
        copy_current_request_context()
        has_app_context()
        url_for()
        abort()
        redirect()
        make_response()
        after_this_request()
        send_file()
        send_from_directory()
        Message Flashing
        flash()
        get_flashed_messages()
        JSON Support
        jsonify()
        dumps()
        dump()
        loads()
        load()
        JSONProvider
        JSONProvider.dumps()
        JSONProvider.dump()
        JSONProvider.loads()
        JSONProvider.load()
        JSONProvider.response()
        DefaultJSONProvider
        DefaultJSONProvider.default()
        DefaultJSONProvider.ensure_ascii
        DefaultJSONProvider.sort_keys
        DefaultJSONProvider.compact
        DefaultJSONProvider.mimetype
        DefaultJSONProvider.dumps()
        DefaultJSONProvider.loads()
        DefaultJSONProvider.response()
        Tagged JSON
        TaggedJSONSerializer
        TaggedJSONSerializer.default_tags
        TaggedJSONSerializer.dumps()
        TaggedJSONSerializer.loads()
        TaggedJSONSerializer.register()
        TaggedJSONSerializer.tag()
        TaggedJSONSerializer.untag()
        JSONTag
        JSONTag.check()
        JSONTag.key
        JSONTag.tag()
        JSONTag.to_json()
        JSONTag.to_python()
        Template Rendering
        render_template()
        render_template_string()
        stream_template()
        stream_template_string()
        get_template_attribute()
        Configuration
        Config
        Config.from_envvar()
        Config.from_file()
        Config.from_mapping()
        Config.from_object()
        Config.from_prefixed_env()
        Config.from_pyfile()
        Config.get_namespace()
        Stream Helpers
        stream_with_context()
        Useful Internals
        RequestContext
        RequestContext.copy()
        RequestContext.match_request()
        RequestContext.pop()
        flask.globals.request_ctx
        AppContext
        AppContext.pop()
        AppContext.push()
        flask.globals.app_ctx
        BlueprintSetupState
        BlueprintSetupState.add_url_rule()
        BlueprintSetupState.app
        BlueprintSetupState.blueprint
        BlueprintSetupState.first_registration
        BlueprintSetupState.options
        BlueprintSetupState.subdomain
        BlueprintSetupState.url_defaults
        BlueprintSetupState.url_prefix
        Signals
        template_rendered
        request_started
        request_finished
        got_request_exception
        request_tearing_down
        appcontext_tearing_down
        appcontext_pushed
        appcontext_popped
        message_flashed
        signals.signals_available
        Class-Based Views
        View
        View.as_view()
        View.decorators
        View.dispatch_request()
        View.init_every_request
        View.methods
        View.provide_automatic_options
        MethodView
        MethodView.dispatch_request()
        URL Route Registrations
        View Function Options
        Command Line Interface
        FlaskGroup
        FlaskGroup.get_command()
        FlaskGroup.list_commands()
        FlaskGroup.make_context()
        FlaskGroup.parse_args()
        AppGroup
        AppGroup.command()
        AppGroup.group()
        ScriptInfo
        ScriptInfo.app_import_path
        ScriptInfo.create_app
        ScriptInfo.data
        ScriptInfo.load_app()
        load_dotenv()
        with_appcontext()
        pass_script_info()
        run_command
        shell_command
        """

        skills_map = {
            "flask/appgroup": "flask/command_line_interface",
            "flask/securecookiesession": "flask/session_interface",
            "flask/request": "flask/incoming_request_data",
            "flask/blueprint": "flask/blueprint_objects",
            "flask/_appctxglobals": "flask/application_globals",
            "flask/config": "flask/configuration",
            "flask/view": "flask/class_based_views",
            "flask/blueprintsetupstate": "flask/useful_internals",
            "flask/appcontext": "flask/useful_internals",
            "flask/session": "flask/sessions",
            "flask/flaskclirunner": "flask/test_cli_runner",
            "flask/response": "flask/response_objects",
            "flask/jsonprovider": "flask/json_support",
            "flask/flaskclient": "flask/test_client",
            "flask/nullsession": "flask/session_interface",
            "flask/sessionmixin": "flask/session_interface",
            "flask/taggedjsonserializer": "flask/json_support",
            "flask/scriptinfo": "flask/command_line_interface",
            "flask/flask": "flask/application_object",
            "flask/defaultjsonprovider": "flask/json_support",
            "flask/jsontag": "flask/json_support",
            "flask/requestcontext": "flask/useful_internals",
        }

        all_skills = {}

        for line in flask_skills.split("\n"):
            if len(line) > 0:
                split_line = line.split(".")
                if len(split_line) > 1:
                    skill_id = line.split(".")[0].strip()
                    skill_function = line.split(".")[1].strip().replace(")", "")
                    if skill_id not in all_skills:
                        all_skills[skill_id] = []
                    all_skills[skill_id].append(skill_function)

        add_skills = []
        for s_name in all_skills:
            for s_id in all_skills[s_name]:
                if s_id in content:
                    add_skills.append(skills_map[f"flask/{s_name.lower()}"])
        return list(set(add_skills))

    def __parse_cpp_skill(self, content):
        skills = []
        # cpp/if_else
        if "if (" in content:
            skills.append("cpp/if_else")
        # cpp/user_input
        if "cin >>" in content:
            skills.append("cpp/user_input")
        # cpp/strings
        if "string " in content:
            skills.append("cpp/strings")
        # cpp/math
        if "math.h" in content:
            skills.append("cpp/math")
        # cpp/booleans
        if "bool " in content:
            skills.append("cpp/booleans")
        # cpp/switch
        if "switch (" in content:
            skills.append("cpp/switch")
        # cpp/while_loop
        if "while (" in content:
            skills.append("cpp/while_loop")
        # cpp/break_continue
        if "break;" in content:
            skills.append("cpp/break_continue")
        # cpp/for_loop
        if "for (" in content:
            skills.append("cpp/for_loop")
        # cpp/arrays
        if "[]" in content:
            skills.append("cpp/arrays")
        # cpp/structures
        if "struct " in content:
            skills.append("cpp/structures")
        # cpp/references
        if "&" in content:
            skills.append("cpp/references")
        # cpp/pointers
        if "*" in content:
            skills.append("cpp/pointers")
        # cpp/data_types
        if (
            "int " in content
            or "float " in content
            or "double " in content
            or "char " in content
        ):
            skills.append("cpp/data_types")
        # cpp/variables
        if "=" in content:
            skills.append("cpp/variables")
        # cpp/output
        if "cout <<" in content:
            skills.append("cpp/output")
        # cpp/functions
        if "() {" in content:
            skills.append("cpp/functions")
        # cpp/function_parameters
        if (
            "(int " in content
            or "(float " in content
            or "(double " in content
            or "(char " in content
        ):
            skills.append("cpp/function_parameters")
        # cpp/function_overloading
        if (
            "int " in content
            and "int " in content[content.index("int ") + 1 :]
            or "float " in content
            and "float " in content[content.index("float ") + 1 :]
            or "double " in content
            and "double " in content[content.index("double ") + 1 :]
            or "char " in content
            and "char " in content[content.index("char ") + 1 :]
        ):
            skills.append("cpp/function_overloading")
        # cpp/recursion
        if "recursion" in content:
            skills.append("cpp/recursion")
        # cpp/oop
        if "class " in content:
            skills.append("cpp/oop")
        # cpp/classes_objects
        if "class " in content and "()" in content:
            skills.append("cpp/classes_objects")
        # cpp/class_methods
        if "class " in content and "()" in content and "void " in content:
            skills.append("cpp/class_methods")
        # cpp/constructors
        if "class " in content and "()" in content and "void " not in content:
            skills.append("cpp/constructors")
        # cpp/access_specifiers
        if "public:" in content or "private:" in content:
            skills.append("cpp/access_specifiers")
        # cpp/encapsulation
        if "private:" in content:
            skills.append("cpp/encapsulation")
        # cpp/inheritance
        if "class " in content and "public:" in content and "private:" not in content:
            skills.append("cpp/inheritance")
        # cpp/polymorphism
        if "virtual " in content:
            skills.append("cpp/polymorphism")
        # cpp/files
        if "fstream" in content:
            skills.append("cpp/files")
        # cpp/exceptions
        if "try {" in content:
            skills.append("cpp/exceptions")

        return list(set(skills))

    def __parse_c_skill(self, content):
        skills = []
        # c/if_else
        if "if (" in content:
            skills.append("c/if_else")
        # c/for_loop
        if "for (" in content:
            skills.append("c/for_loop")
        # c/while_loop
        if "while (" in content:
            skills.append("c/while_loop")
        # c/output
        if "printf(" in content:
            skills.append("c/output")
        # c/variables
        if "=" in content:
            skills.append("c/variables")
        # c/data_types
        if (
            "int " in content
            or "float " in content
            or "double " in content
            or "char " in content
        ):
            skills.append("c/data_types")
        # c/constants
        if "const " in content:
            skills.append("c/constants")
        # c/operators
        if (
            "+" in content
            or "-" in content
            or "*" in content
            or "/" in content
            or "%" in content
        ):
            skills.append("c/operators")
        # c/booleans
        if "bool " in content:
            skills.append("c/booleans")
        # c/switch
        if "switch (" in content:
            skills.append("c/switch")
        # c/break_continue
        if "break;" in content:
            skills.append("c/break_continue")
        # c/arrays
        if "[]" in content:
            skills.append("c/arrays")
        # c/strings
        if "string " in content:
            skills.append("c/strings")
        # c/user_input
        if "scanf(" in content:
            skills.append("c/user_input")
        # c/memory_address
        if "&" in content:
            skills.append("c/memory_address")
        # c/pointers
        if "*" in content:
            skills.append("c/pointers")
        # c/structures
        if "struct " in content:
            skills.append("c/structures")
        # c/enums
        if "enum " in content:
            skills.append("c/enums")
        # c/functions
        if "() {" in content:
            skills.append("c/functions")
        # c/function_parameters
        if (
            "(int " in content
            or "(float " in content
            or "(double " in content
            or "(char " in content
        ):
            skills.append("c/function_parameters")
        # c/function_declaration
        if "int " in content or "float " in content or "double " in content:
            skills.append("c/function_declaration")
        # c/recursion
        if "recursion" in content:
            skills.append("c/recursion")
        # c/math_functions
        if "math.h" in content:
            skills.append("c/math_functions")
        # c/create_files
        if "fopen(" in content:
            skills.append("c/create_files")
        # c/write_to_files
        if "fprintf(" in content:
            skills.append("c/write_to_files")
        # c/read_files
        if "fscanf(" in content:
            skills.append("c/read_files")

        return list(set(skills))

    def __parse_html_skill(self, content):
        tags = [
            "p",
            "abbr",
            "title",
            "head",
            "body",
            "address",
            "section",
            "a",
            "style",
            "article",
            "li",
            "ul",
            "footer",
            "time",
            "aside",
            "audio",
            "source",
            "input",
            "button",
            "progress",
            "b",
            "meta",
            "base",
            "form",
            "label",
            "br",
            "textarea",
            "bdi",
            "div",
            "script",
            "bdo",
            "blockquote",
            "cite",
            "canvas",
            "table",
            "tr",
            "th",
            "td",
            "code",
            "pre",
            "colgroup",
            "col",
            "data",
            "datalist",
            "option",
            "dl",
            "dt",
            "dd",
            "img",
            "del",
            "ins",
            "details",
            "summary",
            "dfn",
            "dialog",
            "link",
            "em",
            "embed ",
            "object",
            "fieldset",
            "legend",
            "figure",
            "figcaption",
            "main",
            "header",
            "nav",
            "hgroup",
            "i",
            "iframe",
            "map",
            "area",
            "kbd",
            "samp",
            "ol",
            "meter",
            "noscript",
            "optgroup",
            "select",
            "output",
            "ruby",
            "rp",
            "rt",
            "small",
            "video",
            "span",
            "s",
            "strong",
            "sub",
            "sup",
            "thead",
            "tbody",
            "tfoot",
            "template",
            "var",
            "caption",
            "mark",
        ]

        skills = []
        for tag in tags:
            if f"<{tag}>" or f"<{tag} " or f"</{tag}>" in content:
                skills.append(f"html/{tag}")
        if "</h1>" or "</h2>" or "</h3>" or "</h4>" or "</h5>" or "</h6>" in content:
            skills.append("html/heading")

    def parse(self, language: str, content: str):
        if language == "python":
            return self.__parse_python_skill(content)
        elif language == "tkinter":
            return self.__parse_tkinter_skill(content)
        elif language == "sklearn":
            return self.__parse_sklearn_skill(content)
        elif language == "shell":
            return self.__parse_shell_skill(content)
        elif language == "rust":
            return self.__parse_rust_skill(content)
        elif language == "pygame":
            return self.__parse_pygame_skill(content)
        elif language == "django":
            return self.__parse_django_skill(content)
        elif language == "go":
            return self.__parse_go_skill(content)
        elif language == "flask":
            return self.__parse_flask_skill(content)
        elif language == "cpp":
            return self.__parse_cpp_skill(content)
        elif language == "c":
            return self.__parse_c_skill(content)
        elif language == "html":
            return self.__parse_html_skill(content)
