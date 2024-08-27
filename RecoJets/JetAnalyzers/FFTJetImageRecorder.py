import FWCore.ParameterSet.Config as cms

def FFTJetImageRecorder(**kwargs):
  mod = cms.EDAnalyzer('FFTJetImageRecorder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
