import FWCore.ParameterSet.Config as cms

def L1TDEMON(**kwargs):
  mod = cms.EDProducer('L1TDEMON',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
