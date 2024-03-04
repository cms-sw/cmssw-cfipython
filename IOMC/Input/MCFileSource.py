import FWCore.ParameterSet.Config as cms

def MCFileSource(**kwargs):
  mod = cms.Source('MCFileSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
