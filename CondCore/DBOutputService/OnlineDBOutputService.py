import FWCore.ParameterSet.Config as cms

def OnlineDBOutputService(*args, **kwargs):
  mod = cms.Service('OnlineDBOutputService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
