import FWCore.ParameterSet.Config as cms

def HcalRecHitReflagger(*args, **kwargs):
  mod = cms.EDProducer('HcalRecHitReflagger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
