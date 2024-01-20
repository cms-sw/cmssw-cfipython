import FWCore.ParameterSet.Config as cms

l1TPFCandMerger = cms.EDProducer('L1TPFCandMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
