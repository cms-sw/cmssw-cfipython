import FWCore.ParameterSet.Config as cms

def PFClusterSoAProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('PFClusterSoAProducer@alpaka',
    pfRecHits = cms.InputTag(''),
    pfClusterParams = cms.ESInputTag('', ''),
    topology = cms.ESInputTag('', ''),
    synchronise = cms.bool(False),
    pfRecHitFractionAllocation = cms.int32(120),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
