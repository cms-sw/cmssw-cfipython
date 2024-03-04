import FWCore.ParameterSet.Config as cms

def ThrowingSource(**kwargs):
  mod = cms.Source('ThrowingSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
