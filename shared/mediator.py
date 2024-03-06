import inspect
from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar

from shared.decorators import singleton

T = TypeVar("T")


class EventHandler(Generic[T], ABC):
    @abstractmethod
    async def handle(self, event: T, *args, **kwargs):
        pass


class ServiceContainer:
    def __init__(self):
        self._services = {}

    def register(self, service_type, service_instance):
        self._services[service_type] = service_instance

    def resolve(self, dep_type):
        return self._services[dep_type]


@singleton
class Mediator:
    def __init__(self):
        self._handlers: Dict[Type, Type[EventHandler]] = {}
        self._service_container: ServiceContainer = ServiceContainer()

    def register_service(self, service_type, service_instance):
        self._service_container.register(service_type, service_instance)

    def bind(self, event_type: Type, event_handler_cls: Type[EventHandler]):
        self._handlers[event_type] = event_handler_cls

    async def dispatch(self, event, **kwargs):
        event_handler_cls = self._handlers.get(type(event))

        if event_handler_cls:
            dependencies = get_first_class_init_parameters(event_handler_cls)
            resolved_dependencies = [self._service_container.resolve(dep) for dep in dependencies]
            event_handler = event_handler_cls(event, *resolved_dependencies)
            print(event_handler)
            await event_handler.handle()
            return event_handler
        else:
            raise Exception(f"Handler to event: {event} don't exist")


def get_first_class_init_parameters(cls):
    mro = cls.mro()
    first_class_with_init = None
    for class_ in mro:
        if "__init__" in class_.__dict__:
            first_class_with_init = class_
            break

    if first_class_with_init:
        parameters = list(inspect.signature(first_class_with_init.__init__).parameters.values())
        parameters = parameters[2:]
        return [param.annotation for param in parameters if param.annotation != inspect.Parameter.empty]
    else:
        return None
