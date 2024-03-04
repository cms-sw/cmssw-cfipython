import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_TestAlpakaESProducerD(**kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerD',
    srcA = cms.ESInputTag('', ''),
    srcB = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
