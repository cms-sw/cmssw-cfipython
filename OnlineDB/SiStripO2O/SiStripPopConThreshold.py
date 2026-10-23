import FWCore.ParameterSet.Config as cms

def SiStripPopConThreshold(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPopConThreshold',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
