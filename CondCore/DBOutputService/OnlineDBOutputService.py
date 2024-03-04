import FWCore.ParameterSet.Config as cms

def OnlineDBOutputService(**kwargs):
  mod = cms.Service('OnlineDBOutputService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
