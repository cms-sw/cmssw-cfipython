import FWCore.ParameterSet.Config as cms

hltMuonRecHitClusterFilter = cms.EDFilter('HLTMuonRecHitClusterFilter',
  ClusterTag = cms.InputTag('hltCSCrechitClusters'),
  MinN = cms.int32(1),
  MinSize = cms.int32(50),
  MinSizeMinusMB1 = cms.int32(0),
  Max_nMB1 = cms.int32(0),
  Max_nMB2 = cms.int32(0),
  Max_nME11 = cms.int32(0),
  Max_nME12 = cms.int32(0),
  Max_nME41 = cms.int32(0),
  Max_nME42 = cms.int32(0),
  MinNstation = cms.int32(0),
  MinAvgStation = cms.double(0),
  MinTime = cms.double(-999),
  MaxTime = cms.double(999),
  MinEta = cms.double(-1),
  MaxEta = cms.double(-1),
  MaxTimeSpread = cms.double(999),
  mightGet = cms.optional.untracked.vstring
)
