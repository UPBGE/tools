# $1 blenderplayer

uftrace record -N "std::__*" -N "__gnu*" -N "_GLOBAL__sub_I_*" -N "tbb::interface*" -N "*Theme*" -N "*simd*" -N "atomic_*" -N "EXP_PYATTRIBUTE_DEF*" -N "*RNA*" $@
