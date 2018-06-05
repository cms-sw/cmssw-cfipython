import FWCore.ParameterSet.Config as cms

l1tObjectsTiming = cms.EDProducer('L1TObjectsTiming',
  monitorDir = cms.untracked.string(''),
  verbose = cms.untracked.bool(False),
  firstBXInTrainAlgo = cms.untracked.string(''),
  lastBXInTrainAlgo = cms.untracked.string(''),
  isoBXAlgo = cms.untracked.string(''),
  useAlgoDecision = cms.untracked.string('initial'),
  egammaPtCuts = cms.untracked.vdouble(
    20,
    10,
    30
  ),
  jetPtCut = cms.untracked.double(20),
  tauPtCut = cms.untracked.double(20),
  etsumPtCut = cms.untracked.double(20),
  muonPtCut = cms.untracked.double(8),
  muonQualCut = cms.untracked.int32(12)
)
