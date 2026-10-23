import FWCore.ParameterSet.Config as cms

def ShallowEventDataProducer(*args, **kwargs):
  mod = cms.EDProducer('ShallowEventDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
