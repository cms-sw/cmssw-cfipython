import FWCore.ParameterSet.Config as cms

def NVProfilerService(**kwargs):
  mod = cms.Service('NVProfilerService',
    highlightModules = cms.untracked.vstring(),
    showModulePrefetching = cms.untracked.bool(False),
    skipFirstEvent = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
