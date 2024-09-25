import FWCore.ParameterSet.Config as cms

def DDTestSpecPars(*args, **kwargs):
  mod = cms.EDAnalyzer('DDTestSpecPars',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
