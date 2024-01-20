import FWCore.ParameterSet.Config as cms

basicClusterMerger = cms.EDProducer('BasicClusterMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
