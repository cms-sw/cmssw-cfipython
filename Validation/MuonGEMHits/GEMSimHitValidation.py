import FWCore.ParameterSet.Config as cms

def GEMSimHitValidation(*args, **kwargs):
  mod = cms.EDProducer('GEMSimHitValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
