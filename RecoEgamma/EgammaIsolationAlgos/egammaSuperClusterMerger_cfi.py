import FWCore.ParameterSet.Config as cms

egammaSuperClusterMerger = cms.EDProducer('EgammaSuperClusterMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
