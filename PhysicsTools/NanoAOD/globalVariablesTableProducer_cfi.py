import FWCore.ParameterSet.Config as cms

globalVariablesTableProducer = cms.EDProducer('GlobalVariablesTableProducer',
  name = cms.optional.string,
  extension = cms.bool(False),
  variables = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
