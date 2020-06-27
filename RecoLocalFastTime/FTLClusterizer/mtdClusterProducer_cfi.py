import FWCore.ParameterSet.Config as cms

mtdClusterProducer = cms.EDProducer('MTDClusterProducer',
  srcBarrel = cms.InputTag('mtdRecHits', 'FTLBarrel'),
  srcEndcap = cms.InputTag('mtdRecHits', 'FTLEndcap'),
  BarrelClusterName = cms.string('FTLBarrel'),
  EndcapClusterName = cms.string('FTLEndcap'),
  ClusterMode = cms.string('MTDThresholdClusterizer'),
  HitThreshold = cms.double(0),
  SeedThreshold = cms.double(0),
  ClusterThreshold = cms.double(0),
  TimeThreshold = cms.double(10),
  PositionThreshold = cms.double(-1),
  mightGet = cms.optional.untracked.vstring
)
