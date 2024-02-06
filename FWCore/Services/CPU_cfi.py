import FWCore.ParameterSet.Config as cms

CPU = cms.Service('CPU',
  reportCPUProperties = cms.untracked.bool(False),
  disableJobReportOutput = cms.untracked.bool(False)
)
