import FWCore.ParameterSet.Config as cms

def AlpgenSource(*args, **kwargs):
  mod = cms.Source('AlpgenSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
