import FWCore.ParameterSet.Config as cms

def PATElectronCollectionMerger(*args, **kwargs):
  mod = cms.EDProducer('PATElectronCollectionMerger',
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
