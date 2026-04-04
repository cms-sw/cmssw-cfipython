import FWCore.ParameterSet.Config as cms

def SiStripPedestalsBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPedestalsBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
