import FWCore.ParameterSet.Config as cms

isolatedPFCandidateMerger = cms.EDProducer('IsolatedPFCandidateMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
