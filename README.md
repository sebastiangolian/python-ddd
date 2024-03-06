# python-ddd

## Commands

```bash
pip install pipenv
pipenv install -d
pipenv run start
pipenv run start_mediator
pipenv run tests
pipenv run lint
```

## Links

- https://github.com/qu3vipon/python-ddd/blob/main/src/display/domain/entity/room.py
- https://dddinpython.com/index.php/2022/07/22/entities/
- https://dddinpython.com/index.php/2021/11/06/where-to-place-the-business-logic-in-ddd/
- https://martinfowler.com/bliki/CQRS.html

## Architecture

- CQS
- Hexagonal Tests Architecture in unit test
- Layers (application, domain, infrastructure, shared)
- Domain building blocks (entity, factory, rule, service, value_object, repository_interface)

### Application

- commands + application_services
- query + application_services

### Domain

- entities, aggregates (register_events, validation)
- value_objects
- domain_services
- events
- repository interface

### Infrastructure

- repositories

## Use cases

- crud school_class
- crud students
- crud students in school_class