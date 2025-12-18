import FWCore.ParameterSet.Config as cms

def SingleLongTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('SingleLongTrackProducer',
    allTracks = cms.InputTag('generalTracks'),
    matchMuons = cms.InputTag('earlyMuons'),
    PrimaryVertex = cms.InputTag('offlinePrimaryVertices'),
    minNumberOfLayers = cms.int32(10),
    requiredDr = cms.double(0.01),
    onlyValidHits = cms.bool(True),
    debug = cms.bool(False),
    minPt = cms.double(15),
    maxEta = cms.double(2.2),
    maxDxy = cms.double(0.02),
    maxDz = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
