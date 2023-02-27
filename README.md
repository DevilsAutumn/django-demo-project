In this demo project i tried to move a model between app.
With this approach:
- all the operations are working on models in their own apps
- reverse migration working
- squash migration working  


In new app, migrations can be applied on empty database simply by removing old app dependencies and changing ```state_only_op``` to false in squashed migrations. some migration and dependencies are commented for squash migrations to work correctly(on empty db).
I have also added migration graph for this demo project before squashing migrations([here](https://github.com/DevilsAutumn/django-demo-project/blob/main/initial.pdf)) and after squashing migrations([here](https://github.com/DevilsAutumn/django-demo-project/blob/main/squashed.pdf)).

```state_only_op``` is a flag which allows us to choose wheather an operation should be applied on db or not.
