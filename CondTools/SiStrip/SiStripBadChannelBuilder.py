import FWCore.ParameterSet.Config as cms

def SiStripBadChannelBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadChannelBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
