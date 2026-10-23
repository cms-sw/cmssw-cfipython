import FWCore.ParameterSet.Config as cms

def CMTRawAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CMTRawAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
