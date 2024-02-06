import FWCore.ParameterSet.Config as cms

testPortableProducerCPU = cms.EDProducer('TestPortableProducerCPU',
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
