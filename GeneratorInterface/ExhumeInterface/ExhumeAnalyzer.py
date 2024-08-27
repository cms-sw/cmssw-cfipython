import FWCore.ParameterSet.Config as cms

def ExhumeAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExhumeAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
