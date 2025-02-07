import FWCore.ParameterSet.Config as cms

def METCorrectorDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('METCorrectorDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
