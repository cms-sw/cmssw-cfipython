import FWCore.ParameterSet.Config as cms

testCUDAProducerGPUtoCPU = cms.EDProducer('TestCUDAProducerGPUtoCPU',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
