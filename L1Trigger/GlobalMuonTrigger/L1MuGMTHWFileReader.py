import FWCore.ParameterSet.Config as cms

def L1MuGMTHWFileReader(*args, **kwargs):
  mod = cms.Source('L1MuGMTHWFileReader')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
