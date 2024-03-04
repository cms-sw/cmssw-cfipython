import FWCore.ParameterSet.Config as cms

def HCALRecHitSoAProducer_alpaka(**kwargs):
  mod = cms.EDProducer('HCALRecHitSoAProducer@alpaka',
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
