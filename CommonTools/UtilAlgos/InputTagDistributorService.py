import FWCore.ParameterSet.Config as cms

def InputTagDistributorService(**kwargs):
  mod = cms.Service('InputTagDistributorService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
