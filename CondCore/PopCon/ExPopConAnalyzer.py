import FWCore.ParameterSet.Config as cms

def ExPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
