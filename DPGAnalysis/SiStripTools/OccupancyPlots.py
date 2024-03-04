import FWCore.ParameterSet.Config as cms

def OccupancyPlots(**kwargs):
  mod = cms.EDAnalyzer('OccupancyPlots',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
