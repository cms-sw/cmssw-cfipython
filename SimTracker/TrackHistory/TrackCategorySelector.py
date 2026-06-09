import FWCore.ParameterSet.Config as cms

def TrackCategorySelector(*args, **kwargs):
  mod = cms.EDFilter('TrackCategorySelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    trackProducer = cms.untracked.InputTag('generalTracks'),
    trackingTruth = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
    trackAssociator = cms.untracked.InputTag('quickTrackAssociatorByHits'),
    bestMatchByMaxValue = cms.untracked.bool(True),
    enableRecoToSim = cms.untracked.bool(True),
    enableSimToReco = cms.untracked.bool(False),
    hitAssociator = cms.PSet(
      associatePixel = cms.bool(False),
      associateStrip = cms.bool(False),
      usePhase2Tracker = cms.bool(False),
      associateRecoTracks = cms.bool(False),
      associateHitbySimTrack = cms.bool(False),
      phase2TrackerSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Tracker'),
      stripSimLinkSrc = cms.InputTag('simSiStripDigis'),
      pixelSimLinkSrc = cms.InputTag('simSiPixelDigis'),
      ROUList = cms.vstring(
        'TrackerHitsTIBLowTof',
        'TrackerHitsTIBHighTof',
        'TrackerHitsTOBLowTof',
        'TrackerHitsTOBHighTof'
      )
    ),
    hepMC = cms.untracked.InputTag('generatorSmeared'),
    beamSpot = cms.untracked.InputTag('offlineBeamSpot'),
    badPull = cms.untracked.double(3),
    longLivedDecayLength = cms.untracked.double(1e-14),
    vertexClusteringDistance = cms.untracked.double(0.0001),
    numberOfInnerLayers = cms.untracked.uint32(2),
    minTrackerSimHits = cms.untracked.uint32(3),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
