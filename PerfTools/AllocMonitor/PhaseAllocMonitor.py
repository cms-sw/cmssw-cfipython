import FWCore.ParameterSet.Config as cms

def PhaseAllocMonitor(*args, **kwargs):
  mod = cms.Service('PhaseAllocMonitor',
    showSignals = cms.untracked.vstring()
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
