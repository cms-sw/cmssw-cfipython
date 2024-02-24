import FWCore.ParameterSet.Config as cms

uniqueStringProducer = cms.EDProducer('UniqueStringProducer',
  strings = cms.PSet(
    allowAnyLabel_ = cms.required.string
  ),
  mightGet = cms.optional.untracked.vstring
)
