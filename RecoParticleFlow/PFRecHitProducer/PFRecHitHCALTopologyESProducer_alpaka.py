import FWCore.ParameterSet.Config as cms

def PFRecHitHCALTopologyESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('PFRecHitHCALTopologyESProducer@alpaka',
    usePFThresholdsFromDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
