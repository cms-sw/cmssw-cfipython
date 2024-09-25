import FWCore.ParameterSet.Config as cms

def FFTJetCorrectorDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('FFTJetCorrectorDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
