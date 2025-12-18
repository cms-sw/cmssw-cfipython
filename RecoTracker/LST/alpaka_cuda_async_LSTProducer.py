import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_LSTProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::LSTProducer',
    lstInput = cms.InputTag('lstInputProducer'),
    verbose = cms.bool(False),
    ptCut = cms.double(0.8),
    clustSizeCut = cms.uint32(16),
    ptCutLabel = cms.string('0.8'),
    nopLSDupClean = cms.bool(False),
    tcpLSTriplets = cms.bool(False),
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
