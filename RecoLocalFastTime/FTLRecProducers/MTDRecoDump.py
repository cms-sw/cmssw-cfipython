import FWCore.ParameterSet.Config as cms

def MTDRecoDump(*args, **kwargs):
  mod = cms.EDAnalyzer('MTDRecoDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
