import FWCore.ParameterSet.Config as cms

def L1TGMT(**kwargs):
  mod = cms.EDProducer('L1TGMT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
