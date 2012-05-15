
INSTALLATION_PATH = 'D:\\MyDemo\\Demo\\thjDjango\\thjDjango'

TEMPLATE_DIRS = (
	# Don't forget to use absolute paths, not relative paths.
	''.join([INSTALLATION_PATH, '/templates/']),
)

LANGUAGE_CODE = 'zh_CN'

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.request",
)