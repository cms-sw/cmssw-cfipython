import FWCore.ParameterSet.Config as cms

def photonIsolationHIProducer(**kwargs):
  mod = cms.EDProducer('photonIsolationHIProducer',
    photonProducer = cms.InputTag('photons'),
    ebRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    eeRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    hbhe = cms.InputTag('hbhereco'),
    hf = cms.InputTag('hfreco'),
    ho = cms.InputTag('horeco'),
    basicClusterBarrel = cms.InputTag('islandBasicClusters', 'islandBarrelBasicClusters'),
    basicClusterEndcap = cms.InputTag('islandBasicClusters', 'islandEndcapBasicClusters'),
    trackCollection = cms.InputTag('hiGeneralTracks'),
    trackQuality = cms.string('highPurity'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
