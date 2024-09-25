import FWCore.ParameterSet.Config as cms

def HectorProducer(*args, **kwargs):
  mod = cms.EDProducer('HectorProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
