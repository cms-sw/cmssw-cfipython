import FWCore.ParameterSet.Config as cms

def BeamSpotToCUDA(*args, **kwargs):
  mod = cms.EDProducer('BeamSpotToCUDA',
    src = cms.InputTag('offlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
