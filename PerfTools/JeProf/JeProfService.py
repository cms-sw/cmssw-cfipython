import FWCore.ParameterSet.Config as cms

def JeProfService(*args, **kwargs):
  mod = cms.Service('JeProfService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
