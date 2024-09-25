import FWCore.ParameterSet.Config as cms

def PFRecHitECALParamsESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('PFRecHitECALParamsESProducer@alpaka',
    cleaningThreshold = cms.double(2),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
