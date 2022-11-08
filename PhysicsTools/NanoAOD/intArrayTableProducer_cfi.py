import FWCore.ParameterSet.Config as cms

intArrayTableProducer = cms.EDProducer('IntArrayTableProducer',
  name = cms.required.string,
  doc = cms.optional.string,
  src = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
