import FWCore.ParameterSet.Config as cms

def timestudy_SleepingServer(*args, **kwargs):
  mod = cms.Service('timestudy::SleepingServer')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
