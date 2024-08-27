import FWCore.ParameterSet.Config as cms

def SiStripBadChannelBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadChannelBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
