import FWCore.ParameterSet.Config as cms

def WatcherSource(**kwargs):
  mod = cms.Source('WatcherSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
