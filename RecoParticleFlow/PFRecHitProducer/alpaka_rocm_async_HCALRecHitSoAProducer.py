import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_HCALRecHitSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::HCALRecHitSoAProducer',
    src = cms.InputTag(''),
    synchronise = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
