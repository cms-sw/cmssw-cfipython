import FWCore.ParameterSet.Config as cms

def WaitingService(*args, **kwargs):
  mod = cms.Service('WaitingService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
