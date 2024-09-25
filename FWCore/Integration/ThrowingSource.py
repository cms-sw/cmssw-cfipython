import FWCore.ParameterSet.Config as cms

def ThrowingSource(*args, **kwargs):
  mod = cms.Source('ThrowingSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
