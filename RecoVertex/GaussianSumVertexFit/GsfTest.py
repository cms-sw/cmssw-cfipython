import FWCore.ParameterSet.Config as cms

def GsfTest(*args, **kwargs):
  mod = cms.EDAnalyzer('GsfTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
