In this demo project i tried to move a model between app.
With this approach:
- all the operations are working on models in their own apps
- reverse migration working
- squash migration working  


new app migrations can be applied on empty database simply by removing old app dependencies and changing ```state_only_op``` to false in squashed migrations. The migration are commented for squash migrations to work correctly.
I have also added migration graph for this project before squashing migrations([here](https://github.com/DevilsAutumn/django-demo-project/blob/main/initial.pdf)) and after squashing migrations([here](https://github.com/DevilsAutumn/django-demo-project/blob/main/squashed.pdf)).
