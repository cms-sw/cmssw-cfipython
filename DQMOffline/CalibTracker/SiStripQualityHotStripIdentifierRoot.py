import FWCore.ParameterSet.Config as cms

def SiStripQualityHotStripIdentifierRoot(**kwargs):
  mod = cms.EDAnalyzer('SiStripQualityHotStripIdentifierRoot',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
