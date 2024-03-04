import FWCore.ParameterSet.Config as cms

def PFRecHitECALParamsESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('PFRecHitECALParamsESProducer@alpaka',
    cleaningThreshold = cms.double(2),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
