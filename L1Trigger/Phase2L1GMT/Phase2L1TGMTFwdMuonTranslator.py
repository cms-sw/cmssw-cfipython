import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTFwdMuonTranslator(**kwargs):
  mod = cms.EDProducer('Phase2L1TGMTFwdMuonTranslator',
    stubs = cms.InputTag('gmtStubs'),
    emtfTracks = cms.InputTag('simEmtfDigisPhase2'),
    omtfTracks = cms.InputTag('simOmtfPhase2Digis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
