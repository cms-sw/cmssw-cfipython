import FWCore.ParameterSet.Config as cms

def L1TCaloUpgradeToGCTConverter(**kwargs):
  mod = cms.EDProducer('L1TCaloUpgradeToGCTConverter',
    bxMin = cms.int32(0),
    bxMax = cms.int32(0),
    InputCollection = cms.InputTag('caloStage1Digis'),
    InputRlxTauCollection = cms.InputTag('caloStage1Digis', 'rlxTaus'),
    InputIsoTauCollection = cms.InputTag('caloStage1Digis', 'isoTaus'),
    InputHFSumsCollection = cms.InputTag('caloStage1Digis', 'HFRingSums'),
    InputHFCountsCollection = cms.InputTag('caloStage1Digis', 'HFBitCounts'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
