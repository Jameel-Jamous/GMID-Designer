add_library(mymath math.cpp)

add_executable(myapp main.cpp)
target_link_libraries(myapp PRIVATE mymath)

install(TARGETS mymath DESTINATION lib)
install(FILES math.h DESTINATION include)
install(TARGETS myapp DESTINATION bin)
