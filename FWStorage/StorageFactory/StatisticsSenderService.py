import FWCore.ParameterSet.Config as cms

def StatisticsSenderService(*args, **kwargs):
  mod = cms.Service('StatisticsSenderService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
