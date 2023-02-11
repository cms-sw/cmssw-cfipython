import FWCore.ParameterSet.Config as cms

testPortableProducerCUDA = cms.EDProducer('TestPortableProducerCUDA',
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
