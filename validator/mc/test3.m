// ******* Anunaki - About.m **********

global group aboutGroup;
global layer glow;
global text txt1, txt2;

global timer refreshTimer, animTimer;
global int seqNo;
global boolean goingdown = 0;

System.onScriptLoaded() {
  refreshTimer = new Timer;
  refreshTimer.setDelay(50);

  animTimer = new Timer;
  animTimer.setDelay(8000);

  aboutGroup = getScriptGroup();

  glow = aboutGroup.getObject("about.glow");
  txt1 = aboutGroup.findObject("txt1");
  txt2 = aboutGroup.findObject("txt2");
}

system.onScriptUnloading() {
  aboutGroup = NULL; // clears all instances

  refreshTimer.stop();
  delete refreshTimer;
}

aboutGroup.onSetVisible(boolean on) {
  if (on) {
    txt1.setTargetX(20);
    txt2.setTargetX(20);
    txt1.setTargetSpeed(0.5);
    txt2.setTargetSpeed(0.8);
  
    txt1.setXMLParam("x", "370");
    txt2.setXMLParam("x", "370");
    seqNo = 1;

    txt1.gotoTarget();
    txt2.gotoTarget();
    animTimer.start();
    refreshTimer.start();
  } else {
    txt1.cancelTarget();
    txt2.cancelTarget();

    refreshTimer.stop();
    animTimer.stop();
  }
}

refreshTimer.onTimer() {
  int a = glow.getAlpha();

  if (getStatus()!=1) {
    if (goingDown) {
      a = a - 10;
      if (a <= 0) goingDown = 0;
    } else {
      a = a + 10;
      if (a >= 255) goingDown = 1;
    }
  } else {
    a = (getLeftVUMeter() + getRightVUMeter())/2;
  }
  glow.setAlpha(a);
}

animTimer.onTimer() {
  txt1.gotoTarget();
  txt2.gotoTarget();
}

txt1.onTargetReached() {
  if (txt1.getLeft() > 0) {
    if ((seqNo >= 3) && (seqNo < 5)) return;
    txt1.setTargetX(-320);
    return;
  }

  txt1.setXMLParam("x", "370");
  txt1.setTargetX(20);

  if (seqNo == 0) txt1.setText("Copyright 2005, by Leechbite");
  if (seqNo == 1) txt1.setText("www.leechbite.com");
  if ((seqNo >= 2) && (seqNo <= 5)) txt1.setText("Credits:"); 
  if ((seqNo >= 3) && (seqNo <= 5)) { 
    txt1.setXMLParam("x", "20");
    txt1.setTargetX(20);
    txt1.setText("Credits:"); 
  }
  if (seqNo == 6) txt1.setText("Anunaki is dedicated to:");
  if (seqNo == 7) txt1.setText("     Thank you for using Anunaki!");

  txt1.gotoTarget();
}

txt2.onTargetReached() {
  if (txt2.getLeft() > 0) {
    txt2.setTargetX(-320);
    return;
  }

  if (seqNo == 0) txt2.setText("mail@leechbite.com");
  if (seqNo == 1) txt2.setText("metaskins.net");
  if (seqNo == 2) txt2.setText("     VAG (godfather) - for suggesting the name Anunaki.");
  if (seqNo == 3) txt2.setText("RPeterClark/martin.deimos - CD Cover scripts and workaround.");
  if (seqNo == 4) txt2.setText("     UUL, SloB - Color Themes");
  if (seqNo == 5) txt2.setText("     Will Fisher - AutorepeatButton.m");
  if (seqNo == 6) txt2.setText("     Lexie, Jethro, Judd at sa lahat ng pinoy ampers!");
  if (seqNo == 7) txt2.setText("     Salamat sa lahat ng gumamit ng Anunaki!");

  txt2.setXMLParam("x", "370");
  txt2.setTargetX(20);
  txt2.gotoTarget();

  seqNo++; if (seqNo > 7) seqNo = 0;
}

