import FWCore.ParameterSet.Config as cms

def SiStripBaselineComparator(**kwargs):
  mod = cms.EDAnalyzer('SiStripBaselineComparator',
    srcClusters = cms.InputTag('siStripClusters'),
    srcClusters2 = cms.InputTag('moddedsiStripClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
