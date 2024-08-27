import FWCore.ParameterSet.Config as cms

def HLTEgammaEtFilter(**kwargs):
  mod = cms.EDFilter('HLTEgammaEtFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('HLTEgammaL1MatchFilter'),
    l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    etcutEB = cms.double(1),
    etcutEE = cms.double(1),
    minEtaCut = cms.double(-9999),
    maxEtaCut = cms.double(9999),
    ncandcut = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
