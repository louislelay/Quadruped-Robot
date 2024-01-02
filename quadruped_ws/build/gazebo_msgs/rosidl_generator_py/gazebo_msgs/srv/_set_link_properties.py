# generated from rosidl_generator_py/resource/_idl.py.em
# with input from gazebo_msgs:srv/SetLinkProperties.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetLinkProperties_Request(type):
    """Metaclass of message 'SetLinkProperties_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_msgs.srv.SetLinkProperties_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_link_properties__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_link_properties__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_link_properties__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_link_properties__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_link_properties__request

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetLinkProperties_Request(metaclass=Metaclass_SetLinkProperties_Request):
    """Message class 'SetLinkProperties_Request'."""

    __slots__ = [
        '_link_name',
        '_com',
        '_gravity_mode',
        '_mass',
        '_ixx',
        '_ixy',
        '_ixz',
        '_iyy',
        '_iyz',
        '_izz',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'link_name': 'string',
        'com': 'geometry_msgs/Pose',
        'gravity_mode': 'boolean',
        'mass': 'double',
        'ixx': 'double',
        'ixy': 'double',
        'ixz': 'double',
        'iyy': 'double',
        'iyz': 'double',
        'izz': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.link_name = kwargs.get('link_name', str())
        from geometry_msgs.msg import Pose
        self.com = kwargs.get('com', Pose())
        self.gravity_mode = kwargs.get('gravity_mode', bool())
        self.mass = kwargs.get('mass', float())
        self.ixx = kwargs.get('ixx', float())
        self.ixy = kwargs.get('ixy', float())
        self.ixz = kwargs.get('ixz', float())
        self.iyy = kwargs.get('iyy', float())
        self.iyz = kwargs.get('iyz', float())
        self.izz = kwargs.get('izz', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.link_name != other.link_name:
            return False
        if self.com != other.com:
            return False
        if self.gravity_mode != other.gravity_mode:
            return False
        if self.mass != other.mass:
            return False
        if self.ixx != other.ixx:
            return False
        if self.ixy != other.ixy:
            return False
        if self.ixz != other.ixz:
            return False
        if self.iyy != other.iyy:
            return False
        if self.iyz != other.iyz:
            return False
        if self.izz != other.izz:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def link_name(self):
        """Message field 'link_name'."""
        return self._link_name

    @link_name.setter
    def link_name(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'link_name' field must be of type 'str'"
        self._link_name = value

    @builtins.property
    def com(self):
        """Message field 'com'."""
        return self._com

    @com.setter
    def com(self, value):
        if self._check_fields:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'com' field must be a sub message of type 'Pose'"
        self._com = value

    @builtins.property
    def gravity_mode(self):
        """Message field 'gravity_mode'."""
        return self._gravity_mode

    @gravity_mode.setter
    def gravity_mode(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'gravity_mode' field must be of type 'bool'"
        self._gravity_mode = value

    @builtins.property
    def mass(self):
        """Message field 'mass'."""
        return self._mass

    @mass.setter
    def mass(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'mass' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'mass' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._mass = value

    @builtins.property
    def ixx(self):
        """Message field 'ixx'."""
        return self._ixx

    @ixx.setter
    def ixx(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'ixx' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ixx' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ixx = value

    @builtins.property
    def ixy(self):
        """Message field 'ixy'."""
        return self._ixy

    @ixy.setter
    def ixy(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'ixy' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ixy' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ixy = value

    @builtins.property
    def ixz(self):
        """Message field 'ixz'."""
        return self._ixz

    @ixz.setter
    def ixz(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'ixz' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ixz' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ixz = value

    @builtins.property
    def iyy(self):
        """Message field 'iyy'."""
        return self._iyy

    @iyy.setter
    def iyy(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'iyy' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'iyy' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._iyy = value

    @builtins.property
    def iyz(self):
        """Message field 'iyz'."""
        return self._iyz

    @iyz.setter
    def iyz(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'iyz' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'iyz' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._iyz = value

    @builtins.property
    def izz(self):
        """Message field 'izz'."""
        return self._izz

    @izz.setter
    def izz(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'izz' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'izz' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._izz = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetLinkProperties_Response(type):
    """Metaclass of message 'SetLinkProperties_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_msgs.srv.SetLinkProperties_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_link_properties__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_link_properties__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_link_properties__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_link_properties__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_link_properties__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetLinkProperties_Response(metaclass=Metaclass_SetLinkProperties_Response):
    """Message class 'SetLinkProperties_Response'."""

    __slots__ = [
        '_success',
        '_status_message',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'status_message': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.status_message = kwargs.get('status_message', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.status_message != other.status_message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def status_message(self):
        """Message field 'status_message'."""
        return self._status_message

    @status_message.setter
    def status_message(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'status_message' field must be of type 'str'"
        self._status_message = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetLinkProperties_Event(type):
    """Metaclass of message 'SetLinkProperties_Event'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_msgs.srv.SetLinkProperties_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_link_properties__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_link_properties__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_link_properties__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_link_properties__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_link_properties__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo.__class__._TYPE_SUPPORT is None:
                ServiceEventInfo.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetLinkProperties_Event(metaclass=Metaclass_SetLinkProperties_Event):
    """Message class 'SetLinkProperties_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<gazebo_msgs/SetLinkProperties_Request, 1>',
        'response': 'sequence<gazebo_msgs/SetLinkProperties_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['gazebo_msgs', 'srv'], 'SetLinkProperties_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['gazebo_msgs', 'srv'], 'SetLinkProperties_Response'), 1),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from service_msgs.msg import ServiceEventInfo
        self.info = kwargs.get('info', ServiceEventInfo())
        self.request = kwargs.get('request', [])
        self.response = kwargs.get('response', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self):
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value):
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self):
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value):
        if self._check_fields:
            from gazebo_msgs.srv import SetLinkProperties_Request
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, SetLinkProperties_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'SetLinkProperties_Request'"
        self._request = value

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if self._check_fields:
            from gazebo_msgs.srv import SetLinkProperties_Response
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, SetLinkProperties_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'SetLinkProperties_Response'"
        self._response = value


class Metaclass_SetLinkProperties(type):
    """Metaclass of service 'SetLinkProperties'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_msgs.srv.SetLinkProperties')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_link_properties

            from gazebo_msgs.srv import _set_link_properties
            if _set_link_properties.Metaclass_SetLinkProperties_Request._TYPE_SUPPORT is None:
                _set_link_properties.Metaclass_SetLinkProperties_Request.__import_type_support__()
            if _set_link_properties.Metaclass_SetLinkProperties_Response._TYPE_SUPPORT is None:
                _set_link_properties.Metaclass_SetLinkProperties_Response.__import_type_support__()
            if _set_link_properties.Metaclass_SetLinkProperties_Event._TYPE_SUPPORT is None:
                _set_link_properties.Metaclass_SetLinkProperties_Event.__import_type_support__()


class SetLinkProperties(metaclass=Metaclass_SetLinkProperties):
    from gazebo_msgs.srv._set_link_properties import SetLinkProperties_Request as Request
    from gazebo_msgs.srv._set_link_properties import SetLinkProperties_Response as Response
    from gazebo_msgs.srv._set_link_properties import SetLinkProperties_Event as Event

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
