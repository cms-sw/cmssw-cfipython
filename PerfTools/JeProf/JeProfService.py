import FWCore.ParameterSet.Config as cms

def JeProfService(**kwargs):
  mod = cms.Service('JeProfService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
