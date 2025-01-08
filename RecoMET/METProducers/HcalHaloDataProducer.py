import FWCore.ParameterSet.Config as cms

def HcalHaloDataProducer(*args, **kwargs):
  mod = cms.EDProducer('HcalHaloDataProducer',
    EBRecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EERecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    HBHERecHitLabel = cms.InputTag('hbhereco'),
    HFRecHitLabel = cms.InputTag('horeco'),
    HORecHitLabel = cms.InputTag('hfreco'),
    caloTowerCollName = cms.InputTag('towerMaker'),
    HBRecHitEnergyThresholdParam = cms.double(0.5),
    HERecHitEnergyThresholdParam = cms.double(0.5),
    SumHcalEnergyThresholdParam = cms.double(18),
    NHitsHcalThresholdParam = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
