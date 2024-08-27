import FWCore.ParameterSet.Config as cms

def VariableHelperService(**kwargs):
  mod = cms.Service('VariableHelperService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
