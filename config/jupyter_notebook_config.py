# Configuration file for ipython-notebook.
from os import getenv, getuid
from pwd import getpwall
from IPython.lib import passwd


user = [u for u in getpwall() if u.pw_uid == getuid()][0]
c = get_config()

#------------------------------------------------------------------------------
# NotebookApp configuration
#------------------------------------------------------------------------------

# NotebookApp will inherit config from: BaseIPythonApplication, Application

# The IPython password to use i.e. "datajoint".
c.NotebookApp.password = passwd(getenv('JUPYTER_PASSWORD', 'datajoint')).encode("ascii")

# Allow root access.
c.NotebookApp.allow_root = True

# The IP to serve on.
c.NotebookApp.ip = u'0.0.0.0'

# The Port to serve on.
c.NotebookApp.port = 8888

c.NotebookApp.default_url = '/lab'

c.NotebookApp.notebook_dir = user.pw_dir

c.NotebookApp.terminado_settings = { 'shell_command': [user.pw_shell, '-l'] }

c.FileContentsManager.root_dir = '/home'
