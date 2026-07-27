import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorTTStub(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorTTStub',
    L1Stub_Global_Position_Barrel_XY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Global_Position_Barrel_XY'),
      title = cms.string('L1Stub_Global_Position_Barrel_XY;L1 Stub Barrel position x [cm];L1 Stub Barrel position y [cm]'),
      NxBins = cms.int32(960),
      xmin = cms.double(-120),
      xmax = cms.double(120),
      NyBins = cms.int32(960),
      ymin = cms.double(-120),
      ymax = cms.double(120)
    ),
    L1Stub_Global_Position_Endcap_Fw_XY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Global_Position_Endcap_Fw_XY'),
      title = cms.string('L1Stub_Global_Position_Endcap_Fw_XY;L1 Stub Endcap position x [cm];L1 Stub Endcap position y [cm]'),
      NxBins = cms.int32(960),
      xmin = cms.double(-120),
      xmax = cms.double(120),
      NyBins = cms.int32(960),
      ymin = cms.double(-120),
      ymax = cms.double(120)
    ),
    L1Stub_Global_Position_Endcap_Bw_XY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Global_Position_Endcap_Bw_XY'),
      title = cms.string('L1Stub_Global_Position_Endcap_Bw_XY;L1 Stub Endcap position x [cm];L1 Stub Endcap position y [cm]'),
      NxBins = cms.int32(960),
      xmin = cms.double(-120),
      xmax = cms.double(120),
      NyBins = cms.int32(960),
      ymin = cms.double(-120),
      ymax = cms.double(120)
    ),
    L1Stub_Global_Position_RZ = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Global_Position_RZ'),
      title = cms.string('L1Stub_Global_Position_RZ;L1 Stub position z [cm];L1 Stub position #rho [cm]'),
      NxBins = cms.int32(900),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(900),
      ymin = cms.double(0),
      ymax = cms.double(120)
    ),
    CrackOverview = cms.PSet(
      name = cms.string('Crack_Overview_L1Stubs'),
      title = cms.string('Crack_Overview_stubs;Module;Layer'),
      xmin = cms.double(0),
      switch = cms.bool(False),
      xmax = cms.double(13),
      ymin = cms.double(0),
      ymax = cms.double(7.5)
    ),
    L1Stub_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Eta'),
      title = cms.string('L1Stub_Eta;#eta;# L1 Stubs'),
      NxBins = cms.int32(45),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    L1Stub_Phi = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Phi'),
      title = cms.string('L1Stub_Phi;#phi;# L1 Stubs'),
      NxBins = cms.int32(60),
      xmin = cms.double(-3.5),
      xmax = cms.double(3.5)
    ),
    L1Stub_R = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_R'),
      title = cms.string('L1Stub_R;R;# L1 Stubs'),
      NxBins = cms.int32(45),
      xmin = cms.double(0),
      xmax = cms.double(120)
    ),
    L1Stub_bendFE = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_bendFE'),
      title = cms.string('L1Stub_bendFE;Trigger bend;# L1 Stubs'),
      NxBins = cms.int32(69),
      xmin = cms.double(-8.625),
      xmax = cms.double(8.625)
    ),
    L1Stub_bendBE = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_bendBE'),
      title = cms.string('L1Stub_bendBE;Hardware bend;# L1 Stubs'),
      NxBins = cms.int32(69),
      xmin = cms.double(-8.625),
      xmax = cms.double(8.625)
    ),
    L1Stub_isPS = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_isPS'),
      title = cms.string('L1Stub_isPS;Is PS?;# L1 Stubs'),
      NxBins = cms.int32(2),
      xmin = cms.double(0),
      xmax = cms.double(2)
    ),
    Num_L1Stubs_Barrel = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Barrel'),
      title = cms.string('Num_L1Stubs_Barrel;Barrel Layer;# L1 Stubs'),
      NxBins = cms.int32(7),
      xmin = cms.double(0.5),
      xmax = cms.double(7.5)
    ),
    Num_L1Stubs_Endcap_Disc = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Endcap_Disc'),
      title = cms.string('Num_L1Stubs_Endcap_Disc;Endcap Disc;# L1 Stubs'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5)
    ),
    Num_L1Stubs_Endcap_Disc_Fw = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Endcap_Disc_Fw'),
      title = cms.string('Num_L1Stubs_Endcap_Disc_Fw;Forward Endcap Disc;# L1 Stubs'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5)
    ),
    Num_L1Stubs_Endcap_Disc_Bw = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Endcap_Disc_Bw'),
      title = cms.string('Num_L1Stubs_Endcap_Disc_Bw;Backward Endcap Disc;# L1 Stubs'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5)
    ),
    Num_L1Stubs_Endcap_Ring = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Endcap_Ring'),
      title = cms.string('Num_L1Stubs_Endcap_Ring;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    L1Stub_Width_Barrel = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Barrel'),
      title = cms.string('L1Stub_Width_Barrel;Barrel Layer;Displacement - Offset'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Width_Endcap_Disc = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Endcap_Disc'),
      title = cms.string('L1Stub_Width_Endcap_Disc;Endcap Disc;Displacement - Offset'),
      NxBins = cms.int32(5),
      xmin = cms.double(0.5),
      xmax = cms.double(5.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Width_Endcap_Ring = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Endcap_Ring'),
      title = cms.string('L1Stub_Width_Endcap_Ring;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Barrel = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Barrel'),
      title = cms.string('L1Stub_Offset_Barrel;Barrel Layer;Trigger Offset'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Endcap_Disc = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Endcap_Disc'),
      title = cms.string('L1Stub_Offset_Endcap_Disc;Endcap Disc;Trigger Offset'),
      NxBins = cms.int32(5),
      xmin = cms.double(0.5),
      xmax = cms.double(5.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Endcap_Ring = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Endcap_Ring'),
      title = cms.string('L1Stub_Offset_Endcap_Ring;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    Num_L1Stubs_Disc_Fw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc+1'),
      title = cms.string('Num_L1Stubs_Disc+1;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Stubs_Disc_Bw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc-1'),
      title = cms.string('Num_L1Stubs_Disc-1;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    L1Stub_Width_Disc_Fw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc+1'),
      title = cms.string('L1Stub_Width_Disc+1;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Width_Disc_Bw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc-1'),
      title = cms.string('L1Stub_Width_Disc-1;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Fw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc+1'),
      title = cms.string('L1Stub_Offset_Disc+1;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Bw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc-1'),
      title = cms.string('L1Stub_Offset_Disc-1;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    Num_L1Stubs_Disc_Fw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc+2'),
      title = cms.string('Num_L1Stubs_Disc+2;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Stubs_Disc_Bw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc-2'),
      title = cms.string('Num_L1Stubs_Disc-2;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    L1Stub_Width_Disc_Fw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc+2'),
      title = cms.string('L1Stub_Width_Disc+2;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Width_Disc_Bw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc-2'),
      title = cms.string('L1Stub_Width_Disc-2;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Fw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc+2'),
      title = cms.string('L1Stub_Offset_Disc+2;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Bw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc-2'),
      title = cms.string('L1Stub_Offset_Disc-2;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    Num_L1Stubs_Disc_Fw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc+3'),
      title = cms.string('Num_L1Stubs_Disc+3;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Stubs_Disc_Bw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc-3'),
      title = cms.string('Num_L1Stubs_Disc-3;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    L1Stub_Width_Disc_Fw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc+3'),
      title = cms.string('L1Stub_Width_Disc+3;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Width_Disc_Bw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc-3'),
      title = cms.string('L1Stub_Width_Disc-3;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Fw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc+3'),
      title = cms.string('L1Stub_Offset_Disc+3;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Bw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc-3'),
      title = cms.string('L1Stub_Offset_Disc-3;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    Num_L1Stubs_Disc_Fw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc+4'),
      title = cms.string('Num_L1Stubs_Disc+4;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Stubs_Disc_Bw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc-4'),
      title = cms.string('Num_L1Stubs_Disc-4;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    L1Stub_Width_Disc_Fw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc+4'),
      title = cms.string('L1Stub_Width_Disc+4;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Width_Disc_Bw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc-4'),
      title = cms.string('L1Stub_Width_Disc-4;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Fw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc+4'),
      title = cms.string('L1Stub_Offset_Disc+4;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Bw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc-4'),
      title = cms.string('L1Stub_Offset_Disc-4;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    Num_L1Stubs_Disc_Fw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc+5'),
      title = cms.string('Num_L1Stubs_Disc+5;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Stubs_Disc_Bw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Stubs_Disc-5'),
      title = cms.string('Num_L1Stubs_Disc-5;Endcap Ring;# L1 Stubs'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    L1Stub_Width_Disc_Fw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc+5'),
      title = cms.string('L1Stub_Width_Disc+5;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Width_Disc_Bw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Width_Disc-5'),
      title = cms.string('L1Stub_Width_Disc-5;Endcap Ring;Displacement - Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Fw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc+5'),
      title = cms.string('L1Stub_Offset_Disc+5;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    L1Stub_Offset_Disc_Bw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Stub_Offset_Disc-5'),
      title = cms.string('L1Stub_Offset_Disc-5;Endcap Ring;Trigger Offset'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5),
      NyBins = cms.int32(43),
      ymin = cms.double(-10.75),
      ymax = cms.double(10.75)
    ),
    TopFolderName = cms.string('OuterTracker'),
    TTStubs = cms.InputTag('TTStubsFromPhase2TrackerDigis', 'StubAccepted'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
