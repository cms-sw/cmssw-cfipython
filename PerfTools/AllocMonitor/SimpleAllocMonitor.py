import FWCore.ParameterSet.Config as cms

def SimpleAllocMonitor(*args, **kwargs):
  mod = cms.Service('SimpleAllocMonitor')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
