import FWCore.ParameterSet.Config as cms

def L1Validator(**kwargs):
  mod = cms.EDProducer('L1Validator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
