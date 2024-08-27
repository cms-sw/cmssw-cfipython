import FWCore.ParameterSet.Config as cms

def PyquenAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PyquenAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
