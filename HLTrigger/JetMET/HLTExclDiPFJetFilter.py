import FWCore.ParameterSet.Config as cms

def HLTExclDiPFJetFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTExclDiPFJetFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
    caloTowerTag = cms.InputTag('hltTowerMakerForAll'),
    minPtJet = cms.double(30),
    minHFe = cms.double(50),
    HF_OR = cms.bool(False),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
