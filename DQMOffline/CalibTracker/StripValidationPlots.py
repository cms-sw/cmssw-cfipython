import FWCore.ParameterSet.Config as cms

def StripValidationPlots(*args, **kwargs):
  mod = cms.EDAnalyzer('StripValidationPlots',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
