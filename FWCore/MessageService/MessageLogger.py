import FWCore.ParameterSet.Config as cms

def MessageLogger(*args, **kwargs):
  mod = cms.Service('MessageLogger')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
