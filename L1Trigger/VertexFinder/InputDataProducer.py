import FWCore.ParameterSet.Config as cms

def InputDataProducer(*args, **kwargs):
  mod = cms.EDProducer('InputDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
