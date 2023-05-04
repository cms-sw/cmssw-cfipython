import FWCore.ParameterSet.Config as cms

testCUDAProducerGPU = cms.EDProducer('TestCUDAProducerGPU',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
