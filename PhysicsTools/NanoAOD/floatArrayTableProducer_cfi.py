import FWCore.ParameterSet.Config as cms

floatArrayTableProducer = cms.EDProducer('FloatArrayTableProducer',
  name = cms.required.string,
  doc = cms.optional.string,
  src = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
