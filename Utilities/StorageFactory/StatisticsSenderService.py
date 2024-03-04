import FWCore.ParameterSet.Config as cms

def StatisticsSenderService(**kwargs):
  mod = cms.Service('StatisticsSenderService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
