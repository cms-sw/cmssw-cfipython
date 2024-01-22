import FWCore.ParameterSet.Config as cms

candViewMerger = cms.EDProducer('CandViewMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
