import FWCore.ParameterSet.Config as cms

def TestModuleChangeLooper(**kwargs):
  mod = cms.EDLooper('TestModuleChangeLooper')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
