import FWCore.ParameterSet.Config as cms

def LaserAlignment(**kwargs):
  mod = cms.EDProducer('LaserAlignment',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
