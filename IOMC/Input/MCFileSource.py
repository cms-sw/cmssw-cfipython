import FWCore.ParameterSet.Config as cms

def MCFileSource(*args, **kwargs):
  mod = cms.Source('MCFileSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
