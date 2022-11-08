import FWCore.ParameterSet.Config as cms

uniqueStringProducer = cms.EDProducer('UniqueStringProducer',
  strings = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
