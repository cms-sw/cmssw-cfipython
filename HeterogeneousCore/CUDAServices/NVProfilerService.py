import FWCore.ParameterSet.Config as cms

def NVProfilerService(*args, **kwargs):
  mod = cms.Service('NVProfilerService',
    highlightModules = cms.untracked.vstring(),
    showModulePrefetching = cms.untracked.bool(False),
    skipFirstEvent = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
