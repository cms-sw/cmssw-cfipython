import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_PFClusterSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::PFClusterSoAProducer',
    pfRecHits = cms.InputTag(''),
    pfClusterParams = cms.ESInputTag('', ''),
    topology = cms.ESInputTag('', ''),
    synchronise = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
