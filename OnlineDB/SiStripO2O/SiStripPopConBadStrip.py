import FWCore.ParameterSet.Config as cms

def SiStripPopConBadStrip(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPopConBadStrip',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
