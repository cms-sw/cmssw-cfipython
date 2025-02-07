import FWCore.ParameterSet.Config as cms

def Phase2ITValidateCluster(*args, **kwargs):
  mod = cms.EDProducer('Phase2ITValidateCluster',
    Delta_X_Pixel = cms.PSet(
      name = cms.string('Delta_X_Pixel'),
      title = cms.string('#Delta X;Cluster resolution X coordinate [#mum]'),
      switch = cms.bool(True),
      xmax = cms.double(250),
      xmin = cms.double(-250),
      NxBins = cms.int32(100)
    ),
    Delta_Y_Pixel = cms.PSet(
      name = cms.string('Delta_Y_Pixel'),
      title = cms.string('#Delta Y ;Cluster resolution Y coordinate [#mum]'),
      xmin = cms.double(-250),
      xmax = cms.double(250),
      switch = cms.bool(True),
      NxBins = cms.int32(100)
    ),
    Delta_X_Pixel_Primary = cms.PSet(
      name = cms.string('Delta_X_Pixel_Primary'),
      title = cms.string('#Delta X ;cluster resolution X coordinate [#mum]'),
      xmin = cms.double(-250),
      xmax = cms.double(250),
      switch = cms.bool(True),
      NxBins = cms.int32(100)
    ),
    Delta_Y_Pixel_Primary = cms.PSet(
      name = cms.string('Delta_Y_Pixel_Primary'),
      title = cms.string('#Delta Y ;cluster resolution Y coordinate [#mum]'),
      xmin = cms.double(-250),
      xmax = cms.double(250),
      switch = cms.bool(True),
      NxBins = cms.int32(100)
    ),
    TopFolderName = cms.string('TrackerPhase2ITClusterV'),
    ClusterSource = cms.InputTag('siPixelClusters'),
    InnerTrackerDigiSimLinkSource = cms.InputTag('simSiPixelDigis', 'Pixel'),
    simtracks = cms.InputTag('g4SimHits'),
    SimTrackMinPt = cms.double(0),
    PSimHitSource = cms.VInputTag(
      'g4SimHits:TrackerHitsPixelBarrelLowTof',
      'g4SimHits:TrackerHitsPixelBarrelHighTof',
      'g4SimHits:TrackerHitsPixelEndcapLowTof',
      'g4SimHits:TrackerHitsPixelEndcapHighTof'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
