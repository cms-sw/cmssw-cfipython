import FWCore.ParameterSet.Config as cms

def PeriodicAllocMonitor(*args, **kwargs):
  mod = cms.Service('PeriodicAllocMonitor',
    filename = cms.untracked.string('timing.log'),
    millisecondsPerMeasurement = cms.untracked.uint64(1000)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
