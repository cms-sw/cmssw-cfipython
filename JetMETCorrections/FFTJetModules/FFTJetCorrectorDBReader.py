import FWCore.ParameterSet.Config as cms

def FFTJetCorrectorDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('FFTJetCorrectorDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
