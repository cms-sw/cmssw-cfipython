import FWCore.ParameterSet.Config as cms

def TFileService(**kwargs):
  mod = cms.Service('TFileService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
