import FWCore.ParameterSet.Config as cms

def Phase2OTValidateRecHit(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTValidateRecHit',
    Delta_X_Pixel = cms.PSet(
      name = cms.string('Delta_X_Pixel'),
      title = cms.string('#Delta X macro-pixel sensor;Cluster resolution X coordinate [#mum]'),
      switch = cms.bool(True),
      xmax = cms.double(250),
      xmin = cms.double(-250),
      NxBins = cms.int32(100)
    ),
    Delta_Y_Pixel = cms.PSet(
      name = cms.string('Delta_Y_Pixel'),
      title = cms.string('#Delta Y macro-pixel sensor;Cluster resolution Y coordinate [#mum]'),
      switch = cms.bool(True),
      xmin = cms.double(-1500),
      xmax = cms.double(1500),
      NxBins = cms.int32(100)
    ),
    err_X_Pixel = cms.PSet(
      name = cms.string('err_X_Pixel'),
      title = cms.string('error X macro-pixel sensor;Cluster error X coordinate [#mum]'),
      switch = cms.bool(True),
      xmax = cms.double(0),
      xmin = cms.double(100),
      NxBins = cms.int32(100)
    ),
    err_Y_Pixel = cms.PSet(
      name = cms.string('err_Y_Pixel'),
      title = cms.string('error Y macro-pixel sensor;Cluster error Y coordinate [#mum]'),
      switch = cms.bool(True),
      xmin = cms.double(0),
      xmax = cms.double(500),
      NxBins = cms.int32(100)
    ),
    Delta_X_Pixel_Primary = cms.PSet(
      name = cms.string('Delta_X_Pixel_Primary'),
      title = cms.string('#Delta X macro-pixel sensor;cluster resolution X coordinate [#mum]'),
      switch = cms.bool(True),
      xmin = cms.double(-250),
      xmax = cms.double(250),
      NxBins = cms.int32(100)
    ),
    Delta_Y_Pixel_Primary = cms.PSet(
      name = cms.string('Delta_Y_Pixel_Primary'),
      title = cms.string('#Delta Y macro-pixel sensor;cluster resolution Y coordinate [#mum]'),
      switch = cms.bool(True),
      xmin = cms.double(-500),
      xmax = cms.double(500),
      NxBins = cms.int32(100)
    ),
    Delta_X_vs_eta_Pixel = cms.PSet(
      name = cms.string('Delta_X_vs_Eta_Pixel'),
      title = cms.string(';|#eta|;#Delta x [#mum]'),
      NyBins = cms.int32(250),
      ymin = cms.double(-250),
      ymax = cms.double(250),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    Delta_Y_vs_eta_Pixel = cms.PSet(
      name = cms.string('Delta_Y_vs_Eta_Pixel'),
      title = cms.string(';|#eta|;#Delta y [#mum]'),
      NyBins = cms.int32(300),
      ymin = cms.double(-1500),
      ymax = cms.double(1500),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    Delta_X_vs_phi_Pixel = cms.PSet(
      name = cms.string('Delta_X_vs_Phi_Pixel'),
      title = cms.string(';#phi;#Delta x [#mum]'),
      NyBins = cms.int32(250),
      ymin = cms.double(-250),
      ymax = cms.double(250),
      NxBins = cms.int32(36),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    Delta_Y_vs_phi_Pixel = cms.PSet(
      name = cms.string('Delta_Y_vs_Phi_Pixel'),
      title = cms.string(';#phi;#Delta y [#mum]'),
      NyBins = cms.int32(300),
      ymin = cms.double(-1500),
      ymax = cms.double(1500),
      NxBins = cms.int32(35),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    err_X_vs_eta_Pixel = cms.PSet(
      name = cms.string('err_X_vs_Eta_Pixel'),
      title = cms.string(';|#eta|;local error x [#mum]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(100),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    err_Y_vs_eta_Pixel = cms.PSet(
      name = cms.string('err_Y_vs_Eta_Pixel'),
      title = cms.string(';|#eta|;local error y [#mum]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(500),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    err_X_vs_phi_Pixel = cms.PSet(
      name = cms.string('err_X_vs_Phi_Pixel'),
      title = cms.string(';#phi;local error x [#mum]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(100),
      NxBins = cms.int32(36),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    err_Y_vs_phi_Pixel = cms.PSet(
      name = cms.string('err_Y_vs_Phi_Pixel'),
      title = cms.string(';#phi;local error y [#mum]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(500),
      NxBins = cms.int32(35),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    Pull_X_Pixel = cms.PSet(
      name = cms.string('Pull_X_Pixel'),
      title = cms.string('Pull X macro-pixel sensor;pull x;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_Y_Pixel = cms.PSet(
      name = cms.string('Pull_Y_Pixel'),
      title = cms.string('Pull Y macro-pixel sensor;pull y;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_X_Pixel_Primary = cms.PSet(
      name = cms.string('Pull_X_Pixel_Primary'),
      title = cms.string('Pull X macro-pixel sensor;pull x;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_Y_Pixel_Primary = cms.PSet(
      name = cms.string('Pull_Y_Pixel_Primary'),
      title = cms.string('Pull Y macro-pixel sensor;pull y;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_X_vs_eta_Pixel = cms.PSet(
      name = cms.string('Pull_X_vs_Eta'),
      title = cms.string(';#eta;pull x'),
      ymax = cms.double(4),
      NxBins = cms.int32(82),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(-4.1),
      ymin = cms.double(-4)
    ),
    Pull_Y_vs_eta_Pixel = cms.PSet(
      name = cms.string('Pull_Y_vs_Eta'),
      title = cms.string(';#eta;pull y'),
      ymax = cms.double(4),
      NxBins = cms.int32(82),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(-4.1),
      ymin = cms.double(-4)
    ),
    nRecHits_Pixel_primary = cms.PSet(
      name = cms.string('Number_RecHits_matched_PrimarySimTrack'),
      title = cms.string('Number of RecHits matched to primary SimTrack;;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(10000),
      NxBins = cms.int32(100)
    ),
    Delta_X_Strip = cms.PSet(
      name = cms.string('Delta_X_Strip'),
      title = cms.string('#Delta X strip sensor;Cluster resolution X coordinate [#mum]'),
      switch = cms.bool(True),
      xmin = cms.double(-250),
      xmax = cms.double(250),
      NxBins = cms.int32(100)
    ),
    Delta_Y_Strip = cms.PSet(
      name = cms.string('Delta_Y_Strip'),
      title = cms.string('#Delta Y strip sensor;Cluster resolution Y coordinate [cm]'),
      xmin = cms.double(-5),
      switch = cms.bool(True),
      xmax = cms.double(5),
      NxBins = cms.int32(100)
    ),
    err_X_Strip = cms.PSet(
      name = cms.string('err_X_Strip'),
      title = cms.string('local error X strip sensor;Cluster error X coordinate [#mum]'),
      switch = cms.bool(True),
      xmin = cms.double(0),
      xmax = cms.double(100),
      NxBins = cms.int32(100)
    ),
    err_Y_Strip = cms.PSet(
      name = cms.string('err_Y_Strip'),
      title = cms.string('local error Y strip sensor;Cluster error Y coordinate [cm]'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(10),
      NxBins = cms.int32(100)
    ),
    Delta_X_Strip_Primary = cms.PSet(
      name = cms.string('Delta_X_Strip_Primary'),
      title = cms.string('#Delta X strip sensor;Cluster resolution X coordinate [#mum]'),
      switch = cms.bool(True),
      xmin = cms.double(-250),
      xmax = cms.double(250),
      NxBins = cms.int32(100)
    ),
    Delta_Y_Strip_Primary = cms.PSet(
      name = cms.string('Delta_Y_Strip_Primary'),
      title = cms.string('#Delta Y strip sensor;Cluster resolution Y coordinate [cm]'),
      xmin = cms.double(-5),
      switch = cms.bool(True),
      xmax = cms.double(5),
      NxBins = cms.int32(100)
    ),
    Delta_X_vs_eta_Strip = cms.PSet(
      name = cms.string('Delta_X_vs_Eta_Strip'),
      title = cms.string(';|#eta|;#Delta x [#mum]'),
      NyBins = cms.int32(250),
      ymin = cms.double(-250),
      ymax = cms.double(250),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    Delta_Y_vs_eta_Strip = cms.PSet(
      name = cms.string('Delta_Y_vs_Eta_Strip'),
      title = cms.string(';|#eta|;#Delta y [cm]'),
      NyBins = cms.int32(100),
      ymin = cms.double(-5),
      ymax = cms.double(5),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    Delta_X_vs_phi_Strip = cms.PSet(
      name = cms.string('Delta_X_vs_Phi_Strip'),
      title = cms.string(';#phi;#Delta x [#mum]'),
      NyBins = cms.int32(250),
      ymin = cms.double(-250),
      ymax = cms.double(250),
      NxBins = cms.int32(36),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    Delta_Y_vs_phi_Strip = cms.PSet(
      name = cms.string('Delta_Y_vs_Phi_Strip'),
      title = cms.string(';#phi;#Delta y [cm]'),
      NyBins = cms.int32(100),
      ymin = cms.double(-5),
      ymax = cms.double(5),
      NxBins = cms.int32(36),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    err_X_vs_eta_Strip = cms.PSet(
      name = cms.string('err_X_vs_Eta_Strip'),
      title = cms.string(';|#eta|;local error x [#mum]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(100),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    err_Y_vs_eta_Strip = cms.PSet(
      name = cms.string('err_Y_vs_Eta_Strip'),
      title = cms.string(';|#eta|;local error y [cm]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(10),
      NxBins = cms.int32(41),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(0)
    ),
    err_X_vs_phi_Strip = cms.PSet(
      name = cms.string('err_X_vs_Phi_Strip'),
      title = cms.string(';#phi;local error x [#mum]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(100),
      NxBins = cms.int32(36),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    err_Y_vs_phi_Strip = cms.PSet(
      name = cms.string('err_Y_vs_Phi_Strip'),
      title = cms.string(';#phi;local error y [cm]'),
      NyBins = cms.int32(100),
      ymin = cms.double(0),
      ymax = cms.double(10),
      NxBins = cms.int32(36),
      switch = cms.bool(True),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    Pull_X_Strip = cms.PSet(
      name = cms.string('Pull_X_Strip'),
      title = cms.string('Pull X strip sensor;pull x;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_Y_Strip = cms.PSet(
      name = cms.string('Pull_Y_Strip'),
      title = cms.string('Pull Y strip sensor;pull y;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_X_Strip_Primary = cms.PSet(
      name = cms.string('Pull_X_Strip_Primary'),
      title = cms.string('Pull X strip sensor;pull x;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_Y_Strip_Primary = cms.PSet(
      name = cms.string('Pull_Y_Strip_Primary'),
      title = cms.string('Pull Y strip sensor;pull y;'),
      xmin = cms.double(-4),
      switch = cms.bool(True),
      xmax = cms.double(4),
      NxBins = cms.int32(100)
    ),
    Pull_X_vs_eta_Strip = cms.PSet(
      name = cms.string('Pull_X_vs_Eta_Strip'),
      title = cms.string(';#eta;pull x'),
      ymax = cms.double(4),
      NxBins = cms.int32(82),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(-4.1),
      ymin = cms.double(-4)
    ),
    Pull_Y_vs_eta_Strip = cms.PSet(
      name = cms.string('Pull_Y_vs_Eta_Strip'),
      title = cms.string(';#eta;pull y'),
      ymax = cms.double(4),
      NxBins = cms.int32(82),
      switch = cms.bool(True),
      xmax = cms.double(4.1),
      xmin = cms.double(-4.1),
      ymin = cms.double(-4)
    ),
    nRecHits_Strip_primary = cms.PSet(
      name = cms.string('Number_RecHits_matched_PrimarySimTrack'),
      title = cms.string('Number of RecHits matched to primary SimTrack;;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(10000),
      NxBins = cms.int32(100)
    ),
    SimVertexSource = cms.InputTag('g4SimHits'),
    associatePixel = cms.bool(False),
    TopFolderName = cms.string('TrackerPhase2OTRecHitV'),
    associateHitbySimTrack = cms.bool(True),
    Verbosity = cms.bool(False),
    associateStrip = cms.bool(True),
    phase2TrackerSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Tracker'),
    associateRecoTracks = cms.bool(False),
    pixelSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Pixel'),
    usePhase2Tracker = cms.bool(True),
    rechitsSrc = cms.InputTag('siPhase2RecHits'),
    simTracksSrc = cms.InputTag('g4SimHits'),
    SimTrackMinPt = cms.double(2),
    PSimHitSource = cms.VInputTag(
      'g4SimHits:TrackerHitsTIBLowTof',
      'g4SimHits:TrackerHitsTIBHighTof',
      'g4SimHits:TrackerHitsTIDLowTof',
      'g4SimHits:TrackerHitsTIDHighTof',
      'g4SimHits:TrackerHitsTOBLowTof',
      'g4SimHits:TrackerHitsTOBHighTof',
      'g4SimHits:TrackerHitsTECLowTof',
      'g4SimHits:TrackerHitsTECHighTof',
      'g4SimHits:TrackerHitsPixelBarrelLowTof',
      'g4SimHits:TrackerHitsPixelBarrelHighTof',
      'g4SimHits:TrackerHitsPixelEndcapLowTof',
      'g4SimHits:TrackerHitsPixelEndcapHighTof'
    ),
    ROUList = cms.vstring(
      'TrackerHitsPixelBarrelLowTof',
      'TrackerHitsPixelBarrelHighTof',
      'TrackerHitsTIBLowTof',
      'TrackerHitsTIBHighTof',
      'TrackerHitsTIDLowTof',
      'TrackerHitsTIDHighTof',
      'TrackerHitsTOBLowTof',
      'TrackerHitsTOBHighTof',
      'TrackerHitsPixelEndcapLowTof',
      'TrackerHitsPixelEndcapHighTof',
      'TrackerHitsTECLowTof',
      'TrackerHitsTECHighTof'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
