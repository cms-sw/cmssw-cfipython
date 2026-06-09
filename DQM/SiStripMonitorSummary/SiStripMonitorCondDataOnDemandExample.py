import FWCore.ParameterSet.Config as cms

def SiStripMonitorCondDataOnDemandExample(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripMonitorCondDataOnDemandExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
