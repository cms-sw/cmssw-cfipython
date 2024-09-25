import FWCore.ParameterSet.Config as cms

def CSCTightHaloTrkMuUnvetoFilter(*args, **kwargs):
  mod = cms.EDFilter('CSCTightHaloTrkMuUnvetoFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
