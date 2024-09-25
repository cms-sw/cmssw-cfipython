import FWCore.ParameterSet.Config as cms

def SiStripBaselineComparator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBaselineComparator',
    srcClusters = cms.InputTag('siStripClusters'),
    srcClusters2 = cms.InputTag('moddedsiStripClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
