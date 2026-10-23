import FWCore.ParameterSet.Config as cms

def IntrusiveAllocMonitor(*args, **kwargs):
  mod = cms.Service('IntrusiveAllocMonitor')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
