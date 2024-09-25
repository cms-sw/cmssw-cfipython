import FWCore.ParameterSet.Config as cms

def OccupancyPlots(*args, **kwargs):
  mod = cms.EDAnalyzer('OccupancyPlots',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
