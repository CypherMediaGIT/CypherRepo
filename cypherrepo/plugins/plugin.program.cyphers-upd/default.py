#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,xbmcplugin,xbmcgui,xbmc,xbmcaddon
addonID = 'plugin.program.cyphers-upd'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')

xbmc.executebuiltin( "Dialog.Close(all,true)" )
icon = xbmc.translatePath("special://home/addons/plugin.program.iptvxtra-upd/icon.png") 
xbmc.executebuiltin('XBMC.Notification(Manual Update, The search can take up to 2 minutes until all updates are found ,30000,'+icon+')')
xbmc.executebuiltin("UpdateLocalAddons")
xbmc.executebuiltin("UpdateAddonRepos")