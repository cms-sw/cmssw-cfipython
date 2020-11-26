import FWCore.ParameterSet.Config as cms

testCUDAProducerGPUEW = cms.EDProducer('TestCUDAProducerGPUEW',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
