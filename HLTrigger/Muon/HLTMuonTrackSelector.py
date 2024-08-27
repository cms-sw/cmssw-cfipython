import FWCore.ParameterSet.Config as cms

def HLTMuonTrackSelector(**kwargs):
  mod = cms.EDProducer('HLTMuonTrackSelector',
    track = cms.InputTag(''),
    muon = cms.InputTag(''),
    originalMVAVals = cms.InputTag(''),
    copyMVA = cms.bool(False),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
