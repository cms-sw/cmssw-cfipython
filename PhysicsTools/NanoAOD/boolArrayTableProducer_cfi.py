import FWCore.ParameterSet.Config as cms

boolArrayTableProducer = cms.EDProducer('BoolArrayTableProducer',
  name = cms.required.string,
  doc = cms.optional.string,
  src = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
