import FWCore.ParameterSet.Config as cms

def SiStripQualityHotStripIdentifier(**kwargs):
  mod = cms.EDAnalyzer('SiStripQualityHotStripIdentifier',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
