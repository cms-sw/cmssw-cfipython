import FWCore.ParameterSet.Config as cms

sonicDummyProducerPseudoAsync = cms.EDProducer('SonicDummyProducerPseudoAsync',
  Client = cms.PSet(
    factor = cms.int32(-1),
    wait = cms.int32(10)
  ),
  input = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
