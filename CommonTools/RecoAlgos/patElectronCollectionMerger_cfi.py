import FWCore.ParameterSet.Config as cms

patElectronCollectionMerger = cms.EDProducer('PATElectronCollectionMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
