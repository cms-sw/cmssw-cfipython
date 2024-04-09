import FWCore.ParameterSet.Config as cms

def FRDStreamSource(**kwargs):
  mod = cms.Source('FRDStreamSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod