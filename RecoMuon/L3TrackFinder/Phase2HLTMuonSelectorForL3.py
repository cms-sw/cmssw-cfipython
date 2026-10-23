import FWCore.ParameterSet.Config as cms

def Phase2HLTMuonSelectorForL3(*args, **kwargs):
  mod = cms.EDProducer('Phase2HLTMuonSelectorForL3',
    l1TkMuons = cms.InputTag('l1tTkMuonsGmt'),
    l2MuonsUpdVtx = cms.InputTag('hltL2MuonsFromL1TkMuon', 'UpdatedAtVtx'),
    l3Tracks = cms.InputTag('hltIter2Phase2L3FromL1TkMuonMerged'),
    IOFirst = cms.bool(True),
    matchingDr = cms.double(0.02),
    applyL3Filters = cms.bool(True),
    MinNhits = cms.int32(1),
    MaxNormalizedChi2 = cms.double(5),
    MinNhitsMuons = cms.int32(0),
    MinNhitsPixel = cms.int32(1),
    MinNhitsTracker = cms.int32(6),
    MaxPtDifference = cms.double(999),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
