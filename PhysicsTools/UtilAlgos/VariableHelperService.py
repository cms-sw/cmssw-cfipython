import FWCore.ParameterSet.Config as cms

def VariableHelperService(*args, **kwargs):
  mod = cms.Service('VariableHelperService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
