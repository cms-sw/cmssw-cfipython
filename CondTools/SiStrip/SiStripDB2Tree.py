import FWCore.ParameterSet.Config as cms

def SiStripDB2Tree(**kwargs):
  mod = cms.EDAnalyzer('SiStripDB2Tree',
    StripQualityLabel = cms.string('MergedBadComponent'),
    isMC = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
