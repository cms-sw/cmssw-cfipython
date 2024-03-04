import FWCore.ParameterSet.Config as cms

def SiStripDetVOffFakeBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffFakeBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
