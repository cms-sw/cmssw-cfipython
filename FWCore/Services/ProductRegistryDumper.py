import FWCore.ParameterSet.Config as cms

def ProductRegistryDumper(*args, **kwargs):
  mod = cms.Service('ProductRegistryDumper')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
