import FWCore.ParameterSet.Config as cms

def CaloRecHitsBeamHaloCleaned(*args, **kwargs):
  mod = cms.EDProducer('CaloRecHitsBeamHaloCleaned',
    EBRecHitsLabel = cms.InputTag('EcalRecHit', 'EcalRecHitsEB'),
    EERecHitsLabel = cms.InputTag('EcalRecHit', 'EcalRecHitsEE'),
    HBHERecHitsLabel = cms.InputTag('hbhereco'),
    GlobalHaloDataLabel = cms.InputTag('GlobalHaloData'),
    IsHLT = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
