import FWCore.ParameterSet.Config as cms

def SiStripAnalyser(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripAnalyser',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
