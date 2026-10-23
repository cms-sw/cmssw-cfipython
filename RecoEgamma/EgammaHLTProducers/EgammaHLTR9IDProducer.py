import FWCore.ParameterSet.Config as cms

def EgammaHLTR9IDProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTR9IDProducer',
    recoEcalCandidateProducer = cms.InputTag('hltRecoEcalCandidate'),
    ecalRechitEB = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB'),
    ecalRechitEE = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
