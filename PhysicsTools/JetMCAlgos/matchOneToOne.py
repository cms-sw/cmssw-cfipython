import FWCore.ParameterSet.Config as cms

def matchOneToOne(**kwargs):
  mod = cms.EDAnalyzer('matchOneToOne',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
