import FWCore.ParameterSet.Config as cms

def DTtTrigDBValidation(**kwargs):
  mod = cms.EDProducer('DTtTrigDBValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
