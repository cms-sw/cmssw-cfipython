import FWCore.ParameterSet.Config as cms

def PlottingDevice(**kwargs):
  mod = cms.EDAnalyzer('PlottingDevice',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
