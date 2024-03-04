import FWCore.ParameterSet.Config as cms

def HcalTBSource(**kwargs):
  mod = cms.Source('HcalTBSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
