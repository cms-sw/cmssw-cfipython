import FWCore.ParameterSet.Config as cms

def SeedCombiner(*args, **kwargs):
  mod = cms.EDProducer('SeedCombiner',
    seedCollections = cms.VInputTag(),
    clusterRemovalInfos = cms.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
