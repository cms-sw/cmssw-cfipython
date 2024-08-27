import FWCore.ParameterSet.Config as cms

def LaserTask(**kwargs):
  mod = cms.EDProducer('LaserTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
