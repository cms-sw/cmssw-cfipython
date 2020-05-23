import FWCore.ParameterSet.Config as cms

sonicDummyProducerAsync = cms.EDProducer('SonicDummyProducerAsync',
  Client = cms.PSet(
    factor = cms.int32(-1),
    wait = cms.int32(10),
    allowedTries = cms.uint32(0),
    fails = cms.uint32(0)
  ),
  input = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
