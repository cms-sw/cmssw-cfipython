import FWCore.ParameterSet.Config as cms

def SiStripLAProfileBooker(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripLAProfileBooker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
