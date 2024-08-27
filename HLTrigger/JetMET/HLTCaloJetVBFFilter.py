import FWCore.ParameterSet.Config as cms

def HLTCaloJetVBFFilter(**kwargs):
  mod = cms.EDFilter('HLTCaloJetVBFFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltAntiKT5ConvPFJets'),
    minPtLow = cms.double(40),
    minPtHigh = cms.double(40),
    etaOpposite = cms.bool(False),
    minDeltaEta = cms.double(4),
    minInvMass = cms.double(1000),
    maxEta = cms.double(5),
    leadingJetOnly = cms.bool(False),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
