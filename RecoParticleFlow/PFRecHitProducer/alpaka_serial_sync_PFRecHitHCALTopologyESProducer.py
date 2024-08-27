import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_PFRecHitHCALTopologyESProducer(**kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::PFRecHitHCALTopologyESProducer',
    usePFThresholdsFromDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
