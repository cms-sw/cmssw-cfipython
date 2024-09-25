import FWCore.ParameterSet.Config as cms

def DeleteEarlyProducer(*args, **kwargs):
  mod = cms.EDProducer('DeleteEarlyProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
