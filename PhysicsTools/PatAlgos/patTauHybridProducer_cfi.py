import FWCore.ParameterSet.Config as cms

patTauHybridProducer = cms.EDProducer('PATTauHybridProducer',
  src = cms.InputTag('slimmedTaus'),
  jetSource = cms.InputTag('slimmedJetsUpdated'),
  dRMax = cms.double(0.4),
  jetPtMin = cms.double(20),
  jetEtaMax = cms.double(2.5),
  UTagLabel = cms.string('pfParticleNetAK4JetTags'),
  tagPrefix = cms.string('byUTag'),
  UTagScoreNames = cms.vstring(),
  UtagPtCorrName = cms.string('ptcorr'),
  tauScoreMin = cms.double(-1),
  vsJetMin = cms.double(-1),
  checkTauScoreIsBest = cms.bool(False),
  chargeAssignmentProbMin = cms.double(0.2),
  addGenJetMatch = cms.bool(True),
  genJetMatch = cms.InputTag('tauGenJetMatch'),
  usePFLeptonsAsChargedHadrons = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
