import FWCore.ParameterSet.Config as cms

def InputTagDistributorService(*args, **kwargs):
  mod = cms.Service('InputTagDistributorService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
