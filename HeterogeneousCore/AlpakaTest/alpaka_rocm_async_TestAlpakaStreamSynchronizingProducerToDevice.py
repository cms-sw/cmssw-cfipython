import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_TestAlpakaStreamSynchronizingProducerToDevice(**kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::TestAlpakaStreamSynchronizingProducerToDevice',
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
