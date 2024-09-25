import FWCore.ParameterSet.Config as cms

def JetToDigiDump(*args, **kwargs):
  mod = cms.EDAnalyzer('JetToDigiDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
