import FWCore.ParameterSet.Config as cms

def RandomEngineStateProducer(*args, **kwargs):
  mod = cms.EDProducer('RandomEngineStateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
