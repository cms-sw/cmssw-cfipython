import FWCore.ParameterSet.Config as cms

def EventProcessingAllocMonitor(*args, **kwargs):
  mod = cms.Service('EventProcessingAllocMonitor')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
