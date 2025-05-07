import nslsii

nslsii.configure_base(get_ipython().user_ns, 
        'xfm',
        publish_documents_with_kafka=True)

#nslsii.configure_olog(get_ipython().user_ns)

import redis
from redis_json_dict import RedisJSONDict

uri = "info.xfm.nsls2.bnl.gov"
# Provide an endstation prefix, if needed, with a trailing "-"
new_md = RedisJSONDict(redis.Redis(uri),prefix="")
#BEAMLINE_ID = 'xfm'

nslsii.configure_olog(get_ipython().user_ns)

#Optional: set any metadata that rarely changes.
#RE.md['beamline_id'] = 'XFM'
RE.md = new_md
