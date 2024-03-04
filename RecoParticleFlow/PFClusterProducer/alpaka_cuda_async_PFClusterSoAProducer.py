import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_PFClusterSoAProducer(**kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::PFClusterSoAProducer',
    pfRecHits = cms.required.InputTag,
    pfClusterParams = cms.required.ESInputTag,
    topology = cms.required.ESInputTag,
    synchronise = cms.required.bool,
    pfRecHitFractionAllocation = cms.int32(120),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
