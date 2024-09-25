import FWCore.ParameterSet.Config as cms

def TrajectorySeedProducer(*args, **kwargs):
  mod = cms.EDProducer('TrajectorySeedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
