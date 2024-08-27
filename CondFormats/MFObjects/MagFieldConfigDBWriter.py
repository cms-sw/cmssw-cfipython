import FWCore.ParameterSet.Config as cms

def MagFieldConfigDBWriter(**kwargs):
  mod = cms.EDAnalyzer('MagFieldConfigDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
