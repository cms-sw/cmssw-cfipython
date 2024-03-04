import FWCore.ParameterSet.Config as cms

def DTHVCheckByAbsoluteValues(**kwargs):
  mod = cms.Service('DTHVCheckByAbsoluteValues')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
