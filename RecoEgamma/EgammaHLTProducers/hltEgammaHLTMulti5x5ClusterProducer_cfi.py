import FWCore.ParameterSet.Config as cms

hltEgammaHLTMulti5x5ClusterProducer = cms.EDProducer('EgammaHLTMulti5x5ClusterProducer',
  doBarrel = cms.bool(False),
  doEndcaps = cms.bool(True),
  doIsolated = cms.bool(True),
  VerbosityLevel = cms.string('ERROR'),
  posCalcParameters = cms.PSet(
    T0_barl = cms.double(7.4),
    T0_endc = cms.double(3.1),
    T0_endcPresh = cms.double(1.2),
    W0 = cms.double(4.2),
    X0 = cms.double(0.89),
    LogWeighted = cms.bool(True)
  ),
  barrelHitProducer = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB'),
  endcapHitProducer = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE'),
  barrelClusterCollection = cms.string('notused'),
  endcapClusterCollection = cms.string('multi5x5EndcapBasicClusters'),
  Multi5x5BarrelSeedThr = cms.double(0.5),
  Multi5x5EndcapSeedThr = cms.double(0.5),
  l1TagIsolated = cms.InputTag('hltL1extraParticles', 'Isolated'),
  l1TagNonIsolated = cms.InputTag('hltL1extraParticles', 'NonIsolated'),
  l1LowerThr = cms.double(5),
  l1UpperThr = cms.double(9999),
  l1LowerThrIgnoreIsolation = cms.double(999),
  regionEtaMargin = cms.double(0.3),
  regionPhiMargin = cms.double(0.4),
  RecHitFlagToBeExcluded = cms.vstring()
)
