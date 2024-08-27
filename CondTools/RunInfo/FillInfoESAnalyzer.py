import FWCore.ParameterSet.Config as cms

def FillInfoESAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('FillInfoESAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
