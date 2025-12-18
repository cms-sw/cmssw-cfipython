import FWCore.ParameterSet.Config as cms

def ModuleEventAllocMonitor(*args, **kwargs):
  mod = cms.Service('ModuleEventAllocMonitor',
    fileName = cms.required.untracked.string,
    moduleNames = cms.untracked.vstring(),
    nEventsToSkip = cms.untracked.uint32(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
