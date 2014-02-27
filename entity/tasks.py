from celery import Task

from entity.sync import sync_entities


class SyncEntitiesTask(Task):
    """
    Syncs all of the mirrored entities
    """
    def run(self, *args, **kwargs):
        sync_entities()
