import FWCore.ParameterSet.Config as cms

def PFRecHitSoAProducerHCAL_alpaka(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
