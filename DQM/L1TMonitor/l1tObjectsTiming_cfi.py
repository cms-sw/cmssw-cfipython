import FWCore.ParameterSet.Config as cms

l1tObjectsTiming = cms.EDProducer('L1TObjectsTiming',
  muonProducer = cms.required.InputTag,
  stage2CaloLayer2JetProducer = cms.required.InputTag,
  stage2CaloLayer2EGammaProducer = cms.required.InputTag,
  stage2CaloLayer2TauProducer = cms.required.InputTag,
  stage2CaloLayer2EtSumProducer = cms.required.InputTag,
  ugtProducer = cms.required.InputTag,
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
  muonQualCut = cms.untracked.int32(12),
  mightGet = cms.optional.untracked.vstring
)
