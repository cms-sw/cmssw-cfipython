import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorTTTrack(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorTTTrack',
    Track_All_N = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_N'),
      title = cms.string('Track_All_N;# L1 Tracks;# Events'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(399)
    ),
    Track_All_NStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_NStubs'),
      title = cms.string('Track_All_NStubs;# L1 Stubs per L1 Track;# L1 Tracks'),
      NxBins = cms.int32(8),
      xmin = cms.double(0),
      xmax = cms.double(8)
    ),
    Track_All_NLayersMissed = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_NLayersMissed'),
      title = cms.string('Track_All_NLayersMissed;# Layers missed;# L1 Tracks'),
      NxBins = cms.int32(8),
      xmin = cms.double(0),
      xmax = cms.double(8)
    ),
    Track_All_Eta_NStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Eta_NStubs'),
      title = cms.string('Track_All_Eta_NStubs;#eta;# L1 Stubs'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(5),
      ymin = cms.double(3),
      ymax = cms.double(8)
    ),
    Track_All_Pt = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Pt'),
      title = cms.string('Track_All_Pt;p_{T} [GeV];# L1 Tracks'),
      NxBins = cms.int32(50),
      xmin = cms.double(0),
      xmax = cms.double(100)
    ),
    Track_All_Phi = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Phi'),
      title = cms.string('Track_All_Phi;#phi;# L1 Tracks'),
      NxBins = cms.int32(60),
      xmin = cms.double(-3.5),
      xmax = cms.double(3.5)
    ),
    Track_All_D0 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_D0'),
      title = cms.string('Track_All_D0;Track D0;# L1 Tracks'),
      NxBins = cms.int32(101),
      xmin = cms.double(-0.15),
      xmax = cms.double(0.15)
    ),
    Track_All_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Eta'),
      title = cms.string('Track_All_Eta;#eta;# L1 Tracks'),
      NxBins = cms.int32(45),
      xmin = cms.double(-3),
      xmax = cms.double(3)
    ),
    Track_All_VtxZ = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_VtxZ'),
      title = cms.string('Track_All_VtxZ;L1 Track vertex position z [cm];# L1 Tracks'),
      NxBins = cms.int32(41),
      xmin = cms.double(-20),
      xmax = cms.double(20)
    ),
    Track_All_Chi2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Chi2'),
      title = cms.string('Track_All_Chi2;L1 Track #chi^{2};# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(50)
    ),
    Track_All_Chi2RZ = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Chi2RZ'),
      title = cms.string('Track_All_Chi2RZ;L1 Track #chi^{2} r-z;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(50)
    ),
    Track_All_Chi2RPhi = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Chi2RPhi'),
      title = cms.string('Track_All_Chi2RPhi;L1 Track #chi^{2};# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(50)
    ),
    Track_All_BendChi2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_BendChi2'),
      title = cms.string('Track_All_BendChi2;L1 Track Bend #chi^{2};# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(10)
    ),
    Track_All_Chi2Red = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Chi2Red'),
      title = cms.string('Track_All_Chi2Red;L1 Track #chi^{2}/ndf;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(10)
    ),
    Track_All_Chi2_Probability = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Chi2_Probability'),
      title = cms.string('Track_All_Chi2_Probability;#chi^{2} probability;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(1)
    ),
    Track_All_MVA1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_MVA1'),
      title = cms.string('Track_All_MVA1;MVA1;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(1)
    ),
    Track_All_Chi2Red_NStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Chi2Red_NStubs'),
      title = cms.string('Track_All_Chi2Red_NStubs;# L1 Stubs;L1 Track #chi^{2}/ndf'),
      NxBins = cms.int32(5),
      xmin = cms.double(3),
      xmax = cms.double(8),
      NyBins = cms.int32(15),
      ymin = cms.double(0),
      ymax = cms.double(10)
    ),
    Track_All_Chi2Red_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Chi2Red_Eta'),
      title = cms.string('Track_All_Chi2Red_Eta;#eta;L1 Track #chi^{2}/ndf'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(15),
      ymin = cms.double(0),
      ymax = cms.double(10)
    ),
    Track_All_Eta_BarrelStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Eta_BarrelStubs'),
      title = cms.string('Track_All_Eta_BarrelStubs;#eta;# L1 Barrel Stubs'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(5),
      ymin = cms.double(3),
      ymax = cms.double(8)
    ),
    Track_All_Eta_ECStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_All_Eta_ECStubs'),
      title = cms.string('Track_All_Eta_ECStubs;#eta;# L1 EC Stubs'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(5),
      ymin = cms.double(3),
      ymax = cms.double(8)
    ),
    Track_HQ_N = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_N'),
      title = cms.string('Track_HQ_N;# L1 Tracks;# Events'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(399)
    ),
    Track_HQ_NStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_NStubs'),
      title = cms.string('Track_HQ_NStubs;# L1 Stubs per L1 Track;# L1 Tracks'),
      NxBins = cms.int32(8),
      xmin = cms.double(0),
      xmax = cms.double(8)
    ),
    Track_HQ_NLayersMissed = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_NLayersMissed'),
      title = cms.string('Track_HQ_NLayersMissed;# Layers missed;# L1 Tracks'),
      NxBins = cms.int32(8),
      xmin = cms.double(0),
      xmax = cms.double(8)
    ),
    Track_HQ_Eta_NStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Eta_NStubs'),
      title = cms.string('Track_HQ_Eta_NStubs;#eta;# L1 Stubs'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(5),
      ymin = cms.double(3),
      ymax = cms.double(8)
    ),
    Track_HQ_Pt = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Pt'),
      title = cms.string('Track_HQ_Pt;p_{T} [GeV];# L1 Tracks'),
      NxBins = cms.int32(50),
      xmin = cms.double(0),
      xmax = cms.double(100)
    ),
    Track_HQ_Phi = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Phi'),
      title = cms.string('Track_HQ_Phi;#phi;# L1 Tracks'),
      NxBins = cms.int32(60),
      xmin = cms.double(-3.5),
      xmax = cms.double(3.5)
    ),
    Track_HQ_D0 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_D0'),
      title = cms.string('Track_HQ_D0;Track D0;# L1 Tracks'),
      NxBins = cms.int32(101),
      xmin = cms.double(-0.15),
      xmax = cms.double(0.15)
    ),
    Track_HQ_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Eta'),
      title = cms.string('Track_HQ_Eta;#eta;# L1 Tracks'),
      NxBins = cms.int32(45),
      xmin = cms.double(-3),
      xmax = cms.double(3)
    ),
    Track_HQ_VtxZ = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_VtxZ'),
      title = cms.string('Track_HQ_VtxZ;L1 Track vertex position z [cm];# L1 Tracks'),
      NxBins = cms.int32(41),
      xmin = cms.double(-20),
      xmax = cms.double(20)
    ),
    Track_HQ_Chi2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Chi2'),
      title = cms.string('Track_HQ_Chi2;L1 Track #chi^{2};# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(50)
    ),
    Track_HQ_BendChi2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_BendChi2'),
      title = cms.string('Track_HQ_BendChi2;L1 Track Bend #chi^{2};# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(10)
    ),
    Track_HQ_Chi2RZ = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Chi2RZ'),
      title = cms.string('Track_HQ_Chi2RZ;L1 Track #chi^{2} r-z;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(50)
    ),
    Track_HQ_Chi2RPhi = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Chi2RPhi'),
      title = cms.string('Track_HQ_Chi2RPhi;L1 Track #chi^{2} r-phi;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(50)
    ),
    Track_HQ_Chi2Red = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Chi2Red'),
      title = cms.string('Track_HQ_Chi2Red;L1 Track #chi^{2}/ndf;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(10)
    ),
    Track_HQ_Chi2_Probability = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Chi2_Probability'),
      title = cms.string('Track_HQ_Chi2_Probability;#chi^{2} probability;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(1)
    ),
    Track_HQ_MVA1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_MVA1'),
      title = cms.string('Track_HQ_MVA1;MVA1;# L1 Tracks'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(1)
    ),
    Track_HQ_Chi2Red_NStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Chi2Red_NStubs'),
      title = cms.string('Track_HQ_Chi2Red_NStubs;# L1 Stubs;L1 Track #chi^{2}/ndf'),
      NxBins = cms.int32(5),
      xmin = cms.double(3),
      xmax = cms.double(8),
      NyBins = cms.int32(15),
      ymin = cms.double(0),
      ymax = cms.double(10)
    ),
    Track_HQ_Chi2Red_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Chi2Red_Eta'),
      title = cms.string('Track_HQ_Chi2Red_Eta;#eta;L1 Track #chi^{2}/ndf'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(15),
      ymin = cms.double(0),
      ymax = cms.double(10)
    ),
    Track_HQ_Eta_BarrelStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Eta_BarrelStubs'),
      title = cms.string('Track_HQ_Eta_BarrelStubs;#eta;# L1 Barrel Stubs'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(5),
      ymin = cms.double(3),
      ymax = cms.double(8)
    ),
    Track_HQ_Eta_ECStubs = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Track_HQ_Eta_ECStubs'),
      title = cms.string('Track_HQ_Eta_ECStubs;#eta;# L1 EC Stubs'),
      NxBins = cms.int32(15),
      xmin = cms.double(-3),
      xmax = cms.double(3),
      NyBins = cms.int32(5),
      ymin = cms.double(3),
      ymax = cms.double(8)
    ),
    TopFolderName = cms.string('TrackerPhase2OTL1Track'),
    TTTracksTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
    HQNStubs = cms.int32(4),
    HQChi2dof = cms.double(10),
    HQBendChi2 = cms.double(2.2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
