import FWCore.ParameterSet.Config as cms

hltEgammaHLTIslandClusterProducer = cms.EDProducer('EgammaHLTIslandClusterProducer',
  VerbosityLevel = cms.string('ERROR'),
  doBarrel = cms.bool(True),
  doEndcaps = cms.bool(True),
  doIsolated = cms.bool(True),
  barrelHitProducer = cms.InputTag('islandEndcapBasicClusters', 'EcalRecHitsEB'),
  endcapHitProducer = cms.InputTag('islandEndcapBasicClusters', 'EcalRecHitsEB'),
  barrelClusterCollection = cms.string('islandBarrelBasicClusters'),
  endcapClusterCollection = cms.string('islandEndcapBasicClusters'),
  IslandBarrelSeedThr = cms.double(0.5),
  IslandEndcapSeedThr = cms.double(0.18),
  l1TagIsolated = cms.InputTag('l1extraParticles', 'Isolated'),
  l1TagNonIsolated = cms.InputTag('l1extraParticles', 'NonIsolated'),
  l1LowerThr = cms.double(0),
  l1UpperThr = cms.double(9999),
  l1LowerThrIgnoreIsolation = cms.double(9999),
  regionEtaMargin = cms.double(0.3),
  regionPhiMargin = cms.double(0.4)
)
