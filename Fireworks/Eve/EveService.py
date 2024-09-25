import FWCore.ParameterSet.Config as cms

def EveService(*args, **kwargs):
  mod = cms.Service('EveService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
