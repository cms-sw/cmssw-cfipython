import FWCore.ParameterSet.Config as cms

def NavigationSchoolAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('NavigationSchoolAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
