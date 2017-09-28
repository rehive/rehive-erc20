from invoke import Collection, task
from etc.tasks import tasks

ns = Collection()
ns.add_collection(Collection.from_module(tasks, name='truffle'))
