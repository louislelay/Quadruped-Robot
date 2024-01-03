#ifndef UTILS_H
#define UTILS_H

#include <algorithm>

template<typename T>
T clamp(T const a, T const low, T const high)
{
    return std::max<T>(low, std::min<T>(high, a));
}

#endif