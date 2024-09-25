import FWCore.ParameterSet.Config as cms

def PixelInactiveAreaTrackingRegionsSeedingLayersProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelInactiveAreaTrackingRegionsSeedingLayersProducer',
    RegionPSet = cms.PSet(
      operationMode = cms.string('BeamSpotFixed'),
      beamSpot = cms.InputTag('offlineBeamSpot'),
      vertexCollection = cms.InputTag('firstStepPrimaryVertices'),
      maxNVertices = cms.int32(-1),
      nSigmaZBeamSpot = cms.double(4),
      zErrorBeamSpot = cms.double(24.2),
      nSigmaZVertex = cms.double(3),
      zErrorVertex = cms.double(0.2),
      extraPhi = cms.double(0),
      extraEta = cms.double(0),
      ptMin = cms.double(0.9),
      originRadius = cms.double(0.2),
      precise = cms.bool(True),
      whereToUseMeasurementTracker = cms.string('Never'),
      measurementTrackerName = cms.InputTag(''),
      seedingMode = cms.string('Global'),
      input = cms.InputTag(''),
      deltaEta_Cand = cms.double(-1),
      deltaPhi_Cand = cms.double(-1),
      searchOpt = cms.bool(False)
    ),
    inactivePixelDetectorLabels = cms.VInputTag('siPixelDigis'),
    badPixelFEDChannelCollectionLabels = cms.VInputTag('siPixelDigis'),
    ignoreSingleFPixPanelModules = cms.bool(False),
    debug = cms.untracked.bool(False),
    createPlottingFiles = cms.untracked.bool(False),
    layerList = cms.vstring(),
    BPix = cms.PSet(),
    FPix = cms.PSet(),
    TIB = cms.PSet(),
    TID = cms.PSet(),
    TOB = cms.PSet(),
    TEC = cms.PSet(),
    MTIB = cms.PSet(),
    MTID = cms.PSet(),
    MTOB = cms.PSet(),
    MTEC = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
