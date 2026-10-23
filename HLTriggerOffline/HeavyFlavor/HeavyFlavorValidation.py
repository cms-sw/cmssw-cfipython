import FWCore.ParameterSet.Config as cms

def HeavyFlavorValidation(*args, **kwargs):
  mod = cms.EDProducer('HeavyFlavorValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
