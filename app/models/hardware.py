""" Resources subclass used to track specific CPU inventory pools"""

from app.models.inventory import  Resources
from app.utils.validators import validate_integer


class CPU(Resources):
    def __init__(self,
                 name, manufacturer, total, allocated, cores, socket,
                 power_watts
                 ):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            cores (int): number of cores
            socket (str): CPU socket type
            power_watts (int): CPU rated wattage
        """
        super().__init__(name, manufacturer, total, allocated)
        validate_integer("cores", cores, 1)
        self._cores = cores
        self._socket = socket
        validate_integer("power", power_watts, 1)
        self._power_watts = power_watts

    @property
    def cores(self):
        """

        Returns:

        """
        return self._cores

    @property
    def socket(self):
        """
        Returns:
        """
        return self._socket

    @property
    def power_watts(self):
        """

        Returns:

        """
        return self._power_watts

    def __repr__(self):
        return f"{self.category}: {self.name}({self.socket} - x{self.cores})"


class Storage(Resources):
    """
        A base class for storage devices - probably not used directly
    """
    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        """

        Args:
            name(str): the name of the device
            manufacturer: name of the manufacturer
            total: total number of storage device
            allocated: total number allocated
            capacity_gb: storage size in gigabyte
        """

        super().__init__(name, manufacturer, total, allocated)
        validate_integer("capacity_gb", capacity_gb, 1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        """

        Returns:
            int: return capacity size

        """
        return self._capacity_gb

    def __repr__(self):
        return f"{self.category}: {self.capacity_gb} GB"


class HDD(Storage):
    """
        class used for HDD type resource
    """
    def __init__(
            self, name, manufacturer, total, allocated, capacity_gb, size, rpm
                ):
        """

        Args:
            name(str): display name of the resource
            manufacturer(str): display name of the manufacturer
            total(int): total number of HDD storage
            allocated(int): total number of storage in-use
            capacity_gb(int): capacity in GB
            size(str): indicates the device size (must be either 2.5" or 3.5")
            rpm(int): disk rotation speed(rpm)
        """

        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        allowed_size = ['2.5"', '3.5"']
        if size not in allowed_size:
            raise ValueError(f"Invalid HDD size. Must be of the size {', '.join(allowed_size)}")
        self._size = size
        validate_integer("rpm", rpm, min_value=1_000, max_value=50_000)
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f"{s}({self.size}, {self.rpm} rpm)"


class SSD(Storage):
    def __init__(self,
                 name, manufacturer, total, allocated, capacity_gb, interface):
        """

        Args:
            name:
            manufacturer:
            total:
            allocated:
            capacity_gb:
            interface:
        """
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = interface

    @property
    def interface(self):
        """

        Returns:

        """
        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return f"{s}({self.interface})"