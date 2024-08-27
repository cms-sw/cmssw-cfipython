import FWCore.ParameterSet.Config as cms

def SeedClusterRemoverPhase2(**kwargs):
  mod = cms.EDProducer('SeedClusterRemoverPhase2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
