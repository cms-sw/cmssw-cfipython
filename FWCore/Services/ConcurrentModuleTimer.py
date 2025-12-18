import FWCore.ParameterSet.Config as cms

def ConcurrentModuleTimer(*args, **kwargs):
  mod = cms.Service('ConcurrentModuleTimer',
    modulesToExclude = cms.untracked.vstring(),
    excludeSource = cms.untracked.bool(False),
    padding = cms.untracked.uint32(0),
    trackGlobalBeginRun = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
