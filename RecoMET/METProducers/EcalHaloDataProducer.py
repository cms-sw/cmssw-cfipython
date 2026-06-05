import FWCore.ParameterSet.Config as cms

def EcalHaloDataProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalHaloDataProducer',
    EBRecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EERecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    ESRecHitLabel = cms.InputTag('ecalPreshowerRecHit', 'EcalRecHitsES'),
    HBHERecHitLabel = cms.InputTag('hbhereco'),
    SuperClusterLabel = cms.InputTag('correctedHybridSuperClusters'),
    PhotonLabel = cms.InputTag(''),
    EBRecHitEnergyThresholdParam = cms.double(0.3),
    EERecHitEnergyThresholdParam = cms.double(0.3),
    ESRecHitEnergyThresholdParam = cms.double(0.3),
    SumEcalEnergyThresholdParam = cms.double(10),
    NHitsEcalThresholdParam = cms.int32(4),
    RoundnessCutParam = cms.double(0.41),
    AngleCutParam = cms.double(0.51),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
