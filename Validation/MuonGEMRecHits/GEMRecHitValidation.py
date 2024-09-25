import FWCore.ParameterSet.Config as cms

def GEMRecHitValidation(*args, **kwargs):
  mod = cms.EDProducer('GEMRecHitValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
