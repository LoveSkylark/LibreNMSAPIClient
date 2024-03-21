from pkg_resources import get_distribution, DistributionNotFound

from pylibrenms.LibreNMSAPIClient import LibreNMSAPIClient

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass