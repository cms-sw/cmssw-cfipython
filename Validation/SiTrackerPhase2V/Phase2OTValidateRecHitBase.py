import FWCore.ParameterSet.Config as cms

def Phase2OTValidateRecHitBase(**kwargs):
  mod = cms.EDProducer('Phase2OTValidateRecHitBase',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
