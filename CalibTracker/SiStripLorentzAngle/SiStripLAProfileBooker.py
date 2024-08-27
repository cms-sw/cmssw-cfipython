import FWCore.ParameterSet.Config as cms

def SiStripLAProfileBooker(**kwargs):
  mod = cms.EDAnalyzer('SiStripLAProfileBooker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
