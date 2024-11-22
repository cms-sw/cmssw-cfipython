import FWCore.ParameterSet.Config as cms

def SeedClusterRemover(*args, **kwargs):
  mod = cms.EDProducer('SeedClusterRemover',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
