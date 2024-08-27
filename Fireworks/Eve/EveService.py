import FWCore.ParameterSet.Config as cms

def EveService(**kwargs):
  mod = cms.Service('EveService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
