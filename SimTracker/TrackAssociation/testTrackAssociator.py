import FWCore.ParameterSet.Config as cms

def testTrackAssociator(**kwargs):
  mod = cms.EDAnalyzer('testTrackAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
