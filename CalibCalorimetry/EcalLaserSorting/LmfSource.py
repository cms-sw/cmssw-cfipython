import FWCore.ParameterSet.Config as cms

def LmfSource(**kwargs):
  mod = cms.Source('LmfSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
