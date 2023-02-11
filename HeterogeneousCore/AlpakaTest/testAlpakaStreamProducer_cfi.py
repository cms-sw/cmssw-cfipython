import FWCore.ParameterSet.Config as cms

testAlpakaStreamProducer = cms.EDProducer('TestAlpakaStreamProducer@alpaka',
  source = cms.required.InputTag,
  size = cms.PSet(
    alpaka_serial_sync = cms.required.int32,
    alpaka_cuda_async = cms.required.int32
  ),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
