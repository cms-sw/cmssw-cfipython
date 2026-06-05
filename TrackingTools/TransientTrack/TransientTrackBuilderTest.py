import FWCore.ParameterSet.Config as cms

def TransientTrackBuilderTest(*args, **kwargs):
  mod = cms.EDAnalyzer('TransientTrackBuilderTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
