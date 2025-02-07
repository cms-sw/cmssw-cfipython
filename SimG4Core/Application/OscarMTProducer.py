import FWCore.ParameterSet.Config as cms

def OscarMTProducer(*args, **kwargs):
  mod = cms.EDProducer('OscarMTProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
