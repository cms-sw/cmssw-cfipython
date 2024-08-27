import FWCore.ParameterSet.Config as cms

def CaloRecHitsBeamHaloCleaned(**kwargs):
  mod = cms.EDProducer('CaloRecHitsBeamHaloCleaned',
    EBRecHitsLabel = cms.InputTag('EcalRecHit', 'EcalRecHitsEB'),
    EERecHitsLabel = cms.InputTag('EcalRecHit', 'EcalRecHitsEE'),
    HBHERecHitsLabel = cms.InputTag('hbhereco'),
    GlobalHaloDataLabel = cms.InputTag('GlobalHaloData'),
    IsHLT = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
