import FWCore.ParameterSet.Config as cms

def PFRecHitECALTopologyESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('PFRecHitECALTopologyESProducer@alpaka',
    usePFThresholdsFromDB = cms.bool(False),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
