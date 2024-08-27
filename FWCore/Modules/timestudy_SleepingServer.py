import FWCore.ParameterSet.Config as cms

def timestudy_SleepingServer(**kwargs):
  mod = cms.Service('timestudy::SleepingServer')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
