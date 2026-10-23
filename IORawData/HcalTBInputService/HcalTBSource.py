import FWCore.ParameterSet.Config as cms

def HcalTBSource(*args, **kwargs):
  mod = cms.Source('HcalTBSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
