import FWCore.ParameterSet.Config as cms

def MuScleFit(**kwargs):
  mod = cms.Looper('MuScleFit')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
