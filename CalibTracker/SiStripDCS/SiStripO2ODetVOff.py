import FWCore.ParameterSet.Config as cms

def SiStripO2ODetVOff(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripO2ODetVOff',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
