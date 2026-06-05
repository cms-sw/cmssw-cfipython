import FWCore.ParameterSet.Config as cms

def BeamSpotRcdReader(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamSpotRcdReader',
    rawFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
