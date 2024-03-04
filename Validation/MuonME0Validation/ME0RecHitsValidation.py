import FWCore.ParameterSet.Config as cms

def ME0RecHitsValidation(**kwargs):
  mod = cms.EDProducer('ME0RecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
