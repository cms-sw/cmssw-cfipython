import FWCore.ParameterSet.Config as cms

def TotemVFATFrameAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TotemVFATFrameAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
