# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from mycroft.skills.context import *
from __future__ import print_function
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
from adapt.intent import IntentBuilder

LOGGER = getLogger(__name__)

__author__ = 'Neel Kapadia'

class SuggestSkill(MycroftSkill):
	def __init__(self):
        super(SuggestSkill, self).__init__(name="SuggestSkill")

    @intent_handler(IntentBuilder("SuggestStartIntent").require("SuggestStart").build())
    @adds_context('SuggestContext')
    def handle_suggest_start(self, message):
        self.speak('Please provide the category of captions you want: ',  expect_response=True)

    @intent_handler(IntentBuilder("GetCategoryIntent").require("category").require('SuggestContext').build())
    @adds_context('GetCategoryContext')
    def handle_get_category(self, message):
    	self.category = message.data.get("category")

    @intent_handler(IntentBuilder('DisplayIntent').require('Suggest').require('GetCategoryContext').build())
    @adds_context('DisplayContext')
    @removes_context('GetCategoryContext')
    def handle_display(self, message):
        if "summer" in utterance:
            self.answer = open("/captions-data/summer.txt")
            self.answer = list(self.answer)
            for line in self.answer:
	            self.speak(line + '\n')
        elif "winter" in utterance:
            self.answer = open("/captions-data/winter.txt")
            self.answer = list(self.answer)
            for line in self.answer:
	            self.speak(line + '\n')   
	    elif "spring" in utterance:
            self.answer = open("/captions-data/spring.txt")
            self.answer = list(self.answer)
            for line in self.answer:
	            self.speak(line + '\n')
        elif "fall" in utterance:
            self.answer = open("/captions-data/fall.txt")
            self.answer = list(self.answer)
            for line in self.answer:
	            self.speak(line + '\n')
        elif "party" in utterance:
            self.answer = open("/captions-data/party.txt")
            self.answer = list(self.answer)
            for line in self.answer:
	            self.speak(line + '\n')
        elif "beach" in utterance:
            self.answer = open("/captions-data/beach.txt")
            self.answer = list(self.answer)
            for line in self.answer:
	            self.speak(line + '\n')
        else:
            LOGGER.error("Invalid Input")

        self.speak('Would you like to get more captions?',  expect_response=True)

    def create_skill():
    	return SuggestSkill()
