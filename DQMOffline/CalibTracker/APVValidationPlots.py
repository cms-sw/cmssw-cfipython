import FWCore.ParameterSet.Config as cms

def APVValidationPlots(*args, **kwargs):
  mod = cms.EDAnalyzer('APVValidationPlots',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
