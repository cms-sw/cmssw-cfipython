import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTSAMuonGhostCleaner(**kwargs):
  mod = cms.EDProducer('Phase2L1TGMTSAMuonGhostCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod