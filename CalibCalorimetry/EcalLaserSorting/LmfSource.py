import FWCore.ParameterSet.Config as cms

def LmfSource(*args, **kwargs):
  mod = cms.Source('LmfSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
