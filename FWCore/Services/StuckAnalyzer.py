import FWCore.ParameterSet.Config as cms

def StuckAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('StuckAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
