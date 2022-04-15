/*
    SPDX-FileCopyrightText: %{CURRENT_YEAR} %{AUTHOR} <%{EMAIL}>
    SPDX-License-Identifier: LGPL-2.1-or-later
*/

#ifndef KDEHOURLYFOXESPLUGIN_H
#define KDEHOURLYFOXESPLUGIN_H

#include <QQmlExtensionPlugin>

class KDEhourlyfoxesPlugin : public QQmlExtensionPlugin
{
    Q_OBJECT
    Q_PLUGIN_METADATA(IID "org.qt-project.Qt.QQmlExtensionInterface")

public:
    void registerTypes(const char *uri) override;
};

#endif // KDEHOURLYFOXESPLUGIN_H
