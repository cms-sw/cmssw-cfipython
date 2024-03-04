import FWCore.ParameterSet.Config as cms

def InvRingCalib(**kwargs):
  mod = cms.EDLooper('InvRingCalib')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
