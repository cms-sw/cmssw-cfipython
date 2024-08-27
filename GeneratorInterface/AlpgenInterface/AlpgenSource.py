import FWCore.ParameterSet.Config as cms

def AlpgenSource(**kwargs):
  mod = cms.Source('AlpgenSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
