import FWCore.ParameterSet.Config as cms

superClusterMerger = cms.EDProducer('SuperClusterMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
