import FWCore.ParameterSet.Config as cms

def L1TRate(**kwargs):
  mod = cms.EDProducer('L1TRate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
