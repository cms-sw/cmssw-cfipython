import FWCore.ParameterSet.Config as cms

def SiStripMonitorCondData(**kwargs):
  mod = cms.EDAnalyzer('SiStripMonitorCondData',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
