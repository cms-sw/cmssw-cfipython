import FWCore.ParameterSet.Config as cms

def PFRecHitSoAProducerHCAL_alpaka(**kwargs):
  mod = cms.EDProducer('PFRecHitSoAProducerHCAL@alpaka',
    producers = cms.VPSet(
      cms.PSet(
        params = cms.ESInputTag('', ''),
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
