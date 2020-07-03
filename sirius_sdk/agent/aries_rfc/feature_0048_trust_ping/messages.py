from typing import Optional

from ..base import AriesProtocolMessage, AriesProtocolMeta, THREAD_DECORATOR


class Ping(AriesProtocolMessage, metaclass=AriesProtocolMeta):
    PROTOCOL = 'trust_ping'
    NAME = 'ping'

    def __init__(self, comment: Optional[str]=None, response_requested: Optional[bool]=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if comment is not None:
            self['comment'] = comment
        if response_requested is not None:
            self['response_requested'] = response_requested

    @property
    def comment(self) -> Optional[str]:
        return self.get('comment', None)

    @property
    def response_requested(self) -> Optional[bool]:
        return self.get('response_requested', None)


class Pong(AriesProtocolMessage, metaclass=AriesProtocolMeta):
    PROTOCOL = 'trust_ping'
    NAME = 'ping_response'

    def __init__(self, ping_id: str=None, comment: Optional[str]=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if ping_id is not None:
            self.get(THREAD_DECORATOR, {}).update({'thid': ping_id})
        if comment is not None:
            self['comment'] = comment

    @property
    def comment(self) -> Optional[str]:
        return self.get('comment', None)