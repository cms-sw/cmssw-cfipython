import FWCore.ParameterSet.Config as cms

def ECALRecHitSoAProducer_alpaka(**kwargs):
  mod = cms.EDProducer('ECALRecHitSoAProducer@alpaka',
    src = cms.InputTag(''),
    synchronise = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
