import FWCore.ParameterSet.Config as cms

def BeamSpotProducer(*args, **kwargs):
  mod = cms.EDProducer('BeamSpotProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
