add_definitions(-DTRANSLATION_DOMAIN=\"plasma_wallpaper_org.kde.plasma.kdehourlyfoxes\")

set(kdehourlyfoxesplugin_SRCS
    kdehourlyfoxesplugin.cpp
)

add_library(kdehourlyfoxesplugin SHARED ${kdehourlyfoxesplugin_SRCS})

target_link_libraries(kdehourlyfoxesplugin
    KF5::I18n
    Qt5::Gui
    Qt5::Qml
)
install(TARGETS kdehourlyfoxesplugin DESTINATION ${KDE_INSTALL_QMLDIR}/org/kde/plasma/private/kdehourlyfoxes)
install(FILES qmldir DESTINATION ${KDE_INSTALL_QMLDIR}/org/kde/plasma/private/kdehourlyfoxes)
