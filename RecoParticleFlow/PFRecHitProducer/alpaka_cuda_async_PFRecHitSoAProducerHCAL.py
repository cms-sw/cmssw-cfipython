import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_PFRecHitSoAProducerHCAL(**kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::PFRecHitSoAProducerHCAL',
    producers = cms.VPSet(
      cms.PSet(
        src = cms.InputTag('')
      )
    ),
    topology = cms.ESInputTag('', ''),
    synchronise = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
