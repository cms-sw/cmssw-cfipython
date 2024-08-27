import FWCore.ParameterSet.Config as cms

def QualityCutsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('QualityCutsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
