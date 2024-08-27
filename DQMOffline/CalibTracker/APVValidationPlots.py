import FWCore.ParameterSet.Config as cms

def APVValidationPlots(**kwargs):
  mod = cms.EDAnalyzer('APVValidationPlots',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
