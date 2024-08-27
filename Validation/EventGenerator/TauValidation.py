import FWCore.ParameterSet.Config as cms

def TauValidation(**kwargs):
  mod = cms.EDProducer('TauValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
