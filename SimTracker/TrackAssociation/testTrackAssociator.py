import FWCore.ParameterSet.Config as cms

def testTrackAssociator(*args, **kwargs):
  mod = cms.EDAnalyzer('testTrackAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
