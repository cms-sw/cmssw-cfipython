import FWCore.ParameterSet.Config as cms

def InvRingCalib(*args, **kwargs):
  mod = cms.Looper('InvRingCalib')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
