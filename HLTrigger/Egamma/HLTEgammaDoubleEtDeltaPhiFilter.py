import FWCore.ParameterSet.Config as cms

def HLTEgammaDoubleEtDeltaPhiFilter(**kwargs):
  mod = cms.EDFilter('HLTEgammaDoubleEtDeltaPhiFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltDoublePhotonEt5L1MatchFilterRegional'),
    l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    etcut = cms.double(5),
    minDeltaPhi = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
