import FWCore.ParameterSet.Config as cms

def HLTMuonL1TtoL3TkPreFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonL1TtoL3TkPreFilter',
    saveTags = cms.bool(True),
    BeamSpotTag = cms.InputTag('hltBeamSpotTag'),
    CandTag = cms.InputTag('hltCandTag'),
    PreviousCandTag = cms.InputTag('hltPreviousCandTag'),
    MinN = cms.int32(0),
    MaxEta = cms.double(9999),
    MinNhits = cms.int32(0),
    MaxDr = cms.double(9999),
    MaxDz = cms.double(9999),
    MinPt = cms.double(0),
    NSigmaPt = cms.double(9999),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
