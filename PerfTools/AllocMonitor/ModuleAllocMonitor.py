import FWCore.ParameterSet.Config as cms

def ModuleAllocMonitor(**kwargs):
  mod = cms.Service('ModuleAllocMonitor',
    fileName = cms.required.untracked.string,
    moduleNames = cms.untracked.vstring(),
    nEventsToSkip = cms.untracked.uint32(0)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
