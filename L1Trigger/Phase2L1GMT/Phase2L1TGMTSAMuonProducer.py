import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTSAMuonProducer(**kwargs):
  mod = cms.EDProducer('Phase2L1TGMTSAMuonProducer',
    muonToken = cms.InputTag('simGmtStage2Digis'),
    Nprompt = cms.uint32(12),
    Ndisplaced = cms.uint32(12),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
