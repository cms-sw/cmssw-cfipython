import FWCore.ParameterSet.Config as cms

def DTHVCheckByAbsoluteValues(*args, **kwargs):
  mod = cms.Service('DTHVCheckByAbsoluteValues')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
