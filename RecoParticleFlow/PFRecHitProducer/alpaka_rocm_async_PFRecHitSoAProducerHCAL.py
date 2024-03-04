import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_PFRecHitSoAProducerHCAL(**kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::PFRecHitSoAProducerHCAL',
    producers = cms.required.VPSet,
    topology = cms.required.ESInputTag,
    synchronise = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
