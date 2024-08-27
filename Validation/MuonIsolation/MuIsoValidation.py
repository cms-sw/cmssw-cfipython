import FWCore.ParameterSet.Config as cms

def MuIsoValidation(**kwargs):
  mod = cms.EDProducer('MuIsoValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
