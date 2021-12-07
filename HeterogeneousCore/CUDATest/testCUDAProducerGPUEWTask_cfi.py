import FWCore.ParameterSet.Config as cms

testCUDAProducerGPUEWTask = cms.EDProducer('TestCUDAProducerGPUEWTask',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
