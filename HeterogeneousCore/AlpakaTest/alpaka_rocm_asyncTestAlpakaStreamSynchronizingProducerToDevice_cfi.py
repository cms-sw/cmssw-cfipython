import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaStreamSynchronizingProducerToDevice = cms.EDProducer('alpaka_rocm_async::TestAlpakaStreamSynchronizingProducerToDevice',
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