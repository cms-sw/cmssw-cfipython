import FWCore.ParameterSet.Config as cms

def BSvsPVAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('BSvsPVAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
