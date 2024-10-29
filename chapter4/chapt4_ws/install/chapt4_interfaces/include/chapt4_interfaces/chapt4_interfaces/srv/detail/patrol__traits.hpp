// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from chapt4_interfaces:srv/Patrol.idl
// generated code does not contain a copyright notice

#ifndef CHAPT4_INTERFACES__SRV__DETAIL__PATROL__TRAITS_HPP_
#define CHAPT4_INTERFACES__SRV__DETAIL__PATROL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "chapt4_interfaces/srv/detail/patrol__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace chapt4_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Patrol_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: target_x
  {
    out << "target_x: ";
    rosidl_generator_traits::value_to_yaml(msg.target_x, out);
    out << ", ";
  }

  // member: target_y
  {
    out << "target_y: ";
    rosidl_generator_traits::value_to_yaml(msg.target_y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Patrol_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: target_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_x: ";
    rosidl_generator_traits::value_to_yaml(msg.target_x, out);
    out << "\n";
  }

  // member: target_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_y: ";
    rosidl_generator_traits::value_to_yaml(msg.target_y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Patrol_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace chapt4_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use chapt4_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const chapt4_interfaces::srv::Patrol_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  chapt4_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use chapt4_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const chapt4_interfaces::srv::Patrol_Request & msg)
{
  return chapt4_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<chapt4_interfaces::srv::Patrol_Request>()
{
  return "chapt4_interfaces::srv::Patrol_Request";
}

template<>
inline const char * name<chapt4_interfaces::srv::Patrol_Request>()
{
  return "chapt4_interfaces/srv/Patrol_Request";
}

template<>
struct has_fixed_size<chapt4_interfaces::srv::Patrol_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<chapt4_interfaces::srv::Patrol_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<chapt4_interfaces::srv::Patrol_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace chapt4_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Patrol_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: result
  {
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Patrol_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Patrol_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace chapt4_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use chapt4_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const chapt4_interfaces::srv::Patrol_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  chapt4_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use chapt4_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const chapt4_interfaces::srv::Patrol_Response & msg)
{
  return chapt4_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<chapt4_interfaces::srv::Patrol_Response>()
{
  return "chapt4_interfaces::srv::Patrol_Response";
}

template<>
inline const char * name<chapt4_interfaces::srv::Patrol_Response>()
{
  return "chapt4_interfaces/srv/Patrol_Response";
}

template<>
struct has_fixed_size<chapt4_interfaces::srv::Patrol_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<chapt4_interfaces::srv::Patrol_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<chapt4_interfaces::srv::Patrol_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<chapt4_interfaces::srv::Patrol>()
{
  return "chapt4_interfaces::srv::Patrol";
}

template<>
inline const char * name<chapt4_interfaces::srv::Patrol>()
{
  return "chapt4_interfaces/srv/Patrol";
}

template<>
struct has_fixed_size<chapt4_interfaces::srv::Patrol>
  : std::integral_constant<
    bool,
    has_fixed_size<chapt4_interfaces::srv::Patrol_Request>::value &&
    has_fixed_size<chapt4_interfaces::srv::Patrol_Response>::value
  >
{
};

template<>
struct has_bounded_size<chapt4_interfaces::srv::Patrol>
  : std::integral_constant<
    bool,
    has_bounded_size<chapt4_interfaces::srv::Patrol_Request>::value &&
    has_bounded_size<chapt4_interfaces::srv::Patrol_Response>::value
  >
{
};

template<>
struct is_service<chapt4_interfaces::srv::Patrol>
  : std::true_type
{
};

template<>
struct is_service_request<chapt4_interfaces::srv::Patrol_Request>
  : std::true_type
{
};

template<>
struct is_service_response<chapt4_interfaces::srv::Patrol_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CHAPT4_INTERFACES__SRV__DETAIL__PATROL__TRAITS_HPP_
