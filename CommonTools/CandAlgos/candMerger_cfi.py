import FWCore.ParameterSet.Config as cms

candMerger = cms.EDProducer('CandMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
