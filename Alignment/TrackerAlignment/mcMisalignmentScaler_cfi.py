import FWCore.ParameterSet.Config as cms

mcMisalignmentScaler = cms.EDAnalyzer('MCMisalignmentScaler',
  scalers = cms.VPSet(
    cms.PSet()
  ),
  pullBadModulesToIdeal = cms.untracked.bool(False),
  outlierPullToIdealCut = cms.untracked.double(-1)
)
