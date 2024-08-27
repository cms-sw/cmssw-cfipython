import FWCore.ParameterSet.Config as cms

def DrellYanValidation(**kwargs):
  mod = cms.EDProducer('DrellYanValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
