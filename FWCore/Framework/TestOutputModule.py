import FWCore.ParameterSet.Config as cms

def TestOutputModule(*args, **kwargs):
  mod = cms.OutputModule('TestOutputModule')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
