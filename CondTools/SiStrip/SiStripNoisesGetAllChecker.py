import FWCore.ParameterSet.Config as cms

def SiStripNoisesGetAllChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesGetAllChecker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
