import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_MPIReceiverPortable(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::MPIReceiverPortable',
    upstream = cms.InputTag('source'),
    products = cms.VPSet(
      template = cms.PSetTemplate(
        type = cms.required.string,
        label = cms.string('')
      )
    ),
    instance = cms.int32(0),
    activity = cms.bool(False),
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
