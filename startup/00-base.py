import nslsii

nslsii.configure_base(get_ipython().user_ns, 
        'xfm',
        publish_documents_with_kafka=False,
        redis_url='xf04bm-xfm-redis1.nsls2.bnl.gov',
        redis_port=6380,
        redis_ssl=True)

#nslsii.configure_olog(get_ipython().user_ns)

import redis
from redis_json_dict import RedisJSONDict

#uri = "info.xfm.nsls2.bnl.gov"
# Provide an endstation prefix, if needed, with a trailing "-"
#new_md = RedisJSONDict(redis.Redis(uri),prefix="")
#BEAMLINE_ID = 'xfm'

#nslsii.configure_olog(get_ipython().user_ns)

#Optional: set any metadata that rarely changes.
#RE.md['beamline_id'] = 'XFM'
#RE.md = new_md
