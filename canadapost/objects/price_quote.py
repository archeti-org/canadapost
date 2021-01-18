from lxml.etree import Element
from .base import CPObject
from .price_details import PriceDetails
from .service_standard import ServiceStandard


class PriceQuote(CPObject):
    _name = 'price-quote'

    def __init__(self, code, name, details, service_standard):
        self.code = code
        self.name = name
        self.details = details
        self.service_standard = service_standard

    @classmethod
    def from_xml(cls, node, ns):
        code = node.find('cp:service-code', namespaces=ns).text
        name = node.find('cp:service-name', namespaces=ns).text

        details = PriceDetails.from_xml(
            node.find('cp:price-details', namespaces=ns),
            ns
        )

        service_standard = ServiceStandard.from_xml(
            node.find('cp:service-standard', namespaces=ns),
            ns
        )

        return PriceQuote(
            code,
            name,
            details,
            service_standard
        )

    def to_xml(self):
        elem = self.get_element()

        code = Element('service-code')
        code.text = self.code
        elem.append(code)

        name = Element('service-name')
        name.text = self.name
        elem.append(name)

        elem.append(self.details.to_xml())

        elem.append(self.service_standard.to_xml())

        return elem
