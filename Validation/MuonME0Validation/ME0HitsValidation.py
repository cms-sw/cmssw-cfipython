import FWCore.ParameterSet.Config as cms

def ME0HitsValidation(**kwargs):
  mod = cms.EDProducer('ME0HitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
