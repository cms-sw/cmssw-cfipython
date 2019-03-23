import FWCore.ParameterSet.Config as cms

caloRecoTauTagInfoProducer = cms.EDProducer('CaloRecoTauTagInfoProducer',
  tkminTrackerHitsn = cms.int32(3),
  ECALBasicClustersAroundCaloJet_DRConeSize = cms.double(0.5),
  tkminPixelHitsn = cms.int32(0),
  ECALBasicClusterpropagTrack_matchingDRConeSize = cms.double(0.015),
  PVProducer = cms.InputTag('offlinePrimaryVertices'),
  tkminPt = cms.double(0.5),
  smearedPVsigmaX = cms.double(0.0015),
  UsePVconstraint = cms.bool(True),
  tkmaxChi2 = cms.double(100),
  EndcapBasicClustersSource = cms.InputTag('multi5x5SuperClusters', 'multi5x5EndcapBasicClusters'),
  smearedPVsigmaY = cms.double(0.0015),
  BarrelBasicClustersSource = cms.InputTag('hybridSuperClusters', 'hybridBarrelBasicClusters'),
  ECALBasicClusterminE = cms.double(1),
  smearedPVsigmaZ = cms.double(0.005),
  tkPVmaxDZ = cms.double(1),
  UseTrackQuality = cms.bool(True),
  tkQuality = cms.string('highPurity'),
  tkmaxipt = cms.double(0.1),
  CaloJetTracksAssociatorProducer = cms.InputTag('ic5JetTracksAssociatorAtVertex')
)
