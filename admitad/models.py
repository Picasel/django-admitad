from admitad.abstract_models import AbstractAdmitadPostbackEvent, AbstractAdmitadPostbackRequest
from admitad.utils import is_model_registered

__all__ = []

if not is_model_registered('admitad', 'AdmitadPostbackEvent)'):
    class AdmitadPostbackEvent(AbstractAdmitadPostbackEvent):
        pass


    __all__.append('AdmitadPostbackEvent')

if not is_model_registered('admitad', 'AdmitadPostbackRequest)'):
    class AdmitadPostbackRequest(AbstractAdmitadPostbackRequest):
        pass


    __all__.append('AdmitadPostbackRequest')
