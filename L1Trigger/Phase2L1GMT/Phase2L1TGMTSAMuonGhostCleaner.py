import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTSAMuonGhostCleaner(*args, **kwargs):
  mod = cms.EDProducer('Phase2L1TGMTSAMuonGhostCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
