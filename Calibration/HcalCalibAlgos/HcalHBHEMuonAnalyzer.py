import FWCore.ParameterSet.Config as cms

def HcalHBHEMuonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalHBHEMuonAnalyzer',
    hlTriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    labelEBRecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    labelEERecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    labelHBHERecHit = cms.InputTag('hbhereco'),
    labelVertex = cms.string('offlinePrimaryVertices'),
    labelMuon = cms.string('muons'),
    triggers = cms.vstring(),
    pMinMuon = cms.double(5),
    verbosity = cms.untracked.int32(0),
    useRaw = cms.int32(0),
    unCorrect = cms.bool(True),
    getCharge = cms.bool(True),
    collapseDepth = cms.bool(False),
    isItPlan1 = cms.bool(False),
    ignoreHECorr = cms.untracked.bool(False),
    isItPreRecHit = cms.untracked.bool(False),
    moduleName = cms.untracked.string(''),
    processName = cms.untracked.string(''),
    maxDepth = cms.untracked.int32(7),
    fileInCorr = cms.untracked.string(''),
    writeRespCorr = cms.untracked.bool(False),
    usePFThreshold = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod