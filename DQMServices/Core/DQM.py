import FWCore.ParameterSet.Config as cms

def DQM(*args, **kwargs):
  mod = cms.Service('DQM')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
