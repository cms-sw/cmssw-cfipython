import FWCore.ParameterSet.Config as cms

def GenWeightValidation(**kwargs):
  mod = cms.EDProducer('GenWeightValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
