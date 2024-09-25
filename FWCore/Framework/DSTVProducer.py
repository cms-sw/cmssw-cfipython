import FWCore.ParameterSet.Config as cms

def DSTVProducer(*args, **kwargs):
  mod = cms.EDProducer('DSTVProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
