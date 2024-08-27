import FWCore.ParameterSet.Config as cms

def MTDRecoDump(**kwargs):
  mod = cms.EDAnalyzer('MTDRecoDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
