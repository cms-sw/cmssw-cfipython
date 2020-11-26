import FWCore.ParameterSet.Config as cms

Phase2ITValidateCluster = cms.EDProducer('Phase2ITValidateCluster',
  Delta_X_Pixel = cms.PSet(
    name = cms.string('Delta_X_Pixel'),
    title = cms.string('#Delta X;Cluster resolution X dimension'),
    switch = cms.bool(True),
    xmax = cms.double(5),
    xmin = cms.double(-5),
    NxBins = cms.int32(100)
  ),
  Delta_Y_Pixel = cms.PSet(
    name = cms.string('Delta_Y_Pixel'),
    title = cms.string('#Delta Y ;Cluster resolution Y dimension'),
    xmin = cms.double(-5),
    switch = cms.bool(True),
    xmax = cms.double(5),
    NxBins = cms.int32(100)
  ),
  Delta_X_Pixel_Primary = cms.PSet(
    name = cms.string('Delta_X_Pixel_Primary'),
    title = cms.string('#Delta X ;cluster resolution X dimension'),
    xmin = cms.double(-5),
    switch = cms.bool(True),
    xmax = cms.double(5),
    NxBins = cms.int32(100)
  ),
  Delta_Y_Pixel_Primary = cms.PSet(
    name = cms.string('Delta_Y_Pixel_Primary'),
    title = cms.string('#Delta Y ;cluster resolution Y dimension'),
    xmin = cms.double(-5),
    switch = cms.bool(True),
    xmax = cms.double(5),
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
