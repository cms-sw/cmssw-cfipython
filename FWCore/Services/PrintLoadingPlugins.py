import FWCore.ParameterSet.Config as cms

def PrintLoadingPlugins(*args, **kwargs):
  mod = cms.Service('PrintLoadingPlugins')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
