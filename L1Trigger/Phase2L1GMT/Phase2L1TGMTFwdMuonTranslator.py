import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTFwdMuonTranslator(*args, **kwargs):
  mod = cms.EDProducer('Phase2L1TGMTFwdMuonTranslator',
    stubs = cms.InputTag('gmtStubs'),
    emtfTracks = cms.InputTag('simEmtfDigisPhase2'),
    omtfConstrSAMs = cms.InputTag('simOmtfPhase2Digis', 'constrCands'),
    omtfUnconstrSAMs = cms.InputTag('simOmtfPhase2Digis', 'unconstrCands'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
