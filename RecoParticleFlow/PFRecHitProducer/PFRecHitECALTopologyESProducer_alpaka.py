import FWCore.ParameterSet.Config as cms

def PFRecHitECALTopologyESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('PFRecHitECALTopologyESProducer@alpaka',
    usePFThresholdsFromDB = cms.bool(False),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
