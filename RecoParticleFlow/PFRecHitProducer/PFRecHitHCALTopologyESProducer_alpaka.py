import FWCore.ParameterSet.Config as cms

def PFRecHitHCALTopologyESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('PFRecHitHCALTopologyESProducer@alpaka',
    usePFThresholdsFromDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
