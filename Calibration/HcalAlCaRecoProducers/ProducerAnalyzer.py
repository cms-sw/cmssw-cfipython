import FWCore.ParameterSet.Config as cms

def ProducerAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ProducerAnalyzer',
    nameProd = cms.untracked.string('hoCalibProducer'),
    jetCalo = cms.untracked.string('GammaJetJetBackToBackCollection'),
    gammaClus = cms.untracked.string('GammaJetGammaBackToBackCollection'),
    ecalInput = cms.untracked.string('GammaJetEcalRecHitCollection'),
    hbheInput = cms.untracked.string('hbhereco'),
    hoInput = cms.untracked.string('horeco'),
    hfInput = cms.untracked.string('hfreco'),
    Tracks = cms.untracked.string('GammaJetTracksCollection'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
