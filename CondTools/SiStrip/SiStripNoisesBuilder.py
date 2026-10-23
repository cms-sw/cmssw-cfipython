import FWCore.ParameterSet.Config as cms

def SiStripNoisesBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
