import FWCore.ParameterSet.Config as cms

candRefMerger = cms.EDProducer('CandRefMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
