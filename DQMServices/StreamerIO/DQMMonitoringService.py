import FWCore.ParameterSet.Config as cms

def DQMMonitoringService(**kwargs):
  mod = cms.Service('DQMMonitoringService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
