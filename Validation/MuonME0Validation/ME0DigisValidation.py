import FWCore.ParameterSet.Config as cms

def ME0DigisValidation(**kwargs):
  mod = cms.EDProducer('ME0DigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
