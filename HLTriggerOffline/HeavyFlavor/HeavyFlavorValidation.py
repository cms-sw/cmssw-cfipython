import FWCore.ParameterSet.Config as cms

def HeavyFlavorValidation(**kwargs):
  mod = cms.EDProducer('HeavyFlavorValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
