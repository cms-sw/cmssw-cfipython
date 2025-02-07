import FWCore.ParameterSet.Config as cms

def ConsumingStreamAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ConsumingStreamAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
