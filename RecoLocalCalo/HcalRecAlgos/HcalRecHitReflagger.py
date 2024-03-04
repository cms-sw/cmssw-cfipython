import FWCore.ParameterSet.Config as cms

def HcalRecHitReflagger(**kwargs):
  mod = cms.EDProducer('HcalRecHitReflagger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
