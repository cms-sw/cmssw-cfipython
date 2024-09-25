import FWCore.ParameterSet.Config as cms

def SiStripDetVOffTkMapPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffTkMapPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
