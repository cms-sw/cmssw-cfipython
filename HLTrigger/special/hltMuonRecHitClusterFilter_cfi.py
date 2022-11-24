import FWCore.ParameterSet.Config as cms

hltMuonRecHitClusterFilter = cms.EDFilter('HLTMuonRecHitClusterFilter',
  ClusterTag = cms.InputTag('hltCSCrechitClusters'),
  MinN = cms.int32(1),
  MinSize = cms.int32(50),
  MinSizeMinusMB1 = cms.int32(-1),
  MinSizeRegionCutEtas = cms.vdouble(
    -1,
    -1,
    1.9,
    1.9
  ),
  MaxSizeRegionCutEtas = cms.vdouble(
    1.9,
    1.9,
    -1,
    -1
  ),
  MinSizeRegionCutNstations = cms.vint32(
    -1,
    1,
    -1,
    1
  ),
  MaxSizeRegionCutNstations = cms.vint32(
    1,
    -1,
    1,
    -1
  ),
  MinSizeRegionCutClusterSize = cms.vint32(
    -1,
    -1,
    -1,
    -1
  ),
  Max_nMB1 = cms.int32(-1),
  Max_nMB2 = cms.int32(-1),
  Max_nME11 = cms.int32(-1),
  Max_nME12 = cms.int32(-1),
  Max_nME41 = cms.int32(-1),
  Max_nME42 = cms.int32(-1),
  MinNstation = cms.int32(0),
  MinAvgStation = cms.double(0),
  MinTime = cms.double(-999),
  MaxTime = cms.double(999),
  MinEta = cms.double(-1),
  MaxEta = cms.double(-1),
  MaxTimeSpread = cms.double(-1),
  mightGet = cms.optional.untracked.vstring
)
