import FWCore.ParameterSet.Config as cms

hcalGeometryDetIdTester = cms.EDAnalyzer('HcalGeometryDetIdTester',
  DetectorMin = cms.int32(1),
  DetectorMax = cms.int32(4),
  mightGet = cms.optional.untracked.vstring
)
