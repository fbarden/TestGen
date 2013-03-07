# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui
import ConfigParser
import sys

def stringDevice(device, color, parameter) :
    return '<span style=" font-style:italic; color:' + color + ';">' + parameter + '</span>'

def stringComment(line) :
    return '<span style=" color:#949494;">' + line.strip() + '</span>'

def stringMethod(method) :
    return '<span style="font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:italic;">' + method + '</span>'

def plainToHTML(testcase):
    config = ConfigParser.RawConfigParser()
    config.optionxform=str
    config.read('parserConfig.conf')

    method_list = config.options('Methods')
    device_list = config.options('Devices')

    testcase_lines = testcase.splitlines(True)
    
    result = ""

    for line in testcase_lines :
        result+=("<p>")
        if line.startswith('\n') :
            result+=("<br />")
        if line.startswith('#') :
            result+=(stringComment(line))
        else :
            line_words = line.split()
            for word in line_words :
                flag_match = False
                if word in method_list :
                    result+=(stringMethod(word))
                    flag_match = True
                elif word.startswith('@@') :
                    for device in device_list :
                        if word.strip('@').startswith(device) :
                            result+=(stringDevice(device, config.get('Devices', device), word))
                            flag_match = True
                if (not flag_match) :
                    result+=(word);

                result+=(' ');
        result+=("</p>")
    return result

def highlightBlock(cursor) :
    normalFormat = QtGui.QTextCharFormat()
    normalFormat.setForeground(QtGui.QColor("#000000"))
    normalFormat.setFontWeight(50)
    normalFormat.setFontItalic(False)
    specialFormat = QtGui.QTextCharFormat()
    cursor.movePosition(cursor.StartOfBlock, cursor.MoveAnchor)
    cursor.setCharFormat(normalFormat)
    counter = 0
    #changed = False
    while not(cursor.atBlockEnd()) :
        cursor.movePosition(cursor.NextWord, cursor.KeepAnchor)
        print str(counter) + " - " + cursor.selectedText() + " - Anchor " + str(cursor.anchor()) + " Pos " + str(cursor.position())
        if (cursor.selectedText().startsWith("#")) :
            #print "Comentarios"
            cursor.movePosition(cursor.EndOfBlock, cursor.KeepAnchor)
            specialFormat.setForeground(QtGui.QColor("#949494"))
            specialFormat.setFontWeight(50)
            specialFormat.setFontItalic(False)
            cursor.setCharFormat(specialFormat)
            return
        elif (cursor.selectedText().trimmed().endsWith(".py")) :
            #print "Metodo"
            specialFormat.setForeground(QtGui.QColor("#000000"))
            specialFormat.setFontWeight(75)
            specialFormat.setFontItalic(False)
            cursor.setCharFormat(specialFormat)
            cursor.setPosition(cursor.position())
            #cursor.movePosition(cursor.NextCharacter, cursor.KeepAnchor)
            cursor.setCharFormat(normalFormat)
        elif cursor.selectedText().startsWith('@@') :
            config = ConfigParser.RawConfigParser()
            config.optionxform=str
            config.read('parserConfig.conf')
            device_list = config.options('Devices')
            flag_match = False
            for device in device_list :
                if cursor.selectedText().contains(device) :
                    specialFormat.setForeground(QtGui.QColor(config.get('Devices', device)))
                    specialFormat.setFontWeight(50)
                    specialFormat.setFontItalic(False)
                    cursor.setCharFormat(specialFormat)
                    flag_match = True
                if (not flag_match) :
                    cursor.setCharFormat(normalFormat)
                    continue
            if (cursor.selectedText().contains(" ")) :
                #print "Espaco"
                cursor.setPosition(cursor.position())
                cursor.setCharFormat(normalFormat)
        elif (cursor.selectedText().contains(" ")) :
            #print "Espaco"
            cursor.setPosition(cursor.position())
            cursor.setCharFormat(normalFormat)
        elif (cursor.selectedText().startsWith("-")) :
            #print "Traço"
            cursor.setCharFormat(normalFormat)
        else :
            #print "Else"
            cursor.setCharFormat(normalFormat)
        counter += 1
    return

    #if cursor.atBlockStart() :
        #textFormat.setForeground(QtGui.QColor("#000000"))
        #textFormat.setFontWeight(50)
        #textFormat.setFontItalic(False)
        #print "Nova Linha e contando"
        #return textFormat
    #elif (cursor.charFormat().foreground() == QtGui.QColor("#949494")) :
        #print "jah eh comentario"
        #return cursor.charFormat()
    #else :
        #print "nao fez nada"
        #return None

#def highlightWord(cursor) :
    #config = ConfigParser.RawConfigParser()
    #config.optionxform=str
    #config.read('parserConfig.conf')

    #method_list = config.options('Methods')
    #device_list = config.options('Devices')
    #textFormat = QtGui.QTextCharFormat()
    #cursor.select(cursor.WordUnderCursor)
    ## Casos imediatos
    #first_word = cursor.selectedText()
    #print "Caso imediato " + str(cursor.selectedText())
    #if first_word=="" :
        #textFormat.setForeground(QtGui.QColor("#000000"))
        #textFormat.setFontWeight(50)
        #textFormat.setFontItalic(False)
        #return textFormat
    #elif first_word=="py":
        #cursor.movePosition(cursor.NextWord, cursor.MoveAnchor, 1)
        #if cursor.movePosition(cursor.PreviousWord, cursor.KeepAnchor, 3):
            #textFormat.setFontWeight(75)
            #return textFormat
    ## Casos de segundo grau
    #else :
        #while cursor.movePosition(cursor.PreviousWord, cursor.KeepAnchor, 1)
            #if cursor.selected() == "" :
                #return textFormat
        #textFormat.setForeground(QtGui.QColor("#000000"))
        #textFormat.setFontWeight(50)
        #textFormat.setFontItalic(False)
        #return textFormat