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
  verbose = cms.untracked.bool(False),
  thresh_SCEt = cms.double(4),
  etawidth_SuperClusterEndcap = cms.double(0.04),
  phiwidth_SuperClusterEndcap = cms.double(0.6),
  useDynamicDPhiWindow = cms.bool(True),
  PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
  regressionConfig = cms.PSet(
    isHLT = cms.bool(False),
    isPhaseII = cms.bool(False),
    regTrainedWithPS = cms.bool(True),
    applySigmaIetaIphiBug = cms.bool(False),
    ecalRecHitsEE = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    ecalRecHitsEB = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
    regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
    uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
    uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
    regressionMinEB = cms.double(0.2),
    regressionMaxEB = cms.double(2),
    regressionMinEE = cms.double(0.2),
    regressionMaxEE = cms.double(2),
    uncertaintyMinEB = cms.double(0.0002),
    uncertaintyMaxEB = cms.double(0.5),
    uncertaintyMinEE = cms.double(0.0002),
    uncertaintyMaxEE = cms.double(0.5),
    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
    eRecHitThreshold = cms.double(1),
    hgcalRecHits = cms.InputTag(''),
    hgcalCylinderR = cms.double(2.7999999523162842)
  ),
  applyCrackCorrections = cms.bool(False),
  satelliteClusterSeedThreshold = cms.double(50),
  etawidth_SuperClusterBarrel = cms.double(0.04),
  PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
  PFClusters = cms.InputTag('particleFlowClusterECAL'),
  thresh_PFClusterSeedBarrel = cms.double(1),
  EnergyWeight = cms.string('Raw'),
  BeamSpot = cms.InputTag('offlineBeamSpot'),
  thresh_PFClusterSeedEndcap = cms.double(1),
  phiwidth_SuperClusterBarrel = cms.double(0.6),
  thresh_PFClusterES = cms.double(0),
  seedThresholdIsET = cms.bool(True),
  isOOTCollection = cms.bool(False),
  barrelRecHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  endcapRecHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
  dropUnseedable = cms.bool(False),
  ClusteringType = cms.string('Mustache'),
  mightGet = cms.optional.untracked.vstring
)
