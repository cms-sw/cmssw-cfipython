import FWCore.ParameterSet.Config as cms

pfClusterRefCandidateMerger = cms.EDProducer('PFClusterRefCandidateMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
