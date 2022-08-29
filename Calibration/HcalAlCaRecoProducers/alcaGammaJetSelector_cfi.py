import FWCore.ParameterSet.Config as cms

alcaGammaJetSelector = cms.EDFilter('AlCaGammaJetSelector',
  PhoInput = cms.InputTag('gedPhotons'),
  PFjetInput = cms.InputTag('ak4PFJetsCHS'),
  MinPtJet = cms.double(10),
  MinPtPhoton = cms.double(10),
  mightGet = cms.optional.untracked.vstring
)
