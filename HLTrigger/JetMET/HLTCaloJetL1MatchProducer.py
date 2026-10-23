import FWCore.ParameterSet.Config as cms

def HLTCaloJetL1MatchProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTCaloJetL1MatchProducer',
    jetsInput = cms.InputTag('hltAntiKT5PFJets'),
    L1TauJets = cms.InputTag('hltL1extraParticles', 'Tau'),
    L1CenJets = cms.InputTag('hltL1extraParticles', 'Central'),
    L1ForJets = cms.InputTag('hltL1extraParticles', 'Forward'),
    DeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
