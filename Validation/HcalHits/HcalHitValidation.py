import FWCore.ParameterSet.Config as cms

def HcalHitValidation(**kwargs):
  mod = cms.EDProducer('HcalHitValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
