#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2019.       Mike Herbert
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

import logging
from tkinter import ttk

from geofinder.util import GridPosition

from tk_helper import TKHelper as TkHelp
from util_menu import UtilListboxFrame

default = ["ADM1", "ADM2", "ADM3", "ADM4", "ADMF", "AREA", "CH", "CSTL", "CMTY", "EST ", "HSP","FT",
           "HSTS", "ISL", "MSQE", "MSTY", "MT", "MUS", "PAL", "PPL", "PPLA", "PPLA2", "PPLA3", "PPLA4",
           "PPLC", "PPLG", "PPLH", "PPLL", "PPLQ", "PPLX", "PRK", "PRN", "PRSH", "RUIN", "RGN","RLG", "STG", 
           "SQR", "SYG", "VAL", "MNMT"]


class SetupFeatureFrame(UtilListboxFrame.ListboxFrame):
    """
    SetupFeatureList allows users to add or delete items in the Feature List
    The Feature list is the Feature types that we will load from a Geonames.org file.  For example, we will load
    Villages, Squares, Parks, Cemeteries, etc but not load Refineries, Glaciers, and Coral Reefs.
    For details on Feature Types see http://www.geonames.org/export/codes.html
    SetupFeatureList is derived from ListboxFrame:

    ListboxFrame Displays a scrolling list box that is based on a CachedDictionary.
    ListboxFrame defines the overall Grid Layout
    """

    def __init__(self, frame, title, dir_name, cache_filename):
        self.logger = logging.getLogger(__name__)

        # Add these widgets in addition to the standard widgets we inherit from ListBoxFrame
        self.add_button = ttk.Button(frame, text="add", command=self.add_handler, width=UtilListboxFrame.BUTTON_WIDTH)
        self.add_label = TkHelp.CLabel(frame, text="Enter Geoname Feature below and click on Add button to add", style='Info.TLabel')
        self.add_entry: TkHelp.CEntry = TkHelp.CEntry(frame, text="   ", width=15)  # , style='Info.TLabel')
        super().__init__(frame, title, dir_name, cache_filename)

        # If dictionary is empty, load in defaults
        if len(self.dict) == 0:
            self.logger.error('Feature list is empty. loading defaults')
            self.set_default(default)
            self.load_defaults()
            super().add_handler()

    def configure_widgets(self, frm):
        # Add the standard widgets in ListBoxFrame
        super().configure_widgets(frm)

        # Add these in addition to the standard widgets in ListBoxFrame
        # todo - remove set_grid_position and just use element.grid()
        GridPosition.set_grid_position(self.add_button, "country_button", grd=self.grd)
        GridPosition.set_grid_position(self.add_label, "country_label", grd=self.grd)
        GridPosition.set_grid_position(self.add_entry, "country_entry", grd=self.grd)

    def add_handler(self):
        # Allow user to add an item to list.
        val: str = self.add_entry.text
        self.dict[val.upper()] = ""  # Add item to dict
        super().add_handler()
