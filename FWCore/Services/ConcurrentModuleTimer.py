import FWCore.ParameterSet.Config as cms

def ConcurrentModuleTimer(**kwargs):
  mod = cms.Service('ConcurrentModuleTimer',
    modulesToExclude = cms.untracked.vstring(),
    excludeSource = cms.untracked.bool(False),
    padding = cms.untracked.uint32(0),
    trackGlobalBeginRun = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
