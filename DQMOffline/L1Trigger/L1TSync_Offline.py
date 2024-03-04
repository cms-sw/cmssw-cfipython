import FWCore.ParameterSet.Config as cms

def L1TSync_Offline(**kwargs):
  mod = cms.EDProducer('L1TSync_Offline',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
