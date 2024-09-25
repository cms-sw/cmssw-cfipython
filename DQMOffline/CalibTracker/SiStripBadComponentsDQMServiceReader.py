import FWCore.ParameterSet.Config as cms

def SiStripBadComponentsDQMServiceReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadComponentsDQMServiceReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
