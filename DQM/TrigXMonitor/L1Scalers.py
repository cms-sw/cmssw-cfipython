import FWCore.ParameterSet.Config as cms

def L1Scalers(**kwargs):
  mod = cms.EDProducer('L1Scalers',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
