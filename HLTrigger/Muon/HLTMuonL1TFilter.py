import FWCore.ParameterSet.Config as cms

def HLTMuonL1TFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonL1TFilter',
    saveTags = cms.bool(True),
    CandTag = cms.InputTag('hltGmtStage2Digis'),
    PreviousCandTag = cms.InputTag(''),
    MaxEta = cms.double(2.5),
    MinPt = cms.double(0),
    MaxDeltaR = cms.double(0.3),
    MinN = cms.int32(1),
    CentralBxOnly = cms.bool(True),
    SelectQualities = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
