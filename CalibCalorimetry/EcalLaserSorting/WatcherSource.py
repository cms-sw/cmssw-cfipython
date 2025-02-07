import FWCore.ParameterSet.Config as cms

def WatcherSource(*args, **kwargs):
  mod = cms.Source('WatcherSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
