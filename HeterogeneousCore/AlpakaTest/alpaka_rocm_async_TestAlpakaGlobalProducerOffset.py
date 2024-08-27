import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_TestAlpakaGlobalProducerOffset(**kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::TestAlpakaGlobalProducerOffset',
    xvalue = cms.PSet(
      alpaka_serial_sync = cms.double(0),
      alpaka_cuda_async = cms.double(0),
      alpaka_rocm_async = cms.double(0)
    ),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
