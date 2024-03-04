import FWCore.ParameterSet.Config as cms

def CSCTightHaloTrkMuUnvetoFilter(**kwargs):
  mod = cms.EDFilter('CSCTightHaloTrkMuUnvetoFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
