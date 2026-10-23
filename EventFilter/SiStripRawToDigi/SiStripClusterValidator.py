import FWCore.ParameterSet.Config as cms

def SiStripClusterValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripClusterValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
