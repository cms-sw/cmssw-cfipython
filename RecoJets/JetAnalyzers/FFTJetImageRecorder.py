import FWCore.ParameterSet.Config as cms

def FFTJetImageRecorder(*args, **kwargs):
  mod = cms.EDAnalyzer('FFTJetImageRecorder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
