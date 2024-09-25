import FWCore.ParameterSet.Config as cms

def ErrorStreamSource(*args, **kwargs):
  mod = cms.Source('ErrorStreamSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
