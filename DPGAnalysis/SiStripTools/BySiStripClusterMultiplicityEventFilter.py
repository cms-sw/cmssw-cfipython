import FWCore.ParameterSet.Config as cms

def BySiStripClusterMultiplicityEventFilter(*args, **kwargs):
  mod = cms.EDFilter('BySiStripClusterMultiplicityEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
