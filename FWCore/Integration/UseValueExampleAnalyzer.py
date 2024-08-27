import FWCore.ParameterSet.Config as cms

def UseValueExampleAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('UseValueExampleAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
