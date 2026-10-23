import FWCore.ParameterSet.Config as cms

def SiStripDetVOffFakeBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffFakeBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
