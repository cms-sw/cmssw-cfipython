import FWCore.ParameterSet.Config as cms

def HLTMuonL2SelectorForL3IO(**kwargs):
  mod = cms.EDProducer('HLTMuonL2SelectorForL3IO',
    l2Src = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
    l3OISrc = cms.InputTag('hltNewOIL3MuonCandidates'),
    InputLinks = cms.InputTag('hltNewOIL3MuonsLinksCombination'),
    applyL3Filters = cms.bool(True),
    MinNhits = cms.int32(1),
    MaxNormalizedChi2 = cms.double(20),
    MinNmuonHits = cms.int32(0),
    MaxPtDifference = cms.double(999),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
