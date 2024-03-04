import FWCore.ParameterSet.Config as cms

def HIProtoTrackFilterProducer(**kwargs):
  mod = cms.EDProducer('HIProtoTrackFilterProducer',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    siPixelRecHits = cms.InputTag('siPixelRecHits'),
    ptMin = cms.double(1),
    tipMax = cms.double(1),
    chi2 = cms.double(1000),
    doVariablePtMin = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
