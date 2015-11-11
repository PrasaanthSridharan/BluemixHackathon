from django.core.management.base import NoArgsCommand

import requests, json
from bluehack.models import Crisis


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        r = requests.post("http://api.rwlabs.org/v1/disasters", data=json.dumps({
                "limit": "1000",
                "fields": {
                    "include": ["id", "name", "url", "status", "glide", "country"]
                },
                "filter": {
                    "field": "status",
                    "value": ["alert", "current"],
                    "operator": "OR"
                },
                "sort": ["id:asc"]
            }))
        assert r.status_code == 200

        latestUpdates = r.json()["data"]
        latestRwids = map(lambda d: d["fields"]["id"], latestUpdates)

        # anything which was alert/active which is missing from latest updates, is now past
        past = Crisis.objects.exclude(rwid__in=latestRwids).exclude(status="past")
        past.select_for_update().update(status="past")
        print "%d crises marked as 'past'" % len(past)

        both = Crisis.objects.filter(rwid__in=latestRwids).order_by('-rwid')
        maxBoth = -1
        if len(both): maxBoth = both[0].rwid

        toCreate = filter(lambda d: d["fields"]["id"] > maxBoth, latestUpdates)
        for disaster in toCreate:
            c = Crisis()
            c.defineFromReliefWebResponse(disaster)
            c.save()
        
        print "%d new crises added to database" % len(toCreate)
