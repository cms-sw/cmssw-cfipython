import FWCore.ParameterSet.Config as cms

def RecoTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('RecoTrackSelector',
    src = cms.InputTag('generalTracks'),
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    passThrough = cms.bool(False),
    invertRapidityCut = cms.bool(False),
    usePV = cms.bool(False),
    lip = cms.double(300),
    maxChi2 = cms.double(10000),
    maxPhi = cms.double(-3.2),
    maxRapidity = cms.double(5),
    minPhi = cms.double(3.2),
    minRapidity = cms.double(-5),
    ptMin = cms.double(0.1),
    tip = cms.double(120),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    vertexTag = cms.InputTag('offlinePrimaryVertices'),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPixelHit = cms.int32(0),
    maxPixelHit = cms.int32(99),
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    originalAlgorithm = cms.vstring(),
    quality = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
