import FWCore.ParameterSet.Config as cms

particleFlowSuperClusterECALMustache = cms.EDProducer('PFECALSuperClusterProducer',
  PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
  doSatelliteClusterMerge = cms.bool(False),
  thresh_PFClusterBarrel = cms.double(0),
  PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
  useRegression = cms.bool(True),
  satelliteMajorityFraction = cms.double(0.5),
  thresh_PFClusterEndcap = cms.double(0),
  ESAssociation = cms.InputTag('particleFlowClusterECAL'),
  PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
  use_preshower = cms.bool(True),
  verbose = cms.untracked.bool(False),
  thresh_SCEt = cms.double(4),
  etawidth_SuperClusterEndcap = cms.double(0.04),
  phiwidth_SuperClusterEndcap = cms.double(0.6),
  useDynamicDPhiWindow = cms.bool(True),
  PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
  regressionConfig = cms.PSet(
    isHLT = cms.bool(False),
    ecalRecHitsEE = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    ecalRecHitsEB = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v1'),
    regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v1'),
    uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v1'),
    uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v1'),
    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
    eRecHitThreshold = cms.double(1)
  ),
  applyCrackCorrections = cms.bool(False),
  satelliteClusterSeedThreshold = cms.double(50),
  etawidth_SuperClusterBarrel = cms.double(0.04),
  PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
  PFClusters = cms.InputTag('particleFlowClusterECAL'),
  thresh_PFClusterSeedBarrel = cms.double(1),
  ClusteringType = cms.string('Mustache'),
  EnergyWeight = cms.string('Raw'),
  BeamSpot = cms.InputTag('offlineBeamSpot'),
  thresh_PFClusterSeedEndcap = cms.double(1),
  phiwidth_SuperClusterBarrel = cms.double(0.6),
  thresh_PFClusterES = cms.double(0),
  seedThresholdIsET = cms.bool(True),
  PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower')
)
