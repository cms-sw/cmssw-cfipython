import FWCore.ParameterSet.Config as cms

def ManyProductAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ManyProductAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
