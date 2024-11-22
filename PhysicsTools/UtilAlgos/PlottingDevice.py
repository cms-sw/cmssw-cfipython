import FWCore.ParameterSet.Config as cms

def PlottingDevice(*args, **kwargs):
  mod = cms.EDAnalyzer('PlottingDevice',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
