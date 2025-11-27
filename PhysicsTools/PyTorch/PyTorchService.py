import FWCore.ParameterSet.Config as cms

def PyTorchService(*args, **kwargs):
  mod = cms.Service('PyTorchService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
