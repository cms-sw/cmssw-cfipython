import FWCore.ParameterSet.Config as cms

def BeamSpotToCUDA(**kwargs):
  mod = cms.EDProducer('BeamSpotToCUDA',
    src = cms.InputTag('offlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
