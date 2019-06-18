import FWCore.ParameterSet.Config as cms

hltEgammaHLTNxNClusterProducer = cms.EDProducer('EgammaHLTNxNClusterProducer',
  doBarrel = cms.bool(True),
  doEndcaps = cms.bool(True),
  barrelHitProducer = cms.InputTag('hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEB'),
  endcapHitProducer = cms.InputTag('hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEE'),
  clusEtaSize = cms.int32(3),
  clusPhiSize = cms.int32(3),
  barrelClusterCollection = cms.string('Simple3x3ClustersBarrel'),
  endcapClusterCollection = cms.string('Simple3x3ClustersEndcap'),
  clusSeedThr = cms.double(0.5),
  clusSeedThrEndCap = cms.double(1),
  useRecoFlag = cms.bool(False),
  flagLevelRecHitsToUse = cms.int32(1),
  useDBStatus = cms.bool(True),
  statusLevelRecHitsToUse = cms.int32(1),
  posCalcParameters = cms.PSet(
    T0_barl = cms.double(7.4),
    T0_endc = cms.double(3.1),
    T0_endcPresh = cms.double(1.2),
    W0 = cms.double(4.2),
    X0 = cms.double(0.89),
    LogWeighted = cms.bool(True)
  ),
  maxNumberofSeeds = cms.int32(1000),
  maxNumberofClusters = cms.int32(200),
  debugLevel = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
