import FWCore.ParameterSet.Config as cms

def FRDStreamSource(*args, **kwargs):
  mod = cms.Source('FRDStreamSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
