import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducer_alpaka(**kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducer@alpaka',
    eventSetupSource = cms.ESInputTag('', ''),
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
