import FWCore.ParameterSet.Config as cms

def HIProtoTrackFilterProducer(*args, **kwargs):
  mod = cms.EDProducer('HIProtoTrackFilterProducer',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    siPixelRecHits = cms.InputTag('siPixelRecHits'),
    ptMin = cms.double(1),
    tipMax = cms.double(1),
    chi2 = cms.double(1000),
    doVariablePtMin = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
