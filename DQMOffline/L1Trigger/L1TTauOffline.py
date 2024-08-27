import FWCore.ParameterSet.Config as cms

def L1TTauOffline(**kwargs):
  mod = cms.EDProducer('L1TTauOffline',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
