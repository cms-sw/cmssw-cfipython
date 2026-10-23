import FWCore.ParameterSet.Config as cms

def printEvent(*args, **kwargs):
  mod = cms.EDAnalyzer('printEvent',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
