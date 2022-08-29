import FWCore.ParameterSet.Config as cms

booleanProducer = cms.EDProducer('BooleanProducer',
  value = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
