import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_ECALRecHitSoAProducer(**kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::ECALRecHitSoAProducer',
    src = cms.required.InputTag,
    synchronise = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
