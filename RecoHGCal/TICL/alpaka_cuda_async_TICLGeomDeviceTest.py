import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_TICLGeomDeviceTest(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::TICLGeomDeviceTest',
    src = cms.ESInputTag('', ''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
