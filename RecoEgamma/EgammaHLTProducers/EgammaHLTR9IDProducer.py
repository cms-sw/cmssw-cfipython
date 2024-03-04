import FWCore.ParameterSet.Config as cms

def EgammaHLTR9IDProducer(**kwargs):
  mod = cms.EDProducer('EgammaHLTR9IDProducer',
    recoEcalCandidateProducer = cms.InputTag('hltRecoEcalCandidate'),
    ecalRechitEB = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB'),
    ecalRechitEE = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
