import FWCore.ParameterSet.Config as cms

def ModuleAllocProfiler(*args, **kwargs):
  mod = cms.Service('ModuleAllocProfiler',
    moduleNames = cms.untracked.vstring(),
    nEventsToSkip = cms.untracked.uint32(0),
    filePattern = cms.untracked.string(''),
    statistics = cms.untracked.bool(False),
    deallocationReport = cms.untracked.bool(True),
    churnReport = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
