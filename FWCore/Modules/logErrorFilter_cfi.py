import FWCore.ParameterSet.Config as cms

logErrorFilter = cms.EDFilter('LogErrorFilter',
  maxErrorKindsPerLumi = cms.uint32(999999),
  maxWarningKindsPerLumi = cms.uint32(999999)
)
