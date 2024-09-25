import FWCore.ParameterSet.Config as cms

def SiStripMonitorCondData(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripMonitorCondData',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
