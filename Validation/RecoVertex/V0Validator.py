import FWCore.ParameterSet.Config as cms

def V0Validator(**kwargs):
  mod = cms.EDProducer('V0Validator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
