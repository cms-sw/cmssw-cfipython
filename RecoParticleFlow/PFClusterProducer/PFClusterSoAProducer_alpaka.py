import FWCore.ParameterSet.Config as cms

def PFClusterSoAProducer_alpaka(**kwargs):
  mod = cms.EDProducer('PFClusterSoAProducer@alpaka',
    pfRecHits = cms.InputTag(''),
    pfClusterParams = cms.ESInputTag('', ''),
    topology = cms.ESInputTag('', ''),
    synchronise = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
