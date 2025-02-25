/*************************************************************

  Anunaki - lockvis.m
  by Leechbite

  - this script locks the mode of the VISes.

*************************************************************/

#include "std.mi"

Global group frameGroup;
Global vis visobj;
Global int vismode;

System.onScriptLoaded() {

  frameGroup = getScriptGroup();

  string Param = getParam();
  string visid = getToken(param, ",", 0);
  vismode = stringToInteger(getToken(param, ",", 1));

  visobj = frameGroup.findObject(visid);
  if (visObj) visObj.setMode(visMode);
}

frameGroup.onSetVisible(boolean on) {
  if (on) if (visObj) visObj.setMode(visMode);
}

