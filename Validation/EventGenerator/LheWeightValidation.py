import FWCore.ParameterSet.Config as cms

def LheWeightValidation(**kwargs):
  mod = cms.EDProducer('LheWeightValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
