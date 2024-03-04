import FWCore.ParameterSet.Config as cms

def Phase2OTValidateCluster(**kwargs):
  mod = cms.EDProducer('Phase2OTValidateCluster',
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
      xmin = cms.double(-1500),
      xmax = cms.double(1500),
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
    TopFolderName = cms.string('TrackerPhase2OTClusterV'),
    ClusterSource = cms.InputTag('siPhase2Clusters'),
    OuterTrackerDigiSimLinkSource = cms.InputTag('simSiPixelDigis', 'Tracker'),
    simtracks = cms.InputTag('g4SimHits'),
    SimTrackMinPt = cms.double(0),
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
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
