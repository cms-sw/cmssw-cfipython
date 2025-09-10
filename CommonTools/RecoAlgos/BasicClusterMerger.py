import FWCore.ParameterSet.Config as cms

def BasicClusterMerger(*args, **kwargs):
  mod = cms.EDProducer('BasicClusterMerger',
    src = cms.VInputTag(
      'collection1',
      'collection2'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
