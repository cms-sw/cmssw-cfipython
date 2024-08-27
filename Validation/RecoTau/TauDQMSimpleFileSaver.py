import FWCore.ParameterSet.Config as cms

def TauDQMSimpleFileSaver(**kwargs):
  mod = cms.EDAnalyzer('TauDQMSimpleFileSaver',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
