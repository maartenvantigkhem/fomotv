import datetime
from main.winner import set_winners


#export DJANGO_SETTINGS_MODULE=fomotv.prod
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fomotv.local")

current_date = datetime.datetime.now()
set_winners(current_date)