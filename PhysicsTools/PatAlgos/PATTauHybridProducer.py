import FWCore.ParameterSet.Config as cms

def PATTauHybridProducer(**kwargs):
  mod = cms.EDProducer('PATTauHybridProducer',
    src = cms.InputTag('slimmedTaus'),
    jetSource = cms.InputTag('slimmedJetsUpadted'),
    dRMax = cms.double(0.4),
    jetPtMin = cms.double(20),
    jetEtaMax = cms.double(2.5),
    pnetLabel = cms.string('pfParticleNetAK4JetTags'),
    pnetScoreNames = cms.vstring(
      'probmu',
      'probele',
      'probtaup1h0p',
      'probtaup1h1p',
      'probtaup1h2p',
      'probtaup3h0p',
      'probtaup3h1p',
      'probtaum1h0p',
      'probtaum1h1p',
      'probtaum1h2p',
      'probtaum3h0p',
      'probtaum3h1p',
      'probb',
      'probc',
      'probuds',
      'probg',
      'ptcorr',
      'ptreshigh',
      'ptreslow',
      'ptnu'
    ),
    pnetPtCorrName = cms.string('ptcorr'),
    tauScoreMin = cms.double(-1),
    vsJetMin = cms.double(-1),
    checkTauScoreIsBest = cms.bool(False),
    chargeAssignmentProbMin = cms.double(0.2),
    addGenJetMatch = cms.bool(True),
    genJetMatch = cms.InputTag('tauGenJetMatch'),
    usePFLeptonsAsChargedHadrons = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
