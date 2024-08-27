import FWCore.ParameterSet.Config as cms

def MessageLogger(**kwargs):
  mod = cms.Service('MessageLogger')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
