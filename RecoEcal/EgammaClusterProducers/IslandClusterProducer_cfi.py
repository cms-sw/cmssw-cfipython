import FWCore.ParameterSet.Config as cms

IslandClusterProducer = cms.EDProducer('IslandClusterProducer',
  VerbosityLevel = cms.string('ERROR'),
  barrelHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  endcapHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  barrelClusterCollection = cms.string('islandBarrelBasicClusters'),
  endcapClusterCollection = cms.string('islandEndcapBasicClusters'),
  IslandBarrelSeedThr = cms.double(0.5),
  IslandEndcapSeedThr = cms.double(0.18),
  posCalcParameters = cms.PSet(
    LogWeighted = cms.bool(True),
    T0_barl = cms.double(7.4),
    T0_endc = cms.double(3.1),
    T0_endcPresh = cms.double(1.2),
    W0 = cms.double(4.2),
    X0 = cms.double(0.89)
  ),
  clustershapecollectionEE = cms.string('islandEndcapShape'),
  clustershapecollectionEB = cms.string('islandBarrelShape'),
  barrelShapeAssociation = cms.string('islandBarrelShapeAssoc'),
  endcapShapeAssociation = cms.string('islandEndcapShapeAssoc'),
  SeedRecHitFlagToBeExcludedEB = cms.vstring(),
  SeedRecHitFlagToBeExcludedEE = cms.vstring(),
  RecHitFlagToBeExcludedEB = cms.vstring(),
  RecHitFlagToBeExcludedEE = cms.vstring()
)
