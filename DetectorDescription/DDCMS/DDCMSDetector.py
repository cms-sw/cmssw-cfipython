import FWCore.ParameterSet.Config as cms

def DDCMSDetector(*args, **kwargs):
  mod = cms.EDAnalyzer('DDCMSDetector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
