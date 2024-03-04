import FWCore.ParameterSet.Config as cms

def BySiStripClusterMultiplicityEventFilter(**kwargs):
  mod = cms.EDFilter('BySiStripClusterMultiplicityEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
