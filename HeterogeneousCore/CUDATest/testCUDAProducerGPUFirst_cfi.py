import FWCore.ParameterSet.Config as cms

testCUDAProducerGPUFirst = cms.EDProducer('TestCUDAProducerGPUFirst',
  mightGet = cms.optional.untracked.vstring
)
