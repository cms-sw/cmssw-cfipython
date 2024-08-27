import FWCore.ParameterSet.Config as cms

def PrintLoadingPlugins(**kwargs):
  mod = cms.Service('PrintLoadingPlugins')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
