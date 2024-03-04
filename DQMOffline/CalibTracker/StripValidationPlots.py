import FWCore.ParameterSet.Config as cms

def StripValidationPlots(**kwargs):
  mod = cms.EDAnalyzer('StripValidationPlots',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
