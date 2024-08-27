import FWCore.ParameterSet.Config as cms

def L1TPUM(**kwargs):
  mod = cms.EDProducer('L1TPUM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
