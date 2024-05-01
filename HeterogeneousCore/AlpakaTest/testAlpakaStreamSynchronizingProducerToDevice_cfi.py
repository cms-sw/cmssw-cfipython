import FWCore.ParameterSet.Config as cms

testAlpakaStreamSynchronizingProducerToDevice = cms.EDProducer('TestAlpakaStreamSynchronizingProducerToDevice@alpaka',
  size = cms.PSet(
    alpaka_serial_sync = cms.required.int32,
    alpaka_cuda_async = cms.required.int32,
    alpaka_rocm_async = cms.required.int32
  ),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
