import FWCore.ParameterSet.Config as cms

def ErrorStreamSource(**kwargs):
  mod = cms.Source('ErrorStreamSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
