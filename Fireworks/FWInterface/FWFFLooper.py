import FWCore.ParameterSet.Config as cms

def FWFFLooper(**kwargs):
  mod = cms.EDLooper('FWFFLooper')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
