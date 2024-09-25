import FWCore.ParameterSet.Config as cms

def DQMStore(*args, **kwargs):
  mod = cms.Service('DQMStore')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
