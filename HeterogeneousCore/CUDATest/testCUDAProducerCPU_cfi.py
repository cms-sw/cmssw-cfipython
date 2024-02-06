import FWCore.ParameterSet.Config as cms

testCUDAProducerCPU = cms.EDProducer('TestCUDAProducerCPU',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
