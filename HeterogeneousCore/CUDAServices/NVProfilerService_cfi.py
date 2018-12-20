import FWCore.ParameterSet.Config as cms

NVProfilerService = cms.Service('NVProfilerService',
  highlightModules = cms.untracked.vstring(),
  showModulePrefetching = cms.untracked.bool(False)
)
