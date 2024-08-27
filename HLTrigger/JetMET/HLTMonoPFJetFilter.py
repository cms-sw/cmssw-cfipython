import FWCore.ParameterSet.Config as cms

def HLTMonoPFJetFilter(**kwargs):
  mod = cms.EDFilter('HLTMonoPFJetFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('hltAntiKT5ConvPFJets'),
    maxPtSecondJet = cms.double(9999),
    maxDeltaPhi = cms.double(99),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
