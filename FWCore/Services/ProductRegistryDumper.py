import FWCore.ParameterSet.Config as cms

def ProductRegistryDumper(**kwargs):
  mod = cms.Service('ProductRegistryDumper')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
