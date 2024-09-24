import FWCore.ParameterSet.Config as cms

def SeedCombiner(*args, **kwargs):
  mod = cms.EDProducer('SeedCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
