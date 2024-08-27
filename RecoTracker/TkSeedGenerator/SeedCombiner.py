import FWCore.ParameterSet.Config as cms

def SeedCombiner(**kwargs):
  mod = cms.EDProducer('SeedCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
