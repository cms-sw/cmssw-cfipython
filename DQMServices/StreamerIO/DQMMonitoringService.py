import FWCore.ParameterSet.Config as cms

def DQMMonitoringService(*args, **kwargs):
  mod = cms.Service('DQMMonitoringService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
