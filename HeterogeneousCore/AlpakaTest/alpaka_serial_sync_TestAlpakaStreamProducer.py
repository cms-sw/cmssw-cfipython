import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_TestAlpakaStreamProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::TestAlpakaStreamProducer',
    source = cms.required.InputTag,
    eventSetupSource = cms.ESInputTag('', ''),
    productInstanceName = cms.string(''),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
