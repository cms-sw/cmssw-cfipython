import FWCore.ParameterSet.Config as cms

pfCandidateListMerger = cms.EDProducer('PFCandidateListMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
