import FWCore.ParameterSet.Config as cms

gsfElectronCollectionMerger = cms.EDProducer('GsfElectronCollectionMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
