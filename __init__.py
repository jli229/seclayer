import playground
from .pls import PLSClientFactory, PLSServerFactory
from .pimp import PIMPServerFactory, PIMPClientFactory

pimpConnector = playground.Connector(protocolStack=(PLSClientFactory(), PLSServerFactory(), PIMPClientFactory(), PIMPServerFactory()))
playground.setConnector("pimp", pimpConnector)
playground.setConnector("lab1_GoldenNuggetNetSec2019", pimpConnector)
