import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_TestAlpakaProducer(**kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::TestAlpakaProducer',
    size = cms.required.int32,
    size2 = cms.required.int32,
    size3 = cms.required.int32,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
