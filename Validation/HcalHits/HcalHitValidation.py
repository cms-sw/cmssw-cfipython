import FWCore.ParameterSet.Config as cms

def HcalHitValidation(*args, **kwargs):
  mod = cms.EDProducer('HcalHitValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
