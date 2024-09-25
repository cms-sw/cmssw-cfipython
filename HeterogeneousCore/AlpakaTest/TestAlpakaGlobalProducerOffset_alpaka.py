import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducerOffset_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducerOffset@alpaka',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
