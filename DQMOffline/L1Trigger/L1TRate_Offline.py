import FWCore.ParameterSet.Config as cms

def L1TRate_Offline(**kwargs):
  mod = cms.EDProducer('L1TRate_Offline',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
