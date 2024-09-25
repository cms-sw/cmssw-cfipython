import FWCore.ParameterSet.Config as cms

def TrackInfoAnalyzerExample(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackInfoAnalyzerExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
