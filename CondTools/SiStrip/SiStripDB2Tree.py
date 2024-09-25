import FWCore.ParameterSet.Config as cms

def SiStripDB2Tree(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDB2Tree',
    StripQualityLabel = cms.string('MergedBadComponent'),
    isMC = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
