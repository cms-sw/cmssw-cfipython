import FWCore.ParameterSet.Config as cms

def TokenHolderService(*args, **kwargs):
  mod = cms.Service('TokenHolderService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
